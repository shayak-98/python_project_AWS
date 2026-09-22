from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Python AWS Project</h1>
    <h2>Successfully Deployed on AWS EC2</h2>
    <p>Python + Flask + GitHub + Ubuntu + EC2</p>
    """

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>My First AWS Python Project</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)