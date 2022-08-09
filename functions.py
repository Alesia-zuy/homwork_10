import json


def load_candidates(file_):
    with open(file_, encoding='utf-8') as file:
        data_candidates = json.load(file)
        return data_candidates


class Candidates:

    def __init__(self, json_file):
        self.json_file = json_file
        self.get_all = [item['name'] for item in self.json_file]

    def get_by_pk(self, pk):
        for item in self.json_file:
            if item['pk'] == int(pk):
                return item['name']

    def get_by_skill(self, skill_name):
        result = [item['name'] for item in self.json_file if skill_name in item['skills']]
        return result
