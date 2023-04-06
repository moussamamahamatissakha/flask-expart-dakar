from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,FloatField,EmailField,PasswordField,FileField,DateTimeField,IntegerField,BooleanField,SelectField,HiddenField
from wtforms.validators import DataRequired

class TaskType(FlaskForm):
    libelle = SelectField('Libelle', choices=[('Multimedia', 'Multimedia'), ('Immobilier', 'Immobilier'), ('Maison', 'Maison'), ('Vehicule', 'Vehicule')])
    titre = StringField('Titre', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    etat= SelectField('Etat', choices=[('Neuf', 'Neuf'), ('Reconditionné', 'Reconditionné'), ('Occasion', 'Occasion'), ('Venant', 'Venant')])
    ville= SelectField('Ville', choices=[('Dakar', 'Dakar'), ('Thies', 'Thies'), ('Ziguinchor', 'Ziguinchor'), ('Touba', 'Touba')])
    quartier= SelectField('Quartier', choices=[('Medina', 'Medina'), ('Fass', 'Fass'), ('Pont E', 'Pont E')])
    prix = FloatField('Prix', validators=[DataRequired()])
    submit = SubmitField('Enregister')
#form emplois
class EmploisType(FlaskForm):
    libelle = StringField('Libelle', validators=[DataRequired()])
    secteur_activite = StringField('Secteur Activite')
    type_contrat = StringField('Type Contrat')
    niveau_emplois = StringField('Niveau Emplois')
    description = TextAreaField('Description',validators=[DataRequired()])
    niveau_etude = StringField('Niveau Etude')
    experience = StringField('Experience')
    date_limit_candidature=StringField('Date Limit')
    ville= SelectField('Ville', choices=[('Dakar', 'Dakar'), ('Thies', 'Thies'), ('Ziguinchor', 'Ziguinchor'), ('Touba', 'Touba')])
    quartier= SelectField('Quartier', choices=[('Medina', 'Medina'), ('Fass', 'Fass'), ('Pont E', 'Pont E')])
    nombre_poste = IntegerField('nombre_poste')
    submit = SubmitField('Enregister')
#userType
class UserType(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Paswword', validators=[DataRequired()])
    submit = SubmitField('Enregister')
#form user connexion
class ConnexionType(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Enregister')


