"""Forms specific to the requests system."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired


class TextRequestForm(FlaskForm):
    """The form for requesting a text."""
    title = StringField("Title", validators=[InputRequired()],
                        render_kw={"placeholder": "Title"})
    authors = StringField(
        "Authors", validators=[InputRequired()],
        render_kw={"placeholder": "Authors, e.g. \"Orwell, George; Vonnegut, "
                   "Kurt\""})
    description = TextAreaField(
        "Notes",
        render_kw={"placeholder": "Enter a description of the book, it’s "
                   "significance, and why it belongs on Annopedia."})
    submit = SubmitField("Submit")


class TagRequestForm(FlaskForm):
    """The form for requesting a tag."""
    tag = StringField("tag", validators=[InputRequired()],
                      render_kw={"placeholder": "tag-name"})
    description = TextAreaField(
        "Notes",
        render_kw={"placeholder": "Enter a description of the tag, it’s "
                   "significance, and why it belongs on Annopedia."})
    submit = SubmitField("Submit")
