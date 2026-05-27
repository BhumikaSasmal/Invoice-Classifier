from flask import Flask, request, jsonify
import pickle


model = pickle.load(open("model.pkl", "rb"))
vec = pickle.load(open("vectorizer.pkl", "rb"))

with open("accuracy.txt", "r") as f:
    acc = f.read()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Invoice Expense Classification API",
        "model_accuracy": f"{acc}%"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    x = vec.transform([text])
    prediction = model.predict(x)[0]
    probs = model.predict_proba(x)

    confidence = max(probs[0]) * 100

    return jsonify({
        "category": prediction,
        "confidence": round(confidence, 2),
        "model_accuracy": f"{acc}%"
    })

if __name__ == "__main__":
    app.run(debug=True)