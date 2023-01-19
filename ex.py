import os
from glob import glob
import re

def example_path():
    PATH_LIST = ['.', './', '..', '../']
    # for path in PATH_LIST:
    #     print(f'> PATH: {path}')
    #     print(f'>> RESULT: {os.listdir(path)}')

    for path in PATH_LIST:
        result_str = '\n'.join(['\t' + x for x in os.listdir(path)])
        print(f'> PATH: {path}')
        print(f'>> RESULT:\n' + result_str)


def generate_amount_list(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
            amount_list = content.split('\n')
    except FileNotFoundError as error:
        print(error)
        return
    print(f'The amount_list for path <{path}> is:\n{amount_list}')

def example_str_methods():
    test_string = '1000 hs 14 min'
    # pattern r'\d+ hs'
    # # matches one or more digits, followed by a space and the characters 'hs'
    hs_raw = re.findall(r'\d+ hs',test_string)
    hs_clean = hs_raw[0].replace(' hs','')
    hs_int = int(hs_clean)
    print(f'The string {test_string} have {hs_int} hs')


print('example_str_methods() START...')
example_str_methods()
print('... example_str_methods() END\n')
print('example_path() START...')
example_path()
print('... example_path() END\n')
print('\ngenerate_amount_list() START...')
print('> test for FAKE_PATH')
generate_amount_list('FAKE_PATH')
path = './examples/BBB - amount_time'
print(f'>> test for {path}')
generate_amount_list(path)
print('... generate_amount_list() END\n')


