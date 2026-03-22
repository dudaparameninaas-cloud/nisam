from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Ana sayfa - giriş ve mesajlar
@app.route('/')
def index():
    return render_template('index.html')

# Kalp animasyonu sayfası
@app.route('/kalp')
def kalp():
    return render_template('kalp.html')

# Statik dosyalar (MP3, resim vs.) için route
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# 404 hatası için özel sayfa (opsiyonel)
@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404

# Render için port ayarı
if __name__ == '__main__':
    # Render'da PORT environment variable'ı kullanılır
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
