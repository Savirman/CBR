from flask import Flask, render_template, url_for
import main
import db

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", date = main.valkurs['Date'], current_date = main.current_date)


if __name__ == '__main__':
    app.run()