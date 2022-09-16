from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# todo schema
class Todo:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90))
    complete = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())


@app.route("/")  # index route
def index():
    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
