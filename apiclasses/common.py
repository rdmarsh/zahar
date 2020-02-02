# magic from https://stackoverflow.com/questions/40182157/python-click-shared-options-and-flags-between-commands

import click

# time

time_from = [click.option('--time_from', help='Return only objects that have been generated after the given time')]
time_till = [click.option('--time_till', help='Return only objects that have been generated before the given time.')]
lastChangeSince = [click.option('--lastChangeSince', 'lastChangeSince', help='Return only triggers that have changed their state after the given time.')]
lastChangeTill = [click.option('--lastChangeTill', 'lastChangeTill', help='Return only triggers that have changed their state before the given time.')]

# booleans

inherited    = [click.option('--inherited', is_flag=True, default=False, help='Return only objects inherited from a template.')]
templated    = [click.option('--templated', is_flag=True, default=False, help='Return only objects that belong to a template.')]
monitored    = [click.option('--monitored', is_flag=True, default=False, help='Return only enabled objects that belong to monitored host.')]
acknowledged = [click.option('--acknowledged', is_flag=True, default=False, help='Return only objects that have been acknowledged.')]
dependent    = [click.option('--dependent', is_flag=True, default=False, help='return only triggers that have dependencies')]
maintenance  = [click.option('--maintenance', is_flag=True, default=False, help='return only enabled triggers that belong to hosts in maintenance')]

editable = [click.option('--editable', is_flag=True, default=False, help='Return objects with write permissions.')]

# flags

withUnacknowledgedEvents = [click.option('--withUnacknowledgedEvents', 'withUnacknowledgedEvents', is_flag=True, default=None, help='Return only triggers that have unacknowledged events.')]
withAcknowledgedEvents = [click.option('--withAcknowledgedEvents', 'withAcknowledgedEvents', is_flag=True, default=None, help='Return only triggers with all events acknowledged')]
withLastEventUnacknowledged = [click.option('--withLastEventUnacknowledged', 'withLastEventUnacknowledged', is_flag=True, default=None, help='Return only triggers with the last event unacknowledged')]
skipDependent = [click.option('--skipDependent', 'skipDependent', is_flag=True, default=None, help='Skip triggers in a problem state that are dependent on other triggers')]
only_true = [click.option('--only_true', 'only_true', is_flag=True, default=None, help='Return only triggers that have recently been in a problem state.')]
expandComment = [click.option('--expandComment', 'expandComment', is_flag=True, default=None, help='Expand macros in the trigger description.')]
expandDescription = [click.option('--expandDescription', 'expandDescription', is_flag=True, default=None, help='Expand macros in the name of the trigger.')]
expandExpression = [click.option('--expandExpression', 'expandExpression', is_flag=True, default=None, help='Expand functions and macros in the trigger expression.')]
noInheritance = [click.option('--noInheritance', 'noInheritance', is_flag=True, default=None, help='Do not return inherited template screens.')]




