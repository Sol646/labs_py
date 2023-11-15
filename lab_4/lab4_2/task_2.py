import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_csv, open(OUTPUT_FILENAME, 'w') as output_json:
        result_dict = []
        for row in csv.DictReader(input_csv):
            result_dict.append(dict(row.items()))
        json.dump(result_dict, output_json, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
