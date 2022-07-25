from Tracker import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    # if you are seeing this problem;
    # Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.

    # run this and try again:    $env:FLASK_APP="run.py"