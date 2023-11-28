from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api_bp = Blueprint('api', __name__, url_prefix='/api')

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

@api_bp.route('/check-pythagorean', methods=['POST'])
def check_pythagorean():
    data = request.get_json()
    input_array = data.get('inputArray', [])
    
    result = has_pythagorean_triples(input_array)
    
    response = {'result': 'Yes' if result else 'No'}
    return jsonify(response)

def generate_comparisons(arr):
    comparisons = []
    n = len(arr)
    arr.sort()

    def backtrack(curr_comparison, remaining):
        if len(curr_comparison) == n:
            comparisons.append(curr_comparison)
            return

        for i in range(len(remaining)):
            new_comparison = curr_comparison + [remaining[i]]

            if len(new_comparison) > 1:
                if new_comparison[-1] == new_comparison[-2]:
                    continue

                if (new_comparison[-1] < new_comparison[-2]) == (len(new_comparison) % 2 == 0):
                    continue

            backtrack(new_comparison, remaining[:i] + remaining[i + 1:])

    backtrack([], arr)

    formatted_comparisons = []
    for comp in comparisons:
        formatted = ""
        for i in range(len(comp) - 1):
            if comp[i] < comp[i + 1]:
                formatted += str(comp[i]) + "<"
            else:
                formatted += str(comp[i]) + ">"
        formatted += str(comp[-1])
        formatted_comparisons.append(formatted)

    return list(set(formatted_comparisons))  # Use set to remove duplicates and convert back to a list

@api_bp.route('/compare', methods=['POST'])
def compare():
    data = request.json
    if 'numbers' in data:
        numbers = data['numbers']
        result = generate_comparisons(numbers)
        return jsonify({'comparisons': result})
    return jsonify({'error': 'Invalid input'})

@api_bp.route('/')
def base_check():
    return "Great Success!"

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
