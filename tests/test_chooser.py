from unittest import TestCase
from master_chooser.main import choose_master
from copy import copy


class TestChooser(TestCase):
    def test_choose_master(self):
        devs = ['Miko', 'Noam', 'Trakman']
        remaining = copy(devs)
        dev, remaining = choose_master(remaining)
        self.assertIsNotNone(dev)
        self.assertEqual(len(remaining), 2)
