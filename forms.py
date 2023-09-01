from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('投稿名', validators=[DataRequired()])
    content = TextAreaField('本文', validators=[DataRequired()])
    category = SelectField('カテゴリー', coerce=int)
    submit = SubmitField('投稿する')
