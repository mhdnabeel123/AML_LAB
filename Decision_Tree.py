from sklearn.tree import DecisionTreeClassifier

# Dataset
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']


# Step 1: Convert text to numbers
def encode(data):
    encoded = []
    for row in data:
        new_row = []
        for val in row:
            new_row.append(hash(val) % 10)  # simple encoding
        encoded.append(new_row)
    return encoded


X = encode(data)

# Convert target also
y = [1 if t == 'Yes' else 0 for t in target]


# Step 2: Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)


# Step 3: Predict
print("Prediction for first sample:", model.predict([X[0]]))
print("namaskara_mysurumaga")