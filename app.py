from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
	       <h1 style='color: green;'>This is my capstone project version 1.1 by (Anurag jain)</h1>
           """
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
