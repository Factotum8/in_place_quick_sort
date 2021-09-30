import sys
from typing import List

from mypackages import Competitor, quick_sort


if __name__ == '__main__':
    number: int = int(input())
    arr: List[Competitor] = [
        Competitor(*sys.stdin.readline().split()) for _ in range(number)
    ]
    result: List[Competitor] = quick_sort(arr, number)
    print(*result, sep='\n')
