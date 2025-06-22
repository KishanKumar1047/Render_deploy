from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cgpi = float(request.form['cgpi'])
        iq = float(request.form['iq'])
        input_data = np.array([[cgpi, iq]])
        prediction = model.predict(input_data)[0]
        
        result = "Placed ✅" if prediction == 1 else "Not Placed ❌"
        return render_template("index.html", prediction_text=f"Prediction: {result}")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
