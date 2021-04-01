from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def hello():
    message = " "
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    return render_template('main.html'), 200


@app.route("/game")
def game():
    return render_template('game.html')


@app.route("/unity")
def unity():
    return render_template('index.html'), 200

@app.route('/echo', methods=['POST'])
def echo():
    # print("Before JSON")
    # data = request.get_json()
    # print(data)
    # print("This is where i am")
    #
    # new_user_id = data['userId']
    # new_user_name = data['userName']
    # new_score = data['score']

    return "Oks"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
