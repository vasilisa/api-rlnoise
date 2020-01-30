"""users routes"""
from flask import current_app as app, jsonify, request
from models import ParticipantsGame, BaseObject
from collections import OrderedDict
import numpy
import json

@app.route('/participants_game/<participant_id>', methods=['GET'])

def get_game_id(participant_id):
    query    = ParticipantsGame.query.filter_by(id=participant_id)
    game_id  = query.first_or_404()

    # format the query into a dictionnary first:
    result              = {}
    arr_block           = game_id.get_game_id().replace('  ',' ').split(' ')
    result['game_id']   = arr_block[0]

    app.logger.info(result)
    return jsonify(result), 200 

    