active = [click.option('--active', 'active', is_flag=True, default=None, help='Return only enabled triggers that belong to monitored hosts.')]
countOutput = [click.option('--countOutput', 'countOutput', is_flag=True, default=None, help='Return count of records instead of data.')]
expandUrls = [click.option('--expandUrls', 'expandUrls', is_flag=True, default=None, help='Adds global map URLs to the corresponding map elements and expands macros in all map element URLs.')]
webitems = [click.option('--webitems', 'webitems', is_flag=True, default=None, help='Include web items in the result.')]
expandStepName = [click.option('--expandStepName', 'expandStepName', is_flag=True, default=None, help='Expand macros in the names of steps.')]
expandName  = [click.option('--expandName',  'expandName',  is_flag=True, default=None, help='Expand macros in the name.')]
select_image  = [click.option('--select_image',  'select_image',  is_flag=True, default=None, help='Return the Base64 encoded image in the image property.')]
monitored_hosts  = [click.option('--monitored_hosts',  'monitored_hosts',  is_flag=True, default=None, help='Return only host groups that contain monitored hosts.')]
real_hosts  = [click.option('--real_hosts',  'real_hosts',  is_flag=True, default=None, help='Return only host groups that contain hosts.')]
templated_hosts  = [click.option('--templated_hosts',  'templated_hosts',  is_flag=True, default=None, help='Return only host groups that templates.')]
with_applications  = [click.option('--with_applications',  'with_applications',  is_flag=True, default=None, help='Return only host groups that contain hosts with applications.')]
with_graphs  = [click.option('--with_graphs',  'with_graphs',  is_flag=True, default=None, help='Return only host groups that contain hosts with graphs.')]
with_hosts_and_templates  = [click.option('--with_hosts_and_templates',  'with_hosts_and_templates',  is_flag=True, default=None, help='Return only host groups that contain hosts or templates.')]
with_httptests  = [click.option('--with_httptests',  'with_httptests',  is_flag=True, default=None, help='Return only host groups that contain http checks.')]
with_items  = [click.option('--with_items',  'with_items',  is_flag=True, default=None, help='Return only host groups that contain hosts or templates with items.')]
with_monitored_httptests  = [click.option('--with_monitored_httptests',  'with_monitored_httptests',  is_flag=True, default=None, help='Return only host groups that contain hosts with enabled web checks.')]
with_monitored_items  = [click.option('--with_monitored_items',  'with_monitored_items',  is_flag=True, default=None, help='Return only host groups that contain hosts or templates with enabled items.')]
with_monitored_triggers  = [click.option('--with_monitored_triggers',  'with_monitored_triggers',  is_flag=True, default=None, help='Return only host groups that contain hosts with enabled triggers. All of the items used in the trigger must also be enabled.')]
with_simple_graph_items  = [click.option('--with_simple_graph_items',  'with_simple_graph_items',  is_flag=True, default=None, help='Return only host groups that contain hosts with numeric items.')]
with_triggers  = [click.option('--with_triggers',  'with_triggers',  is_flag=True, default=None, help='Return only host groups that contain hosts with triggers.')]
proxy_hosts  = [click.option('--proxy_hosts',  'proxy_hosts',  is_flag=True, default=None, help='Return only proxies.')]
withInventory  = [click.option('--withInventory',  'withInventory',  is_flag=True, default=None, help='Return only hosts that have inventory data.')]
globalmacro  = [click.option('--globalmacro',  'globalmacro',  is_flag=True, default=None, help='Return global macros instead of host macros.')]
getAccess  = [click.option('--getAccess',  'getAccess',  is_flag=True, default=None, help='Return user groups that the user belongs to in the usrgrps property.')]

# strings

group  = [click.option('--group',  'group',  help='Return only items that belong to a group with the given name.')]
functions  = [click.option('--functions',  'functions',  help='Return only triggers that use the given functions.')]
host  = [click.option('--host',  'host',  help='Return only items that belong to a host with the given name.')]
application  = [click.option('--application',  'application',  help='Return only items that belong to an application with the given name.')]
intervals  = [click.option('--intervals',  'intervals',  help='Time intervals to return service layer availability information about')]

# todo: this should be a flag, but zabbix doco says otherwise
recent  = [click.option('--recent',  'recent',  help='return PROBLEM and recently RESOLVED problems')]



# ints

min_severity  = [click.option('--min_severity',  'min_severity',  help='Return only triggers with severity greater or equal than the given severity.')]
# todo: make this a choices
eventobject  = [click.option('--eventobject',  'eventobject',  default='0', help='Return objects generated by events related to objects of the given type.')]
eventsource  = [click.option('--eventsource',  'eventsource',  default='0', help='Return objects generated by events of the given type')]
limitSelects = [click.option('--limitSelects', 'limitSelects', type=int, default=1000, help='Return objects generated by events of the given type')]
severities = [click.option('--severity', type=int, multiple=True, help='Return only objects with given trigger severities.')]
evaltype = [click.option('--evaltype', type=int, multiple=True, default=0, help='Rules for tag searching')]

value          = [click.option('--value',         'value',          type=int, multiple=True, help='Return objects with given value.')]
status         = [click.option('--status',        'status',         type=int, multiple=True, help='Return users with given status.')]
with_gui_access = [click.option('--with_gui_access', 'with_gui_access', type=int, multiple=True, help='Return users with given status.')]

# todo: these don't work or are wonky https://www.zabbix.com/documentation/3.2/manual/api/reference/event/get
source       = [click.option('--source',       'source',       type=int, help='Return objects with the given type')]
history      = [click.option('--history',      'history',      type=int, help='History object types to return.')]
object       = [click.option('--object',       'object',       type=int, help='Return objects with the given type')]
type         = [click.option('--type',         'type',         type=int, default=0, help='Return only graph items with the given type.')]


# ids

