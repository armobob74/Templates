from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import re

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')
