from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/excersize')
def excersize():
    return render_template('exercise.html')