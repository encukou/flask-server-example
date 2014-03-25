import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
      <head>
        <title>Ahoj!</title>
      </head>
      <body>
        <h1>Ahoj svete!</h1>
        <p>
          <a href="neco">
            Klikni sem!
          </a>
          nebo:
          <a href="http://www.google.com">
            Google
          </a>
        </p>
        <p>
            <img src="obrazek">
        </p>
      </body>
    </html>
    """

@app.route('/neco')
def neco():
    return 'Tady neco je.'

@app.route('/obrazek')
def obrazek():
    jmeno_souboru = '/home/petr/pictures/eck/icon/eck256.png'
    with open(jmeno_souboru, 'rb') as f:
        obsah = f.read()
    return flask.Response(
        obsah,
        mimetype='image/png')

app.run(debug=True)
