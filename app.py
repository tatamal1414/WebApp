from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/show_html')
def show_html():
    return render_template('test_html.html')