import flask
from Utils import SCORES_FILE_NAME

def score_server():
    read_file = open(SCORES_FILE_NAME, 'r')
    current_score = int(read_file.readline())
    read_file.close()

    app = flask.Flask(__name__)  # Update Flask import here

    @app.route('/')
    def index():

        return flask.render_template('index.html', score=current_score)  # Update render_template call here

    if __name__ == '__main__':
        app.run(debug=True)

score_server()
