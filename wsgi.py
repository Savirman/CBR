from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Информация по курсам валют"

if __name__ == '__main__':
    app.run()