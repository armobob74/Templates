from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from website.models import TestModel, db
import pdb
import re

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def index():
    return redirect('/sqlite-example')

@views.route('/sqlite-example', methods=['GET','POST'])
def sqliteExample():
    if request.method == 'POST':
        testmodel = TestModel(
                    word = request.form['word']
                )
        db.session.add(testmodel)
        db.session.commit()
        #this redirect sends a GET so that we don't end up resubmitting this POST on each refresh.
        return redirect('/sqlite-example')
    #the query below will return a list of Row objects
    #hit gx below for more info on selection:
    # https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
    rows = db.session.execute(
                db.select(TestModel)
            ).all()
    words = []
    for row in rows:
        word = row[0].word
        words.append(word)
    return render_template('home.html', words=words)
