"""api routes."""
import sys
from flask import request
from flask_restful import Resource
from apps import redis_client
from apps.authentication.models import Users, UserTokens
from sqlalchemy import inspect
from apps.authentication.util import verify_pass
from apps.authentication.token_generator import generate_token
from datetime import datetime, timedelta
import pytz
import time
utctz=pytz.UTC

# request_args = reqparse.RequestParser()

# request_args.add_argument("website", type=str, help="This is property listing is the website.")
# request_args.add_argument("userId", type=int, help="Authorized user id.")
# request_args.add_argument("propertyId", type=str, help="This is property id from the website.")
# request_args.add_argument("address", type=str, help="This is property id from the website.")
# request_args.add_argument("image", type=str, help="This is property image url.")

# request_args.add_argument("all_insurance", type=str, help="This is property data.")
# request_args.add_argument("all_water", type=str, help="This is property data.")
# request_args.add_argument("all_electricity", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_RM", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_vacancy", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_revenue", type=list, action="append", help="This is property data.")

# request_args.add_argument("all_management", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_HOA", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_utilities", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_gas", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_capex", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_total_expenses", type=list, action="append", help="This is property data.")

# request_args.add_argument("loan", type=float, action="append", help="This is property data.")
# request_args.add_argument("interest", type=float, action="append", help="This is property data.")
# request_args.add_argument("principal", type=float, action="append", help="This is property data.")
# request_args.add_argument("all_total_loan", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_principal", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_interest", type=list, action="append", help="This is property data.")

# request_args.add_argument("all_loan_balance", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_baloon", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_ending_balance", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_NOI", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_NOI_margin", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_net_deposit_proceeds", type=list, action="append", help="This is property data.")

# request_args.add_argument("cap_rate", type=float, action="append", help="This is property data.")
# request_args.add_argument("unlevered_irr", type=float, action="append", help="This is property data.")
# request_args.add_argument("levered_irr", type=float, action="append", help="This is property data.")
# request_args.add_argument("unleveredmom", type=float, action="append", help="This is property data.")
# request_args.add_argument("levered_mom", type=float, action="append", help="This is property data.")
# request_args.add_argument("levered_profit", type=float, action="append", help="This is property data.")

# request_args.add_argument("all_coc", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_unlevered_yield", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_DSCR", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_debt_yield", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_NOI_growth", type=list, action="append", help="This is property data.")
# request_args.add_argument("all_CFG_growth", type=list, action="append", help="This is property data.")

class API(Resource):
    
    def get(self, userId, propertyId=None):
        """
        GET request
        """
        try:
            resp = redis_client.get(userId, propertyId)
            return {"data": resp}, 200 if resp else {"data": resp}, 204
        except:
            return {"data": ""}, 203

    def post(self, token):
        """
        POST request
        """
        print("POST")
        print(request.get_json(force=True))
        anlysis_data = request.get_json(force=True)['extensionData']['analysis']
        raw_feature_data = request.get_json(force=True)['extensionData']['feature']
        raw_fundamentals_data = request.get_json(force=True)['extensionData']['fundamentals']
        userId = token_is_valid(token)
        if userId:
            try:
                # REDIS INSERT
                anlysis_data["userId"] = userId
                propertyId = anlysis_data['propertyId']
                data = {}
                data[propertyId] = {i:anlysis_data[i] for i in anlysis_data if i not in ['userId', 'propertyId']}
                redis_client.set(userId, data)
                # redis_client.set(userId, raw_feature_data)
                # redis_client.set(userId, raw_fundamentals_data)
                return {"message": "Success"}, 201
            except Exception as err:
                print(err, sys.stdout)
                return {"error": f"An error ocurred during request.\nError={err}"}, 400
        else:
            print(f"{userId} does not exist")
            return {"data": ""}, 203


class TokenAPI(Resource):
    
    def get(self, username, password):
        """
        GET request
        """
        user = Users.query.filter_by(username=username).first()

        if user and verify_pass(password, user.password):
            token = generate_token(user.id)
            time.sleep(1)
            if token:
                return {"data": {"token": token}}, 200
        else: 
            return {"data": "", "message": "Either token did not exist or token expired. Please create a new token"}, 203
        

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

def token_is_valid(token) -> bool:
    """
    Check if token exists and is not expired.
    """
    user_token = UserTokens.query.filter(UserTokens.token == token).first()
    if user_token:
        userId, delta, last_modified = user_token.userId, int(user_token.time_to_live), user_token.last_modified
        
        expiration_date = timedelta(milliseconds=delta) + last_modified.replace(tzinfo=utctz)
        NOW = datetime.utcnow().replace(tzinfo=utctz)
        print(userId, user_token, NOW, expiration_date, (NOW < expiration_date))
        if (user_token and NOW < expiration_date):
            return userId