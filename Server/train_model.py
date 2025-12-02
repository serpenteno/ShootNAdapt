import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib


data = pd.DataFrame([
    [1.0, 0.0, 2, 2],
    [0.9, 0.1, 2, 2],
    [0.8, 0.2, 2, 2],
    [0.7, 0.3, 1, 2],
    [0.6, 0.4, 1, 1],
    [0.5, 0.5, 1, 1],
    [0.4, 0.6, 1, 1],
    [0.3, 0.7, 1, 1],
    [0.2, 0.8, 0, 0],
    [0.1, 0.9, 0, 0],
    [0.0, 1.0, 0, 0],
], columns=["accuracy", "reactionTimeRatio", "targetSize", "targetLifeSpan"])

X_target_size = data[["accuracy"]]
y_target_size = data["targetSize"]

X_target_life_span = data[["reactionTimeRatio"]]
y_target_life_span = data["targetLifeSpan"]

model_target_size = DecisionTreeClassifier(max_depth=2)
model_target_life_span = DecisionTreeClassifier(max_depth=2)

model_target_size.fit(X_target_size, y_target_size)
model_target_life_span.fit(X_target_life_span, y_target_life_span)

joblib.dump(model_target_size, "model_target_size.pkl")
joblib.dump(model_target_life_span, "model_target_life_span.pkl")
