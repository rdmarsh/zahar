#!/usr/bin/env python3

import pdb
import click
from click.testing import CliRunner
from zart import cli
from tests import test_modules

def main():
    runner = CliRunner()
    test_modules.zart(cli, runner)
    test_modules.zart_flag_help(cli, runner)
    test_modules.zart_flag_version(cli, runner)

    test_modules.zart_flag_config(cli, runner)
    test_modules.zart_flag_zab_url(cli, runner)
    test_modules.zart_flag_zab_usr(cli, runner)
    test_modules.zart_flag_zab_pwd(cli, runner)

    test_modules.zart_flag_sck_prx(cli, runner)
    test_modules.zart_flag_sck_prx_bad_flag(cli, runner)

    test_modules.zart_command_action(cli, runner)
    test_modules.zart_command_alert(cli, runner)
    test_modules.zart_command_apiinfo(cli, runner)
    test_modules.zart_command_application(cli, runner)
    test_modules.zart_command_autoregistration(cli, runner)
    test_modules.zart_command_correlation(cli, runner)
    test_modules.zart_command_dashboard(cli, runner)
    test_modules.zart_command_dcheck(cli, runner)
    test_modules.zart_command_dhost(cli, runner)
    test_modules.zart_command_discoveryrule(cli, runner)
    test_modules.zart_command_drule(cli, runner)
    test_modules.zart_command_dservice(cli, runner)
    test_modules.zart_command_event(cli, runner)
    test_modules.zart_command_graph(cli, runner)
    test_modules.zart_command_graphitem(cli, runner)
    test_modules.zart_command_graphprototype(cli, runner)
    test_modules.zart_command_history(cli, runner)
    test_modules.zart_command_host(cli, runner)
    test_modules.zart_command_hostgroup(cli, runner)
    test_modules.zart_command_hostinterface(cli, runner)
    test_modules.zart_command_hostprototype(cli, runner)
    test_modules.zart_command_httptest(cli, runner)
    test_modules.zart_command_iconmap(cli, runner)
    test_modules.zart_command_image(cli, runner)
    test_modules.zart_command_item(cli, runner)
    test_modules.zart_command_itemprototype(cli, runner)
    test_modules.zart_command_maintenance(cli, runner)
    test_modules.zart_command_map(cli, runner)
    test_modules.zart_command_mediatype(cli, runner)
    test_modules.zart_command_problem(cli, runner)
    test_modules.zart_command_proxy(cli, runner)
    test_modules.zart_command_screen(cli, runner)
    test_modules.zart_command_screenitem(cli, runner)
    test_modules.zart_command_script(cli, runner)
    test_modules.zart_command_service(cli, runner)
    #test_modules.zart_command_servicesla(cli, runner)
    test_modules.zart_command_template(cli, runner)
    test_modules.zart_command_templatescreen(cli, runner)
    test_modules.zart_command_templatescreenitem(cli, runner)
    test_modules.zart_command_trend(cli, runner)
    test_modules.zart_command_trigger(cli, runner)
    test_modules.zart_command_triggerprototype(cli, runner)
    test_modules.zart_command_user(cli, runner)
    test_modules.zart_command_usergroup(cli, runner)
    test_modules.zart_command_usermacro(cli, runner)
    test_modules.zart_command_usermedia(cli, runner)
    test_modules.zart_command_valuemap(cli, runner)


if __name__ == '__main__':
    main()
