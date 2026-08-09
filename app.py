import os
import random
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if "attempts" not in session:
        session["attempts"] = 0
    if "max_attempts" not in session:
        session["max_attempts"] = 5
    if "num" not in session:
        session["num"] = random.randint(1, 100)

    if request.method == "POST":
    
        if session["attempts"] < session["max_attempts"]:
            try:
                
                guess = int(request.form.get("guess", 0))
                session["attempts"] += 1

                
                if guess > session["num"]:
                    message = "lol too high" if guess >= session["num"] + 10 else "maybe try a little lower"
                elif guess < session["num"]:
                    message = "lol too low" if guess <= session["num"] - 10 else "maybe try a little higher"
                else:
                    message = "WAY TO GO YOU WON!! 🎉"

            except (ValueError, TypeError):
                message = "Please enter a valid integer."
        else:
            message = "You've used all attempts! Would you like a hint to continue?"

    return render_template(
        "game.html",
        message=message,
        attempts=session["attempts"],
        hint=session.get("hint", "")
    )


@app.route("/reset", methods=["POST"])
def reset():
   
    session.clear() 
    return redirect(url_for("home"))


@app.route("/hint", methods=["POST"])
def hint():
    
    target_num = session.get("num", random.randint(1, 100))
    
    lower = max(1, target_num - 3)
    upper = min(100, target_num + 3)
    
    session["hint"] = f"The number lies between {lower} and {upper}."
    session["max_attempts"] = session.get("max_attempts", 5) + 5
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
