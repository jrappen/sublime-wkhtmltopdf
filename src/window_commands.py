#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


CSS = '''
html {
    margin: 16px;
}
body {
    font-family: "Open Sans", "Helvetica Neue", "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6;
}
h1 {
    font-size: 2.0rem;
    margin: 0.7rem 0 0 0;
}
h2 {
    font-size: 1.4rem;
    margin: 1rem 0 0.4rem 0;
}
h3 {
    font-size: 1.2rem;
    margin: 1rem 0 0.1rem 0;
}
code {
    font-size: 0.9rem;
    border-radius: 2px;
    padding: 0 4px;
}
ul {
    padding-left: 1.8rem;
}
li {
    margin: 2px;
}
li ul {
    margin: 2px 0 4px;
}
'''
PKG_NAME = __package__.split('.')[0]


# TODO: add type hints
class WkhtmltopdfOpenDocs(sublime_plugin.WindowCommand):

    def run(self, resource_path='docs/en/README.md'):
        try:
            w = self.window
            v = w.active_view()
            import mdpopups
            preview_sheet = mdpopups.new_html_sheet(
                window=w,
                # TODO: update for Py3.8 with f-strings
                name='{}/{}'.format(PKG_NAME, resource_path),
                contents=sublime.load_resource('Packages/{}/{}'.format(PKG_NAME, resource_path)),
                md=True,
                css='{}'.format(CSS)
            )
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))
            # TODO: print(f'{PKG_NAME}: Exception: {e}')

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            import mdpopups
            return True
        except Exception as e:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None
