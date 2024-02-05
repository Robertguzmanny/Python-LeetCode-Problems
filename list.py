# test_SLList.py
# unittest example

from linkedlist import *
import sys
import unittest

sys.path.insert(0, '..')


class SLListTest(unittest.TestCase):

    def testEmpty(self):

        l = SLList()
        self.assertEqual(l.head, None)
        self.assertEqual(len(l), 0)

    def testOne(self):

        l = SLList()
        l.insert_at_head(5)
        self.assertEqual(l.get_item(l.head), 5)
        self.assertEqual(l.head.link, None)
        self.assertEqual(len(l), 1)

    def testThree(self):

        l = SLList()
        for x in [2, 4, 6]:
            l.insert_at_head(x)
        self.assertEqual(l.get_item(l.head), 6)
        self.assertEqual(l.get_item(l.head.link), 4)
        self.assertEqual(l.get_item(l.head.link.link), 2)
        self.assertEqual(l.head.link.link.link, None)
        self.assertEqual(len(l), 3)

    def testSearch(self):

        l = SLList()
        for x in [2, 4, 6, 8, 2]:
            l.insert_at_head(x)
        self.assertEqual(l.search(2), l.head)
        self.assertEqual(l.search(4), l.head.link.link.link)
        self.assertEqual(len(l), 5)

    def testInsertAfter(self):

        l = SLList()
        for x in [2, 4, 6]:
            l.insert_at_head(x)
        n4 = l.search(4)
        l.insert_after(n4, 5)
        self.assertEqual(l.get_item(l.head.link.link), 5)
        n5 = l.search(5)
        self.assertEqual(l.get_item(n5.link), 2)
        self.assertEqual(len(l), 4)

    def testDeleteAfter(self):

        l = SLList()
        for x in [2, 4, 6, 8]:
            l.insert_at_head(x)
        n6 = l.search(6)
        l.delete_after(n6)
        self.assertEqual(l.get_item(l.head.link.link), 2)
        self.assertEqual(len(l), 3)


def main(argv):
    unittest.main()


if __name__ == '__main__':
    main(sys.argv)
