from flask import Flask, render_template, redirect, url_for,Blueprint,request
import os
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

app = Flask(__name__,template_folder='template/')

from .models import getAllMultimedia,getAllImmobilier,getAllMaison,getAllVehicule
#
@app.route("/")
def index():
    return render_template("front/index.html")
#le index to emplois
@app.route("/index_emplois")
def index_emplois():
    articles=getAllImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,)
#le index to emplois
@app.route("/index_immobilier")
def index_immobilier():
    articles=getAllImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,)
#le index to emplois
@app.route("/index_contact", methods=['GET', 'POST'])
def index_contact():
    contacts=[]
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            filename = file.filename
            file.save(os.path.join('./application/static/images', filename))
            nam = request.args.get("name")
            emails = request.args.get("email")
            new_contact = Contact(name="xx", email="ff",image=filename)
            #addContact(new_contact)
            return render_template("front/contact/index.html",contacts=contacts)
    return render_template("front/contact/index.html",contacts=contacts)


    
@app.route("/index_maison")
def index_maison():
    articles=getAllMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,)
#le index to emplois
@app.route("/index_multimedia")
def index_multimedia():
    articles=getAllMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,)
#le index to emplois
@app.route("/index_vehicules")
def index_vehicules():
    articles=getAllVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,)





