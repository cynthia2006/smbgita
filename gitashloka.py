#!/usr/bin/python
import random
import json

# Number of shlokas in each chapter (indexed from zero).
num_shlokas = [47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]

chapter = random.randint(0, 17)
shloka = random.randint(0, num_shlokas[chapter]-1)

# TODO Make the location adjustable using environment vars.
with open(f'data/{chapter}/{shloka}.json') as shloka:
    shloka = json.load(shloka)

    # print(shloka['sanskrit'])
    # print(shloka['iast'])
    print(shloka['translation'])
