import time
from flask import request, redirect, session, url_for
from . import comment
from .. import db
from .. models import Article, User, Comment


@comment.route('/', methods=['POST'])
def add_comment():
    """
    添加评论
    :return:
    """
    if session.get('user_id'):
        article_id = request.form.get('article_id')

        comment_content = request.form.get('comment')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        username = User.query.filter(User.id == session.get('user_id')).first().username
        # email = User.query.filter(User.id == session.get('user_id')).first().email
        c = Comment(article_id=article_id, content=comment_content, time=date,
                    comment_user_id=session.get('user_id'), comment_user_name=username)
        # article_username = Article.query.filter(Article.id == article_id).first().author_name
        # article_email = User.query.filter(User.username == article_username).first().email
        db.session.add(c)
        db.session.commit()

        return redirect(url_for('article.show', article_id=article_id))
    else:
        return redirect(url_for('main.login'))
