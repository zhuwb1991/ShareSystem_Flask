from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.Text, nullable=False)
    last_time = db.Column(db.Text, nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    first_content = db.Column(db.Text, nullable=False)
    first_image = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.String(50), nullable=False)
    post = db.Column(db.Integer, nullable=False)
    author_name = db.Column(db.String(50), nullable=False)

    article_author = db.relationship('User', backref=db.backref('articles'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    comment_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.String(50), nullable=False)
    comment_user_name = db.Column(db.String(50), nullable=False)

    article = db.relationship('Article', backref=db.backref('article_comments', order_by=id.desc()))
    comment_user = db.relationship('User', backref=db.backref('user_comments'))