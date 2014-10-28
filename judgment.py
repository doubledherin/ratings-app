from flask import Flask, render_template, redirect, request, flash
import model


app = Flask(__name__)
app.secret_key = "ADFLKASDJF"

@app.route("/")
def index():
    # session = model.connect()
    print "hello"
    user_list = db_session.query(model.User).limit(25).all()
    print user_list
    return render_template("user_list.html", user_list=user_list)

@app.route("/signup")
def signup_view():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_complete():
    email = request.form.get("email")
    password = request.form.get("password")
    pass_validation = request.form.get("passwordvalidation")
    age = request.form.get("age")
    occupation = request.form.get("occupation")
    zipcode = request.form.get("zip")

    if password == pass_validation:
        new_user = model.User(email = email, password = password, age = age, occupation = occupation, zipcode = zipcode)
        db_session.add(new_user)
        db_session.commit()

    return render_template("welcome.html", occupation=new_user.occupation)

@app.route("/login")
def login_view():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    # TODO: Consider what happens if there is more than one user with that email address
    user = db_session.query(model.User).filter_by(email=email).first()
    if user.password == password:
        return render_template("welcome.html", occupation=user.occupation)
    else:
        flash("Invalid password.")
        return redirect("/login")

@app.route("/user/<int:id>")
def view_user(id):
    pass
    ratings_list = db_session.query(model.Rating).filter_by(user_id = id).all()
    print len(ratings_list)
    return render_template("user.html", ratings_list = ratings_list)

if __name__ == "__main__":
    db_session = model.connect()
    app.run(debug=True)