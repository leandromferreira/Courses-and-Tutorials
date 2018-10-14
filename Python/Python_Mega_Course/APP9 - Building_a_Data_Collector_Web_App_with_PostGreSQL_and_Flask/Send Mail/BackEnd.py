"""
This is Documentation.
It's a Backend script
Python3
"""
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_mail
from sqlalchemy.sql import func

app = Flask(__name__)

# connection to database with pass word
app.config(["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password/databasename")
# DB variable to store SQLAlchemy
db = SQLAlchemy(app)
# class inheriting for db.Model class of the SQLAlchemy object
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    # get email in string and limit in 120 characters long
    email_ = db.Colimn(db.String(120), unique = True)
    # get height in int
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


# decorator for homepage
@app.route("/")
def index():
    return render_template("index.html")

# decorator for success page
@app.route("/success", methods = ["POST"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email == email).count == 0:
            data = Date(email, heught)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_emil(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html",
    text = "Seems like we've got  something from that email address already!")

# Case 1 - Script executed: __name__ == "__main__"
# Case 2 - Script imported: __name__ == "__script1"
if __name__ == "__main__":
    app.debug = True
    app.run()
