from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/Location_names')
def get_location_names():
    response = jsonify({
        "locations" : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin' , '*')

    return response

@app.route("/Predict_Price" , methods = ['POST'])
def predict_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        "estimated_price": util.get_price(location , total_sqft , bhk, bath)
    })
    response.headers.add("Access-Control-Allow-Origin" , "*")
    return response

if __name__ == "__main__":
    app.run()