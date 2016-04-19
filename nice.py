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

    return """
    Hi! This is the home page.<br>

    <a href="/hello">Hello Page</a>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br><br>
          Pick a Compliment:
            <select name="compliment">
              <option value = "awesome">Awesome</option>
              <option value = "terrific">Terrific</option>
              <option value = "fantastic">Fantastic</option>
              <option value = "neato">Neato</option>
              <option value = "fantabulous">Fantabulous</option>
              <option value = "wowza">Wowza</option>
              <option value = "oh-not-so-meh">Oh-So-Not-Meh</option>
              <option value = "brilliant">Brilliant</option>
              <option value = "ducky">Ducky</option>
              <option value = "coolio">Coolio</option>
              <option value = "incredible">Incredible</option>
              <option value = "wonderful">Wonderful</option>
              <option value = "smashing">Smashing</option>
              <option value = "lovely">Lovely</option>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment_choice = request.args.get("compliment", 'funky')

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
    """ % (player, compliment_choice)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
