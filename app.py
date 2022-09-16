from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)


# DB configuration ->
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# todo schema
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # unique id
    title = db.Column(db.String(90))  # todo title
    complete = db.Column(db.Boolean)  # todo complete
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())  # create date


@app.route("/")  # index route
def index():
    # all todos
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/todo-add", methods=["POST"])
def add_todo():
    # form (title) query string
    title = request.form.get("title")
    # new todo item
    new_todo = Todo(title=title, complete=False)
    # todo stores in data base
    db.session.add(new_todo)
    # todo commit ->
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