actionids      = [click.option('--actionid',      'actionids',      type=int, multiple=True, help='Return responses with the given action id.')]
parentTemplateids = [click.option('--parentTemplateid', 'parentTemplateids', type=int, multiple=True, help='Return responses with the given parentTemplate id.')]
serviceids     = [click.option('--serviceid',     'serviceids',     type=int, multiple=True, help='Return responses with the given service id.')]
parentids      = [click.option('--parentid',      'parentids',      type=int, multiple=True, help='Return responses with the given parent id.')]
childids       = [click.option('--childid',       'childids',       type=int, multiple=True, help='Return responses with the given child id.')]
valuemapids    = [click.option('--valuemapid',    'valuemapids',    type=int, multiple=True, help='Return responses with the given valuemap id.')]
globalmacroids = [click.option('--globalmacroid', 'globalmacroid',  type=int, multiple=True, help='Return responses with the given globmacro id.')]
hostmacroids   = [click.option('--hostmacroid',   'hostmacroids',   type=int, multiple=True, help='Return responses with the given hostmacro id.')]
iconmapids     = [click.option('--iconmapid',     'iconmapids',     type=int, multiple=True, help='Return responses with the given iconmap id.')]
nodeids        = [click.option('--nodeid',        'nodeids',        type=int, multiple=True, help='Return responses with the given node id.')]
proxyids       = [click.option('--proxyid',       'proxyids',       type=int, multiple=True, help='Return only hosts that are monitored by the given proxies.')]
alertids       = [click.option('--alertid',       'alertids',       type=int, multiple=True, help='Return responses with the given alert id.')]
applicationids = [click.option('--applicationid', 'applicationids', type=int, multiple=True, help='Return only actions that are configured to send messages to the given user groups.')]
correlationids = [click.option('--correlationid', 'correlationids', type=int, multiple=True, help='Return only objects with the given correlations IDs.')]
correlationids = [click.option('--correlationid', 'correlationids', type=int, multiple=True, help='Return responses with the given correlation id.')]
dcheckids      = [click.option('--dcheckid',      'dcheckids',      type=int, multiple=True, help='Return only objects with the Discovered Host ID')]
dhostids       = [click.option('--dhostid',       'dhostids',       type=int, multiple=True, help='Return only objects with the Discovered Host ID')]
discoveryids   = [click.option('--discoveryid',   'discoveryids',   type=int, multiple=True, help='Return responses with the given discovery id.')]
druleids       = [click.option('--druleid',       'druleids',       type=int, multiple=True, help='Return only discovered hosts that have been created by the given discovery rules.')]
dserviceids    = [click.option('--dserviceid',    'dserviceids',    type=int, multiple=True, help='Return only discovered hosts that are running the given services.')]
eventid_from   = [click.option('--eventid_from',  'eventid_from',   type=int, multiple=False, help='Return results equal to or less than event id.')]
eventid_till   = [click.option('--eventid_till',  'eventid_till',   type=int, multiple=False, help='Return results equal to or more than event id.')]
eventids       = [click.option('--eventid',       'eventids',       type=int, multiple=True, help='Return only actions that are configured to send messages to the given user groups.')]
gitemids       = [click.option('--gitemid',       'gitemids',       type=int, multiple=True, help='Return results with the given graphitem id.')]
graphids       = [click.option('--graphid',       'graphids',       type=int, multiple=True, help='Return objects that use the given graph id.')]
groupids       = [click.option('--groupid',       'groupids',       type=int, multiple=True, help='Return responses that use the host groups in conditions')]
hostids        = [click.option('--hostid',        'hostids',        type=int, multiple=True, help='Return responses that use the host id.')]
httptestids    = [click.option('--httptestid',    'httptestids',    type=int, multiple=True, help='Return responses with the given httptest id.')]
imageids       = [click.option('--imageid',       'imageids',       type=int, multiple=True, help='Return objects that use the given image id.')]
interfaceids   = [click.option('--interfaceid',   'interfaceid',    type=int, multiple=True, help='Return results with the given interface id')]
itemids        = [click.option('--itemid',        'itemids',        type=int, multiple=True, help='Return only actions that are configured to send messages to the given user groups.')]
maintenanceids = [click.option('--maintenanceid', 'maintenanceids', type=int, multiple=True, help='Return responses with the given maintenance id.')]
mediatypeids   = [click.option('--mediatypeid',   'mediatypeids',   type=int, multiple=True, help='Return only actions that use the given media types to send messages.')]
objectids      = [click.option('--objectid',      'objectids',      type=int, multiple=True, help='Return only actions that are configured to send messages to the given user groups.')]
screenids      = [click.option('--screenid',      'screenids',      type=int, multiple=True, help='Return objects that use the given screen id.')]
screenitemids  = [click.option('--screenitemid',  'screenitemid',   type=int, multiple=True, help='Return objects that use the given screenitem id.')]
scriptids      = [click.option('--scriptid',      'scriptids',      type=int, multiple=True, help='Return only actions that are configured to run the given scripts.')]
sysmapids      = [click.option('--sysmapid',      'sysmapids',      type=int, multiple=True, help='Return objects that use the given sysmap id.')]
templateids    = [click.option('--templateid',    'templateids',    type=int, multiple=True, help='Return objects that use the given template id.')]
triggerids     = [click.option('--triggerid',     'triggerids',     type=int, multiple=True, help='Return only actions that use the given triggers in action conditions.')]
userids        = [click.option('--userid',        'userids',        type=int, multiple=True, help='Return only actions that are configured to send messages to the given users.')]
usrgrpids      = [click.option('--usrgrpid',      'usrgrpids',      type=int, multiple=True, help='Return only actions that are configured to send messages to the given user groups.')]
mediaids       = [click.option('--mediaid',       'mediaids',       type=int, multiple=True, help='Return responses with the given media id.')]

