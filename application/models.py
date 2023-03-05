from flask_sqlalchemy import SQLAlchemy
from .front import app
import os
import logging as log

from sqlalchemy import desc
import datetime
# # Creer une instance de la base de donnees
#db = SQLAlchemy()
# # Relier la base de donnee avec l'application
# db.init_app(app)
# OU BIEN
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "expart.sqlite")
#db = SQLAlchemy(app)
# initialize the app with the extension
db.init_app(app)


#db.init_app(app)
# Creation des Models

class Multimedia(db.Model):
    #__tablename__ = "article"  # Au cas ou on change le nom de la table
    #
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    pays = db.Column(db.String(200))
    ville = db.Column(db.String(255))
    image = db.Column(db.String(100))
    published_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published = db.Column(db.Boolean, default=True)
    etat = db.Column(db.String(200))

with app.app_context():
    db.create_all()
    """

# Creation du model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)


# //LES FONCTION POUR COMMUNIQUER AVEC LA BASE DE DONNEES ===============================
#
#
# LES METHODES POUR USER==============================================
#
#

def saveUser(user: User):
    db.session.add(user)
    db.session.commit()


def getAllUsers():
    return User.query.order_by(User.lastname).all()


def de_activate(id_user: int):
    user = User.query.get(id_user)
    #
    user.active = not user.active
    #
    db.session.commit()


#
#
#
# LES METHODES POUR ARTICLES==========================================
def getAllArticles(type_list=0):
    return (
        Article.query.filter(Article.deleted == type_list)
        .order_by(desc(Article.published_at))
        .all()
    )


def getArticles():  # Les articles publiés
    return (
        Article.query.filter(Article.published == 1, Article.deleted == 0)
        .order_by(desc(Article.published_at))
        .all()
    )


def findArticleById(id_article):
    # return User.query.filter(User.id == id_article).first()
    return Article.query.get(id_article)


def saveArticle(article: Article):
    db.session.add(article)
    db.session.commit()


def editArticle(article: Article):
    old_article = Article.query.get(article.id)
    #
    old_article.content = article.content
    old_article.summary = article.summary
    old_article.published = article.published
    old_article.img_title = article.img_title
    old_article.img_url = article.img_url
    old_article.title = article.title
    db.session.commit()


def un_published(id_article):
    article = Article.query.get(id_article)

    # Tester si c'est une publication:
    if not article.published:
        article.published_at = datetime.datetime.utcnow()

    article.published = not article.published
    db.session.commit()


def un_delete(id_article):
    article = Article.query.get(id_article)

    article.deleted = not article.deleted
    db.session.commit()


# with app.app_context():
#     db.drop_all()
#     db.create_all()
# #
#
#
#"""
#
#
#
#
#
#
#
#
#
#
