from flask import Flask, render_template
app = Flask(__name__, static_folder="static")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
@app.route("/catalog")
@app.route("/books/index")
def books():
    return render_template("books/index.html")
@app.route("/books/book<int:id>")
def book(id):
    return render_template(f"books/book{id}.html")