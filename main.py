from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if n == sum:
       result = {
           "Number" : n,
           "Armstrong" : True,
       } 
    else:
       
       result = {
           "Number" : n,
           "Armstrong" : False,
       } 

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)