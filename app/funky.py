from app import app, db
from app.models import Tag
from flask import request
from werkzeug.urls import url_parse

# This method is used to run through all the lines for a read view and convert/
# prep them to be shown: (a) converts underscores to <em>/</em> tags, and (b)
# opens and closes surrounding <em></em> tags on lines that need it so that the
# tags don's span multiple levels in the DOM and throw everything into a tizzy.
# It also allows me to display an arbitrary number of lines perfectly.
def preplines(lines):
    us = False

    for i, line in enumerate(lines):

        if '_' in lines[i].line:
            newline = []
            for c in lines[i].line:
                if c == '_':
                    if us:
                        newline.append('</em>')
                        us = False
                    else:
                        newline.append('<em>')
                        us = True
                else:
                    newline.append(c)
            lines[i].line = ''.join(newline)

        if line.em_status.label == 'oem':
            lines[i].line = lines[i].line + '</em>'
        elif line.em_status.label == 'cem':
            lines[i].line = '<em>' + lines[i].line
        elif line.em_status.label == 'em':
            lines[i].line = '<em>' + lines[i].line + '</em>'

def is_filled(data):
    if not data.strip():
        return False
    if data == None:
        return False
    if data == '':
        return False
    if data == []:
        return False
    return True

def generate_next(alt_url):
    redirect_url = request.args.get("next")
    print(request.referrer)
    if redirect_url and url_parse(redirect_url).netloc == "":
        print("1")
        return request.args.get("next")
    elif request.referrer:
        print("2")
        return request.referrer
    else:
        print("3")
        return alt_url
