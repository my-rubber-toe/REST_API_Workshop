from create_app import create_app

my_app = create_app()

if __name__ == "__main__":
    my_app.run(host='localhost', port=8080, debug=True)
