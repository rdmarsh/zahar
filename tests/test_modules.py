def zart(cli, runner):
    result = runner.invoke(cli)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'Usage:' in result.output, "Text 'Usage:' missing in output"
    assert 'Options:' in result.output, "Text 'Options:' missing in output"
    assert 'Commands:' in result.output, "Text 'Commands:' missing in output"

def zart_flag_help(cli,runner):
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'Usage:' in result.output, "Text 'Usage:' missing in output"
    assert 'Options:' in result.output, "Text 'Options:' missing in output"
    assert 'Commands:' in result.output, "Text 'Commands:' missing in output"

def zart_flag_version(cli,runner):
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'version' in result.output, "Text 'version' missing in output"

def zart_flag_config(cli,runner):
    result = runner.invoke(cli, ['--config'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_zaburl(cli,runner):
    result = runner.invoke(cli, ['--zaburl'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_userid(cli,runner):
    result = runner.invoke(cli, ['--userid'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_passwd(cli,runner):
    result = runner.invoke(cli, ['--passwd'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_proxy(cli,runner):
    result = runner.invoke(cli, ['--proxy'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires 2 arguments' in result.output, "Text 'option requires 2 arguments' missing in output"

def zart_flag_proxy_bad_flag(cli,runner):
    result = runner.invoke(cli, ['--proxy', 'bad', 'flag'])
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'flag is not a valid integer' in result.output, "Text 'flag is not a valid integer' missing in output"

def zart_command_action(cli,runner):
    result = runner.invoke(cli, ['action'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_alert(cli,runner):
    result = runner.invoke(cli, ['alert'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_apiinfo(cli,runner):
    result = runner.invoke(cli, ['apiinfo'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_application(cli,runner):
    result = runner.invoke(cli, ['application'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_autoregistration(cli,runner):
    result = runner.invoke(cli, ['autoregistration'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_correlation(cli,runner):
    result = runner.invoke(cli, ['correlation'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dashboard(cli,runner):
    result = runner.invoke(cli, ['dashboard'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dcheck(cli,runner):
    result = runner.invoke(cli, ['dcheck'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dhost(cli,runner):
    result = runner.invoke(cli, ['dhost'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_discoveryrule(cli,runner):
    result = runner.invoke(cli, ['discoveryrule'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_drule(cli,runner):
    result = runner.invoke(cli, ['drule'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dservice(cli,runner):
    result = runner.invoke(cli, ['dservice'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_event(cli,runner):
    result = runner.invoke(cli, ['event'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graph(cli,runner):
    result = runner.invoke(cli, ['graph'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graphitem(cli,runner):
    result = runner.invoke(cli, ['graphitem'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graphprototype(cli,runner):
    result = runner.invoke(cli, ['graphprototype'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_history(cli,runner):
    result = runner.invoke(cli, ['history'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_host(cli,runner):
    result = runner.invoke(cli, ['host'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostgroup(cli,runner):
    result = runner.invoke(cli, ['hostgroup'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostinterface(cli,runner):
    result = runner.invoke(cli, ['hostinterface'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostprototype(cli,runner):
    result = runner.invoke(cli, ['hostprototype'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_httptest(cli,runner):
    result = runner.invoke(cli, ['httptest'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_iconmap(cli,runner):
    result = runner.invoke(cli, ['iconmap'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_image(cli,runner):
    result = runner.invoke(cli, ['image'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_item(cli,runner):
    result = runner.invoke(cli, ['item'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_itemprototype(cli,runner):
    result = runner.invoke(cli, ['itemprototype'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_maintenance(cli,runner):
    result = runner.invoke(cli, ['maintenance'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_map(cli,runner):
    result = runner.invoke(cli, ['map'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_mediatype(cli,runner):
    result = runner.invoke(cli, ['mediatype'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_problem(cli,runner):
    result = runner.invoke(cli, ['problem'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_proxy(cli,runner):
    result = runner.invoke(cli, ['proxy'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_screen(cli,runner):
    result = runner.invoke(cli, ['screen'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_screenitem(cli,runner):
    result = runner.invoke(cli, ['screenitem'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_script(cli,runner):
    result = runner.invoke(cli, ['script'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_service(cli,runner):
    result = runner.invoke(cli, ['service'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_servicesla(cli,runner):
    result = runner.invoke(cli, ['servicesla'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_template(cli,runner):
    result = runner.invoke(cli, ['template'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_templatescreen(cli,runner):
    result = runner.invoke(cli, ['templatescreen'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_templatescreenitem(cli,runner):
    result = runner.invoke(cli, ['templatescreenitem'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_trend(cli,runner):
    result = runner.invoke(cli, ['trend'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_trigger(cli,runner):
    result = runner.invoke(cli, ['trigger'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_triggerprototype(cli,runner):
    result = runner.invoke(cli, ['triggerprototype'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_user(cli,runner):
    result = runner.invoke(cli, ['user'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usergroup(cli,runner):
    result = runner.invoke(cli, ['usergroup'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usermacro(cli,runner):
    result = runner.invoke(cli, ['usermacro'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usermedia(cli,runner):
    result = runner.invoke(cli, ['usermedia'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_valuemap(cli,runner):
    result = runner.invoke(cli, ['valuemap'])
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
