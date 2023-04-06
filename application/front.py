from flask import Flask, render_template, redirect, url_for,Blueprint,request,session
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


from .models import (findTaskeById,Task,getAllArticleToUser,publishedArticle,dePublishedArticle,getAllEmploisToUser,Emplois,
                    #multimedia
                    getAllMultimedia,getAllTablettes,getAllImprimante,getAllTV,getAllTelephones,getAllAccessoires,
                     getAllImmobilier,getAllOrdinateurs,
                     getAllDakarMultimedia,getAllToubaMultimedia,getAllThiesMultimedia,
                     getAllNeufMultimedia,getAllVenantMultimedia,getAllOccasionMultimedia,getAllReconditionnéMultimedia,getAllPrix,
                     getAllDateMultimedia,listerParPrixCroissant,listerParPrixDecroissant,listerPaTitleMultimedia,
                     #immobilier
                     getAllImmobilier,getAppartementAlouer,getAppartementMeubler,getTerainsAVendre,getMaisonAVendre,getMaisonAlouer,
                     getChambreAlouer,getAllDakarImmobilier,getAllToubaImmobilier,getAllThiesImmobilier,getAllNeufImmobilier,
                     getAllVenantImmobilier,getAllOccasionImmobilier,getAllReconditionnéImmobilier,getAllDateImmobilier,
                     listerParPrixCroissantImmobilier,listerParPrixDecroissantImmobilier,listerPaTitleImmobilier,getAllPrixImmobiler,
                     #vehicules
                    getAllVehicule,getVoiture,getMotos,getLocationVoitures,getEquipementAndPieces,getCamions,getBateau,getAllDakarVehicule,getAllThiesVehicule,getAllToubVehicule,
                    getAllNeufVehicule,getAllVenantVehicule,getAllOccasionVehicule,getAllReconditionnéVehicule,getAllDateVehicule,listerParPrixCroissantVehicule,
                    listerParPrixDecroissantVehicule,listerPaTitleVehicule,getAllPrixVehicule,
                    getToyotaVehicule,getFordVehicule,getAHundayVehicule,getNissanVehicule,
                    #emplois
                    getAllEmplois,findEmploisById,publishedEmplois,dePublisheEmplois,getAdministratif,getSecurite,getAgricole,getIngenierie,
                    getAllDakarEmplois,getAllToubEmplois,getAllThiesEmplois,getAllTempsPartiel,getAllTempsPlein,
                    #Maison
                    getAllMaison,getMobiliers,getElectromenager,getDecoration,getVaiselle,getJardinage,getAllDakarMaison,getAllToubaMaison,getAllThiesMaison,
                    getAllNeufMaison,getAllVenantMaison,getAllOccasionMaison,getAllReconditionnéMaison,getAllDateMaison,
                    listerParPrixCroissantMaison,listerParPrixDecroissantMaison,listerPaTitleMaison,getAllPrixMaison,
                    
                     
 
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
tableauVehicule={
    #etat
    "occasion":len(getAllOccasionVehicule()),"neuf":len(getAllNeufVehicule()),"venant":len(getAllVenantVehicule()),"recondisionne":len(getAllReconditionnéVehicule()),       
    #ville 
     "dakar":len(getAllDakarVehicule()),"thies":len(getAllThiesVehicule()),"touba":len(getAllToubVehicule()),
     #type
     "voiture":len(getVoiture()),"moto":len(getMotos()),"locationVoiture":len(getLocationVoitures()),"equipementAndPiece":len(getEquipementAndPieces()),"camions":len(getCamions()),"bateau":len(getBateau()),       
     #getToyotaVehicule,getFordVehicule,getAHundayVehicule,getNissanVehicule
     "toyota":len(getToyotaVehicule()),"ford":len(getFordVehicule()),"hunday":len(getAHundayVehicule()),"nissan":len(getNissanVehicule()),

     #all multimedia
     "all":len(getAllVehicule()),           
        }
tableauMaison={
    #etat
    "occasion":len(getAllOccasionMaison()),"neuf":len(getAllNeufMaison()),"venant":len(getAllVenantMaison()),"recondisionne":len(getAllReconditionnéMaison()),       
    #ville 
     "dakar":len(getAllDakarMaison()),"thies":len(getAllThiesMaison()),"touba":len(getAllToubaMaison()),
     #type
     "electromenager":len(getElectromenager()),"decoration":len(getDecoration()),"vaiselle":len(getVaiselle()),"jardinage":len(getJardinage()),       
     #all 
     "all":len(getAllMaison()), "mobilier":len(getMobiliers()),           
        }
tableauEmplois={
    #ville 
     "dakar":len(getAllDakarEmplois()),"thies":len(getAllThiesEmplois()),"touba":len(getAllToubEmplois()),
     #type
     "administratif":len(getAdministratif()),"securite":len(getSecurite()),"agricole":len(getAgricole()),"ingenierie":len(getIngenierie()),       
     "plein":len(getAllTempsPlein()),"partiel":len(getAllTempsPartiel()),
     #all 
     "all":len(getAllEmplois()),    
        }






#
@app.route("/")
def index():
    return render_template("front/index.html")

@app.route("/compte")
def compte():
    sessio=session.get('favories')
    tail=len(sessio)
    my_list = list(set(sessio))
    return render_template("front/connexion/compte.html",taille=len(my_list))
#=========================================================details d'un produit===============================
#declaration du tableau de favories


@app.route("/detail/<int:id>")
def detail(id):
    task=Task
    task=findTaskeById(id)
    my_array = session.get('favories')
    my_array.append(task.id)
    session['favories'] = my_array
    date=format_date(task.users.created_date)
    return render_template("front/detail.html",article=task,date=date)

@app.route("/favories")
def favories():
    liste=[]
   
    sessio=session.get('favories')
    tail=len(sessio)
    my_list = list(set(sessio))
    for i in my_list:
        task=findTaskeById(i)
        liste.append(task)
        
    return render_template("front/connexion/favories.html",articles=liste)
@app.route('/clearSession')
def clearSession():
    session['favories'] = []
    return redirect('favories')

from datetime import datetime

def format_date(value, format="%m/%d/%Y"):
    if not value:
        return ""
    return value.strftime(format)



#=========================================================emplois===============================
#,getAdministratif,getSecurite,getAgricole,getIngenierie,getAllDakarEmplois,getAllToubEmplois,getAllThiesEmplois,
#le index to emplois,getAllTempsPartiel,getAllTempsPlein,
@app.route("/index_emplois")
def index_emplois():
    title=""
    articles=getAllEmplois()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#le index to emplois

#le index to emplois

@app.route("/detailEmplois/<int:id>")
def detailEmplois(id):
    emplois=Emplois
    emplois=findEmploisById(id)
    date=format_date(emplois.users.created_date)
    return render_template("front/emplois/detail.html",article=emplois,date=date)


#getAdministratif
@app.route("/getAdministratif")
def getAdministratifs():
    title="/Administratif"
    articles=getAdministratif()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#getSecurite
@app.route("/getSecurite")
def getSecurites():
    title="/Securite"
    articles=getSecurite()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#getJardinage
@app.route("/getAgricole")
def getAgricoles():
    title="/Agricole"
    articles=getAgricole()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#getIngenierie
@app.route("/Ingenierie")
def getIngenieries():
    title="/Agricole"
    articles=getIngenierie()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)


