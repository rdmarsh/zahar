
json for commands
to validate:


jsonlint myfile.json
--validate



for i in `jq -r '.[]' < _commands.json` ; do ls $i.json ; done



cat  commands.json | jq '.["commands"][]["command"]'


item.get

This directory holds our definitions for connecting to the zabbix api
