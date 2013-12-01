from flask import Flask
from flask import render_template
from flask import request
from model.movie import Movie
from database.database import session
from  sqlalchemy.sql.expression import func

app = Flask(__name__)

@app.route('/')
def help():
    return '''
    POST to /movies with title=<new-title> to add movie to the DB.
    GET to /movies/random to get the title of a movie to watch.

'''


@app.route('/movies', methods=['POST'])
def add():
    import pdb; pdb.set_trace()
    m = Movie(**{x: y for x, y in request.form.iteritems()})
    session.add(m)
    session.commit()
    return 'Movie "%s" was added.\n' % (m.title)

@app.route('/movies/random', methods=['GET'])
def random():
    m = session.query(Movie).order_by(func.random()).first()
    return 'You should watch "%s".\n' % (m.title)


if __name__ == '__main__':
    app.run(debug=True)
