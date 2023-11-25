from flask import Flask, request, jsonify
from flask_cors import CORS
from itertools import permutations

app = Flask(__name__)
CORS(app)

def has_pythagorean_triples(arr):
    # Function to check for Pythagorean triples
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    arr.sort()

    for i in range(n - 1, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            if (arr[l] + arr[r] == arr[i]):
                return True
            if (arr[l] + arr[r] < arr[i]):
                l += 1
            else:
                r -= 1
    return False


@app.route('/check-pythagorean', methods=['POST'])
def check_pythagorean():
    data = request.get_json()
    input_array = data.get('inputArray', [])
    
    result = has_pythagorean_triples(input_array)
    
    response = {'result': 'Yes' if result else 'No'}
    return jsonify(response)


def generate_comparisons(arr):
    comparisons = []
    n = len(arr)
    for i in range(n):
        comparison = ""
        for j in range(n):
            if i != j:  # Exclude self-comparisons
                if arr[i] < arr[j]:
                    comparison += str(arr[i]) + " < " + str(arr[j]) + " > "
                elif arr[i] > arr[j]:
                    comparison += str(arr[i]) + " > " + str(arr[j]) + " < "
        if comparison:
            if comparison not in comparisons and comparison[::-1] not in comparisons:
                comparisons.append(comparison[:-3])  # Remove the last three characters (space and two symbols)
    comparisons.sort()  # Sort the comparisons
    return comparisons


@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    if 'numbers' in data:
        numbers = data['numbers']
        result = generate_comparisons(numbers)
        return jsonify({'comparisons': result})
    return jsonify({'error': 'Invalid input'})


if __name__ == '__main__':
    app.run(debug=True)
