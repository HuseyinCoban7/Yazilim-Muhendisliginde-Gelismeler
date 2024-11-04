from flask import Flask, request
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


#Verilen Sayıların Çarpımını Yapan POST endpoint'i

@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return {'result': result}
