from flask import Flask ,render_template,request, jsonify
from flask_wtf import FlaskForm
import requests, json

app= Flask(__name__)

@app.route('/')
def page_acceuil():
	return render_template('page_acceuil.html')


@app.route('/afficher_films')
def get_afficher(name=None):
    req=requests.get('http://127.0.0.1:5001/films')
    data=json.loads(req.content)
    print(req.content)

    return render_template('afficher_films.html', data=data)

###############################################################################33



@app.route('/get/<name>/<years>', methods=['GET'])
def get_Info(titre, annee):
    return "le titre de film est:  " + titre + "modifié en  " + annee

#Ajouter un film

"""

films = []

@app.route('/post_films', methods=['POST'])
def add_film():
    data = request.get_json()
    films.append(data)
    return jsonify({'message': 'Film ajouté avec succès!'}), 201

class FilmForm(FlaskForm):
    titre = StringField('Title', validators=[DataRequired()])
    annee = DateField('Release Date', validators=[DataRequired()])
    realisateurnom = TextAreaField('Description', validators=[DataRequired()])
    realisateurprenom = TextAreaField('Description', validators=[DataRequired()])

@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    form = FilmForm()
    if form.validate_on_submit():
        titre = form.title.data
        realisateurnom = form.description.data
        realisateurprenom = form.description.data
        annee = form.release_date.data

        # Ajoutez les informations du film à votre base de données ou à votre fichier JSON ici.
        return redirect('/films')
    return render_template('post_film.html', form=form)
"""

#creation de demmarrage de l'API   
if __name__ == '__main__':
    app.run(debug=True)
    print("api start!")


