from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "hemlig_nyckel"  # Krävs för sessionshantering

words = ["äpple", "banan", "druva", "bil", "skumtomte", "bamse", "skola"]

@app.route("/", methods=["GET", "POST"])
def game():
    # Om spelet ska starta om eller är nytt
    if "word" not in session or request.form.get("new_game"):
        session["word"] = random.choice(words)
        session["lives"] = 10
        session["guessed_letters"] = []
        session["display_word"] = ["_" for _ in session["word"]]
        return redirect(url_for("game"))

    # Om en gissning görs
    if request.method == "POST" and "letter" in request.form:
        letter = request.form["letter"].lower()

        # Kontrollera att gissningen är giltig och inte redan gissad
        if letter and len(letter) == 1 and letter not in session["guessed_letters"]:
            session["guessed_letters"].append(letter)

            # Uppdatera display_word baserat på alla gissade bokstäver
            session["display_word"] = [
                char if char in session["guessed_letters"] else "_" for char in session["word"]
            ]

            # Minska liv om bokstaven inte finns i ordet
            if letter not in session["word"]:
                session["lives"] -= 1

        # Kontrollera om spelet är slut
        if "_" not in session["display_word"]:
            return redirect(url_for("win"))
        if session["lives"] <= 0:
            return redirect(url_for("lose"))

    return render_template("index.html", 
                           display_word=" ".join(session["display_word"]),
                           lives=session["lives"],
                           guessed_letters=", ".join(session["guessed_letters"]))

@app.route("/win")
def win():
    return render_template("win.html", word=session["word"])

@app.route("/lose")
def lose():
    return render_template("lose.html", word=session["word"])

if __name__ == "__main__":
    app.run(debug=True)