#getAllDakarMaison
@app.route("/getAllDakarEmplois")
def getAllDakarEmploiss():
    title="/Dakar"
    articles=getAllDakarEmplois()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#getAllThiesEmplois
@app.route("/getAllThiesEmplois")
def getAllThiesEmploiss():
    title="/Thies"
    articles=getAllThiesEmplois()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)

#getAllToubaMaison
@app.route("/getAllToubEmplois")
def getAllToubEmploiss():
    title="/Touba"
    articles=getAllToubEmplois()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)
#getAllTempsPlein ,,
@app.route("/getAllTempsPlein")
def getAllTempsPleins():
    title="/Thies"
    articles=getAllTempsPlein()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)

#getAllTempspartel
@app.route("/getAllTempsPartiel")
def getAllTempsPartiels():
    title="/Touba"
    articles=getAllTempsPartiel()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/emplois/index.html", articles=articles,pagination=pagination,tableau=tableauEmplois,title=title)









#=====================================================================================================fin emplois====

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
    


#===================================user
#allEmploisUser
@app.route("/allEmploisUser")
def allEmploisUser():
    title=""
    articles=getAllEmploisToUser()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/user/emplois.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)


@app.route("/allArticleUser")
def allArticleUser():
    title=""
    articles=getAllArticleToUser()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/user/allArticle.html", articles=articles,pagination=pagination,tableau=tableauImobilier,title=title)




