from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def main_route():
    """
        Main route. Returns a list of the available endpoints on this service.
    """
    available_routes = {
        0: '/',
        1: '/movies',
        2: '/movies/<id>',
        3: '/movies?start=<int>&offset=<int>',
    }

    return jsonify(available_routes), 200


@app.route("/movies")
def movies_endpoint():
    return "GET all movies based on parameters or POST a movie"


@app.route("/movies/<int:id>")
def movies_by_id():
    pass





if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
