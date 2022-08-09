from functions import load_candidates, Candidates

data = load_candidates('candidates.json')


item = Candidates(data)
a = item.get_all
for i in a:
    print(item.get_by_pk(i))