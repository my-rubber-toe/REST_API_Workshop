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
        3: '/movies?year=<int>&lt=<bool>&mt=<bool>',
        4: '/movies?genre=<string>',
        5: '/movies?runtime=<int>&lt=<bool>&mt=<bool>',
        6: '/movies?servicename=<string>'
    }

    return jsonify(available_routes), 200


if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
