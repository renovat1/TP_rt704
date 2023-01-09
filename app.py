
#! /usr/bin/python3


from flask import Flask  #render_templates

app = Flask(__name__)


videotheque = {
    "proprietaire" : {
        "nom" : "Doe",
        "prénom" : "john"
    },
    "dernère_modif" : "08/06/2022",
    "films": [
        {
            "titre": "Pulp fiction",
            "année": 1994,
            "réalisateur": {
                "nom": "Tanrantino",
                "prénom": "Quentin"
            },
            "acteurs": [
                {
                    "nom": "Travolta",
                    "prénom": "John"
                },
                {
                    "nom": "Thurman",
                    "prénom": "Uma"
                },
                {
                    "nom": "Jackson",
                    "prénom": "Samuel L."
                }
            ]
        },
        {
            "titre": "Impitoyable",
            "année": 1992,
            "réalisateur": {
                "nom": "Eastwood",
                "prénom": "Clint"
            },
            "acteurs": [
                {
                    "nom": "Eastwood",
                    "prénom": "Clint"
                },
                {
                    "nom": "Ackman",
                    "prénom": "Gene"
                },
                {
                    "nom": "Freeman",
                    "prénom": "Morgan"
                }
            ]
        },
        {
            "titre": "Tigre et dragon",
            "année": 2000,
            "réalisateur": {
                "nom": "Lee",
                "prénom": "Ang"
            },
            "acteurs": [
                {
                    "nom": "Yun-Fat",
                    "prénom": "Chow"
                },
                {
                    "nom": "Yeoh",
                    "prénom": "Michelle"
                },
                {
                    "nom": "Ziyi",
                    "prénom": "Zhang"
                }
            ]
        },
        {
            "titre": "Le Secret des poignards volants",
            "année": 2004,
            "réalisateur": {
                "nom": "Yimou",
                "prénom": "Zhang"
            },
            "acteurs": [
                {
                    "nom": "Kaneshiro",
                    "prénom": "Takeshi"
                },
                {
                    "nom": "Lau",
                    "prénom": "Andy"
                },
                {
                    "nom": "Ziyi",
                    "prénom": "Zhang"
                }
            ]
        },
        {
            "titre": "Forrest Gump",
            "année": 1994,
            "réalisateur": {
                "nom": "Zemeckis",
                "prénom": "Robert"
            },
            "acteurs": [
                {
                    "nom": "Hanks",
                    "prénom": "Tom"
                },
                {
                    "nom": "Wright",
                    "prénom": "Robin"
                },
                {
                    "nom": "Sinise",
                    "prénom": "Gary"
                }
            ]
        },
        {
            "titre": "Lawrence d'Arabie",
            "année": 1962,
            "réalisateur": {
                "nom": "Lean",
                "prénom": "David"
            },
            "acteurs": [
                {
                    "nom": "O'Toole",
                    "prénom": "Peter"
                },
                {
                    "nom": "Sharif",
                    "prénom": "Omar"
                },
                {
                    "nom": "Guinness",
                    "prénom": "Alec"
                }
            ]
        },
        {
            "titre": "Le pacha",
            "année": 1968,
            "réalisateur": {
                "nom": "Lautner",
                "prénom": "Georges"
            },
            "acteurs": [
                {
                    "nom": "Gabin",
                    "prénom": "Jean"
                },
                {
                    "nom": "Carrel",
                    "prénom": "Dany"
                },
                {
                    "nom": "Pousse",
                    "prénom": "André"
                }
            ]
        },
        {
            "titre": "Le Bon, la Brute et le Truand",
            "année": 1966,
            "réalisateur": {
                "nom": "Leone",
                "prénom": "Sergio"
            },
            "acteurs": [
                {
                    "nom": "Eastwood",
                    "prénom": "Clint"
                },
                {
                    "nom": "Wallach",
                    "prénom": "Eli"
                },
                {
                    "nom": "Van Cleef",
                    "prénom": "Lee"
                }
            ]
        },
        {
            "titre": "Les tontons flingueurs",
            "année": 1963,
            "réalisateur": {
                "nom": "Lautner",
                "prénom": "Georges"
            },
            "acteurs": [
                {
                    "nom": "Ventura",
                    "prénom": "Lino"
                },
                {
                    "nom": "Blier",
                    "prénom": "Bernard"
                },
                {
                    "nom": "Blanche",
                    "prénom": "Francis"
                }
            ]
        },
        {
            "titre": "Les Blues Brothers",
            "année": 1980,
            "réalisateur": {
                "nom": "Landis",
                "prénom": "John"
            },
            "acteurs": [
                {
                    "nom": "John",
                    "prénom": "Belushi"
                },
                {
                    "nom": "Akroyd",
                    "prénom": "Dan"
                },
                {
                    "nom": "Brown",
                    "prénom": "James"
                }
            ]
        }
    ]
}
#@app.route("/")

@app.get("/environments/tp704/videotheque") # http://127.0.0.1:5000/environments/tp704/videotheque
def get_videotheque():
    return {"videotheque": videotheque}


@app.get("/environments/tp704/films")
def get_films():
    videotheques= get_videotheque()
    films = []
    for i in range (len (videotheque)):
        films.append (videotheque[i].films)
    return  {"films": films}




@app.get("/environments/tp704/actors")
def get_actors():
    # videotheques= get_videotheque()
    films = get_films()
    actors = []
    for i in range (len (films)):
        actors.append (films[i].acteurs)
    return  {"actors": actors}




