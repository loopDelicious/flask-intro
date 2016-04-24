from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    print "Hi! This is the home page."
    return """
    <a href="/hello">hello page</a>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name and allows them to select a 
    compliment."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <br>
          <label>What's your name? <input type="text" name="person" /></label>
          <br>
          Select a compliment. 
          <select name="compliment"><br>
            <option value="swell">swell</option>
            <option value="pretty">pretty</option>
            <option value="smart">smart</option>
          </select> 
          <br>
          <input type="submit">
        </form>
        <br>

        <form action="/diss">
          <br>
          <label>What's your name? <input type="text" name="person" /></label>
          <br>
          Select an insult. 
          <select name="insult"><br>
            <option value="stinky">stinky</option>
            <option value="ignorant">ignorant</option>
            <option value="basic">basic</option>
          </select>
          <br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def insult_person():
  """Insult someone"""

  player = request.args.get("person")

  insult = request.args.get("insult")

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
