from flask import Flask, render_template, redirect, url_for,Blueprint,request,flash,session,abort,session
import os
from flask_paginate import Pagination, get_page_parameter 
from functools import wraps

#authentification et autorisation
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_changed, Identity

from .FormType import TaskType,UserType,ConnexionType,EmploisType
from .front import app,findTaskeById,publishedArticle,dePublishedArticle
from .models import (Task,add_task,add_user,User,getUserBuEmail,getUserById,add_Emplois,Emplois,
                     findEmploisById,publishedEmplois,dePublisheEmplois,updateImageToUser)
app.config['SECRET_KEY'] = 'ma_clé_secrète_ici'


@app.route("/password")
def password():
    return render_template("front/connexion/password.html")

@app.route("/create_task",methods=['GET', 'POST'])
@login_required
def create_task():
    #print(current_user.id)
    form=TaskType()
    if form.validate_on_submit():
        file = request.files['file']
        libelle = form.libelle.data
        titre = form.titre.data
        text = form.text.data
        content = form.content.data
        description = form.description.data
        etat = form.etat.data
        ville = form.ville.data
        quartier = form.quartier.data
        prix = form.prix.data
        filename = file.filename
        file.save(os.path.join('./application/static/images/tasks', filename))
        #user=User(id=10,name="nom",email="email",password="password",role="role",image="filename")
        task=Task(libelle=libelle,title=titre,text=text,content=content,description=description,pays="senegal",ville=ville,quartier=quartier,etat=etat,image=filename,prix=prix,user_id=current_user.id)
        #(libelle={self.libelle}, title={self.title}, description={self.description},pays={self.pays}, ville={self.ville}, quartier={self.quartier}, etat={self.etat}, image={self.image})
        add_task(task)
        """
        libelle = SelectField('Libelle', choices=[('Multimedia', 'Multimedia'), ('banana', 'Banane'), ('orange', 'Orange')])
        titre = StringField('Titre', validators=[DataRequired()])
        description = TextAreaField('Description', validators=[DataRequired()])
        etat= SelectField('Etat', choices=[('Neuf', 'x'), ('banana', 'Banane'), ('orange', 'Orange')])
        ville= SelectField('Ville', choices=[('Dakar', 'Dakar'), ('Thies', 'Thies'), ('orange', 'Orange')])
        quartier= SelectField('Quartier', choices=[('quartier', 'quartier'), ('Thies', 'Thies'), ('orange', 'Orange')])
        prix = FloatField('Prix', validators=[DataRequired()])
        image = FileField('Image', validators=[DataRequired()])
        submit = SubmitField('Enregister')
        """
        return redirect(url_for('compte'))
    #return render_template("front/immobilier/index.html")
    return render_template("back/create_task.html",form=form)

#create epmois
@app.route("/create_emplois",methods=['GET', 'POST'])
@login_required
def create_emplois():
    form=EmploisType()
    # if request.method == "POST":
    if form.validate_on_submit():
        file = request.files['file']
        libelle = form.libelle.data
        secteur_activite = form.secteur_activite.data
        type_contrat = form.type_contrat.data
        niveau_emplois = form.niveau_emplois.data
        description = form.description.data
        niveau_etude = form.niveau_etude.data
        experience = form.experience.data
        date_limit_candidature = form.date_limit_candidature.data
        ville = form.ville.data
        quartier = form.quartier.data
        nombre_poste = form.nombre_poste.data
        filename = file.filename
        file.save(os.path.join('./application/static/images/emplois', filename))
        #user=User(id=10,name="nom",email="email",password="password",role="role",image="filename")
        
        emplois=Emplois(libelle=libelle,secteur_activite=secteur_activite,type_contrat=type_contrat,niveau_emplois=niveau_emplois,description=description,pays="senegal",ville=ville,quartier=quartier,niveau_etude=niveau_etude,nombre_poste=nombre_poste,date_limit_candidature=date_limit_candidature,image=filename,experience=experience,user_id=current_user.id)
        #(libelle={self.libelle}, title={self.title}, description={self.description},pays={self.pays}, ville={self.ville}, quartier={self.quartier}, etat={self.etat}, image={self.image})
        add_Emplois(emplois)
        return redirect(url_for('compte'))
    #return render_template("front/immobilier/index.html")
    return render_template("back/create_emplois.html",form=form)

#authorisaion

login_manager = LoginManager()
login_manager.init_app(app)

principals = Principal(app)

# Définition des rôles
admin_role = RoleNeed('admin')
user_role = RoleNeed('user')

