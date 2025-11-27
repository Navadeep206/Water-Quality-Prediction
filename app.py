from flask import Flask, render_template, request, jsonify, url_for
import joblib

app = Flask(__name__)

# Load your trained SVM model
model = joblib.load("svm.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_waterQ', methods=['GET', 'POST'])
def predict_waterQ():
    if request.method == 'POST':
        try:
            # Read input values from form
            ph = float(request.form["ph"])
            hardness = float(request.form["hardness"])
            solids = float(request.form["solids"])
            chloramines = float(request.form["chloramines"])
            sulfate = float(request.form["sulfate"])
            conductivity = float(request.form["conductivity"])
            organicCarbon = float(request.form["organicCarbon"])
            trihalomethanes = float(request.form["trihalomethanes"])
            turbidity = float(request.form["turbidity"])
        except ValueError:
            return "Please enter valid numeric values.", 400

        input_values = [ph, hardness, solids, chloramines, sulfate, conductivity,
                        organicCarbon, trihalomethanes, turbidity]

        # Make prediction
        prediction = model.predict([input_values])[0]
        prediction_label = "Safe" if prediction == 1 else "Unsafe"

        return render_template('result.html', prediction=prediction_label)

    return render_template('index.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json
    try:
        input_values = [
            float(data.get("ph")),
            float(data.get("hardness")),
            float(data.get("solids")),
            float(data.get("chloramines")),
            float(data.get("sulfate")),
            float(data.get("conductivity")),
            float(data.get("organicCarbon")),
            float(data.get("trihalomethanes")),
            float(data.get("turbidity"))
        ]
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input values"}), 400

    prediction = model.predict([input_values])[0]
    prediction_label = "Safe" if prediction == 1 else "Unsafe"

    return jsonify({"prediction": prediction_label})


if __name__ == '__main__':
    app.run(debug=True)
