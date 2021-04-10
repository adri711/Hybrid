# Hybrid - Master
from src import socketio, application

if __name__ == '__main__':
	socketio.run(application, debug=True, host='0.0.0.0', port=5000)