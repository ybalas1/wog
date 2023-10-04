import flask
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def score_server():
    try:
        read_file = open(SCORES_FILE_NAME, 'r')
        current_score = int(read_file.readline())
        read_file.close()
    except Exception as e:
        current_score = None

    app = flask.Flask(__name__)

    @app.route('/')
    def index():
        if current_score is not None:
            return flask.render_template('index.html', score=current_score)
        else:
            return flask.redirect('/error')

    @app.route('/error')
    def error():
        if current_score is None:
            return flask.render_template('error.html', error_code=BAD_RETURN_CODE)
        else:
            return flask.redirect('/')

    if __name__ == '__main__':
        app.run(debug=True)

score_server()
