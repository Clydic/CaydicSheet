from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello", #name=Caydic.last_name, 
    personnage=Caydic, pj= caydic , armes=weapon, armor = harmor, ca=CA,
                           sauvegardes=JS, modificateur=modif
    )



