from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=now)

@app.route('/guess')
def guess():
    # response = requests.get(f"https://api.agify.io/?name={name}").json
    return render_template("guess.html")

@app.route('/guess/<name>')
def result(name):
    response = requests.get(f"https://api.nationalize.io/?name={name}").json()
    return render_template("result.html", name=response["name"], age=response["country"][0]["country_id"])

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/31162d0724c4afa70120"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
if __name__ == "__main__":
    app.run(debug=True)