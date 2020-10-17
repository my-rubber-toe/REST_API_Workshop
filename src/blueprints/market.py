from flask import Blueprint, jsonify
from utils.responses import ApiResponse

bp = Blueprint(name="market", url_prefix='/market', import_name=__name__)

@bp.route('/')
def market_main():
    return ApiResponse({
        'message': "Welcome to the Market :)"
    })
