from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators=[Required()])
    submit = SubmitField('Save')


class BlogForm(FlaskForm):
    title = StringField('Title :', validators=[Required()])
    blog = TextAreaField('Your Blog :', validators=[Required()])
    submit = SubmitField('Blog')


class CommentForm(FlaskForm):
    comment_by = StringField("Enter a nickname", validators=[Required()])
    comment = TextAreaField('Enter Comment : ', validators=[Required()])
    submit = SubmitField("Comment")


class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title :", validators=[Required()])
    blog = TextAreaField("Blog :", validators=[Required()])
    submit = SubmitField("Update")
