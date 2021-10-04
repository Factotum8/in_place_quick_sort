from unittest import TestCase

from mypackages import Competitor, quick_sort


class Test(TestCase):
    def test_quick_sort(self):
        alla, gena, gosha, rita, timofey = (Competitor('alla', 4, 100), Competitor('gena', 6, 1000),
                                            Competitor('gosha', 2, 90), Competitor('rita', 2, 90),
                                            Competitor('timofey', 4, 80))
        b, c, a, d, e = (Competitor('b', 0, 0), Competitor('c', 0, 0),
                         Competitor('a', 0, 0), Competitor('d', 0, 0),
                         Competitor('e', 0, 0))
        # test_suite - ([name, input , expected], [...])
        test_suite = [
            ('integers', [5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
            ('competitors', [alla, gena, gosha, rita, timofey], [gena, timofey, alla, gosha, rita]),
            ('alphabetic', [b, c, a, d, e], [a, b, c, d, e])
        ]

        for name, input_, expected in test_suite:
            with self.subTest(name=name):
                _ = quick_sort(input_, len(input_))
                self.assertEqual(expected, quick_sort(input_, len(input_)))


if __name__ == '__main__':
    Test.run()
