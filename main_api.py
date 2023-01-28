from flask import Flask ,render_template
import requests, json

app= Flask(__name__)

@app.route('/afficher_films')
def get_afficher(name=None):
    req=requests.get('http://127.0.0.1:5001/films')
    data=json.loads(req.content)
    print(req.content)

    return render_template('afficher_films.html', data=data)



        #creation de demmarrage de l'API
if __name__ == '__main__':
    app.run(debug=True)
    print("api start!")

