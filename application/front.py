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

from .models import (findTaskeById,Task,
                    #multimedia
                    getAllMultimedia,getAllTablettes,getAllImprimante,getAllTV,getAllTelephones,getAllAccessoires,
                     getAllImmobilier,getAllMaison,getAllVehicule,getAllOrdinateurs,
                     getAllDakarMultimedia,getAllToubaMultimedia,getAllThiesMultimedia,
                     getAllNeufMultimedia,getAllVenantMultimedia,getAllOccasionMultimedia,getAllReconditionnéMultimedia,getAllPrix,
                     getAllDateMultimedia,listerParPrixCroissant,listerParPrixDecroissant,listerPaTitleMultimedia,
                     #immobilier
                     getAllImmobilier,getAppartementAlouer,getAppartementMeubler,getTerainsAVendre,getMaisonAVendre,getMaisonAlouer,
                     getChambreAlouer,getAllDakarImmobilier,getAllToubaImmobilier,getAllThiesImmobilier,getAllNeufImmobilier,
                     getAllVenantImmobilier,getAllOccasionImmobilier,getAllReconditionnéImmobilier,getAllDateImmobilier,
                     listerParPrixCroissantImmobilier,listerParPrixDecroissantImmobilier,listerPaTitleImmobilier,getAllPrixImmobiler
                     
 
                     )
#le tableau
tableau = {
    #etat
    "occasion":len(getAllOccasionMultimedia()),"neuf":len(getAllNeufMultimedia()),"venant":len(getAllVenantMultimedia()),"recondisionne":len(getAllReconditionnéMultimedia()),       
    #ville 
     "dakar":len(getAllDakarMultimedia()),"thies":len(getAllThiesMultimedia()),"touba":len(getAllToubaMultimedia()),
     #type
     "ordinateurs":len(getAllOrdinateurs()),"accessoires":len(getAllAccessoires()),"tv":len(getAllTV()),"imprimantes":len(getAllImprimante()),"tablettes":len(getAllTablettes()),"telephones":len(getAllTelephones()),       
     #all multimedia
     "all":len(getAllMultimedia()),           
        }
tableauImobilier={
    #etat
    "occasion":len(getAllOccasionImmobilier()),"neuf":len(getAllNeufImmobilier()),"venant":len(getAllVenantImmobilier()),"recondisionne":len(getAllReconditionnéImmobilier()),       
    #ville 
     "dakar":len(getAllDakarImmobilier()),"thies":len(getAllThiesImmobilier()),"touba":len(getAllToubaImmobilier()),
     #type
     "aptAlouer":len(getAppartementAlouer()),"aptMeuble":len(getAppartementMeubler()),"terrainVendre":len(getTerainsAVendre()),"maisonVendre":len(getMaisonAVendre()),"maisonLouer":len(getMaisonAlouer()),"chambre":len(getChambreAlouer()),       
     #all multimedia
     "all":len(getAllImmobilier()),           
        }
#
@app.route("/")
def index():
    return render_template("front/index.html")

@app.route("/compte")
def compte():
    return render_template("front/connexion/compte.html")
#details d'un produit
@app.route("/detail/<int:id>")
def detail(id):
    task=Task
    task=findTaskeById(id)
    date=format_date(task.created_date)
    return render_template("front/detail.html",article=task,date=date)

from datetime import datetime

def format_date(value, format="%m/%d/%Y"):
    if not value:
        return ""
    return value.strftime(format)




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



#==========================================IMMOBILIER==================================================
#index
@app.route("/index_immobilier")
def index_immobilier():
    title=""
    articles=getAllImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#all getAppartementAlouer
@app.route("/AppartementAlouer")
def AppartementAlouer():
    title="/Appartement à louer"
    articles=getAppartementAlouer()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#all getAppartementMeubler
@app.route("/appartementMeuble")
def appartementMeuble():
    title="/Appartement Meublé"
    articles=getAppartementMeubler()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#getTerainsAVendre
@app.route("/terainsAVendre")
def terainsAVendre():
    title="/Terains à vendre"
    articles=getTerainsAVendre()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#getMaisonAVendre
@app.route("/maisonAVendre")
def maisonAVendre():
    title="/Maison à vendre"
    articles=getMaisonAVendre()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#getMaisonAlouer
@app.route("/maisonAlouer")
def maisonAlouer():
    title="/Maison à louer"
    articles=getMaisonAlouer()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)

#getChambreAlouer
@app.route("/chambreAlouer")
def chambreAlouer():
    title="/Chambre à louer"
    articles=getChambreAlouer()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)

#AllDakar
@app.route("/dakarImmobilier")
def dakarImmobilier():
    title="/Dakar"
    articles=getAllDakarImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#AllTouba
@app.route("/toubaImmobilier")
def toubaImmobilier():
    title="/Touba"
    articles=getAllToubaImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)

#getAllThies
@app.route("/thiesImmobilier")
def thiesImmobilier():
    title="/Thies"
    articles=getAllThiesImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#AllNeuf getAllNeufImmobilier
@app.route("/neufImmobilier")
def neufImmobilier():
    title="/Neuf"
    articles=  getAllNeufImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)

