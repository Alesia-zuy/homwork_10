from functions import load_candidates, Candidates

data = load_candidates('candidates.json')


item = Candidates(data)
print(item.get_by_skill('go'))