from flask import Flask, render_template, request, send_from_directory
import segno
from segno import helpers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_QR-mcard.html')

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    urls = request.form['url'].split(',')

    qrcode = helpers.make_mecard(name=name, email=email, phone=phone, url=urls)
    filename = 'my-mecard.svg'
    qrcode.save(f'{filename}', scale=4)

    return send_from_directory(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
