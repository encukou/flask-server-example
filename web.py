import os
import flask

app = flask.Flask(__name__)

# PyLadies logo z: https://github.com/pyladies/pyladies-kit/blob/master/pyladies/logos/general/logo_300x300.png
CESTA_K_OBRAZKU = os.path.join(os.path.dirname(__file__), 'logo_300x300.png')

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
        <form method="POST" action="ahoj">
          Jak se jmenujes?
          <input type="text" name="jmeno">
          <input type="submit" value="OK">
        </form>
      </body>
    </html>
    """

@app.route('/neco')
def neco():
    return 'Tady neco je.'

@app.route('/ahoj', methods=['POST'])
def ahoj():
    text = 'Ahoj. {} je hezke jmeno.'
    jmeno = flask.request.form['jmeno']
    return text.format(jmeno)

@app.route('/obrazek')
def obrazek():
    with open(CESTA_K_OBRAZKU, 'rb') as f:
        obsah = f.read()
    return flask.Response(
        obsah,
        mimetype='image/png')

app.run(debug=True)
