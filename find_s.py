data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same']
]

target = ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']

def find_s(data, target):
    # Step 1: Take first positive example
    for i in range(len(target)):
        if target[i] == 'Yes':
            hypothesis = data[i]
            break

    # Step 2: Compare with other positive examples
    for i in range(len(data)):
        if target[i] == 'Yes':
            for j in range(len(hypothesis)):
                if hypothesis[j] != data[i][j]:
                    hypothesis[j] = '?'

    return hypothesis

print("Final Hypothesis:", find_s(data, target))
print("namaskara_mysurumaga")