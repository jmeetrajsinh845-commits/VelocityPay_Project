import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print("=" * 50)

print(importance)