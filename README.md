zart Zabbix API Retrieval Tool

zahar Zabbix Audit Hygiene and Report

config in ~/.config/zahar

$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .

```
$ ./zart.py --help
Usage: zart.py [OPTIONS] COMMAND [ARGS]...

  zart Zabbix API Retrieval Tool.

Options:
  --config PATH  Read configuration from FILE.
  --zaburl TEXT  Zabbix URL.
  --userid TEXT  Zabbix username.
  --passwd TEXT  Zabbix password.
  --version      Show the version and exit.
  --help         Show this message and exit.

Commands:
  action              retrieve actions
  alert               retrieve alerts
  application         retrieve applications
  correlation         This command retrieves correlations.
  dcheck              This command retrieves dchecks.
  dhost               This command retrieves dhosts.
  discoveryrule       This command retrieves discoveryrules.
  drule               This command retrieves drules.
  dservice            This command retrieves dservices.
  event               This command retrieves events.
  graph               retrieve graphs
  graphitem           This command retrieves graphitems.
  graphprototype      retrieve graphprototype
  history             This command retrieves historys.
  host                This command retrieves hosts.
  hostgroup           This command retrieves hostgroups.
  hostinterface       This command retrieves hostinterfaces.
  hostprototype       retrieve hostprototypes
  httptest            retrieve httptests
  iconmap             This command retrieves iconmaps.
  image               retrieve images
  item                This command retrieves items.
  itemprototype       This command retrieves itemprototypes.
  maintenance         This command retrieves maintenances.
  map                 This command retrieves maps.
  mediatype           This command retrieves mediatypes.
  problem             This command retrieves problems.
  proxy               This command retrieves proxys.
  screen              This command retrieves screens.
  screenitem          This command retrieves screenitems.
  script              This command retrieves scripts.
  service             This command retrieves services.
  template            This command retrieves templates.
  templatescreen      This command retrieves templatescreens.
  templatescreenitem  This command retrieves templatescreenitems.
  trend               This command retrieves trends.
  trigger             This command retrieves triggers.
  triggerprototype    This command retrieves triggerprototypes.
  user                This command retrieves users.
  usergroup           This command retrieves usergroups.
  usermacro           This command retrieves usermacros.
  usermedia           This command retrieves usermedias.
  valuemap            This command retrieves valuemaps.
  ```
