from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"


# Create form class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
@app.route('/')
def index():
    # FILTERS
    # safe
    # capitalize
    # lower
    # upper
    # title
    # trim
    # striptags
    favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    stuff = "This is a <strong>Bold</strong> text."
    return render_template(
        "index.html",
        stuff=stuff,
        fav_pizza=favourite_pizza
    )


# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error Thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Va;idate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
                           name=name,
                           form=form
                           )
