import sys
import argparse
import codecs
import io
import json
from icc import db, create_app
from icc.models.content import Line, Text
from icc.models.user import User
from icc.models.annotation import Annotation, Tag

"""Parse annotations from json file into the prepopulated database."""

def get_community():
    community = User.query.filter_by(display='Community').first()
    if not community and __name__ == ' __main__':
        sys.exit("The Community user hasn't been created in the database yet.")

def get_tags():
    original_tag = Tag.query.filter_by(tag='original').first()
    annotator_tag = Tag.query.filter_by(tag=args.annotator).first()
    if annotator_tag is None:
        annotator_tag = Tag(tag=args.annotator, description="Original "
                            f"annotations from [[Writer:{args.annotator}]]",
                            locked=True)
        if not args.dryrun:
            db.session.add(annotator_tag)
    return [original_tag, annotator_tag]

def get_edition(title, num):
    text = Text.query.filter_by(title=title).first()
    edition = text.editions.filter_by(num=num).first()
    if __name__ == '__main__':
        if not text:
            parser.error(f"The text {args.title} was not found.")
        if not edition:
            parser.error(f"The edition number {args.edition_num} was not found "
                         f"for {text.title}")
    return edition

def populate_annotations(title, edition_num, annotator, annotations):
    community = get_community()
    tags = get_tags(annotator)
    edition = get_edition(title, edition_num)

    cnt = 0
    for annotation in annotations:
        line = Line.query.filter_by(line=annotation['line']).first()

        if not line:
            db.session.rollback()
            sys.exit(f"Fail on {cnt}: {annotation}")

        annotation = Annotation(edition=edition, annotator=community,
                                fl=line.num, ll=line.num, fc=0, lc=-1,
                                locked=True, body=annotation['annotation'],
                                tags=tags)
        db.session.add(annotation)

        cnt += 1
        if cnt % 25 == 0:
            print(cnt)

    if not args.dryrun:
        print(f"{cnt} annotations added.")
        print("Now committing...")
        db.session.commit()
        print("Committed.")
        # I don't want to import SearchableMixin to test this, but I don't want to
        # eliminate the method in case I change my mind.
        if 'SearchableMixin' in str(Annotation.__bases__):
            Annotation.reindex(edition_id=args.edition_id)
            print("Now reindexing...")
        print("Done.")
    else:
        db.session.rollback()
        print(f"{cnt} annotations created.")

if __name__ == '__main__':
    main()
    return cnt

def main():
    """The main runner for the command line interface."""

    parser = argparse.ArgumentParser("Process icc annotations.json files "
                                     "into the database.")
    parser.add_argument('-i', '--in', action='store', type=str, help="The json "
                        "file containing the annotations.")
    parser.add_argument('-t', '--title', action='store', type=str,
                        required=True, help="The title of the text for the "
                        "annotations")
    parser.add_argument('-e', '--edition_num', action='store', type=int,
                        required=True, help="The edition number of the text "
                        "for the annotations.")
    parser.add_argument('-a', '--annotator', action='store', type=str,
                        required=True, help="The name of the annotator in the "
                        "form of a tag (i.e., no spaces)")
    parser.add_argument('-d', '--dryrun', action='store_true', help="Flag for "
                        "a dry run test.")
    args = parser.parse_args()
    app = create_app()
    readin = args.in if args.in else sys.stdin.buffer
    fin = io.open(readin, 'r', encoding='utf-8-sig')
#    fin = codecs.getreader('utf_8_sig')(sys.stdin.buffer, errors='replace')
    annotations = json.load(fin)

    with app.app_context():
        cnt = populate_annotations(args.title, args.edition_num, args.annotator,
                                   annotations)
