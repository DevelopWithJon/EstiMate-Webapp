"""token generator"""
from apps import db
from apps.authentication.models import UserTokens
from uuid import uuid4


def generate_token(userId):
    """
    Generate user token
    """
    token = uuid4().hex
    print(check_user(userId))
    if not check_user(userId):
        user_token = UserTokens(
            userId=userId,
            token=token,
            time_to_live=600000)
        db.session.add(user_token)
        db.session.commit()
    else:
        UserTokens.query.filter(UserTokens.userId == userId)\
            .update({'token': token})
        db.session.commit()
    return token

def check_user(userId) -> bool:
    """check if token record exists for user"""
    return bool(UserTokens.query.filter(UserTokens.userId == userId).first())