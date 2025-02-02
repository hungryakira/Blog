from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

#Retrieve Blog text from api
response = requests.get(blog_url)
all_posts = response.json()

#---- Home Page showing list of blog posts using template "index.html"
@app.route('/')
def home():
    return render_template("index.html", posts = all_posts)

#---- create pages for individual pages using the template "post.html"
@app.route('/post/<int:id>')
def post(id):
    for entry in all_posts:
        if entry["id"] == id:
            requested_post = entry
    return render_template("post.html", posts = requested_post)


if __name__ == "__main__":
    app.run(debug=True)
