from flask import Flask, request, jsonify, render_template
import base64
admission_controller = Flask(__name__)
@main.route('/', methods=['GET'])
def hello():
    # return "Hello"
    return render_template('index.html', title='Docker Python', name='Namct')

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=5000)