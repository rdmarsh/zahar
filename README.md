![Zart application](https://github.com/rdmarsh/zahar/workflows/Zart%20application/badge.svg)

zart (Zabbix API Retrieval Tool)

Part of the zahar (Zabbix Audit Hygiene and Report) project

config in ~/.config/zahar

```
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```

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

```
$ ./zart.py action --help
Usage: zart.py action [OPTIONS]

  This command retrieves actions.

Options:
  --actionid INTEGER              Return responses with the given action ids.
  --groupid INTEGER               Return responses that use the host groups in
                                  conditions
  --hostid INTEGER                Return responses that use the host id.
  --triggerid INTEGER             Return only actions that use the given
                                  triggers in action conditions.
  --mediatypeid INTEGER           Return only actions that use the given media
                                  types to send messages.
  --usrgrpid INTEGER              Return only actions that are configured to
                                  send messages to the given user groups.
  --userid INTEGER                Return only actions that are configured to
                                  send messages to the given users.
  --scriptid INTEGER              Return only actions that are configured to
                                  run the given scripts.
  --sortfield [actionid|name|status]
  --countOutput                   Return count of records instead of data.
  --editable                      Return objects with write permissions.
  --filter TEXT                   Return only results that exactly match the
                                  filter.
  --limit INTEGER                 Limit results returned.
  --output TEXT                   Object properties to be returned (refered to
                                  as "output" in API docs).
  --preservekeys                  Use IDs as keys in the resulting array.
  --sortorder [ASC|DESC]          Order of sorting
  --search TEXT                   Return results that match wildcard search
                                  (case-insensitive).
  -f [csv|html|json|latex|raw|clip|xls|txt]
                                  Output format.
  --help                          Show this message and exit.
  ```
  
  ```
  $ ./zart.py action --actionid 3 --output extend -f json | jq
[
  {
    "actionid": "3",
    "name": "Report problems to Zabbix administrators",
    "eventsource": "0",
    "status": "0",
    "esc_period": "1h",
    "def_shortdata": "Problem: {EVENT.NAME}",
    "def_longdata": "Problem started at {EVENT.TIME} on {EVENT.DATE}\r\nProblem name: {EVENT.NAME}\r\nHost: {HOST.NAME}\r\nSeverity: {EVENT.SEVERITY}\r\n\r\nOriginal problem ID: {EVENT.ID}\r\n{TRIGGER.URL}",
    "r_shortdata": "Resolved: {EVENT.NAME}",
    "r_longdata": "Problem has been resolved at {EVENT.RECOVERY.TIME} on {EVENT.RECOVERY.DATE}\r\nProblem name: {EVENT.NAME}\r\nHost: {HOST.NAME}\r\nSeverity: {EVENT.SEVERITY}\r\n\r\nOriginal problem ID: {EVENT.ID}\r\n{TRIGGER.URL}",
    "pause_suppressed": "1",
    "ack_shortdata": "Updated problem: {EVENT.NAME}",
    "ack_longdata": "{USER.FULLNAME} {EVENT.UPDATE.ACTION} problem at {EVENT.UPDATE.DATE} {EVENT.UPDATE.TIME}.\r\n{EVENT.UPDATE.MESSAGE}\r\n\r\nCurrent problem status is {EVENT.STATUS}, acknowledged: {EVENT.ACK.STATUS}."
  }
]
```

```
$ ./zart.py action --actionid 3 --output name --output ack_shortdata -f html
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>actionid</th>
      <th>name</th>
      <th>ack_shortdata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>Report problems to Zabbix administrators</td>
      <td>Updated problem: {EVENT.NAME}</td>
    </tr>
  </tbody>
</table>
```

```
$ ./zart.py action --actionid 3 --output name --output ack_shortdata -f latex
\begin{tabular}{lll}
\toprule
actionid &                                      name &                  ack\_shortdata \\
\midrule
       3 &  Report problems to Zabbix administrators &  Updated problem: \{EVENT.NAME\} \\
\bottomrule
\end{tabular}
```
