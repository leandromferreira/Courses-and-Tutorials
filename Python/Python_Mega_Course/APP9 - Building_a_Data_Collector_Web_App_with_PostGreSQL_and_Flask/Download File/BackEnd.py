"""
This is Documentation.
It's a Backend script
Python3
"""
from flask import Flask, render_template, request, send_file
from flask.ext.sqlalchemy import SQLAlchemy
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
    global file
    if request.method == "POST":
        file = request.files["file"]
        file.save(secure_filename("uploaded" + file.filename))
        with open("uploaded" + file.filename)) as f:
            f.write("This was added later!")
        return render_template("success.html", btn = "download.html")

@app.route("/download")
def download():
    return send_file("uploaded" + file.filename, attachment_filename = "yourfile.csv", as_attachment = True)

# Case 1 - Script executed: __name__ == "__main__"
# Case 2 - Script imported: __name__ == "__script1"
if __name__ == "__main__":
    app.debug = True
    app.run()
