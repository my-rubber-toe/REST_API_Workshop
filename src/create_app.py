import os
from werkzeug.utils import find_modules, import_string
from flask import Flask, Blueprint
from utils.responses import ApiResponse, ApiException


class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResponse):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_result()
        return Flask.make_response(self, rv)


def create_app(config_file=None) -> ApiFlask:
    """
        Creates and returns a Flask app instance.

        Parameters
        ----------
            config
                the file to be used as the configuration file
        Returns
        -------
            app
                Instance of the ApiFlask class.
    """
    app = ApiFlask(__name__)

    with app.app_context():
        app.config.from_object(config_file or {})

        _register_blueprints(app)

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


def _register_blueprints(app: ApiFlask):
    """
        Register all blueprints under the {.blueprint} module in the passed application instance.

        Parameters
        ----------
            app
                the ApiFlask application instance.
    """

    for module_str in find_modules('blueprints'):
        module = import_string(module_str)

        # If module has the attribute "bp" extract its object instance and register it as a blueprint.
        if hasattr(module, 'bp'):
            if(isinstance(module.bp, Blueprint)):
                app.register_blueprint(module.bp)
            else:
                raise Exception(f"Class is not instance of Blueprint.")
