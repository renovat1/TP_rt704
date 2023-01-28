#! /usr/bin/python3
#-*-coding:utf8-*-

from flask import Flask  ,render_template
import json
app = Flask(__name__)


videotheque = {
    "proprietaire" : {
        "nom" : "Doe",
        "prenom" : "john"
    },
    "dernier_modif" : "08/06/2022",
    "films": [
        {
            "titre": "Pulp fiction",
            "annee": 1994,
            "realisateur": {
                "nom": "Tanrantino",
                "prenom": "Quentin"
            },
            "acteurs": [
                {
                    "nom": "Travolta",
                    "prenom": "John"
                },
                {
                    "nom": "Thurman",
                    "prenom": "Uma"
                },
                {
                    "nom": "Jackson",
                    "prenom": "Samuel L."
                }
            ]
        },
        {
            "titre": "Impitoyable",
            "annee": 1992,
            "realisateur": {
                "nom": "Eastwood",
                "prenom": "Clint"
            },
            "acteurs": [
                {
                    "nom": "Eastwood",
                    "prenom": "Clint"
                },
                {
                    "nom": "Ackman",
                    "prenom": "Gene"
                },
                {
                    "nom": "Freeman",
                    "prenom": "Morgan"
                }
            ]
        },
        {
            "titre": "Tigre et dragon",
            "annee": 2000,
            "realisateur": {
                "nom": "Lee",
                "prenom": "Ang"
            },
            "acteurs": [
                {
                    "nom": "Yun-Fat",
                    "prenom": "Chow"
                },
                {
                    "nom": "Yeoh",
                    "prenom": "Michelle"
                },
                {
                    "nom": "Ziyi",
                    "prenom": "Zhang"
                }
            ]
        },
        {
            "titre": "Le Secret des poignards volants",
            "annee": 2004,
            "realisateur": {
                "nom": "Yimou",
                "prenom": "Zhang"
            },
            "acteurs": [
                {
                    "nom": "Kaneshiro",
                    "prenom": "Takeshi"
                },
                {
                    "nom": "Lau",
                    "prenom": "Andy"
                },
                {
                    "nom": "Ziyi",
                    "prenom": "Zhang"
                }
            ]
        },
        {
            "titre": "Forrest Gump",
            "annee": 1994,
            "realisateur": {
                "nom": "Zemeckis",
                "prenom": "Robert"
            },
            "acteurs": [
                {
                    "nom": "Hanks",
                    "prenom": "Tom"
                },
                {
                    "nom": "Wright",
                    "prenom": "Robin"
                },
                {
                    "nom": "Sinise",
                    "prenom": "Gary"
                }
            ]
        },
        {
            "titre": "Lawrence d'Arabie",
            "annee": 1962,
            "realisateur": {
                "nom": "Lean",
                "prenom": "David"
            },
            "acteurs": [
                {
                    "nom": "O'Toole",
                    "prenom": "Peter"
                },
                {
                    "nom": "Sharif",
                    "prenom": "Omar"
                },
                {
                    "nom": "Guinness",
                    "prenom": "Alec"
                }
            ]
        },
        {
            "titre": "Le pacha",
            "annee": 1968,
            "realisateur": {
                "nom": "Lautner",
                "prenom": "Georges"
            },
            "acteurs": [
                {
                    "nom": "Gabin",
                    "prenom": "Jean"
                },
                {
                    "nom": "Carrel",
                    "prénom": "Dany"
                },
                {
                    "nom": "Pousse",
                    "prenom": "Andre"
                }
            ]
        },
        {
            "titre": "Le Bon, la Brute et le Truand",
            "annee": 1966,
            "realisateur": {
                "nom": "Leone",
                "prenom": "Sergio"
            },
            "acteurs": [
                {
                    "nom": "Eastwood",
                    "prenom": "Clint"
                },
                {
                    "nom": "Wallach",
                    "prenom": "Eli"
                },
                {
                    "nom": "Van Cleef",
                    "prenom": "Lee"
                }
            ]
        },
        {
            "titre": "Les tontons flingueurs",
            "annee": 1963,
            "realisateur": {
                "nom": "Lautner",
                "prenom": "Georges"
            },
            "acteurs": [
                {
                    "nom": "Ventura",
                    "prenom": "Lino"
                },
                {
                    "nom": "Blier",
                    "prenom": "Bernard"
                },
                {
                    "nom": "Blanche",
                    "prenom": "Francis"
                }
            ]
        },
        {
            "titre": "Les Blues Brothers",
            "annee": 1980,
            "realisateur": {
                "nom": "Landis",
                "prenom": "John"
            },
            "acteurs": [
                {
                    "nom": "John",
                    "prenom": "Belushi"
                },
                {
                    "nom": "Akroyd",
                    "prenom": "Dan"
                },
                {
                    "nom": "Brown",
                    "prenom": "James"
                }
            ]
        }
    ]
}
#@app.route("/")

@app.get("/videotheques") 
def get_videotheques():
    # return {"videotheque": videotheque}
    print("Started writing JSON data into a file")
    with open("videotheque.json", "w") as videotheque_file:
        json.dump(videotheque,videotheque_file, indent=4, separators=(", ", ": "), sort_keys=True) # encode dict into JSON
    print("Done writing JSON data into .json file")
    return json.dumps(videotheque["films"])


@app.route("/films",methods=['GET'])
def get_films():
    videotheques = get_videotheques()
    f = open('videotheque.json','r')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
   
    # Iterating through the json
    # list

    films = []
    if data['films'] is not None:
        print ("len videotheque", len (data))
        for film in data['films']:
            print (film)
        
            films.append (film)
    #return  {"films": films}
    return json.dumps(films)

    if __name__ == '__main__':
        app.run(debug=True, port=5001)
        print("apif start!")





