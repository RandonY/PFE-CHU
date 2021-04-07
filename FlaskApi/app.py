from flask import Flask, render_template
from Code.Fonction import parse_info_to_list

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/polluants')
def show_polluants_data():
    polluant_data = parse_info_to_list("polluants")
    return render_template('polluants.html', polluant_data = polluant_data)


@app.route('/meteo')
def show_meteo_data():
    meteo_data = parse_info_to_list("meteo")
    return render_template('meteos.html', meteo_data=meteo_data)


@app.route('/hopital')
def show_hopital_data():
    hopital_data = parse_info_to_list("hopital")
    return render_template("hopitals.html", hopital_data = hopital_data)


@app.route('/date/<date>')
def show_info_date(date):
    return 0


if __name__ == '__main__':
    app.run(debug=True)