from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kalp')
def kalp():
    return render_template('kalp.html')

# MP3 dosyası için route (ses dosyanızı static klasörüne koyun)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_file(os.path.join('static', filename))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
