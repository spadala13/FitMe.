import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helper import login_required

# Configure application
app = Flask(__name__)


EXERCISES = [
    "Cardio",
    "Weight Lifting",
    "Muscle Strengthening",
    "Flexibility",
    "Swimming",
    "Walking",
    "Other"
]


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1:
            flash("Username is not registered.")
            return redirect(request.url)
        elif not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid password")
            return redirect(request.url)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Select row in database for the inputted username
        row = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username") )

        # Check the validity of the username
        if len(row) != 0:
            flash("Username is taken. Please choose another one.")
            return redirect(request.url)

        # Check the validity of the password
        elif request.form.get("confirmation") != request.form.get("password"):
            flash("Passwords do not match")
            return redirect(request.url)

        # Register user into the database
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :password)",
        username = request.form.get("username"), password = generate_password_hash(request.form.get("password")) )

        # Redirect users to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    names=[]
    types=[]
    dates=[]
    reps=[]
    stimes=[]
    etimes=[]
    calories=[]
    colors=[]

    if request.method == "GET":
        rows = db.execute("SELECT * FROM recipes WHERE id=:username ORDER BY date DESC", username=session["user_id"])

        for row in rows:
            names.append(row["name"])
            types.append(row["type"])
            if row["type"] == "Cardio":
                colors.append("table-primary")
            elif row["type"] == "Weight Lifting":
                colors.append("table-success")
            elif row["type"] == "Muscle Strengthening":
                colors.append("table-danger")
            elif row["type"] == "Flexibility":
                colors.append("table-warning")
            elif row["type"] == "Swimming":
                colors.append("table-info")
            elif row["type"] == "Walking":
                colors.append("table-primary")
            elif row["type"] == "Other":
                colors.append("table-dark")
            else:
                colors.append("table-active")
            dates.append(row["date"])
            reps.append(row["reps"])
            stimes.append(row["starttime"])
            etimes.append(row["endtime"])
            calories.append(row["totalburned"])

        length = len(names)
        return render_template ("dashboard.html", names=names, types=types, dates=dates, reps=reps, stimes=stimes, etimes=etimes, length=length, colors=colors, calories=calories)

    else:
        search = request.form.get("search")
        username = session["user_id"]
        rows = db.execute("SELECT * FROM recipes WHERE name=? IN (SELECT id FROM recipes WHERE id=?)", search, username)

        if len(rows) == 0:
            flash("Invalid Name")
            return redirect("/dashboard")

        for row in rows:
            names.append(row["name"])
            types.append(row["type"])
            if row["type"] == "Cardio":
                colors.append("table-danger")
            elif row["type"] == "Weight Lifting":
                colors.append("table-danger")
            elif row["type"] == "Muscle Strengthening":
                colors.append("table-warning")
            elif row["type"] == "Flexibility":
                colors.append("table-success")
            elif row["type"] == "Swimming":
                colors.append("table-info")
            elif row["type"] == "Walking":
                colors.append("table-primary")
            elif row["type"] == "Other":
                colors.append("table-dark")
            else:
                colors.append("table-active")
            dates.append(row["date"])
            reps.append(row["reps"])
            stimes.append(row["starttime"])
            etimes.append(row["endtime"])
            calories.append(row["totalburned"])

        length = len(names)
        return render_template ("dashboard.html", names=names, types=types, dates=dates, reps=reps, stimes=stimes, etimes=etimes, length=length, colors=colors, calories=calories)



@app.route('/addexercise', methods=['GET', 'POST'])
@login_required
def addexercise():
    if request.method == "POST":
        name = request.form.get("name")
        select = request.form.get("type")
        date = request.form.get("date")
        reps = request.form.get("reps")
        stime = request.form.get("stime")
        etime = request.form.get("etime")
        calories = request.form.get("calories")

        if request.form.get("type") not in EXERCISES:
            flash("Please select the correct type")
            return render_template ("addexercise.html", exercises=EXERCISES)

        db.execute("INSERT INTO recipes (id,name,type,date,reps, starttime, endtime, totalburned) VALUES(:username,:name,:exercise,:date,:reps, :starttime, :endtime, :totalburned)", username=session["user_id"], name=name, exercise=select, date=date, reps=reps, starttime=stime, endtime=etime, totalburned=calories)
        return redirect("/home")
    else:
        return render_template ("addexercise.html", exercises=EXERCISES)



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/")
def homepage():
    return render_template("homepage.html")



@app.route("/home")
@login_required
def home():
    cardio = 0
    lifting = 0
    muscle= 0
    flexibility = 0
    swimming = 0
    walking = 0
    other = 0
    total = 0

    rows = db.execute("SELECT * FROM recipes WHERE id=:username", username=session["user_id"])
    for row in rows:
        if row["type"] == "Cardio":
            cardio += 1
            total += row["totalburned"]
        elif row["type"] == "Weight Lifting":
            lifting += 1
            total += row["totalburned"]
        elif row["type"] == "Muscle Strengthening":
            muscle += 1
            total += row["totalburned"]
        elif row["type"] == "Flexibility":
            flexibility += 1
            total += row["totalburned"]
        elif row["type"] == "Swimming":
            swimming += 1
            total += row["totalburned"]
        elif row["type"] == "Walking":
            walking += 1
            total += row["totalburned"]
        elif row["type"] == "Other":
            other += 1
            total += row["totalburned"]


    return render_template("home.html", total=total, cardio=cardio, lifting=lifting, muscle=muscle, flexibility=flexibility, swimming=swimming, walking=walking, other=other)



