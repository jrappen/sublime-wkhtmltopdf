#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import os
import subprocess
from threading import Thread

from .thread_progress import ThreadProgress


PKG_NAME = __package__.split('.')[0]
PKG_PREF = None
DEFAULT_OPTIONS = '--javascript-delay 10000 --outline-depth 8 --encoding utf-8'


# TODO: type hints
def status_msg(msg):

    sublime.status_message('{}: {}'.format(PKG_NAME, msg))
    # TODO: sublime.status_message(f'{PKG_NAME}: {msg}')


# TODO: type hints
def load_settings(reload=False):

    try:
        global PKG_PREF
        PKG_PREF = sublime.load_settings('{}.sublime-settings'.format(PKG_NAME))
        # TODO: PKG_PREF = sublime.load_settings(f'{PKG_NAME}.sublime-settings')
        PKG_PREF.clear_on_change('reload')
        PKG_PREF.add_on_change('reload', lambda: load_settings(reload=True))
    except Exception as e:
        print('{}: Exception: {}'.format(PKG_NAME, e))
        # TODO: print(f'{PKG_NAME}: Exception: {e}')

    if reload:
        status_msg('Reloaded settings on change.')


def plugin_loaded():

    load_settings()


def plugin_unloaded():

    global PKG_PREF
    PKG_PREF.clear_on_change('reload')


# TODO: type hints
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
        ThreadProgress(thread,
                       '{}: Converting HTML to PDF ...'.format(PKG_NAME),
                       # TODO: f'{PKG_NAME}: Converting HTML to PDF ...',
                       '{}: Successfully created "{}".'.format(PKG_NAME, os.path.split(path_pdf)[1]))

    # TODO: type hints
    def html_to_pdf(self, path_html, path_pdf):
        cmd_options = PKG_PREF.get('wkhtmltopdf.cmd_options',
                                   DEFAULT_OPTIONS)
        subprocess.call('wkhtmltopdf {} {} {}'.format(cmd_options, path_html, path_pdf), shell=True)
        # TODO: subprocess.call(f'wkhtmltopdf {cmd_options} {path_html} {path_pdf}', shell=True)

    def is_visible(self):
        return self.view.settings().get('syntax').startswith('Packages/HTML/')
