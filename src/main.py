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
    return "/movies"


# Request parameter <id> can be set to be a specific numeric type int, float
@app.route("/movies/<id>")
def movies_by_id(id):  # Since we will be josking with bson we need it to be a str
    return f"/movies/{id}"


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
