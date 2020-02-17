
json for commands
to validate:


jsonlint myfile.json
--validate



for i in `jq -r '.[]' < _commands.json` ; do ls $i.json ; done



cat  commands.json | jq '.["commands"][]["command"]'


item.get

This directory holds our definitions for connecting to the zabbix api


is nodeids still supported option for history? it's missing from source code
todo: nodeid may be an error in zabbix api doco


servicesget sla:
    # todo: this is probably not working, getsla needs to be in engine.py

template:
# todo: status may not be part of the api even though it's in the zabbix doco

http://www.catb.org/~esr/writings/taoup/html/ch10s05.html

# todo: preservekeys messes up stuff, should we keep it?

todo: tags suck at the moment
# todo: fix bare except left lying around and write a better error messages
# todo: pull in help text for search from definition file

# todo: for zahar: 
#action = subprocess.run(['./zart.py', 'action','--limit','2','-o','json'], stdout=subprocess.PIPE, encoding='utf-8')
#user = subprocess.run(['./zart.py', 'user','--limit','2','-o','json'], stdout=subprocess.PIPE, encoding='utf-8')

