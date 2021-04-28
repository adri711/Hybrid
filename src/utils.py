from flask import redirect,session
from sqlalchemy.orm import load_only
from flask_sqlalchemy import SQLAlchemy
from src.models import User, Friendship,DirectMessage
from random import randint
from src import constants


def generate_tag():
    return ''.join([chr(randint(48, 57)) for i in range(constants.TAG_DIGIT_COUNT)])

def setattr_n_return(object, name,value):
    setattr(object, name, value)
    return object

# has to be changed to a more efficient way
def generate_user_tag(username):
    tags, tag = set(), constants.INITIAL_TAG_FOR_USERNAME
    while User.query.filter_by(username=username, tag=tag).first():
        while True:
            tag = generate_tag()
            if tag not in tags:
                tags.append(tag)
                break
    return tag

def logout_user():
    if 'user_id' in session:
        session.pop('user_id')

def load_user_contacts():
    if 'user_id' in session:
        load = lambda id: setattr_n_return(User.query.filter_by(id=id).options(load_only('id', 'username', 'tag')).first(), "last_message", DirectMessage.query.filter(
            (DirectMessage.origin_userid.in_([id, session['user_id']])) & (DirectMessage.other_userid.in_([id, session['user_id']]))).order_by(DirectMessage.id.desc()).first())
        relations = Friendship.query.filter((Friendship.origin_userid==session['user_id']) | (Friendship.other_userid==session['user_id'])).all()
        return [load(relation.origin_userid) if relation.origin_userid != session['user_id'] else load(relation.other_userid) for relation in relations]