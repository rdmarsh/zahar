
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

