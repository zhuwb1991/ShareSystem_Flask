from flask import session, render_template, redirect, url_for, request
from sqlalchemy import and_
from . import people
from ..models import Article, User


@people.route('/')
def index():
    """
    个人中心页面展示
    :return:
    """
    id = session.get('user_id')
    if not id:
        session['next_url_after_login'] = request.url
        return redirect(url_for("main.login"))
    user = User.query.filter(User.id == id).first()
    articles = Article.query.filter(and_(Article.user_id == id, Article.post == 1))
    not_post = Article.query.filter(and_(Article.user_id == id, Article.post == 0))
    return render_template('people.html', user=user, articles=articles, not_post=not_post)
