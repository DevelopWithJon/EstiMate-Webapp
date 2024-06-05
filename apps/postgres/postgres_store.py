"""postgres store"""
import json

from apps import db
from apps.authentication.models import Reports
from apps import redis_client
from sqlalchemy.exc import SQLAlchemyError

def permanent_store(userId, propertyId):  # make async
    """
    save redis data to postgres db.
    """
    try:
        data = redis_client.get(userId, propertyId)
        report = Reports(
        userId=userId,
        propertyId=propertyId,
        address=data.get("address"),
        website=data.get("website"),
        image=data.get('image'),
        city=data.get('city'),
        state=data.get('state'),

        year_one_cap=data.get('year_one_cap', 0),
        unlevered_irr=data.get('unlevered_irr', 0),
        levered_irr=data.get('unlevered_irr', 0),
        unleveredmom=data.get('unleveredmom', 0),
        levered_mom=data.get('levered_mom', 0),
        levered_profit=data.get('levered_profit',0),
        all_cash_on_cash=data.get('all_cash_on_cash', 0),

        all_insurance=json.dumps(data.get('all_insurance')) if data.get('all_insurance') else None, # Array
        all_monthly_insurance=json.dumps(data.get('all_monthly_insurance')) if data.get('all_monthly_insurance') else None, # Array
        all_water=json.dumps(data.get('all_water')) if data.get('all_water') else None,  # Array
        all_monthly_water=json.dumps(data.get('all_monthly_water')) if data.get('all_monthly_water') else None,  # Array
        all_electricity=json.dumps(data.get('all_water')) if data.get('all_water') else None,  # Array
        all_monthly_electricity = json.dumps(data.get('all_monthly_electricity')) if data.get('all_monthly_electricity') else None,  # Array
        all_RM=json.dumps(data.get('all_RM')) if data.get('all_RM') else None, # Array
        all_monthly_RM=json.dumps(data.get('all_monthly_RM')) if data.get('all_monthly_RM') else None, # Array
        all_vacancy=json.dumps(data.get('all_vacancy')) if data.get('all_vacancy') else None,  # Array
        all_revenue=json.dumps(data.get('all_revenue')) if data.get('all_revenue') else None, # Array
        all_monthly_revenue=json.dumps(data.get('all_monthly_revenue')) if data.get('all_monthly_revenue') else None, # Array
        all_management=json.dumps(data.get('all_management')) if data.get('all_management') else None,  # Array
        all_monthly_management=json.dumps(data.get('all_monthly_management')) if data.get('all_monthly_management') else None,  # Array
        all_HOA=json.dumps(data.get('all_HOA')) if data.get('all_HOA') else None,  # Array
        all_monthly_HOA=json.dumps(data.get('all_monthly_HOA')) if data.get('all_monthly_HOA') else None,  # Array
        all_utilities=json.dumps(data.get('all_utilities')) if data.get('all_utilities') else None,  # Array
        all_monthly_utilities=json.dumps(data.get('all_monthly_utilities')) if data.get('all_monthly_utilities') else None,  # Array
        all_gas=json.dumps(data.get('all_gas')) if data.get('all_gas') else None,  # Array
        all_monthly_gas=json.dumps(data.get('all_monthly_gas')) if data.get('all_monthly_gas') else None,  # Array
        all_capex=json.dumps(data.get('all_capex')) if data.get('all_capex') else None,  # Array
        all_monthly_capex=json.dumps(data.get('all_monthly_capex')) if data.get('all_monthly_capex') else None,  # Array
        all_total_expenses=json.dumps(data.get('all_total_expenses')) if data.get('all_total_expenses') else None,  # Array
        all_monthly_total_expenses=json.dumps(data.get('all_monthly_total_expenses')) if data.get('all_monthly_total_expenses') else None,  # Array
        all_total_loan_payment=json.dumps(data.get('totalCost')) if data.get('totalCost') else None,  # Array
        all_monthly_total_loan_payment=json.dumps(data.get('all_monthly_total_loan_payment')) if data.get('all_monthly_total_loan_payment') else None,  # Array
        all_principal=json.dumps(data.get('all_principal')) if data.get('all_principal') else None,  # Array
        all_interest=json.dumps(data.get('all_interest')) if data.get('all_interest') else None, # Array
        all_loan_balance=json.dumps(data.get('all_loan_balance')) if data.get('all_loan_balance') else None, # Array
        all_balloon=json.dumps(data.get('balloonPayment')) if data.get('balloonPayment') else None, # Array
        all_ending_balance=json.dumps(data.get('all_ending_balance')) if data.get('all_ending_balance') else None,  # Array
        all_NOI=json.dumps(data.get('all_NOI')) if data.get('all_NOI') else None,  # Array
        all_NOI_margin=json.dumps(data.get('all_NOI_margin')) if data.get('all_NOI_margin') else None,  # Array
        all_net_deposit_proceeds=json.dumps(data.get('all_net_deposit_proceeds')) if data.get('all_net_deposit_proceeds') else None, # Array
        all_unlevered_yield=json.dumps(data.get('all_unlevered_yield')) if data.get('all_unlevered_yield') else None,  # Array
        all_DSCR=json.dumps(data.get('all_DSCR')) if data.get('all_DSCR') else None, # Array
        all_debt_yield=json.dumps(data.get('all_debt_yield')) if data.get('all_debt_yield') else None, # Array
        all_NOI_growth=json.dumps(data.get('all_net_operating_income_growth')) if data.get('all_net_operating_income_growth') else None,  # Array
        all_CFG_growth=json.dumps(data.get('all_CFG_growth')) if data.get('all_CFG_growth') else None, # Array
        all_levered_cash_on_cash=json.dumps(data.get('all_levered_cash_flow')) if data.get('all_levered_cash_flow') else None,  # Array
        all_monthly_levered_cash_on_cash=json.dumps(data.get('all_monthly_levered_cash_flow')) if data.get('all_monthly_levered_cash_flow') else None,  # Array
        all_unlevered_cash_on_cash=json.dumps(data.get('all_unlevered_cash_flow')) if data.get('all_unlevered_cash_flow') else None,  # Array
        all_monthly_unlevered_cash_on_cash=json.dumps(data.get('all_monthly_unlevered_cash_flow')) if data.get('all_monthly_unlevered_cash_flow') else None,  # Array
        )
        db.session.add(report)
        db.session.commit()
        return {"status": "ok"}
    except SQLAlchemyError as err:
        print(err)
    except Exception as err:
        print(err)