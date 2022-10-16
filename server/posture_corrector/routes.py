from posture_corrector import app
from flask import render_template, Response
from posture_corrector.camera import VideoCamera

@app.route('/')
@app.route('/')
def index():
    return render_template('index.js')
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')