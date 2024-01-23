from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "matthewhunt"


@app.route("/")
def start():

    if "gold_count" not in session:
        session["gold_count"] = 0

    if "act_log" not in session:
        print("Nothing Here")
        session["act_log"] = []


    act_log = session["act_log"]

    gold_count = session["gold_count"]

    return render_template("ninja_gold.html", act_log = act_log, gold_count = gold_count)

@app.route("/process_money", methods=["POST"])
def get_gold():

    if request.form["button"] == "farm":
        gamble = random.randrange(1,3)
        if gamble == 1:
            goldval = random.randrange(10,21)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'> You've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session.modified = True
            session["gold_count"] += goldval
        if gamble == 2:
            goldval = random.randrange(10,21)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='redtext'> You lose %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval


    if request.form["button"] == "cave":
        gamble = random.randrange(1,3)
        if gamble == 1:
            goldval = random.randrange(5,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'> Found %s gold!  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if gamble == 2:
            goldval = random.randrange(5,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='redtext'> Lost %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "house":
        gamble = random.randrange(1,3)
        if gamble == 1:
            goldval = random.randrange(2,6)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'> You earned %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if gamble == 2:
            goldval = random.randrange(2,5)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='redtext'> You lose %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "casino":
        gamble = random.randrange(1,3)
        if gamble == 1:
            goldval = random.randrange(0,51)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'> You won %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval

        if gamble == 2:
            goldval = random.randrange(0,51)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='redtext'> you've lost %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval




    return redirect("/")

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")




if __name__=="__main__":

    app.run(debug=True)