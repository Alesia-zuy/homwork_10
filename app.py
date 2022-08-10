from flask import Flask
from functions import load_candidates, Candidates

candidates = 'candidates.json'
candidates_class = Candidates(load_candidates(candidates))

app = Flask(__name__)


@app.route("/")
def page_home():
    candidates_all = candidates_class.get_all
    enumeration = [f'\n{candidates_class.get_by_pk(i)}\n' for i in candidates_all]
    return f'<pre>{" ".join(enumeration)}</pre>'


@app.route("/candidates/<x>")
def page_candidates(x):
    return f'{candidates_class.get_by_pk_picture(x)}\n' \
           f'<pre>{candidates_class.get_by_pk(x)}<pre>'


if __name__ == '__main__':
    app.run()
