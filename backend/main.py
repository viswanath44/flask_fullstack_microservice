from flask import Flask, request, jsonify

from basic_calculator_function import basic_calculator

app = Flask(__name__)


@app.route('/', methods=['POST', "GET"])
def handle_post():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        # {"operator1: "", "operator2":"", "operation":""}
        result = basic_calculator(content["operator1"], content["operator2"], content["operation"])
        return jsonify({"result": result})

    elif request.method == 'GET':
        return "A sample calculator app - backend"

    else:
        return "Not a valid method"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
