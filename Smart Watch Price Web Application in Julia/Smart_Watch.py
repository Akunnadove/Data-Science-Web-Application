from flask import Flask, request, jsonify, render_template
import numpy as np 
import pickle 

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("smart_watch_model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("Smart_Watch.html") 
 
@flask_app.route("/predict", methods = ["POST"])

def predict():
    data1 = request.form['Brand']
    data2 = request.form['Model']
    data3 = request.form['Operating System']
    data4 = request.form['Connectivity']
    data5 = request.form['Display Type']
    data6 = request.form['Display Size inches']
    data7 = request.form['Resolution']
    data8 = request.form['Water Resistance meters']
    data9 = request.form['Battery Life days']
    data10 = request.form['Heart Rate Monitor']
    data11 = request.form['GPS']
    data12 = request.form['NFC']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]]) 

    arr_float = arr.astype(float) 

    prediction = model.predict(arr_float) 
    
    return render_template("Smart_Watch_Prediction.html", prediction_text="Predicted Smart Watch Price is {}".format(prediction),data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9) 

if __name__ == "__main__":
    flask_app.run(debug=True)  