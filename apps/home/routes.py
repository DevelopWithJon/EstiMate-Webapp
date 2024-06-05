# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.home.forms import SearchForm
from apps.authentication.models import Users, Reports


# Send to Nav Bar

@blueprint.context_processor
def base():
    form = SearchForm()
    reports = Reports.query.filter(Reports.userId == current_user.id)
    report_data = []
    for report in reports:
        report_data.append(report.reportId)
        report_data.append(report.propertyId)
        report_data.append(report.address)
    return dict(form=form, report_data=report_data)


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/search', methods=["POST"])
@blueprint.route('/search.html', methods=["POST"])
@login_required
def search():
    form = request.form
    if form:
        post_searched = form.get('Searched')
        return render_template("home/search.html", form=form, searched=post_searched, segment='search')
    

@blueprint.route('/profile')
@blueprint.route('/profile.html')
@login_required
def profile():
    # try:
    # if not template.endswith('.html'):
    #     template += '.html'

    # Detect the current page
    segment = get_segment(request)

    # Serve the file (if exists) from app/templates/home/FILE.html
    return render_template("home/profile.html", segment=segment)

    # except TemplateNotFound:
    #     return render_template('home/page-404.html'), 404

    # except:
    #     return render_template('home/page-500.html'), 500



@blueprint.route('/tables')
@blueprint.route('/tables.html')
@login_required
def tables():
    return render_template("home/tables.html", segment='tables')

def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
