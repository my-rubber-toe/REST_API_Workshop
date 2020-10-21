from flask import Blueprint, jsonify, request
from utils.responses import ApiResponse
from db import db_operations

bp = Blueprint(
    name=__name__,
    import_name=__name__,
    url_prefix='/movies'
)


@bp.route('/')
def base_url():
    db_operations.get_all_movies()
    return ApiResponse({
        'message': f"Welcome to the {__name__}."
    })


@bp.route('/all', methods=['GET'])
def get_all_movies():
    return jsonify(db_operations.get_all_movies())
    # return ApiResponse({
    #     'message': f"Welcome to the {__name__}."
    # })


@bp.route('/some')
def get_movies_paginated():
    # https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
    # /some?start=1&end=3
    start = request.args.get('start', default=1, type=int)
    request.args.get('end', default=1, type=1)
    return ApiResponse({
        'message': f"Welcome to the {__name__}."
    })