#!/usr/bin/env python
# coding: utf-8


from .thread_progress import *
from .window_commands import *
from .wkhtmltopdf import *


def plugin_loaded():
    wkhtmltopdf.plugin_loaded()
    window_commands.plugin_loaded()


def plugin_unloaded():
    wkhtmltopdf.plugin_unloaded()
    # window_commands.plugin_unloaded()
