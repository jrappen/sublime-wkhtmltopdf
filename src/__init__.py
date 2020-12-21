#!/usr/bin/env python
# coding: utf-8


import sublime

from .thread_progress import *
from .window_commands import *
from .wkhtmltopdf import *


PKG_NAME = __package__.split('.')[0]


def is_installed():
    pkgctrl_settings = sublime.load_settings('Package Control.sublime-settings')
    return PKG_NAME in set(pkgctrl_settings.get('installed_packages', []))


def plugin_loaded():
    wkhtmltopdf.plugin_loaded()

    try:
        from package_control import events
        if events.install(PKG_NAME) and not is_installed():
            sublime.run_command(
                'wkhtmltopdf_open_docs',
                {
                    'resource_path': '.sublime/messages/install.md'
                }
            )
        elif events.post_upgrade(PKG_NAME):
            sublime.run_command(
                'wkhtmltopdf_open_docs',
                {
                    'resource_path': '.sublime/messages/upgrade.md'
                }
            )
    except Exception as e:
        print('{}: Exception: {}'.format(PKG_NAME, e))


def plugin_unloaded():
    wkhtmltopdf.plugin_unloaded()
