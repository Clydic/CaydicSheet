from flask import Flask, render_template, redirect, url_for
from data import *
import os


app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'



def toggle(is_active):
    return not is_active

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    dons = {"general": general_don, "class": class_aptitude}

    is_active = True
    return render_template("index.html", title="Hello",  # name=Caydic.last_name,
                           pj=caydic, artic_wolf=artic_wolf,  armor=harmor,
                           ca=CA, sauvegardes=JS, modificateur=modif,
                           competences=competences,
                           dons=dons,
                           potions=potions, weapons=weapon, bag_title="Les objets",
                           mei=mei, author=os.getenv("NOM", "Author"), items=other_item,
                           giant_caydic=giant_caydic,
                           giant_weapons=giant_weapons,
                           magic_items=magic_item,
                           magic_equipments=magic_equipment,
                           is_active=is_active, toggle=toggle


                           )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234)
