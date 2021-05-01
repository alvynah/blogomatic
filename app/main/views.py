from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quotes
from ..models import Quote,User,Blog,Upvote,Downvote,Comment
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its content
    '''
    #getting Quotes
    quotes=get_quotes()
    blogview = Blog.get_all_blogs()

    return render_template('index.html', quotes=quotes, blogview=blogview)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    blogs = Blog.query.filter_by(user_id=user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user,blogs=blogs,user_id=user_id)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/create_new', methods=['POST', 'GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        user_id = current_user
        new_blog_object = Blog(blog=blog, user_id=current_user._get_current_object().id, title=title)
        new_blog_object.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', form=form)


@main.route('/like/<int:id>', methods=['POST', 'GET'])
def like(id):
    blog = Blog.query.get(id)
    new_vote_like = Upvote(blog=blog, upvote=1)
    new_vote_like.save_upvote()
    return redirect(url_for('main.index', id=id))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
def dislike(id):
    blog = Blog.query.get(id)
    new_vote_dislike = Downvote(blog=blog, downvote=1)
    new_vote_dislike.save_downvote()
    return redirect(url_for('main.index', id=id))


@main.route('/comment/<int:id>', methods=['POST', 'GET'])
def comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()
    all_comments = Comment.query.filter_by(blog_id=id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        comment_by=form.comment_by.data
        
        if current_user.is_authenticated:
            comment_by = current_user.username

        
        new_comment = Comment(comment=comment, blog_id=id, comment_by=comment_by)
        new_comment.save_comment()
        return redirect(url_for('.comment', id=blog.id))
    return render_template('comment.html', form=form, blog=blog, all_comments=all_comments)

@main.route("/blog/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    blog = Blog.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.comment", id = blog.id))
