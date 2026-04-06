data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']


def candidate_elimination(data, target):
    # Step 1: Initialize S and G
    S = data[0].copy()                 # Most specific
    G = [['?' for _ in range(len(S))]] # Most general

    # Step 2: Loop through data
    for i in range(len(data)):

        # If YES → generalize S
        if target[i] == 'Yes':
            for j in range(len(S)):
                if S[j] != data[i][j]:
                    S[j] = '?'

        # If NO → specialize G
        else:
            for j in range(len(S)):
                if S[j] != data[i][j]:
                    G[0][j] = S[j]

    return S, G


S, G = candidate_elimination(data, target)

print("Final S:", S)
print("Final G:", G)
print("mysurumaga namaskara")