from flask import Flask
app = Flask(__name__)
@app.route('/another')
def inex():
    return 'Another Response'