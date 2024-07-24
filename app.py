from flask import Flask, render_template, redirect, url_for
from data import *
import os


app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'



@app.route("/", methods=['GET','POST'])
def hello_world():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    dons={"general" : general_don, "class":class_aptitude}
    return render_template("index.html", title="Hello", #name=Caydic.last_name, 
                            pj= caydic , artic_wolf = artic_wolf,  armor = harmor,
                           ca=CA, sauvegardes=JS, modificateur=modif,
                           competence_don_title="Compétence et don",
                           competence_title="Compétence", don_title="Dons",
                           competences=competences, 
                           dons=dons,
                            potions=potions, weapons=weapon, bag_title="Les objets",
                           mei=mei, author=os.getenv("NOM", "Author")

    )



if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000) 