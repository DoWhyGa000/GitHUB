from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    nazivSpiska = "Spisak restorana"
    spisakRestorana = ["Pastica", "Pica Tim", "HasHub", "Sahara", "ABC", "Lele", "Oskar", "Cap Cap", "Promenada"]
    return render_template("index.html", naziv=nazivSpiska, spisak=spisakRestorana)

@app.route("/restorani")
def restorani():
    nazivRestorana = "Svi restorani"
    spisakRestorani = ["Pastica", "Pica Tim", "HasHub", "Sahara", "ABC", "Lele", "Oskar", "Cap Cap", "Promenada"]
    return render_template("restorani.html", naziv=nazivRestorana, spisak=spisakRestorani)

@app.route("/restorani/1")
def meni():
    nazivMeni = "Meni restorana Pica Tim"
    spisakMeni = ["Pica Margarita", "Pica Capricciosa", "Pica Vesuvio", "Pica Quattro Stagioni", "Pica Napolitana"]
    return render_template("meni.html", naziv=nazivMeni, spisak=spisakMeni)

@app.route("/primer-niz")
def niz():
    nekiNiz = [1, 2, 3, 4, 5]
    return jsonify(nekiNiz)

@app.route("/primer-json")
def primerJson():
    data = {"message": "This is a JSON response", "status": "success"}
    return jsonify(data)

@app.route("/primer-html")
def primerHTML():
    data = """
    <!DOCTYPE html>
    <html lang="sr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Primer HTML</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container sredina">
            <h1>Zdravo programeri</h1>
            <p>Ovo je primer HTML stranice</p>
            <a href="/" class="btn">Nazad na početnu</a>
        </div>
    </body>
    </html>
    """
    return data

if __name__ == "__main__":
    app.run(debug=True)