#========================================================Maison==================================================
#index
#getAllMaison,getMobiliers,getElectromenager,getDecoration,getVaiselle,getJardinage,getAllDakarMaison,getAllToubaMaison,getAllThiesMaison
#getAllNeufMaison,getAllVenantMaison,getAllOccasionMaison,getAllReconditionnéMaison,getAllDateMaison,
#listerParPrixCroissantMaison,listerParPrixDecroissantMaison,listerPaTitleMaison,getAllPrixMaison
@app.route("/index_maison")
def index_maison():
    articles=getAllMaison()
    title=""
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#all getMobiliers
@app.route("/getMobiliers")
def getMobilierss():
    title="/Mobiliers"
    articles=getMobiliers()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#all getElectromenager
@app.route("/getElectromenager")
def getElectromenagers():
    title="/Electromenager"
    articles=getElectromenager()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#getDecoration
@app.route("/getDecoration")
def getDecorations():
    title="/Decoration"
    articles=getDecoration()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#getMaisonAVendre
@app.route("/getVaiselle")
def getVaiselles():
    title="/Vaiselle"
    articles=getVaiselle()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#getJardinage
@app.route("/getJardinage")
def getJardinages():
    title="/Jardinage"
    articles=getJardinage()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)


#getAllDakarMaison
@app.route("/getAllDakarMaison")
def getAllDakarMaisons():
    title="/Dakar"
    articles=getAllDakarMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#getAllThiesMaison
@app.route("/getAllThiesMaison")
def getAllThiesMaisons():
    title="/Thies"
    articles=getAllThiesMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)

#getAllToubaMaison
@app.route("/getAllToubaMaison")
def getAllToubaMaisons():
    title="/Touba"
    articles=getAllToubaMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#AllNeuf getAllVenantMaison
@app.route("/getAllVenantMaison")
def getAllVenantMaisons():
    title="/Venant"
    articles=  getAllVenantMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)

#getAllVenantImmobilier
@app.route("/getAllNeufMaison")
def getAllNeufMaisons():
    title="/Neuf"
    articles=getAllNeufMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)


#getAllReconditionnéMaison
@app.route("/getAllReconditionnéMaison")
def getAllReconditionnéMaisons():
    title="/Reconditionné"
    articles=getAllReconditionnéMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)

#getAllOccasionImmobilier
@app.route("/getAllOccasionMaison")
def getAllOccasionMaisons():
    title="/Occasions"
    articles=getAllOccasionMaison()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
#==========prix
@app.route("/listeprixMaison",methods=['GET', 'POST'])
def listeprixMaison():
    title="/Prix"
    articles=getAllVehicule() 
    if request.method == "POST": 
   # Recuprer les donnees par post:
        minPrice = request.form.get("minPrice")
        maxPrice = request.form.get("maxPrice")
        articles=getAllPrixMaison(minPrice,maxPrice)

        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    #return render_template("front/immobilier/index.html")


@app.route("/sortVehicule",methods=['GET', 'POST'])
def sortMaison():
    title="/Accessoires"
    x = request.args.get("sort")
    if(x=="recent"):
        articles=getAllDateMaison()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    if(x=="croissant"):
        articles=listerParPrixCroissantMaison()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    if(x=="decroissant"):
        articles=listerParPrixDecroissantMaison()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    return redirect(url_for('index_multimedia'))
#filter_by_libelle
@app.route("/filter_by_libelleMaison",methods=['GET', 'POST'])
def filter_by_libelleMaison():
    title="/Title"
    if request.method == "POST": 
        title = request.form.get("title")
        articles=listerPaTitleMaison(title)
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/maison/index.html", articles=articles,pagination=pagination,tableau=tableauMaison,title=title)
    return redirect(url_for('index_multimedia'))
#============================================================================================fin Maison========================
























#========================================================Vehicule==================================================
#index
#getAllVehicule,getVoiture,getMotos,getLocationVoitures,getEquipementAndPieces,getCamions,getBateau,getAllDakarVehicule,getAllThiesVehicule,getAllToubVehicule
#getAllNeufVehicule,getAllVenantVehicule,getAllOccasionVehicule,getAllReconditionnéVehicule,getAllDateVehicule,listerParPrixCroissantVehicule
#listerParPrixDecroissantVehicule,listerPaTitleVehicule,getAllPrixVehicule

@app.route("/index_vehicules")
def index_vehicules():
    articles=getAllVehicule()
    title=""
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/acceuil.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

