class Person:
    first_name = "Caydic"
    last_name = "Croc-Blanc"
    age = 25
    classe = "Paladin(lvl4), Barbare(lvl2), guerrier lupinae(lvl2), rôdeur(lvl4), bellimorphe(lvl4)"
    force = 17
    dexterite = 12
    constitution = 16
    bba = 12
    CA = 22
    CA_depourvu = 22
    CA_cac = 11
    allonge = 3

    def getModif(self, carac):
        return int((carac-10)/2)

def modif(carac):
    return (carac-10)//2

Caydic = Person() 



magic_item = {
    "bracelet_force" : {"name" : "Bracelet de force", "bonus" : 2}
}

weapon={
    "epee_longue" : {"name" : "épée longue de givre", "bonus" : 0, "degat": "1d8 froid + 1d6 froid" , "critique" : "19/20 x2" , "range" : "càc"},
    "epee_batarde" : {"name" : "épée bâtarde", "bonus" : 1, "degat": "1d10 feu + 1d6 feu" , "critique" : "19/20 x2" , "range" : "càc"},
    "arc_court" : {"name" : "arc court composite +3", "bonus" : 0, "degat": "1d6 + 1d6 foudre" , "critique" : "20 x3" , "range" : "distance"},
    "marteau_saint" : {"name" : "Marteau de Gurre Saint", "bonus" : 0, "degat": "1d8 + 2d6 saint" , "critique" : "20 x3" , "range" : "càc"},
    "epee_argent" : {"name" : "épée longue en argent", "bonus" : 0, "degat": "1d8-1" , "critique" : "19/20 x2" , "range" : "càc"},
}

# Model of harmor {"name" : "" , "bonus_ca": 0 "type": ""}

harmor={ 
    "harnois" : {"name" : "Harnois" , "bonus_ca": 8, "type": "amure lourde"},
    "cuirrasse": {"name" : "Cuirrasse" , "bonus_ca": 5, "type": "amure intermédiaire"},
    "pavois" : {"name" : "Pavois" , "bonus_ca": 5, "type": "Bouclier"}
}


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
    "for" : 18 + magic_item['bracelet_force']['bonus'],
    "dex" : 10 + 2,
    "con" : 16 + 4,
    "sag" : 8,
    "intel" : 13,
    "cha" : 14 + 2, 
    "race" : "Humain",
    "pv_max" : "143 (DV 3d12 + 4d10 + 3d8 + 3d8 + (3 x 13) = 117, 2x13 = 26)",
    "allonge" : 1.5,
    "espace_occupe" : 1.5,
    "vm" : 12,
    "ref" : 6,
    "vig" : 8,
    "vol" : 4
    
}

CA = {
    "harnois" : (10 + modif(caydic['dex'])) + harmor[ "harnois" ]["bonus_ca"]+harmor[ "pavois" ]["bonus_ca"] ,
    "cuirrasse" : (10 + modif(caydic['dex'])) + harmor[ "cuirrasse" ]["bonus_ca"]+harmor[ "pavois" ]["bonus_ca"] ,
}

JS={
    "ref":{"name":"Réflexe" , "value" : caydic['ref'] + modif(caydic['dex'])} ,
    "vig": {"name":"Vigueur" , "value" : caydic['vig'] + modif(caydic['con'])},
    "vol": {"name":"Volonté" , "value" : caydic['vol'] + modif(caydic['sag'])},
}
