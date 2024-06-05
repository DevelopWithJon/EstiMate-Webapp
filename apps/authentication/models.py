# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from apps import db, login_manager
from apps.authentication.util import hash_pass
from datetime import datetime

CURRENT_TIMESTAMP = datetime.utcnow().strftime("%Y/%m/%d, %H:%M:%S.%f")[:-3]

class Reports(db.Model):

    __tablename__ = 'Reports'

    # metadata
    reportId = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    propertyId = db.Column(db.String(64), nullable=False)
    reportNickName = db.Column(db.String(256))
    creation_date = db.Column(db.DateTime(timezone=True), default=CURRENT_TIMESTAMP)
    last_modified = db.Column(db.TIMESTAMP, server_default=CURRENT_TIMESTAMP, onupdate=CURRENT_TIMESTAMP)

    website = db.Column(db.String(256))
    address = db.Column(db.String(256))
    city = db.Column(db.String(256))
    state = db.Column(db.String(256))
    image = db.Column(db.String(1000))

    interest = db.Column(db.Float)
    principal = db.Column(db.Float)
    year_one_cap = db.Column(db.Float)
    unlevered_irr = db.Column(db.Float)
    levered_irr = db.Column(db.Float)
    unleveredmom = db.Column(db.Float)
    levered_mom = db.Column(db.Float)
    levered_profit = db.Column(db.Float)
    

    all_cash_on_cash = db.Column(db.String(1000))
    all_insurance = db.Column(db.String(1000))
    all_monthly_insurance = db.Column(db.String(1000))
    all_water = db.Column(db.String(1000))
    all_monthly_water = db.Column(db.String(1000))
    all_electricity = db.Column(db.String(1000))
    all_monthly_electricity = db.Column(db.String(1000))
    all_RM = db.Column(db.String(1000))
    all_monthly_RM = db.Column(db.String(1000))
    all_vacancy = db.Column(db.String(1000))
    all_revenue = db.Column(db.String(1000))
    all_monthly_revenue = db.Column(db.String(1000))
    all_management = db.Column(db.String(1000))
    all_monthly_management = db.Column(db.String(1000))
    all_HOA = db.Column(db.String(1000))
    all_monthly_HOA = db.Column(db.String(1000))
    all_utilities = db.Column(db.String(1000))
    all_monthly_utilities = db.Column(db.String(1000))
    all_gas = db.Column(db.String(1000))
    all_monthly_gas = db.Column(db.String(1000))
    all_capex = db.Column(db.String(1000))
    all_monthly_capex = db.Column(db.String(1000))
    all_total_expenses = db.Column(db.String(1000))
    all_monthly_total_expenses = db.Column(db.String(1000))
    all_total_loan_payment = db.Column(db.String(1000))
    all_monthly_total_loan_payment = db.Column(db.String(1000))
    all_principal = db.Column(db.String(1000))
    all_interest = db.Column(db.String(1000))
    all_loan_balance = db.Column(db.String(1000))
    all_balloon = db.Column(db.String(1000))
    all_ending_balance = db.Column(db.String(1000))
    all_NOI = db.Column(db.String(1000))
    all_NOI_margin = db.Column(db.String(1000))
    all_net_deposit_proceeds = db.Column(db.String(1000))
    all_unlevered_yield = db.Column(db.String(1000))
    all_DSCR = db.Column(db.String(1000))
    all_debt_yield = db.Column(db.String(1000))
    all_NOI_growth = db.Column(db.String(1000))
    all_CFG_growth = db.Column(db.String(1000))
    all_levered_cash_on_cash = db.Column(db.String(1000))
    all_unlevered_cash_on_cash = db.Column(db.String(1000))
    all_monthly_levered_cash_on_cash = db.Column(db.String(1000))
    all_monthly_unlevered_cash_on_cash = db.Column(db.String(1000))

    def __init__(self, **kwargs):
        
        for property, value in kwargs.items():
            setattr(self, property, value)

    def __repr__(self):
        return str(self.reportNickName)
    
# class RawPayloads(db.Model):

#     # metadata
#     reportId = db.Column(db.Integer, nullable=False)
#     userId = db.Column(db.Integer, nullable=False)
#     paylaodId = db.Column(db.Integer, primary_key=True, nullable=False)
#     reportNickName = db.Column(db.String(256))
#     creation_date = db.Column(db.DateTime(timezone=True), default=CURRENT_TIMESTAMP)
#     last_modified = db.Column(db.TIMESTAMP, server_default=CURRENT_TIMESTAMP, onupdate=CURRENT_TIMESTAMP)
#     raw_data = db.Column(db.ext.MutableDict.as_mutable(db.dialects.postgresql.JSONB))

#     __table__ = 'RawPayloads'

#     def __init__(self, **kwargs):
        
#         for property, value in kwargs.items():
#             setattr(self, property, value)

#     def __repr__(self):
#         return str(self.reportNickName)

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)
    creation_date = db.Column(db.DateTime(timezone=True), default=CURRENT_TIMESTAMP)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

class UserTokens(db.Model):

    __tablename__ = 'UserTokens'
    
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False, unique=True)
    token = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    last_modified = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    time_to_live = db.Column(db.Integer, nullable=False)  # TTL in miliseconds

    def __init__(self, **kwargs):
        
        for property, value in kwargs.items():
            setattr(self, property, value)

@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None