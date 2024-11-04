from flask import Flask
#API Servisini Oluşturma
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the REST API!"

if __name__ == '__main__':
    app.run(port=5000)

#2 Sayıyı Toplayan Endpoint

@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add_numbers(num1, num2):
    result = num1 + num2
    return {'result': result}
