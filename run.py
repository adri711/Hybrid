# Hybrid - Master
from src import socketio, application, constants

if __name__ == '__main__':
	socketio.run(application, debug=constants.DEBUG, host='0.0.0.0', port=constants.APP_PORT)