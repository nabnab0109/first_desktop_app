from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, Optional, URL

class PostForm(FlaskForm):
    title = StringField('投稿名', validators=[DataRequired()])
    content = TextAreaField('本文', validators=[DataRequired()])
    category = SelectField('大カテゴリー', coerce=int)
    sub_category = SelectField('小カテゴリー', coerce=int)  # 小カテゴリの追加
    link = StringField('リンク', validators=[Optional(), URL()])  # リンクの追加
    attachment = FileField('ファイル添付')  # ファイルの添付
    table_data = TextAreaField('表データ', validators=[Optional()])  # 表の作成
    submit = SubmitField('投稿する')
