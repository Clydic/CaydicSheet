from flask import Flask, render_template
class Person:
    first_name = "Caydic"
    last_name = "Croc-Blanc"
    age = 25
    classe = "Paladin(lvl4), Barbare(lvl2), guerrier lupinae(lvl2), rôdeur(lvl4), bellimorphe(lvl4)"

Caydic = Person() 

caydic = {

    "first_name" : "Caydic",
    "last_name" : "Croc-Blanc",
    "age" : 25,
    "classe" : "Paladin(lvl4), Barbare(lvl2), guerrier lupinae(lvl2), rôdeur(lvl4), bellimorphe(lvl4)",
    "description" : "Caydic est un jeune homme de 26 ans portant une barbe brousailleux, des cheveux " + 
    "court, des yeux verts et une cicatrice au niveau du bras. Il est équipé d'un harnois fait d'écaille de " +
    "dragon, 3 épées à sa ceinture et son fidèle Pavois ainsi que d'autres équipements. De lui dégage "+
    "une aura bienveillante malgré son regard sérieux et son air farouche près à en découdre.",
    "bba" : 12,
    "CA" : 22,
    "CA dépourvu" : 22,
    "CA cac" : 11, 
    "for" : 17,
    "dex" : 13,
    "race" : "Humain",
    "pv_max" : "143 (DV 3d12 + 4d10 + 3d8 + 3d8 + (3 x 13) = 117, 2x13 = 26)"
    
}

weapon={
    "epee_longue" : {"name" : "épée longue de givre", "bonus" : 1, "degat": "1d8 froid + 1d6 froid" , "critique" : "19/20 x2" , "range" : "càc"},
    "epee_batarde" : {"name" : "épée bâtarde", "bonus" : 2, "degat": "1d10 feu + 1d6 feu" , "critique" : "19/20 x2" , "range" : "càc"},
    "arc_court" : {"name" : "arc court composite +3", "bonus" : 0, "degat": "1d6 + 1d6 foudre" , "critique" : "20 x3" , "range" : "distance"}
}

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello", #name=Caydic.last_name, 
    personnage=Caydic, pj= caydic , armes=weapon
    )
