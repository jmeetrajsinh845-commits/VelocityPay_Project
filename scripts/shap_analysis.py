import pandas as pd
import shap

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("LOADING DATA...")

df = pd.read_csv(
    "reports/ml_dataset.csv"
)

df = df.dropna(subset=["is_churned"])

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "renewal_count",
    "discount_pct"
]

X = df[features]
y = df["is_churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("TRAINING MODEL...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("GENERATING SHAP VALUES...")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

print("\nSHAP SUMMARY")
print("=" * 50)

print(type(shap_values))
print("SHAP generated successfully")