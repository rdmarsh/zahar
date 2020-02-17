#!/usr/bin/env python3

import json
from jinja2 import Environment, FileSystemLoader


def render_zart(env, commands):
    print('rendering zart')
    template = env.get_template('zart.py.j2')
    output = template.render(commands=commands)

    file_name = '../zart.py'
    print("\tbuilding", file_name)
    f = open(file_name, 'w')
    f.write(output)
    f.close()


def render_commands(env, commands):
    print('rendering commands')
    template = env.get_template('command.py.j2')

    for command in commands:

        with open('../definitions/' + command + '_options.json') as json_file:
            command_options_obj = json.load(json_file)
            output = template.render(command_options=command_options_obj)

            file_name = '../commands/' + command + '.py'
            print("\tbuilding", file_name)
            f = open(file_name, 'w')
            f.write(output)
            f.close()


def render_options(env):
    print('rendering options')
    template = env.get_template('options.py.j2')

    with open('../definitions/options.json') as json_file:
        options_obj = json.load(json_file)
        output = template.render(options=options_obj['options'])

        file_name = '../commands/options.py'
        print("\tbuilding", file_name)
        f = open(file_name, 'w')
        f.write(output)
        f.close()


def render_engine(env):
    print('rendering engine')

    with open('../definitions/options.json') as json_file:
        options_obj = json.load(json_file)
    
    properties = []
    for options_detail in options_obj['options']:
        try:
            options_detail['metavar']

            if options_detail['metavar'] == 'PROPERTY':
                properties.append(options_detail['option'])
                print('\t\tadding', options_detail['option'])
        except:
            pass

    template = env.get_template('engine.py.j2')
    output = template.render(properties=properties)

    file_name = '../engine.py'
    print("\tbuilding", file_name)
    f = open(file_name, 'w')
    f.write(output)
    f.close()


def main():
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    # load our commands from denifition file
    with open('../definitions/commands.json') as json_file:
        commands_obj = json.load(json_file)

    commands = []
    for command_detail in commands_obj['commands']:
        commands.append(command_detail['command'])

    render_zart(env, commands)
    render_commands(env, commands)
    render_options(env)
    render_engine(env)


if __name__ == '__main__':
    main()
