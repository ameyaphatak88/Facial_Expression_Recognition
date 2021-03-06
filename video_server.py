from flask import Flask
import camera
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/frames/')
def print_frames():
	return(str(camera.video_capt('sample1.mkv')))

@app.route('/frames/<filename>')
def print_frames_for(filename):
	if os.path.exists(filename):
		return (str(camera.video_capt(filename)))
	else:
		return("File path is not valide, plz enter the correct path")


@app.route('/images/')
def print_image_size():
	return(str(camera.picture_capt('ameya.jpeg')))


@app.route('/emotion')
def pred_emotion():
	return(str(camera.emotion('ameya.jpeg')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)