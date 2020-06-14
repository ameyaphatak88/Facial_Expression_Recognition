from flask import Flask
import camera


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/frames/')
def print_frames():
	return(str(camera.video_capt('sample1.mkv')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)