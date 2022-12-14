import json


def load_candidates(file_):
    """
    Загружает json файл
    """
    with open(file_, encoding='utf-8') as file:
        data_candidates = json.load(file)
        return data_candidates


class Candidates:

    def __init__(self, json_file):
        self.json_file = json_file
        self.get_all = [item['pk'] for item in self.json_file]

    def get_by_pk(self, pk):
        """
        Вывод кандидата по pk
        """
        for item in self.json_file:
            if item['pk'] == int(pk):
                return f'{item["name"]}\n' \
                       f'{item["position"]}\n' \
                       f'{item["skills"]}'

    def get_by_pk_picture(self, pk):
        """
        Вывод картинки по pk
        """
        for item in self.json_file:
            if item['pk'] == int(pk):
                return f'<img src="{item["picture"]}">'

    def get_by_skill(self, skill_name):
        """
        Вывод кандидатов по навыку
        """
        skill = []

        for item in self.json_file:
            if skill_name.lower() in item['skills'].lower():
                skill.append(item['pk'])

        return skill

    def __repr__(self):
        return self.json_file
