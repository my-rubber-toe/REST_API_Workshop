from flask import Blueprint, jsonify
from utils.responses import ApiResponse

bp = Blueprint(
    name=__name__,
    import_name=__name__,
    url_prefix='/movies'
)


@bp.route('/')
def base_url():
    return ApiResponse({
        'message': f"Welcome to the {__name__}."
    })
