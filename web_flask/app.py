from flask import Flask
from flask import render_template, request, send_file

from tempfile import TemporaryFile

import numpy as np
from scipy.interpolate import RBFInterpolator
from scipy.stats.qmc import Halton

import base64
from io import BytesIO
from matplotlib.figure import Figure

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

    n_samples = request.args.get("n", 10, type=int)

    samples = list(np.random.random(size=n_samples))
    x = list(range(len(samples)))

    return render_template("sampling.html", n_samples=n_samples, samples=samples, x=x)


@app.route("/interpolation/idw")
def interpolation_idw():
    return render_template("interpolation/idw.html")


@app.route("/interpolation/rbf")
def interpolation_rbf():

    rng = np.random.default_rng()
    xobs = 2 * Halton(2, seed=rng).random(100) - 1
    yobs = np.sum(xobs, axis=1) * np.exp(-6 * np.sum(xobs ** 2, axis=1))
    xgrid = np.mgrid[-1:1:50j, -1:1:50j]
    xflat = xgrid.reshape(2, -1).T
    yflat = RBFInterpolator(xobs, yobs)(xflat)
    ygrid = yflat.reshape(50, 50)

    fig = Figure()
    ax = fig.subplots()

    ax.pcolormesh(*xgrid, ygrid, vmin=-0.25, vmax=0.25, shading="gouraud")
    p = ax.scatter(*xobs.T, c=yobs, s=50, ec="k", vmin=-0.25, vmax=0.25)
    fig.colorbar(p)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    plot = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("interpolation/rbf.html", plot=plot)


@app.route("/interpolation/1d")
def interpolation_1d():
    return render_template("interpolation/1d.html")


@app.route("/api/scatter")
def scatter():

    y = np.random.random(10)
    x = np.linspace(0, 1, num=len(y))

    fig = Figure()
    ax = fig.subplots()

    ax.scatter(x, y)
    # TODO unique name
    filename = "scatter.png"

    fig.savefig(filename, format="png")

    return send_file(filename, mimetype="image/png")
