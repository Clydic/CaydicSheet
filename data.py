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
    "bracelet_force" : {"name" : "Bracelet de force", "bonus" : 2},
    "ceinture_dex" : {"name" : "Ceinture de dextérité", "bonus" : 2},
    "amulette_cons" : {"name" : "Amulette de constitution", "bonus" : 4},
    "botte_patinage" : {"name" : "Botte de patinage", "bonus" : 0},
    "anneau_resistance" : {"name" : "Anneau de resistance" , "bonus" : 3},
    "anneau de pistage" :{"name" : "Anneau de pistage" , "bonus" : 5},
    "bandeau_charisme" : {"name" : "Bandeau de charisme" , "bonus" : 2}
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
    "dex" : 10 + magic_item['ceinture_dex']['bonus'],
    "con" : 16 + magic_item['amulette_cons']['bonus'],
    "sag" : 8,
    "intel" : 13,
    "cha" : 14 + magic_item['bandeau_charisme']['bonus'] ,
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

competences=[
    {"name" : "saut" , "maitrise" : 13, "carac" : "for", "spécialité" : [ ("saut en longueur", 3) ] },
    {"name" : "survie" , "maitrise" : 13, "carac" : "sag", "spécialité" : [] },
    {"name" : "escalade" , "maitrise" : 13, "carac" : "for","spécialité" : []  },
    {"name" : "connnaissance religion" , "maitrise" : 13, "carac" : "intel" },
    {"name" : "connnaissance nature" , "maitrise" : 13, "carac" : "intel" },
    {"name" : "connnaissance geographie" , "maitrise" : 13, "carac" : "intel" },
    {"name" : "connnaissance sousterrain" , "maitrise" : 13, "carac" : "intel" },
    {"name" : "connnaissance mystère" , "maitrise" : 13, "carac" : "intel" },
    {"name" : "connnaissance plan" , "maitrise" : 13, "carac" : "intel" },
    
]

general_don = [
    {"name" : "Expertise du combat" , "description" : "1 -> 5 maluse de jet de jet et bonus à la CA"},
    {"name" : "Science du croque en jambe" , "description" : "+4 au test de croc en jambe"},
    {"name" : "Attaque en puissance" , "description" : "1 -> Niveau global du perso : bonus de dégât et malus au jet d'attaque"},
    {"name" : "Arme de prédilection (épée bâtarde)" , "description" : "+1 au jet d'attaque lorsque équipée de l'épée bâtarde"},
    {"name" : "Attaque sauté" , "description" : "Double les dégâts de l'attaque en puissance"},
    {"name" : "Rage supplémentaire" , "description" : "+2 utilisation de rage quotidienne"},
    {"name" : "Bouclier Divin" , "description" : "Action simple, sacrifie un renvoie de mort-vivant pour ajouter modif charisme à la CA"},
]

class_aptitude = {
    "barbare" : {
            "name" : "Barbare" , "aptitudes" : [
                {"name": "rage" , "description" : "Force +4, Con +4, volonté +2, CA -2, dure Constitution + 3 rounds"},
                {"name" : "Esquive insteinctive", "description" : "CA dépourvu = CA"},
    ]
    },
    "rodeur" : {
        "name" : "Rôdeur",
        "aptitudes" : [

            {"name" : "empathie sauvage", "description" : "1d20 + lvl rôdeur + cha"},
            {"name" : "pistage", "description" : "Utilisation de survie pour pister" },
            {"name" : "Maniement à deux armes", "description" : "Peut se battre avec deux armes avec malus réduit" },
            {"name" : "ennemi juré(créature magique)", "description" : "bonus +2 dégât, bluff, perception auditive, psychologie, survie, détection" },
            {"name" : "Endurance", "description" : "Peut dormir avec son Harnois" },

        ]
    },
    "paladin_of_freedom" : {
            "name" : "Paladin de la liberté" , "aptitudes" : [

                {"name" : "Aura de bien", "description" : "" },
                {"name" : "châtiment du mal(1/j)", "description" : ""},
                {"name" : "Détection du mal", "description" : ""},
                {"name" : "Grâce divine", "description" : "" },
                {"name" : "imposition divine (26pv)", "description" : "" },
                {"name" : "Aura de détermination", "description" : "Immunité contre coerciction, +4 moral au alliées contre ceux-ci" },
                {"name" : "Santé divine", "description" : "Immuité contre les maladies" },
                {"name" : "Destrier" , "description" : "Peut appeler un Destrier" },
                {"name" : "Renvoie de mort vivant" , "description" : "Peut renvoyer les morts vivants 3+2+1 = 6 par jour" },
    ]},
    "bellimorphe" : {"name" : "Bellimorphe" , "aptitudes": [

        {"name" : "Armes morphiques" , "description" : "Peut faire apparaître des armes naturrlles différentes de sa forme" },
        {"name" : "Immunité morphique", "description" : "Immunité au coup critique et aux étourdissement lorsque transformé" },
        {"name" : "Corp morphique", "description" : "+ 4 Force, +4 Constitution volonté +2 " },
        {"name" : "allonge morphique" , "description" : "Lorsque transformé augement la portée de 1m50" },
    ] },
    "guerrier_lupdide" : {"name" : "Guerrier lupidé" , "aptitudes" :[

        {"name" : "Transformation lupidé (Jeune Loup Artique taille M)" , "description" : "Lors d'une utilisation de rage, For +6, Con +4, Vol +2" },
    ]}

}
