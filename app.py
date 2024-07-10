from flask import Flask, render_template
from data import *
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET','POST'])
def hello_world():
    names = ['Bart', 'Lisa', 'Homer']
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    dons={"general" : general_don, "class":class_aptitude}
    return render_template("index.html", title="Hello", #name=Caydic.last_name, 
    personnage=Caydic, pj= caydic ,  armor = harmor, ca=CA,
                           sauvegardes=JS, modificateur=modif, competence_don_title="Compétence et don",
                           competence_title="Compétence",don_title="Dons", competences=competences, 
                           dons=dons, names=names, potions=potions, weapons=weapon

    )