@app.route("/all_vehicules")
def all_vehicules():
    articles=getAllVehicule()
    title=""
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#all getAppartementAlouer
@app.route("/getVoitureVehicule")
def getVoitureVehicule():
    title="/Voiture"
    articles=getVoiture()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#all getAppartementMeubler
@app.route("/getMotosVehicule")
def getMotosVehicule():
    title="/Motos"
    articles=getMotos()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#getTerainsAVendre
@app.route("/getLocationVoitures")
def getLocationVoituress():
    title="/Location des voitures"
    articles=getLocationVoitures()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#getMaisonAVendre
@app.route("/getEquipementAndPieces")
def getEquipementAndPiecess():
    title="/Equipement et Pieces"
    articles=getEquipementAndPieces()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#getMaisonAlouer
@app.route("/getCamions")
def getCamionss():
    title="/Camions"
    articles=getCamions()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

#getBateau
@app.route("/getBateau")
def getBateaus():
    title="/Bateau"
    articles=getBateau()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

#AllDakar
@app.route("/getAllDakarVehicule")
def getAllDakarVehicules():
    title="/Dakar"
    articles=getAllDakarVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#AllTouba
@app.route("/getAllThiesVehicule")
def getAllThiesVehicules():
    title="/Thies"
    articles=getAllThiesVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

#getAllThies
@app.route("/getAllToubVehicule")
def getAllToubVehicules():
    title="/Touba"
    articles=getAllToubVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
#AllNeuf getAllNeufImmobilier
@app.route("/getAllVenantVehicule")
def getAllVenantVehicules():
    title="/Venant"
    articles=  getAllVenantVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

#getAllVenantImmobilier
@app.route("/getAllNeufVehicule")
def getAllNeufVehicules():
    title="/Neuf"
    articles=getAllNeufVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)


#getAllReconditionnéImmobilier
@app.route("/getAllReconditionnéVehicule")
def getAllReconditionnéVehicules():
    title="/Reconditionné"
    articles=getAllReconditionnéVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)

#getAllOccasionImmobilier
@app.route("/getAllOccasionVehicule")
def getAllOccasionVehicules():
    title="/Occasions"
    articles=getAllOccasionVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)


 #getToyotaVehicule,getFordVehicule,getAHundayVehicule,getNissanVehicule
#getToyotaVehicule
@app.route("/getToyotaVehicule")
def getToyotaVehicules():
    title="/Toyota"
    articles=getToyotaVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)


#getFordVehicule
@app.route("/getFordVehicule")
def getFordVehicules():
    title="/Ford"
    articles=getFordVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)


#getAHundayVehicule
@app.route("/getAHundayVehicule")
def getAHundayVehicules():
    title="/Hundai"
    articles=getAHundayVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)


#getNissanVehicule
@app.route("/getNissanVehicule")
def getNissanVehicules():
    title="/Nissan"
    articles=getNissanVehicule()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)







#==========prix
@app.route("/listeprixVehicule",methods=['GET', 'POST'])
def listeprixVehicule():
    title="/Prix"
    articles=getAllVehicule() 
    if request.method == "POST": 
   # Recuprer les donnees par post:
        minPrice = request.form.get("minPrice")
        maxPrice = request.form.get("maxPrice")
        articles=getAllPrixVehicule(minPrice,maxPrice)

        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    #return render_template("front/immobilier/index.html")


@app.route("/sortVehicule",methods=['GET', 'POST'])
def sortVehicule():
    title="/Accessoires"
    x = request.args.get("sort1")
    if(x=="recent"):
        articles=getAllDateVehicule()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    if(x=="croissant"):
        articles=listerParPrixCroissantVehicule()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    if(x=="decroissant"):
        articles=listerParPrixDecroissantVehicule()
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    return redirect(url_for('all_vehicule'))
#filter_by_libelle
@app.route("/filter_by_libelleVehicule",methods=['GET', 'POST'])
def filter_by_libelleVehicule():
    title="/Title"
    if request.method == "POST": 
        title = request.form.get("title")
        articles=listerPaTitleVehicule(title)
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=len(articles) ,search=search, record_name='articles')
        return render_template("front/vehicules/index.html", articles=articles,pagination=pagination,tableau=tableauVehicule,title=title)
    return redirect(url_for('index_multimedia'))



#============================================================================================fin Vehicule========================


























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
    



























