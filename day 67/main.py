from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

list = []
posts = db.session.query(BlogPost).all()

for post in posts:
    item = post.to_dict()
    list.append(item)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=list)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-post", methods=["GET", "POST"])
def create():
    form = CreatePostForm()
    if form.validate_on_submit():

        new = BlogPost(
        title = form.title.data,
        subtitle = form.subtitle.data,
        date = datetime.datetime.now().strftime('%B %d, %Y'),
        body = form.body.data,
        author = form.author.data,
        img_url = form.img_url.data
        )

        db.session.add(new)
        db.session.commit()
        return redirect (url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    search = BlogPost.query.get(post_id)
    form = CreatePostForm(
        title=search.title,
        subtitle=search.subtitle,
        img_url=search.img_url,
        author=search.author,
        body=search.body
    )

    if form.validate_on_submit():
        search.title=form.title.data
        search.subtitle=form.subtitle.data
        search.img_url=form.img_url.data
        search.author=form.author.data
        search.body=form.body.data
        db.session.commit()
        return redirect (url_for ('show_post', index=post_id) )
    return render_template("make-post.html", form=form, is_edit=True)
    
@app.route("/delete/<int:post_id>")
def delete(post_id):
    search = BlogPost.query.get(post_id)
    db.session.delete(search)
    db.session.commit()
    return redirect( url_for ("get_all_posts"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)