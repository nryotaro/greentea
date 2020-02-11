import os.path
from unittest import TestCase
from dataclasses import dataclass
import greentea.first_class_collection as fcc


class Double(fcc.FirstClassFileContextManagerProvider):

    def transform(self, item):
        return len(item)


class TestFirstClassFileContextManagerProvider(TestCase):

    def test_call(self):
        module_dir = os.path.dirname(__file__)
        testdata = os.path.join(module_dir,
                                'first_class_collection_call_test.txt')
        target = Double(testdata)

        with target() as stream:
            self.assertEqual([3, 5], list(stream))


@dataclass
class DoubleSequence(fcc.FirstClassSequence):
    items: list

    @property
    def sequence(self):
        return self.items


class TestFirstClassSequence(TestCase):

    def test_getitems_mono(self):
        self.assertEqual(DoubleSequence(
            ['a', 'b'])[0],
            'a')

    def test_getitems_multi(self):
        self.assertEqual(DoubleSequence(
            ['a', 'b'])[1:],
            DoubleSequence(['b']))

