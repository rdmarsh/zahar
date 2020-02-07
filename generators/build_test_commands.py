#!/usr/bin/env python3

import json
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)

template = env.get_template('test_command.py.jinja2')

# load our commands from denifition file
with open('../definitions/commands.json') as json_file:
    json_obj = json.load(json_file)

flags=['config', 'zaburl', 'userid', 'passwd']

commands = []
for command_detail in json_obj['commands']:
    commands.append(command_detail['command'])

#output = template.render(command=command)
output = template.render(flags=flags,commands=commands)

f = open('../tests/test_modules.py', 'w' )
f.write(output)
f.close()

