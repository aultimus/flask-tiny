from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

# python -m venv .venv
# pip3 install flask
# python app.py
# TODO: freeze reqts into requirements.txt
