def zart(cli, runner):
    print('zart')
    result = runner.invoke(cli)
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'Usage:' in result.output, "Text 'Usage:' missing in output"
    assert 'Options:' in result.output, "Text 'Options:' missing in output"
    assert 'Commands:' in result.output, "Text 'Commands:' missing in output"

def zart_flag_help(cli,runner):
    print('zart --help')
    result = runner.invoke(cli, ['-v', '--help'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'Usage:' in result.output, "Text 'Usage:' missing in output"
    assert 'Options:' in result.output, "Text 'Options:' missing in output"
    assert 'Commands:' in result.output, "Text 'Commands:' missing in output"

def zart_flag_version(cli,runner):
    print('zart --version')
    result = runner.invoke(cli, ['-v', '--version'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
    assert 'version' in result.output, "Text 'version' missing in output"

def zart_flag_config(cli,runner):
    print('zart --config')
    result = runner.invoke(cli, ['-v', '--config'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_zab_url(cli,runner):
    print('zart --zab_url')
    result = runner.invoke(cli, ['-v', '--zab_url'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_zab_usr(cli,runner):
    print('zart --zab_usr')
    result = runner.invoke(cli, ['-v', '--zab_usr'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_zab_pwd(cli,runner):
    print('zart --zab_pwd')
    result = runner.invoke(cli, ['-v', '--zab_pwd'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires an argument' in result.output, "Text 'option requires an argument' missing in output"

def zart_flag_sck_prx(cli,runner):
    print('zart --sck_prx')
    result = runner.invoke(cli, ['-v', '--sck_prx'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'option requires 2 arguments' in result.output, "Text 'option requires 2 arguments' missing in output"

def zart_flag_sck_prx_bad_flag(cli,runner):
    print('zart --sck_prx')
    result = runner.invoke(cli, ['-v', '--sck_prx', 'bad', 'flag'])
    print(result.exit_code)
    assert result.exit_code == 2, "exitcode: " + str(result.exit_code)
    assert 'Error:' in result.output, "Text 'Error:' missing in output"
    assert 'flag is not a valid integer' in result.output, "Text 'flag is not a valid integer' missing in output"


def zart_command_action(cli,runner):
    print('zart action')
    result = runner.invoke(cli, ['-v', 'action'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_alert(cli,runner):
    print('zart alert')
    result = runner.invoke(cli, ['-v', 'alert'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_apiinfo(cli,runner):
    print('zart apiinfo')
    result = runner.invoke(cli, ['-v', 'apiinfo'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_application(cli,runner):
    print('zart application')
    result = runner.invoke(cli, ['-v', 'application'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_autoregistration(cli,runner):
    print('zart autoregistration')
    result = runner.invoke(cli, ['-v', 'autoregistration'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_correlation(cli,runner):
    print('zart correlation')
    result = runner.invoke(cli, ['-v', 'correlation'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dashboard(cli,runner):
    print('zart dashboard')
    result = runner.invoke(cli, ['-v', 'dashboard'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dcheck(cli,runner):
    print('zart dcheck')
    result = runner.invoke(cli, ['-v', 'dcheck'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dhost(cli,runner):
    print('zart dhost')
    result = runner.invoke(cli, ['-v', 'dhost'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_discoveryrule(cli,runner):
    print('zart discoveryrule')
    result = runner.invoke(cli, ['-v', 'discoveryrule'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_drule(cli,runner):
    print('zart drule')
    result = runner.invoke(cli, ['-v', 'drule'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_dservice(cli,runner):
    print('zart dservice')
    result = runner.invoke(cli, ['-v', 'dservice'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_event(cli,runner):
    print('zart event')
    result = runner.invoke(cli, ['-v', 'event'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graph(cli,runner):
    print('zart graph')
    result = runner.invoke(cli, ['-v', 'graph'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graphitem(cli,runner):
    print('zart graphitem')
    result = runner.invoke(cli, ['-v', 'graphitem'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_graphprototype(cli,runner):
    print('zart graphprototype')
    result = runner.invoke(cli, ['-v', 'graphprototype'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_history(cli,runner):
    print('zart history')
    result = runner.invoke(cli, ['-v', 'history'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_host(cli,runner):
    print('zart host')
    result = runner.invoke(cli, ['-v', 'host'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostgroup(cli,runner):
    print('zart hostgroup')
    result = runner.invoke(cli, ['-v', 'hostgroup'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostinterface(cli,runner):
    print('zart hostinterface')
    result = runner.invoke(cli, ['-v', 'hostinterface'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_hostprototype(cli,runner):
    print('zart hostprototype')
    result = runner.invoke(cli, ['-v', 'hostprototype'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_httptest(cli,runner):
    print('zart httptest')
    result = runner.invoke(cli, ['-v', 'httptest'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_iconmap(cli,runner):
    print('zart iconmap')
    result = runner.invoke(cli, ['-v', 'iconmap'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_image(cli,runner):
    print('zart image')
    result = runner.invoke(cli, ['-v', 'image'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_item(cli,runner):
    print('zart item')
    result = runner.invoke(cli, ['-v', 'item'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_itemprototype(cli,runner):
    print('zart itemprototype')
    result = runner.invoke(cli, ['-v', 'itemprototype'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_maintenance(cli,runner):
    print('zart maintenance')
    result = runner.invoke(cli, ['-v', 'maintenance'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_map(cli,runner):
    print('zart map')
    result = runner.invoke(cli, ['-v', 'map'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_mediatype(cli,runner):
    print('zart mediatype')
    result = runner.invoke(cli, ['-v', 'mediatype'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_problem(cli,runner):
    print('zart problem')
    result = runner.invoke(cli, ['-v', 'problem'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_proxy(cli,runner):
    print('zart proxy')
    result = runner.invoke(cli, ['-v', 'proxy'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_screen(cli,runner):
    print('zart screen')
    result = runner.invoke(cli, ['-v', 'screen'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_screenitem(cli,runner):
    print('zart screenitem')
    result = runner.invoke(cli, ['-v', 'screenitem'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_script(cli,runner):
    print('zart script')
    result = runner.invoke(cli, ['-v', 'script'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_service(cli,runner):
    print('zart service')
    result = runner.invoke(cli, ['-v', 'service'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_servicesla(cli,runner):
    print('zart servicesla')
    result = runner.invoke(cli, ['-v', 'servicesla'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_template(cli,runner):
    print('zart template')
    result = runner.invoke(cli, ['-v', 'template'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_templatescreen(cli,runner):
    print('zart templatescreen')
    result = runner.invoke(cli, ['-v', 'templatescreen'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_templatescreenitem(cli,runner):
    print('zart templatescreenitem')
    result = runner.invoke(cli, ['-v', 'templatescreenitem'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_trend(cli,runner):
    print('zart trend')
    result = runner.invoke(cli, ['-v', 'trend'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_trigger(cli,runner):
    print('zart trigger')
    result = runner.invoke(cli, ['-v', 'trigger'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_triggerprototype(cli,runner):
    print('zart triggerprototype')
    result = runner.invoke(cli, ['-v', 'triggerprototype'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_user(cli,runner):
    print('zart user')
    result = runner.invoke(cli, ['-v', 'user'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usergroup(cli,runner):
    print('zart usergroup')
    result = runner.invoke(cli, ['-v', 'usergroup'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usermacro(cli,runner):
    print('zart usermacro')
    result = runner.invoke(cli, ['-v', 'usermacro'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_usermedia(cli,runner):
    print('zart usermedia')
    result = runner.invoke(cli, ['-v', 'usermedia'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)

def zart_command_valuemap(cli,runner):
    print('zart valuemap')
    result = runner.invoke(cli, ['-v', 'valuemap'])
    print(result.exit_code)
    assert result.exit_code == 0, "exitcode: " + str(result.exit_code)
