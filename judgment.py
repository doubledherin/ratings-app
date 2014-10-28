from flask import Flask, render_template, redirect, request
import model


app = Flask(__name__)


@app.route("/")
def index():
    # session = model.connect()
    print "hello"
    user_list = db_session.query(model.User).limit(5).all()
    print user_list
    return render_template("user_list.html", user_list=user_list)

@app.route("/signup")
def signup_view():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_complete():
    return "IT WORKED"

if __name__ == "__main__":
    db_session = model.connect()
    app.run(debug=True)