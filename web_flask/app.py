from flask import Flask
from flask import render_template, request

import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():

    q = request.args.get("q", "")

    db = ["idw", "rbf"]
    results = [x for x in db if q in x]
    empty = len(results) == 0
    return render_template("search.html", results=results, empty=empty)


@app.route("/sampling/")
def sampling():

    n_samples = int(request.args.get("n", 10))

    samples = list(np.random.random(size=n_samples))
    x = list(range(len(samples)))

    return render_template("sampling.html", n_samples=n_samples, samples=samples, x=x)


@app.route("/interpolation/idw")
def interpolation_idw():
    return render_template("interpolation/idw.html")


@app.route("/interpolation/rbf")
def interpolation_rbf():
    return render_template("interpolation/rbf.html")


@app.route("/interpolation/1d")
def interpolation_1d():
    return render_template("interpolation/1d.html")
