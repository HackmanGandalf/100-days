from flask import Flask, render_template, request
import requests
import smtplib

blog_url = requests.get("https://api.npoint.io/31162d0724c4afa70120")
all_posts = blog_url.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    clicked = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            clicked = blog_post
    return render_template('post.html', post=clicked)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form_entry', methods=['post'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    print(name)
    print(email)
    print(phone)
    print(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="email", password="password")
        connection.sendmail(
            from_addr=f"email",
            to_addrs="email",
            msg=f"Subject: Client from Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                    )

    return render_template('success.html')



if __name__ == "__main__":
    app.run(debug=True)

