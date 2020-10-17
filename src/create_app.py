import os
from flask import Flask
from utils.responses import ApiResponse, ApiException


class ApiFlask(Flask):
    def make_response(self, rv):
        """
            Override make_response method to return custom response objects.
        """
        if isinstance(rv, ApiResponse):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_result()
        return Flask.make_response(self, rv)


def create_app(config_file=None) -> ApiFlask:
    """
        Create and configure a Flask app instance with 
    """
    app = ApiFlask(__name__)

    with app.app_context():
        app.config.from_object(config_file or {})

        # register_blueprints(app)

        _register_base_url(app)
        
        return app

def _register_base_url(app: ApiFlask):
    """
        Register the base url for the application instance.
    """

    @app.route('/')
    def main_route():
        return ApiResponse({
            'message': 'You have reached the main route of this api.'
        })
