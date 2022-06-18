from flask import Flask,request
app = Flask(__name__)
@app.route('/exercise_request/<int:number>')
def test_request(number):
    return f'exercise_request:{number}'
