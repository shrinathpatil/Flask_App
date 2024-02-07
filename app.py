from flask import Flask,request,jsonify


app=Flask(__name__)

print("hello")

@app.route("/api/test", methods=['GET'])
def message():
  body=request.get_json()
  print(body)
  return "hello"

@app.route("/api/hello/<string:name>", methods=['GET'])
def sayHello(name):
  print(name)
  return jsonify({"data":f"Hello, {name}","code":69}),200

if __name__=='main':
  app.run()

