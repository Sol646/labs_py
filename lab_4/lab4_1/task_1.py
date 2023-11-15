import json

INPUT = 'input.json'


def task() -> float:
    with open(INPUT) as input_data:
        json_data = json.load(input_data)
        sum_data = sum([i['score'] * i['weight'] for i in json_data])
        return round(sum_data, 3)


print(task())
