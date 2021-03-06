#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import os
import subprocess
from threading import Thread


PKG_NAME = __package__.split('.')[0]
PKG_PREF = None
DEFAULT_OPTIONS = '--javascript-delay 10000 --outline-depth 8 --encoding utf-8'


def status_msg(msg):

    sublime.status_message('{}: {}'.format(PKG_NAME, msg))


def load_settings(reload=False):

    try:
        global PKG_PREF
        PKG_PREF = sublime.load_settings('{}.sublime-settings'.format(PKG_NAME))
        PKG_PREF.clear_on_change('reload')
        PKG_PREF.add_on_change('reload', lambda: load_settings(reload=True))
    except Exception as e:
        print('{}: Exception: {}'.format(PKG_NAME, e))

    if reload:
        status_msg('Reloaded settings on change.')


def unload_settings():

    global PKG_PREF
    PKG_PREF.clear_on_change('reload')


class Wkhtmltopdf(sublime_plugin.TextCommand):

    def run(self, edit):
        path_html = self.view.file_name()
        if not path_html:
            status_msg('Missing file path.')
            return
        if not path_html.lower().endswith('.html'):
            status_msg('File does not have an HTML extension.')
            return
        path_pdf = os.path.splitext(path_html)[0] + '.pdf'
        thread = Thread(target=self.html_to_pdf, args=(path_html, path_pdf))
        thread.start()

    def html_to_pdf(self, path_html, path_pdf):
        cmd_options = PKG_PREF.get('wkhtmltopdf.cmd_options',
                                   DEFAULT_OPTIONS)
        subprocess.call('wkhtmltopdf {} {} {}'.format(cmd_options, path_html, path_pdf), shell=True)

    def is_visible(self):
        return self.view.settings().get('syntax').startswith('Packages/HTML/')
