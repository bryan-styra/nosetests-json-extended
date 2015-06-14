
from __future__ import absolute_import

import traceback
from nose.plugins import Plugin

from nosetests_json_extended.sink import (Sink, TestCaseDescription,
                                          ErrorDescription)


class JsonExtendedPlugin(Plugin):
    name = 'json-extended'
    score = 2000

    def options(self, parser, env):
        Plugin.options(self, parser, env)

    def configure(self, options, config):
        Plugin.configure(self, options, config)

        self.config = config
        if not self.enabled:
            return

        self._sink = Sink()

    def report(self, stream):
        self._sink.write()

    def addError(self, test, err, capt=None):
        self._sink.add('error', _split_id(test.id()), _format_error(err))

    def addFailure(self, test, err, capt=None, tb_info=None):
        self._sink.add('failed', _split_id(test.id()), _format_error(err))

    def addSuccess(self, test, capt=None):
        self._sink.add('success', _split_id(test.id()), None)


def _format_error(err):
    message_list = traceback.format_exception_only(err[0], err[1])
    message = '\n'.join(message_list).strip('\n')

    tb = list(wrap_traceback(traceback.extract_tb(err[2])))

    return ErrorDescription(message, tb)


def wrap_traceback(traceback_in):
    names = ('filename', 'linenr', 'function', 'line')
    for tb in traceback_in:
        yield dict(zip(names, tb))


def _split_id(test_id):
    parts = test_id.split('.')
    return TestCaseDescription('.'.join(parts[:-1]), parts[-1])
