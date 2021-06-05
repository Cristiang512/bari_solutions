from flask import Flask , jsonify,render_template, request
from datetime import datetime


app = Flask(__name__)




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

@app.route('/form/')
def days():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
