from flask import url_for, flash, redirect, request, jsonify, session
from flask_socketio import SocketIO, emit, send, disconnect, join_room, leave_room
from src.models import DirectMessage,User
from src import socketio,online_users,db

@socketio.on("connect")
def onUserConnect():
    if 'user_id' not in session:
        return redirect(url_for(login))
    # Add user to online users dict/list
    online_users[User.query.filter_by(id=session['user_id']).first().email] = request.sid

@socketio.on("disconnect")
def onUserDisconnect():
    if 'user_id' not in session:
        return None
    # Remove user from online users dict/list
    del online_users[User.query.filter_by(id=session['user_id']).first().email]

@socketio.on("direct_message")
def onMessageReceived(data):
    print(data)
    db.session.add(DirectMessage(origin_userid=session['user_id'], other_userid=data["target"], message=data["message"])) # Storing the message in the database
    db.session.commit()
    # Sending to the target
    try:
        emit("direct_message", {"text": data["message"], "from": session['user_id'], "sender_username": User.query.filter_by(id=session['user_id']).first().username,}, room=online_users[User.query.filter_by(id=data["target"]).first().email])
    except:
        pass