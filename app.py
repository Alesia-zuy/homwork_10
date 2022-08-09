from flask import Flask
import json

candidates = 'candidates.json'

with open(candidates, encoding='utf-8') as file:
    data_candidates = json.load(file)

