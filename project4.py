# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something

from pathlib import Path
from code import *
import random
import sys
def _read_input_file_path(file_path):
    input_file_path = Path(file_path)
    if (input_file_path.exists() or input_file_path.is_file()) is False:
        print("FILE NOT FOUND")
        sys.exit()
    else:
        return Path(input_file_path)

def get_the_input():
    input_file_path = _read_input_file_path(input())
    sentence_time = int(input())
    rule_name = input()
    return input_file_path, sentence_time, rule_name

def main() -> None:
    input_file_path, sentence_time, rule_name = get_the_input()
    with open(input_file_path, "r") as file1:
        all_data = file1.readlines()
        strip_data = [data.strip() for data in all_data]
        parsed_info = Parsing(strip_data)
        for _ in range(sentence_time):
            print(next(recursion_function(parsed_info, rule_name)))

def recursion_function(parsed_info, rule_name):
    opt = random_choose_the_option(parsed_info.get_rule(rule_name).get_options())
    result_str = ""
    for j in opt.var_terminal:
        if isinstance(j, Terminal):
            result_str += j.get_terminal() + " "
        else:
            result_str += next(recursion_function(parsed_info, j.get_variable())) + " "
    yield result_str[:-1]


def random_choose_the_option(options):
    weight = []
    for i in range(len(options)):
        weight.append(int(options[i]._weight))
    return random.choices(options, weights = weight)[0]


if __name__ == '__main__':
    main()
