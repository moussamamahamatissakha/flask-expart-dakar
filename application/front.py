from flask import Flask, render_template, redirect, url_for,Blueprint,request
from flask_paginate import Pagination, get_page_parameter 

from .fake_data import getAllArticles
# from . import fake_data

# from .fake_data import getAllArticles, findArticleById
#
""""

search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    users = User.find(...)
    pagination = Pagination(page=page, total=users.count(), search=search, record_name='users')
    # 'page' is the default name of the page parameter, it can be customized
    # e.g. Pagination(page_parameter='p', ...)
    # or set PAGE_PARAMETER in config file
    # also likes page_parameter, you can customize for per_page_parameter
    # you can set PER_PAGE_PARAMETER in config file
    # e.g. Pagination(per_page_parameter='pp')

    return render_template('users/index.html',
                           users=users,
                           pagination=pagination,
                           )


"""


app = Flask(__name__,template_folder='template')
#
@app.route("/")
def index():
    return render_template("/front/index.html")
#le index to emplois
@app.route("/index_emplois")
def index_emplois():
    return render_template("/front/emplois/index.html")
#le index to emplois
@app.route("/index_immobilier")
def index_immobilier():
    return render_template("/front/immobilier/index.html")
#le index to emplois
@app.route("/index_maison")
def index_maison():
    return render_template("/front/maison/index.html")
#le index to emplois
@app.route("/index_multimedia")
def index_multimedia():
    articles = [
    {
        "id": 1,
        "title": "Article 1",
        "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 1",
    },
    {
        "id": 2,
        "title": "Macky le ...",
        "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article sur Macky Sall",
    },
    {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    },
     {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    },
     {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    },
     {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    },
     {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    }, {
        "id": 3,
        "title": "Article 3",
       "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article 3",
    },
]
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')

    return render_template("/front/multimedia/index.html", articles=articles,pagination=pagination,)
#le index to emplois
@app.route("/index_vehicules")
def index_vehicules():
    return render_template("/front/vehicules/index.html")


