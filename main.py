from flask import Flask, render_template
from utils import load_candidates, get_by_pk, get_by_name, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:x>")
def page_index_pk(x):
    candidate = get_by_pk(x)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_index_name(candidate_name):
    candidates = get_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_cand=len(candidates))


@app.route("/skills/<skill>")
def page_index_skills(skill):
    candidates = get_by_skill(skill)
    return render_template('skill.html', candidates=candidates, count_cand=len(candidates))


app.run(debug=True)
