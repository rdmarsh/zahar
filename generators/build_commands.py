#!/usr/bin/env python3

import json
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)

template = env.get_template('command.py.jinja2')

# load our commands from denifition file
with open('../definitions/commands.json') as json_file:
    json_obj = json.load(json_file)

for command_detail in json_obj['commands']:
    command = command_detail['command']

    print('building', command)

    with open('../definitions/options_' + command + '.json') as command_options_file:
        command_options = json.load(command_options_file)
        output = template.render(command_options=command_options)

        f = open('../apiclasses/' + command + '.py', 'w' )
        f.write(output)
        f.close()

