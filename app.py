from flask import Flask, render_template
import caching
app = Flask(__name__)

def curr_symbols():
    print(caching.get_rate())
@app.route("/")
@app.route("/home/")
def home(title="Home page"):
    return render_template('home.html',title=title, )

@app.route("/about/")
def about(title="About page"):
    return render_template('about.html',title=title, )


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
