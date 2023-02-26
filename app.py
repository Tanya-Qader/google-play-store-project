import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from flask import render_template
from flask import jsonify
import psycopg2
from config import username, password

#################################################
# Database Setup
#################################################
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/playstore_db")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
avg_cat_rating = Base.classes.average_category_rating
max_rev = Base.classes.max_reviews
avg_type_rating = Base.classes.average_type_rating

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/average_category_rating")
def average_category_rating():
    session = Session(engine)

    """Return a list for the average category rating"""
    results = session.query(avg_cat_rating.Category,
                            avg_cat_rating.Rating)

    session.close()

    Category_list = []
    for Category, Rating in results:
        Category_dict = {}
        Category_dict["Category"] = Category
        Category_dict["Rating"] = Rating
        Category_list.append(Category_dict)

    return jsonify(Category_list)


@app.route("/average_type_rating")
def average_type_rating():
    session = Session(engine)

    """Return a list for average type rating"""
    results = session.query(avg_type_rating.Type,
                            avg_type_rating.Rating)

    session.close()

    Type_list = []
    for Type, Rating in results:
        Type_dict = {}
        Type_dict["Type"] = Type
        Type_dict["Rating"] = Rating
        Type_list.append(Type_dict)

    return jsonify(Type_list)


@app.route("/max_reviews")
def max_reviews():
    session = Session(engine)

    """Return a list for maximum reviews"""
    results = session.query(max_rev.App,
                            max_rev.Reviews)

    session.close()

    App_list = []
    for App, Reviews in results:
        App_dict = {}
        App_dict["App"] = App
        App_dict["Reviews"] = Reviews
        App_list.append(App_dict)

    return jsonify(App_list)


if __name__ == "__main__":
    app.run(debug=True)