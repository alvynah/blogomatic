from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quotes
from ..models import Quote

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its content
    '''
    #getting Quotes
    quotes=get_quotes()


    return render_template('index.html',quotes=quotes)
