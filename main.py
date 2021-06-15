from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

app.static_folder = 'static'


@app.route('/data',methods=["POST"])
def data():
    id = request.form.get("id")
    date = request.form.get("date")
    date_birth = datetime.strptime(date, '%Y-%m-%d')
    date_today = datetime.now()

    if date_birth > date_today:
        message = "Date of birht invalid"
        return render_template("show.html", id=id, date=date, message=message)
    else:

        difference = date_today - date_birth
        days_lived = difference.days

        message = "The citizen with identification {}. and with date of birth {} Has lived {} day(s)".format(
            id, date_birth, days_lived)

        return render_template("show.html",id=id, date=date, message=message)


def calculate(id,date):
    date_birth = datetime.strptime(date, '%Y-%m-%d')
    date_today = datetime.now()

    if date_birth > date_today:
        return ("Date of birht invalid")
    else:

        difference = date_today - date_birth
        days_lived = difference.days

        message = "The citizen with identification {}. and with date of birth {} Has lived {} day(s)".format(
            id, date_birth, days_lived)

        return (message)

@app.route('/form/')
def days():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
