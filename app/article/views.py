import json
import re
import time
from flask import redirect, request, render_template, url_for, session
from ..models import User, Article
from .. import db
from . import article


@article.route('/save/', methods=['POST'])
def save():
    """
    首次添加分享时保存
    :return:
    """
    data = request.data.decode('utf-8')
    json_data = json.loads(data)
    title = json_data['title']
    content = json_data['content']
    content_text = json_data['content_text']
    if '<img' in content:
        first_content = re.search(r'.{1,100}', content_text)
        if first_content == None:
            first_content = ' '
        else:
            first_content = first_content.group()
        first_image = re.search(r'<img.*?>', content).group()
    else:
        first_content = re.search(r'.{15,100}', content_text)
        if first_content == None:
            first_content = ' '
        else:
            first_content = first_content.group()
        first_image = ''
    user_id = session.get('user_id')
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    post = 0
    author_name = User.query.filter(User.id == user_id).first().username
    a = Article(title=title, content=content, user_id=user_id, time=date,
                post=post, author_name=author_name, first_content=first_content, first_image=first_image)
    db.session.add(a)
    db.session.commit()
    return redirect(url_for("people.index"))


@article.route('/add/', methods=['GET', 'POST'])
def add_content():
    """
     发布分享
     :return:
     """
    if request.method == 'GET':
        if session.get('user_id'):
            return render_template('add_content.html')
        else:
            session['next_url_after_login'] = request.url
            return redirect(url_for('main.login'))
    else:
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        title = json_data['title']
        content = json_data['content']
        content_text = json_data['content_text']
        if '<img' in content:
            first_content = re.search(r'.{1,100}', content_text)
            if first_content == None:
                first_content = ' '
            else:
                first_content = first_content.group()
            first_image = re.search(r'<img.*?>', content).group()
        else:
            first_content = re.search(r'.{15,100}', content_text)
            if first_content == None:
                first_content = ' '
            else:
                first_content = first_content.group()
            first_image = ''
        user_id = session.get('user_id')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        post = 1
        author_name = User.query.filter(User.id == user_id).first().username
        article = Article(title=title, content=content, user_id=user_id, time=date,
                          post=post, author_name=author_name, first_content=first_content, first_image=first_image)
        db.session.add(article)
        db.session.commit()

        return redirect(url_for('article.add_content'))


@article.route('/show/<article_id>')
def show(article_id):
    """
    分享文章详情页面
    :param article_id:
    :return:
    """
    a = Article.query.filter(Article.id == article_id).first()
    return render_template('show.html', article=a)


@article.route('/edit/<article_id>', methods=['GET', 'POST'])
def edit_content(article_id):
    """
    个人中心编辑分享-发布
    :param article_id:
    :return:
    """
    if request.method == "GET":
        a = Article.query.filter_by(id=article_id).first()
        return render_template('edit_content.html', article=a)
    else:
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        title = json_data['title']
        content = json_data['content']
        content_text = json_data['content_text']
        if '<img' in content:
            first_content = re.search(r'.{1,100}', content_text)
            if first_content == None:
                first_content = ' '
            else:
                first_content = first_content.group()
            first_image = re.search(r'<img.*?>', content).group()
        else:
            first_content = re.search(r'.{15,100}', content_text)
            if first_content == None:
                first_content = ' '
            else:
                first_content = first_content.group()
            first_image = ''
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        article = Article.query.filter_by(id=article_id).first()
        article.title = title
        article.content = content
        article.time = date
        article.first_content = first_content
        article.first_image = first_image
        article.post = 1
        db.session.commit()
        return redirect(url_for('main.index'))


@article.route('/edit/save_again/<article_id>', methods=['POST'])
def save_again(article_id):
    data = request.data.decode('utf-8')
    json_data = json.loads(data)
    title = json_data['title']
    content = json_data['content']
    content_text = json_data['content_text']
    if '<img' in content:
        first_content = re.search(r'.{1,100}', content_text)
        if first_content == None:
            first_content = ' '
        else:
            first_content = first_content.group()
        first_image = re.search(r'<img.*?>', content).group()
    else:
        first_content = re.search(r'.{15,100}', content_text)
        if first_content == None:
            first_content = ' '
        else:
            first_content = first_content.group()
        first_image = ''

    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    article = Article.query.filter_by(id=article_id).first()
    article.title = title
    article.content = content
    article.time = date
    article.first_content = first_content
    article.first_image = first_image
    article.post = 0
    db.session.commit()
    return redirect(url_for("people.index"))


@article.route('/delete/<article_id>')
def delete(article_id):
    """
    个人中心删除分享
    :param article_id:
    :return:
    """
    a = Article.query.filter_by(id=article_id).first()
    db.session.delete(a)
    db.session.commit()
    return redirect(url_for("people.index"))
