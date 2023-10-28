from flask import request, session,jsonify,make_response
from flask_restful import Resource

from config import db,app,api

if __name__ == '__main__':
    app.run(port=5555, debug=True)