import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("dementia.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("Dementia.html")

#@flask_app.route('/static/<path:path>')
#def static_file(path):
    #return app.send_static_file(path)

@flask_app.route("/predict", methods = ["POST"])
def predict():
    data1 = request.form['Visit']
    data2 = request.form['MR Delay']
    data3 = request.form['M/F']
    data4 = request.form['Age']
    data5 = request.form['EDUC']
    data6 = request.form['SES']
    data7 = request.form['MMSE']
    data8 = request.form['CDR']
    data9 = request.form['eTIV']
    data10 = request.form['nWBV']
    data11 = request.form['ASF']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]])
    prediction = model.predict(arr)
    return render_template("DementiaPrediction.html", prediction_text = "The flower species is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)