# Définition des permissions
admin_permission = Permission(admin_role)
user_permission = Permission(user_role)

# Définition de la fonction d'authentification
@login_manager.user_loader
def load_user(user_id):
    # Charger l'utilisateur depuis la base de données
    return getUserById(user_id)

# Définition de la fonction de déconnexion
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session['favories'] = []
    return redirect(url_for('index'))

# Vue protégée par une authentification et une autorisation
@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return 'Welcome to the admin page.'

# Vue protégée par une authentification et une autorisation
@app.route('/user')
@login_required
@user_permission.require(http_exception=403)
def user():
    return 'Welcome to the user page.'

#=============================================
#accees interdit
@app.errorhandler(401)
def forbidden(error):
    return render_template('errors/403.html')

@app.errorhandler(404)
def forbidden(error):
    return render_template('errors/404.html')


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html')

# Vue pour l'authentification
@app.route("/login",methods=['GET', 'POST'])
def login():
    form=ConnexionType()
    if form.validate_on_submit():
        email = form.email.data
        # Vérifier les informations d'authentification de l'utilisateur
        # Si l'authentification est réussie, appeler la fonction login_user
        #user = User.query.filter_by(email=email).first()
        user=getUserBuEmail(email)
        #if user and check_password_hash(user.password, request.form['password']):
        if user :
            login_user(user)
            session['favories'] = []
        # Changer l'identité de l'utilisateur pour inclure ses r
            return redirect(url_for('index'))
    return render_template("front/connexion/login.html",form=form)
#=======================================user==========================================================

#publishedEmplois
@app.route("/publishedEmploisById",methods=['GET', 'POST'])
def publishedEmploisById():
    if request.method == "POST": 
            id = request.form.get("idArtcle")
            task=findEmploisById(id)
            #print(f'task : {task}')
            publishedEmplois(task)
            return redirect(url_for('allEmploisUser'))
    return redirect(url_for('compte'))
#dePublishedEmploisById
@app.route("/dePublishedEmploisById",methods=['GET', 'POST'])
def dePublishedEmploisById():
    if request.method == "POST": 
            id = request.form.get("idArtcle")
            task=findEmploisById(id)
            #print(f'task : {task}')
            dePublisheEmplois(task)
            return redirect(url_for('allEmploisUser'))
    return redirect(url_for('compte'))



#publishedArticle
@app.route("/publishedArticle",methods=['GET', 'POST'])
def publishedArticleById():
    if request.method == "POST": 
            id = request.form.get("idArtcle")
            task=findTaskeById(id)
            #print(f'task : {task}')
            publishedArticle(task)
            return redirect(url_for('allArticleUser'))
    return redirect(url_for('compte'))
#dePublishedArticleById
@app.route("/dePublishedArticleById",methods=['GET', 'POST'])
def dePublishedArticleById():
    if request.method == "POST": 
            id = request.form.get("idArtcle")
            task=findTaskeById(id)
            #print(f'task : {task}')
            dePublishedArticle(task)
            return redirect(url_for('allArticleUser'))
    return redirect(url_for('compte'))

@app.route("/create_user",methods=['GET', 'POST'])
def create_user():
    form=UserType()
    if form.validate_on_submit():
        #file = request.files['file']
        email = form.email.data
        nom = form.name.data
        password = form.password.data
        #filename = file.filename
        role="user"
        #file.save(os.path.join('./application/static/images/users', filename))
        user=User(name=nom,email=email,password=password,role=role)
        #(libelle={self.libelle}, title={self.title}, description={self.description},pays={self.pays}, ville={self.ville}, quartier={self.quartier}, etat={self.etat}, image={self.image})
        add_user(user)
        return redirect(url_for('index'))
    #return render_template("front/immobilier/index.html")
    return render_template("front/connexion/register.html",form=form)

#updateImageToUser
@app.route("/updateImageUser",methods=['GET', 'POST'])
def updateImageUser():
    if request.method == "POST": 
        #title = request.form.get("title")
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('./application/static/images/users', filename))
        #current_user.image=file
        updateImageToUser(current_user.id,filename)
        #user=User(name=nom,email=email,password=password,role=role,image=filename)
        #(libelle={self.libelle}, title={self.title}, description={self.description},pays={self.pays}, ville={self.ville}, quartier={self.quartier}, etat={self.etat}, image={self.image})
        #add_user(user)
        return redirect(url_for('compte'))
    #return render_template("front/immobilier/index.html")
    return redirect(url_for('compte'))
#=======================================user==========================================================




"""
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
"""

#@app.route('/')
#@login_required
#def home():


