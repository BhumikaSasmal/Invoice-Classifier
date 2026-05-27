import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


df = pd.read_csv("data.csv")
x_train, x_test, y_train, y_test = train_test_split(
    df["text"],
    df["category"],
    test_size=0.2,
    random_state=42,
    stratify=df["category"]
)
vec = TfidfVectorizer()

x_train_vec = vec.fit_transform(x_train)
x_test_vec = vec.transform(x_test)

model = LogisticRegression(max_iter=1000)
model.fit(x_train_vec, y_train)
y_pred = model.predict(x_test_vec)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:", round(acc * 100, 2), "%")

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vec, open("vectorizer.pkl", "wb"))

with open("accuracy.txt", "w") as f:
    f.write(f"{acc*100:.2f}")