# object

# todo this sucks
tags      = [click.option('--tags',      'tags',      help='Return objects with given tags.')]

# todo: for future use once we sort out passing queries
# selectFilter = [
#     click.option('--selectFilter', 'selectFilter',
#                help='Returns the action filter in the filter property.'),
#    ]

# todo: for future use once we sort out passing queries
# selectOperations = [
#    click.option('--selectOperations', 'selectOperations',
#                help='Return action operations in the operations property.'),
#    ]

# todo: for future use once we sort out passing queries
# selectRecoveryOperations = [
#    click.option('--selectRecoveryOperations', 'selectRecoveryOperations',
#                help='Return action recovery operations in the recoveryOperations property.'),
#    ]

# todo: for future use once we sort out passing dynamic choices
# sortfield = [
#    click.option('--sortfield',
#        help='Sort the result by the given properties.'),
#    ]

# These parameters being common for all get command


filter = [
    click.option('--filter',
                 help='Return only results that exactly match the filter.'),
    ]

limit = [
    click.option('-l', '--limit', 'limit',
                 type=int, default=1000,
                 help='Limit results returned.'),
    ]

output = [
    click.option('--output', 'output',
                 multiple=True,
                 help='Object properties to be returned (refered to as "output" in API docs).'),
    ]

# todo: this messes up stuff, should we keep it?
preservekeys = [
    click.option('--preservekeys',
                 is_flag=True, default=None,
                 help='Use IDs as keys in the resulting array.'),
    ]

search = [click.option('--search', help='Return results that match wildcard search (case-insensitive).'), ]
searchInventory = [click.option('--searchInventory', help='Return only hosts that have inventory data matching the given wildcard search.')]

excludeSearch = [
    click.option('--excludeSearch', 'excludeSearch',
                 is_flag=True, default=None,
                 help='Return results that do not match the search criteria.'),
    ]

searchByAny = [
    click.option('--searchByAny', 'searchByAny',
                 is_flag=True, default=False,
                 help='Return results that match either filter or search instead of all of them'),
    ]

searchWildcardsEnabled = [
    click.option('--searchWildcardsEnabled', 'searchWildcardsEnabled',
                 is_flag=True, default=False,
                 help='Enables use of "*" as a wildcard character'),
    ]

startSearch = [
    click.option('--startSearch', 'startSearch',
                 is_flag=True, default=None,
                 help='Compare from the beginning of fields.'),
    ]

sortorder = [
    click.option('--sortorder',
                 type=click.Choice(['ASC', 'DESC']),
                 help='Order of sorting'),
    ]

# These parmataers are common for all zart commands
# we add them to the end rather than the start as they
# are more natural

outputformat = [
    click.option('-o', 'outputformat',
                 default='txt',
                 type=click.Choice(['csv', 'html', 'json', 'latex', 'raw', 'clip', 'xls', 'txt']),
                 help='Output format.')
    ]


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options
