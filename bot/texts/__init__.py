import os

import yaml

all_yaml_files = list(filter(lambda x: x.endswith('.yaml'), os.listdir('bot/texts')))

for file in all_yaml_files:
    with open(f'bot/texts/{file}', 'r') as stream:
        filename = file.split('.')[0]
        data = yaml.safe_load(stream)
        exec(f'{filename} = {data}')


"""
It works, but there can be pitfalls.
"""
