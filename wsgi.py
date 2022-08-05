from flask import Flask, render_template, url_for, request
import psycopg2
import main
import db

# Create an instanse of Flask App
app = Flask(__name__)

@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    if request.method == 'GET':
        print(request.form)
    valute_name = request.args.get('valute')
    selected_date = request.args.get('date')

    # Connection to DB cbr
    connection = psycopg2.connect(
        database="cbr",
        user="postgres",
        password="111111",
        host="127.0.0.1",
        port="5432"
    )
    connection.autocommit = True
    # Data extraction from table "valutes" cbr
    cursor = connection.cursor()
    sql_query = f"SELECT * from valutes WHERE name='{valute_name}' AND date='2022-08-01'"
    cursor.execute(sql_query)
    context_records = cursor.fetchall()
    for row in context_records:
        date = row[0]
        valuteid = row[1]
        numcode = row[2]
        charcode = row[3]
        nominal = row[4]
        name = row[5]
        value = row[6]
    connection.commit()
    return render_template("index.html", quantity = 2, valute = valute_name, date = selected_date, curs = 3)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена")

if __name__ == '__main__':
    app.run()