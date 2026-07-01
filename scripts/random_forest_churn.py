import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("LOADING DATASET...")

df = pd.read_csv(
    "reports/ml_dataset.csv"
)

print("DATA SHAPE:", df.shape)

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

print("\nTRAIN TEST SPLIT...")

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

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nMODEL RESULTS")
print("=" * 50)
print(f"Accuracy : {accuracy:.4f}")