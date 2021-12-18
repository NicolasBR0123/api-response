from flask import Flask

app = Flask("API em Python")

@app.route("/user", methods=["GET"])
def getUser():
    body = {
	    "Nome": "Nicolas",
	    "idade": 22,
	    "telefone": "11 942644773"
    }

    return body

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
