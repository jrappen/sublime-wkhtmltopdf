#!/usr/bin/env python
# coding: utf-8


from .src import *


def plugin_loaded():

    from .src.wkhtmltopdf import load_settings
    load_settings()


def plugin_unloaded():

    from .src.wkhtmltopdf import unload_settings
    unload_settings()
