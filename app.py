from flask import Flask, render_template, request

app = Flask(__name__)

import weather as db

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        country = request.form['country']
        state = request.form['state']
        city = request.form['city']
        pressure = request.form['pressure']
        humidity = request.form['humidity']
        db.insert_details(country,state,city,pressure,humidity)
        details = db.get_details()
        print(details)
        return render_template('index.html',var=var)

if __name__ == "__main__":
    
    app.run(debug=True)
