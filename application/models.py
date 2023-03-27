from sqlalchemy import Column, Integer, String,Boolean,DateTime,Float,ForeignKey
from flask_login import UserMixin
from sqlalchemy.orm import relationship


from .config import Base,engine,Session
from .front import app
import os
from sqlalchemy import desc,asc
import datetime
#

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    role = Column(String(30), nullable=False)
    active = Column(Boolean(), default=True)
    image = Column(String(120), nullable=True)
    tasks = relationship('Task', backref='users', lazy=True)
    def get_id(self):
        return self.id
    def is_active(self):
        return self.active
    def __repr__(self):
        return f'<User(id={self.id},name={self.name}, email={self.email}, password={self.password}, role={self.role},image={self.image})>'
class Task(Base):
    __tablename__ = "tasks"  # Au cas ou on change le nom de la table
    #
    id = Column(Integer, primary_key=True)
    libelle = Column(String(100), nullable=False)#il peut etre mulimedia,maison,..
    title = Column(String(100), nullable=False)#Ordinateur,accesoire,...
    text = Column(String(100), nullable=False)#HP,Lenovo,etc
    description = Column(String(100), nullable=False)#ordinateur bureau hp prodesk 400 G1..
    pays = Column(String(200)) 
    ville = Column(String(255), nullable=False) #dakar,
    quartier = Column(String(200), nullable=False) #medina,..
    etat = Column(String(200), nullable=False) #neuf
    image = Column(String(100), nullable=False) #
    prix=Column(Float, nullable=False)
    published_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    published = Column(Boolean, default=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    #user_id = Column(Integer)
    def __repr__(self):
        return f'<Task(libelle={self.libelle}, title={self.title}, description={self.description},pays={self.pays}, ville={self.ville}, quartier={self.quartier}, etat={self.etat}, image={self.image}, prix={self.prix},user_id={self.user_id})>'
# Create the tables in the database
Base.metadata.create_all(engine)

# Add some data
session = Session()   


def add_user(user: User):
    session.add(user)
    session.commit()

def add_task(task: Task):
    session.add(task)
    session.commit()




#find by id task
def findTaskeById(id_task:int):
    #session.query(Task).get(id=id_task)
    return session.query(Task).filter(Task.id==id_task).first()

def getAllMaison():
    maisons=session.query(Task).filter_by(libelle="Maison").all()
    return maisons
#Vehicule
def getAllVehicule():
    vehicules=session.query(Task).filter_by(libelle="Vehicule").all()
    return vehicules
def getUserBuEmail(email:String):
    user=session.query(User).filter_by(email=email).first()
    return user
#return User.query.get(int(user_id))
def getUserById(id:int):
    user=session.query(User).get(int(id))
    return user
#========================================Immobilier============================
def getAllImmobilier():
    immobiliers=session.query(Task).filter_by(libelle="Immobilier").all()
    return immobiliers
#Appartements a louer
def getAppartementAlouer():
    return session.query(Task).filter_by(title="Appartement à louer").all()
#Appartements meublés
def getAppartementMeubler():
    return session.query(Task).filter_by(title="Appartement meublé ").all()
#Terrains à vendre
def getTerainsAVendre():
    return session.query(Task).filter_by(title="Terrains à vendre").all()
#Maison à vendre
def getMaisonAVendre():
    return session.query(Task).filter_by(title="Maison à vendre").all()
#Maison à louer
def getMaisonAlouer():
    return session.query(Task).filter_by(title="Maison à louer").all()
#Chambre à louer
def getChambreAlouer():
    return session.query(Task).filter_by(title="Chambre à louer").all()
#--ville
#all dakar
def getAllDakarImmobilier():
    return (session.query(Task).filter(Task.ville== "Dakar",Task.libelle=="Immobilier").all())
#all Touba
def getAllToubaImmobilier():
    return (session.query(Task).filter(Task.ville== "Touba",Task.libelle=="Immobilier").all())
#all Thies
def getAllThiesImmobilier():
    return (session.query(Task).filter(Task.ville== "Thies",Task.libelle=="Immobilier").all())
#---etat
#all Neuf
def getAllNeufImmobilier():
    return (session.query(Task).filter(Task.etat== "Neuf",Task.libelle=="Immobilier").all())
#all Venant
def getAllVenantImmobilier():
    return (session.query(Task).filter(Task.etat== "Venant",Task.libelle=="Immobilier").all())
#all Occasion
def getAllOccasionImmobilier():
    return (session.query(Task).filter(Task.etat== "Occasion",Task.libelle=="Immobilier").all())
#all Reconditionné
def getAllReconditionnéImmobilier():
    return (session.query(Task).filter(Task.etat== "Reconditionné",Task.libelle=="Immobilier").all())

#par date datetime.datetime.utcnow()
def getAllDateImmobilier():
    return session.query(Task).filter(Task.created_date== datetime.datetime.utcnow(),Task.libelle=="Immobilier").all()
#
def listerParPrixCroissantImmobilier():
    return session.query(Task).filter(Task.prix <= 10000,Task.libelle=="Immobilier").order_by(asc(Task.prix)).all()
#
def listerParPrixDecroissantImmobilier():
    return session.query(Task).filter(Task.prix>= 100000,Task.libelle=="Immobilier").order_by(desc(Task.prix)).all()
#tirer title
def listerPaTitleImmobilier(title:String):
   return session.query(Task).filter(Task.title==title,Task.libelle=="Immobilier").all()
#lister par itervalle de prix
def getAllPrixImmobiler(min:float,max:float):
     return session.query(Task).filter(Task.prix >= min, Task.prix <= max,Task.libelle=="Immobilier").all()

#==============================================================================================fin immobilier==========

#===========================prix========================
#all prix
def getAllPrix(min:float,max:float):
    #list = session.query(Task).filter_by(Task.prix >= min and Task.prix <= max).all()
    #list=vehicules=session.query(Task).filter_by(Task.prix>=min).all()
    #multimedias=session.query(Task).filter_by(libelle="Multimedia").all()
    return (session.query(Task).filter(Task.prix >= min, Task.prix <= max,Task.libelle=="Multimedia").all())
    

    
#=====================Multimedia===================================
#all multimedia
def getAllMultimedia():
    #multimedias = session.query(Task).all()
    #models = session.query.filter_by(Tasklibelle="Multimedia").all()
    multimedias=session.query(Task).filter_by(libelle="Multimedia").all()
    return multimedias
#all ordinateurs
def getAllOrdinateurs():
    ordinateurs=session.query(Task).filter_by(title="Ordinateur").all()
    return ordinateurs
#all tablettes
def getAllTablettes():
    tablettes=session.query(Task).filter_by(title="Tablettes").all()
    return tablettes
#all imprimantes
def getAllImprimante():
    imprimantes=session.query(Task).filter_by(title="Imprimante").all()
    return imprimantes
#all tv
def getAllTV():
    tvs=session.query(Task).filter_by(title="TV").all()
    return tvs
#all tv
def getAllTelephones():
    telephones=session.query(Task).filter_by(title="Telephones").all()
    return telephones
#all acceesoires
def getAllAccessoires():
    accessoires=session.query(Task).filter_by(title="Accessoires").all()
    return accessoires
#--ville
#all dakar
def getAllDakarMultimedia():
    return (session.query(Task).filter(Task.ville== "Dakar",Task.libelle=="Multimedia").all())
#all Touba
def getAllToubaMultimedia():
    return (session.query(Task).filter(Task.ville== "Touba",Task.libelle=="Multimedia").all())
#all Thies
def getAllThiesMultimedia():
    return (session.query(Task).filter(Task.ville== "Thies",Task.libelle=="Multimedia").all())
#---etat
#all Neuf
def getAllNeufMultimedia():
    return (session.query(Task).filter(Task.etat== "Neuf",Task.libelle=="Multimedia").all())
#all Venant
def getAllVenantMultimedia():
    return (session.query(Task).filter(Task.etat== "Venant",Task.libelle=="Multimedia").all())
#all Occasion
def getAllOccasionMultimedia():
    return (session.query(Task).filter(Task.etat== "Occasion",Task.libelle=="Multimedia").all())
#all Reconditionné
def getAllReconditionnéMultimedia():
    return (session.query(Task).filter(Task.etat== "Reconditionné",Task.libelle=="Multimedia").all())

#par date datetime.datetime.utcnow()
def getAllDateMultimedia():
    return session.query(Task).filter(Task.created_date== datetime.datetime.utcnow(),Task.libelle=="Multimedia").all()
#
def listerParPrixCroissant():
    return session.query(Task).filter(Task.prix <= 10000,Task.libelle=="Multimedia").order_by(asc(Task.prix)).all()
#
def listerParPrixDecroissant():
    return session.query(Task).filter(Task.prix>= 100000,Task.libelle=="Multimedia").order_by(desc(Task.prix)).all()
#tirer title
def listerPaTitleMultimedia(title:String):
   return session.query(Task).filter(Task.title==title,Task.libelle=="Multimedia").all()
#==============================================================================================================

"""
----------upload

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


<table class="table">
  <thead>
    <tr>
      <th>Product Name</th>
      <th>Price</th>
      <th>Image</th>
    </tr>
  </thead>
  <tbody>
    {% for product in products %}
    <tr>
      <td>{{ product.name }}</td>
      <td>{{ product.price }}</td>
      <td><img src="{{ url_for('static', filename='img/' + product.image) }}" height="50"></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

    -------------------
#add Multimedia
new_multimedia = Multimedia(libelle='ordinateur', title='pc',description="original",pays='tchad',
    ville="moussoro",image="xxx",etat="neuf")
session.add(new_multimedia)
session.commit()


new_contact = Contact(name='John Doe', email='johndoe@example.com')
session.add(new_contact)
session.commit()
# Query the data
users = session.query(Client).all()

for user in users:
    print(user)

# Update some data
user1.age = 26
session.commit()

# Delete some data
session.delete(user2)
session.commit()

# Close the session
session.close()


new_contact = Contact(name='John Doe', email='johndoe@example.com')
db.session.add(new_contact)
db.session.commit()
app.app_context().push()



    

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
new_multimedia = Multimedia(libelle='ordinateur', title='pc',description="original",pays='tchad',
    ville="moussoro",image="xxx",etat="neuf")
db.session.add(new_multimedia)
db.session.commit()
    
new_contact = Contact(name='John Doe', email='johndoe@example.com')
db.session.add(new_contact)
db.session.commit()
Ces étapes de base devraient vous permettre de créer et d'interagir avec une base de données Flask en utilisant Flask-SQLAlchemy. Bien sûr, cela ne couvre pas toutes les fonctionnalités possibles de Flask-SQLAlchemy ou de SQLAlchemy en général, mais c'est un bon point de départ.








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
