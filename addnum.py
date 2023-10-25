from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        data = request.get_json()
        num1 = int(data['num1'])  
        num2 = int(data['num2'])  
        result = num1 + num2
        return jsonify({'result': result})
    except KeyError:
        return jsonify({'error': 'Invalid input. Please provide "num1" and "num2" as JSON parameters.'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide valid numbers as JSON parameters.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
