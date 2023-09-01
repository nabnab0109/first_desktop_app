from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # セキュリティのための秘密鍵を設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PostForm(FlaskForm):
    title = StringField('投稿名', validators=[DataRequired()])
    content = TextAreaField('本文', validators=[DataRequired()])
    category = SelectField('カテゴリー', coerce=int)
    submit = SubmitField('投稿する')

@app.route('/')
def dashboard():
    latest_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    categories = Category.query.all()
    return render_template('dashboard.html', latest_posts=latest_posts, categories=categories)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    form.category.choices = [(category.id, category.name) for category in Category.query.all()]

    if form.validate_on_submit():
        category_id = form.category.data
        category = Category.query.get(category_id)
        if not category:
            category = Category(name=category_id)
            db.session.add(category)
            db.session.commit()

        post = Post(title=form.title.data, content=form.content.data, category=category)
        db.session.add(post)
        db.session.commit()
        flash('投稿が作成されました', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_post.html', form=form)

@app.route('/manage_categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('manage_categories.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