#getAllVenantImmobilier
@app.route("/venantImmobilier")
def venantImmobilier():
    title="/Venant"
    articles=getAllVenantImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)


#getAllReconditionnéImmobilier
@app.route("/reconditionnéImmobilier")
def reconditionnéImmobilier():
    title="/Reconditionné"
    articles=getAllReconditionnéImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)

#getAllOccasionImmobilier
@app.route("/occasionImmobilier")
def occasionImmobilier():
    title="/Occasions"
    articles=getAllOccasionImmobilier()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
#==========prix
@app.route("/listeprixImmobiler",methods=['GET', 'POST'])
def listeprixImmobiler():
    title="/Prix"
    articles=getAllImmobilier() 
    if request.method == "POST": 
   # Recuprer les donnees par post:
        minPrice = request.form.get("minPrice")
        maxPrice = request.form.get("maxPrice")
        articles=getAllPrixImmobiler(minPrice,maxPrice)

        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    #return render_template("front/immobilier/index.html")


@app.route("/sortImmobilier",methods=['GET', 'POST'])
def sortImmobilier():
    title="/Accessoires"
    x = request.args.get("sort")
    if(x=="recent"):
        articles=getAllDateImmobilier()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    if(x=="croissant"):
        articles=listerParPrixCroissantImmobilier()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    if(x=="decroissant"):
        articles=listerParPrixDecroissantImmobilier()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    return redirect(url_for('index_multimedia'))
#filter_by_libelle
@app.route("/filter_by_libelleImmobilier",methods=['GET', 'POST'])
def filter_by_libelleImmobilier():
    title="/Title"
    if request.method == "POST": 
        title = request.form.get("title")
        articles=listerPaTitleImmobilier(title)
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/immobilier/index.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)
    return redirect(url_for('index_multimedia'))
#============================================================================================fin IMMOBILIER========================























#==========================================Multimedia==================================================
#index
@app.route("/index_multimedia")
def index_multimedia():
    title=""
    articles=getAllMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#all ordinateurs
@app.route("/ordinateurs")
def ordinateurs():
    title="/Ordinateurs"
    articles=getAllOrdinateurs()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#all tablettes
@app.route("/tablettes")
def tablettes():
    title="/Tablettes"
    articles=getAllTablettes()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#AllImprimante
@app.route("/imprimantes")
def imprimantes():
    title="/Imprimantes"
    articles=getAllImprimante()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#AllTV
@app.route("/tvs")
def tvs():
    title="/Tv"
    articles=getAllTV()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#AllTelephones
@app.route("/telephones")
def telephones():
    title="/Telephones"
    articles=getAllTelephones()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)

#getAllAccessoires
@app.route("/accessoires")
def accessoires():
    title="/Accessoires"
    articles=getAllAccessoires()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)

#AllDakar
@app.route("/dakarMultimedia")
def dakarMultimedia():
    title="/Dakar"
    articles=getAllDakarMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#AllTouba
@app.route("/toubaMultimedia")
def toubaMultimedia():
    title="/Touba"
    articles=getAllToubaMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)

#getAllThies
@app.route("/thiesMultimedia")
def thiesMultimedia():
    title="/Thies"
    articles=getAllThiesMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#AllNeuf Multimedia
@app.route("/neufMultimedia")
def neufMultimedia():
    title="/Neuf"
    articles=  getAllNeufMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)

#getAllOccasionMultimedia
@app.route("/occasionMultimedia")
def occasionMultimedia():
    title="/Occasion"
    articles=getAllOccasionMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)


#AllReconditionneMultimedia
@app.route("/reconditionnerMultimedia")
def reconditionnerMultimedia():
    title="/Reconditionné"
    articles=getAllReconditionnéMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)

#getAllVenantMultimedia
@app.route("/venantMultimedia")
def venantMultimedia():
    title="/Venants"
    articles=getAllVenantMultimedia()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
#==========prix
@app.route("/prix",methods=['GET', 'POST'])
def prix():
    title="/Prix"
    articles=getAllVenantMultimedia() 
    if request.method == "POST": 
   # Recuprer les donnees par post:
        minPrice = request.form.get("minPrice")
        maxPrice = request.form.get("maxPrice")
        articles=getAllPrix(minPrice,maxPrice)
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    #return render_template("front/immobilier/index.html")


@app.route("/sort",methods=['GET', 'POST'])
def sort():
    title="/Accessoires"
    x = request.args.get("sort")
    if(x=="recent"):
        articles=getAllDateMultimedia()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    if(x=="croissant"):
        articles=listerParPrixCroissant()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    if(x=="decroissant"):
        articles=listerParPrixDecroissant()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    return redirect(url_for('index_multimedia'))
#filter_by_libelle
@app.route("/filter_by_libelle",methods=['GET', 'POST'])
def filter_by_libelle():
    title="/Title"
    if request.method == "POST": 
        title = request.form.get("title")
        articles=listerPaTitleMultimedia(title)
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/multimedia/index.html", articles=articles,pagination=pagination,tableau=tableau,title=title)
    return redirect(url_for('index_multimedia'))
#============================================================================================fin========================
    
























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





