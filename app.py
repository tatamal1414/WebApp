from flask import Flask,request
app = Flask(__name__)
@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'
