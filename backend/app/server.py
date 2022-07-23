from flask_cors import CORS
from flask import Flask, request, make_response
import clashdeck
import jsonpickle as jp

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'Clash Deck API'

@app.route('/api/v1/deck', methods=['GET'])
def get_deck():
    try:
        user = request.args.get('player')
        trophies = int(request.args.get('trophies'))
    except Exception as e:
        print(f'Error: {e}')
        return make_response('Invalid request', 400)
    
    deck = clashdeck.get_deck(user, trophies)
    return make_response(jp.encode(deck), 200)