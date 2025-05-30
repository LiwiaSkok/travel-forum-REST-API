from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import PostForm 
from flask import request, redirect, url_for  
from forms import CommentForm
from flask import flash
from sqlalchemy import func
from flask import jsonify
from flask_migrate import Migrate
import os
from werkzeug.utils import secure_filename
from datetime import datetime #dodanie że post jest dodawany na stronę i ustawiony po czasie wstawienia


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-key")
app.config['UPLOAD_FOLDER'] = 'static/uploads'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'instance', 'posts.db')}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)




# Model Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(300), nullable=True)
    image2 = db.Column(db.String(300), nullable=True) #dodawanie drugiego zdjęcia
    country = db.Column(db.String(100), nullable=True)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
     
    

    def __repr__(self):
        return f"<Post {self.id}>"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    post = db.relationship('Post', backref=db.backref('comments',cascade="all, delete", lazy=True))

    def __repr__(self):
        return f"<Post {self.title}>"
    

# Strona główna
@app.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = PostForm()
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    if form.validate_on_submit():
        file1 = form.image.data
        file2 = form.image2.data

        filename1 = None
        filename2 = None

        if file1:
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        if file2:
            filename2 = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        new_post = Post(
            title=form.title.data,
            content=form.content.data,
            location=form.location.data,
            image=f"/static/uploads/{filename1}" if filename1 else None,
            image2=f"/static/uploads/{filename2}" if filename2 else None,
            country=form.country.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        file1 = form.image.data
        file2 = form.image2.data

        post.title = form.title.data
        post.content = form.content.data
        post.location = form.location.data
        post.country = form.country.data

        # Usuwanie zdjęcia 1
        if request.form.get("remove_image"):
            post.image = None
        elif file1 and hasattr(file1, 'filename') and file1.filename:
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            post.image = f"/static/uploads/{filename1}"

        # Usuwanie zdjęcia 2
        if request.form.get("remove_image2"):
            post.image2 = None
        elif file2 and hasattr(file2, 'filename') and file2.filename:
            filename2 = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            post.image2 = f"/static/uploads/{filename2}"

        db.session.commit()
        flash("Zaktualizowano post.")
        return redirect(url_for("index"))

    return render_template("edit.html", form=form, post=post)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post=post)
        db.session.add(comment)
        db.session.commit()
        flash("Dodano komentarz.")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("post_detail.html", post=post, form=form)


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))

#Usuwanie komentarzy 
@app.route("/delete_comment/<int:comment_id>", methods=["POST"])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post_id  # zapisz ID posta, by przekierować z powrotem
    db.session.delete(comment)
    db.session.commit()
    flash("Komentarz został usunięty.")
    return redirect(url_for("post_detail", post_id=post_id))

#Edytowanie komentarzy
@app.route("/comment/edit/<int:comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form = CommentForm(obj=comment)

    if form.validate_on_submit():
        comment.content = form.content.data
        db.session.commit()
        flash("Komentarz został zaktualizowany.")
        return redirect(url_for("post_detail", post_id=comment.post_id))

    return render_template("edit_comment.html", form=form, comment=comment)


@app.route("/country/<country>")
def posts_by_country(country):
    posts = Post.query.filter(func.lower(Post.country) == func.lower(country))\
                      .order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)

@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return jsonify({"likes": post.likes})



# Zwracanie wszystkich postów jako JSON
@app.route("/api/posts", methods=["GET"])
def api_get_posts():
    posts = Post.query.all()
    return jsonify([{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "location": post.location,
        "image": post.image,
        "country": post.country,
        "likes": post.likes
    } for post in posts])

# Zwracanie jednego posta jako JSON
@app.route("/api/posts/<int:post_id>", methods=["GET"])
def api_get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "location": post.location,
        "image": post.image,
        "country": post.country,
        "likes": post.likes
    })



# Tworzenie posta przez JSON
@app.route("/api/posts", methods=["POST"])
def api_create_post():
    data = request.get_json()
    new_post = Post(
        title=data["title"],
        content=data["content"],
        location=data.get("location"),
        image = data.get("image"),
        image2 = data.get("image2"),
        country=data.get("country")
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created", "id": new_post.id}), 201
  

# Aktualizacja posta
@app.route("/api/posts/<int:post_id>", methods=["PUT"])
def api_update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data["title"]
    post.content = data["content"]
    post.location = data.get("location")
    post.image = data.get("image")
    post.image2 = data.get("image2")
    post.country = data.get("country")
    db.session.commit()
    return jsonify({"message": "Post updated"})

# Usuwanie posta
@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
def api_delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"})


@app.route("/api/comments/<int:post_id>", methods=["POST"])
def api_add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    comment = Comment(content=data['content'], post=post)
    db.session.add(comment)
    db.session.commit()
    return jsonify({"content": comment.content})

#Zmina 
#if __name__ == "__main__":
 #   app.run(debug=True)

if __name__ == "__main__":
    app.run()


