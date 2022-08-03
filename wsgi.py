from flask import Flask, render_template
import main
import db

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", date = main.valkurs['Date'])


if __name__ == '__main__':
    app.run()