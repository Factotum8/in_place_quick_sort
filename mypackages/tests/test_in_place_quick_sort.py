from unittest import TestCase

from mypackages import Competitor, quick_sort


class Test(TestCase):
    def test_quick_sort(self):
        alla, gena, gosha, rita, timofey = (Competitor('alla', 4, 100), Competitor('gena', 6, 1000),
                                            Competitor('gosha', 2, 90), Competitor('rita', 2, 90),
                                            Competitor('timofey', 4, 80))
        # test_suite - ([name, input , expected], [...])
        test_suite = [
            ('integers', [5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
            ('competitors', [alla, gena, gosha, rita, timofey], [rita, gosha, alla, timofey, gena])
        ]

        for name, input_, expected in test_suite:
            with self.subTest(name=name):
                _ = quick_sort(input_, len(input_))
                self.assertEqual(expected, quick_sort(input_, len(input_)))


if __name__ == '__main__':
    Test.run()
