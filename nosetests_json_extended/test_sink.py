from __future__ import absolute_import

import unittest

from nosetests_json_extended.sink import Sink
from nosetests_json_extended.sink import TestCaseDescription as TC
from nosetests_json_extended.sink import ErrorDescription


class SinkTest(unittest.TestCase):

    def test_module_headers(self):
        sink = Sink()
        sink.add('success', TC('module.A', 'test1'), None)
        sink.add('success', TC('module.A', 'test2'), None)
        sink.add('success', TC('module.B', 'test3'), None)
        sink.add('failed', TC('module.B', 'test4'), None)
        sink.add('success', TC('module.C', 'test5'), None)
        sink.add('error', TC('module.C', 'test6'), None)

        out = sink.generate()

        self.assertEqual(out['modules'][0]['name'], 'module.A')
        self.assertEqual(out['modules'][0]['nr_success'], 2)
        self.assertEqual(out['modules'][0]['nr_failed'], 0)
        self.assertEqual(out['modules'][0]['nr_error'], 0)

        self.assertEqual(out['modules'][1]['name'], 'module.B')
        self.assertEqual(out['modules'][1]['nr_success'], 1)
        self.assertEqual(out['modules'][1]['nr_failed'], 1)
        self.assertEqual(out['modules'][1]['nr_error'], 0)

        self.assertEqual(out['modules'][2]['name'], 'module.C')
        self.assertEqual(out['modules'][2]['nr_success'], 1)
        self.assertEqual(out['modules'][2]['nr_failed'], 0)
        self.assertEqual(out['modules'][2]['nr_error'], 1)

    def _single_testcase(self, *a):
        sink = Sink()
        sink.add(*a)
        return sink.generate()

    def test_testcase_success(self):
        out = self._single_testcase('success', TC('mod', 'test1'), None)
        tc1 = out['modules'][0]['testcases'][0]
        self.assertEqual(tc1['name'], 'test1')
        self.assertEqual(tc1['result'], 'success')

    def test_testcase_failed(self):
        er = ErrorDescription('error_desc', ['tb0', 'tb1'])
        out = self._single_testcase('error', TC('mod', 'test1'), er)
        tc1 = out['modules'][0]['testcases'][0]

        self.assertEqual(tc1['name'], 'test1')
        self.assertEqual(tc1['result'], 'error')
        self.assertEqual(tc1['error']['message'], 'error_desc')
        self.assertEqual(tc1['error']['traceback'], ['tb0', 'tb1'])
