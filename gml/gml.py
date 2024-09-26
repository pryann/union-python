import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    "Age": [25, 30, 45, 50, 35, 40, 60],
    "Income": [50000, 60000, 100_000, 80000, 30000, 75000, 20000],
    "JobType": [
        "Employee",
        "Self-Employed",
        "Employee",
        "Retired",
        "Unemployee",
        "Employee",
        "Retired",
    ],
    "ExistingInsurane": ["No", "Yes", "No", "Yes", "No", "Yes", "No"],
    "PurchasedInsurance": ["No", "Yes", "Yes", "No", "No", "Yes", "Yes"],
}

df = pd.DataFrame(data)

label_encoder_job = LabelEncoder()
label_encoder_insurance = LabelEncoder()

label_encoder_job.fit(df["JobType"])
label_encoder_insurance.fit(df["ExistingInsurane"])

df["JobType"] = label_encoder_job.transform(df["JobType"])
df["ExistingInsurane"] = label_encoder_insurance.transform(df["ExistingInsurane"])
df["PurchasedInsurance"] = label_encoder_insurance.fit_transform(
    df["PurchasedInsurance"]
)

X = df.drop("PurchasedInsurance", axis=1)
y = df["PurchasedInsurance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accurancy = accuracy_score(y_test, y_pred)

print(accurancy)

new_customer = {
    "Age": [40],
    "Income": [80000],
    "JobType": label_encoder_job.transform(["Employee"]),
    "ExistingInsurane": label_encoder_insurance.transform(["No"]),
}

new_customer_df = pd.DataFrame(new_customer)
insurance_prediction = model.predict(new_customer_df)
print("Yes" if insurance_prediction[0] == 1 else "No")
