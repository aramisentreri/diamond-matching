from __future__ import unicode_literals
import glob
import re
import sqlite3
import math

from django.http import HttpResponse
from django.shortcuts import render
from .forms import DiamondForm

def index(request):

    template = "index.html"
    form = DiamondForm()
    return render(request, template, {'form':form})

def deals(request):
    template = "deals.html"
    return render(request, template)

def about(request):
    template = "about.html"
    return render(request, template)

def blog(request):
    template = "blog1.html"
    return render(request, template)

def result(request):
    if 'carat' in request.GET:
        color = request.GET['color']
        cut = request.GET['cut']
        clarity = request.GET['clarity']
        carat = float(request.GET['carat'])

        # Database connection
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        query = c.execute('SELECT coef, intercept from coef_table where color = ? and cut = ? and clarity = ?', (color, cut, clarity,))

        coef, intercept = [(row[0],row[1]) for row in query][0]
        if coef != '':
                coef = float(coef)
                intercept = float(intercept)
        else:
            return HttpResponse("I'm sorry, but the there were too few diamonds in my database with color %s, clarity %s and cut %s to do a proper interpolation.\n Maybe try another combination?" % (color, clarity, cut))
        predicted_price = math.exp(intercept + coef*math.log(carat))

        query2 = c.execute('SELECT carat, price, detailsPageUrl from diamonds_table where color = ? and cut = ? and clarity = ?', (color, cut, clarity,))

        graph_data = []
        links = []
        carat_list = []
        for row in query2:
            if row[0] not in carat_list:
                graph_data.append([float(row[0]),float(row[1])])
                carat_list.append(row[0])
            if float(row[1]) <= predicted_price and float(row[0]) >= carat-0.2:
                links.append([row[0],row[1],row[2]])

        graph_data = sorted(graph_data, key=lambda tup: tup[0])
        links = sorted(links, key=lambda tup: tup[0], reverse=True)

        template = "result.html"
        context = {'predicted_price': int(predicted_price), 'carat': float(request.GET['carat']), 'cut': request.GET['cut'], 'color': request.GET['color'], 'clarity': request.GET['clarity'], 'graph_data': graph_data, 'links':links}

        return render(request, template, context)
