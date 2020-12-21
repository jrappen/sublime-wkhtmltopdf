#!/usr/bin/env python
# coding: utf-8


import sublime


PKG_NAME = __package__.split('.')[0]


class ThreadProgress():

    def __init__(self, thread, message, success_message):
        self.thread = thread
        self.message = message
        self.success_message = success_message
        self.addend = 1
        self.size = 8
        self.last_view = None
        self.window = None
        sublime.set_timeout_async(lambda: self.run(0), 100)

    def run(self, i):
        if self.window is None:
            self.window = sublime.active_window()
        active_view = self.window.active_view()

        if self.last_view is not None and active_view != self.last_view:
            self.last_view.erase_status(PKG_NAME)
            self.last_view = None

        if not self.thread.is_alive():
            def cleanup():
                active_view.erase_status(PKG_NAME)
            if hasattr(self.thread, 'result') and not self.thread.result:
                cleanup()
                return
            active_view.set_status(PKG_NAME, self.success_message)
            sublime.set_timeout_async(cleanup, 1000)
            return

        before = i % self.size
        after = (self.size - 1) - before

        active_view.set_status(PKG_NAME, '{} [{}={}]'.format(self.message, ' ' * before, ' ' * after))
        if self.last_view is None:
            self.last_view = active_view

        if not after:
            self.addend = -1
        if not before:
            self.addend = 1
        i += self.addend

        sublime.set_timeout_async(lambda: self.run(i), 100)
