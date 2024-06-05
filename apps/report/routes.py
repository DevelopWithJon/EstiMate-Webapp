# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps import redis_client
from apps.report import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.authentication.models import Reports
from apps.home.forms import SearchForm
from apps.postgres.postgres_store import permanent_store

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


@blueprint.route('/reports')
@blueprint.route('/reports.html')
@login_required
def reports():

    # report_data = Reports.query.filter(Reports.userId == current_user.id)
    report_data = Reports.query.filter(Reports.userId == current_user.id)


    return render_template('report/reports.html', report_data=report_data, segment='reports')


@blueprint.route('/new_report/<propertyId>', methods=['GET', 'POST'])
@login_required
def new_report(propertyId):
    print(request)
    if request.method == "POST":
        permanent_store(current_user.id, propertyId)
        return redirect(url_for('report_blueprint.reports'))
    try:
        # report_data = redis_client.get(str(current_user), str(propertyId))
        report_data = redis_client.get('1', str(propertyId))

        # Serve the file (if exists) from app/templates/report/FILE.html
        return render_template("report/new_report.html", report_data=report_data, propertyId=propertyId, segment='new_report')

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('/saved_report/<reportId>', methods=['GET'])
@login_required
def saved_report(reportId):

    # try:
    report_data = Reports.query.filter(Reports.reportId == reportId)

    # Serve the file (if exists) from app/templates/report/FILE.html
    return render_template("report/saved_report.html", report_data=report_data, segment='saved_report')

    # except TemplateNotFound:
    #     return render_template('home/page-404.html'), 404

    # except:
    #     return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'reports'

        return segment

    except:
        return None
