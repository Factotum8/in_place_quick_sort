from typing import List, Any


def quick_sort(array: List[Any], arr_length: int) -> List[Any]:

    def __quick_sort(start: int, end: int) -> None:
        if start >= end:
            return

        pivot = array[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        __quick_sort(start, right)
        __quick_sort(left, end)

    __quick_sort(0, arr_length - 1)
    return array
