import time
from flask import request, render_template, session, redirect, url_for
from sqlalchemy import or_
from ..models import Article, User
from .. import db
from . import main


@main.route('/')
def index():
    """
    首页列表展示
    :return:
    """
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.time.desc()).filter(Article.post == 1).paginate(page, per_page=4,
                                                                                                error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)


@main.route('/register/', methods=['GET', 'POST'])
def register():
    """
    注册
    :return:
    """
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        register_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_time = register_time
        user = User(username=username, email=email, password=password, register_time=register_time, last_time=last_time)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))


@main.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登陆
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter(User.email == email, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user = User.query.filter(User.id == session['user_id']).first()
            user.last_time = last_time
            db.session.commit()
            if session.get('next_url_after_login'):
                return redirect(session.get('next_url_after_login'))
            else:
                return redirect(url_for('main.index'))
        else:
            return '<h1>用户名或密码错误</h1>'


@main.route('/search/')
def search():
    """
    全局搜索
    :return:
    """
    keywords = request.args.get("keywords")
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.time.desc()).filter(or_(
        Article.title.like("%" + keywords + "%")if keywords is not None else "",
        Article.content.like("%" + keywords + "%")if keywords is not None else "")).filter(Article.post == 1)\
        .paginate(page, per_page=4, error_out=False)

    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)


@main.route('/logout/')
def logout():
    """
    注销
    :return:
    """
    session.clear()
    return redirect(url_for('main.index'))


@main.app_context_processor
def my_context_processor():
    if session.get('user_id'):
        user = User.query.filter(User.id == session.get('user_id')).first()
        return {'user': user}
    return {}
