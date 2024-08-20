from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for

api = Blueprint('api', __name__, url_prefix='/api')

@api.post('/make-data')
def makeData():
    """ Make data to be displayed to the user """
    m = float(request.form['m'])
    b = float(request.form['b'])
    x = [i / 19 for i in range(20)]
    y = list(map(lambda a: m*a + b, x))
    data = {
        'x':x,
        'y':y
    }
    return jsonify(data)
