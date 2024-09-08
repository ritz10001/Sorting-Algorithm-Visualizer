from draw_utils import DrawUtils
import random

class Sort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(draw_instance):
        arr = draw_instance.arr
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    DrawUtils.draw_list(draw_instance, {j: (0,255,0), j+1 : (255,0,0)}, True)
                    yield True
        return arr

    @staticmethod
    def insertion_sort(draw_instance):
        arr = draw_instance.arr
        for i in range(1,len(arr)):
            val = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > val:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1
            arr[j+1] = val
            DrawUtils.draw_list(draw_instance, {j: (0,255,0), j+1 : (255,0,0)}, True)
            yield True
        return arr
    
    @staticmethod
    def selection_sort(draw_instance):
        arr = draw_instance.arr
        for i in range(len(arr)):
            min_idx = i
            for j in range(i, len(arr)):
                if j == i:
                    continue
                else:
                    if arr[j] < arr[min_idx]:
                        min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            DrawUtils.draw_list(draw_instance, {i: (0,255,0), min_idx : (255,0,0)}, True)
            yield True
                        
        return arr

    @staticmethod
    def bogo_sort(draw_instance):
        arr = draw_instance.arr
        def is_sorted(arr):
            length = len(arr) 
            for i in range(0, length-1): 
                if (arr[i] > arr[i+1]): 
                    return False
            return True
        
        def shuffle(arr):
            length = len(arr)
            for i in range(length):
                r = random.randint(0, length-1)
                arr[i], arr[r] = arr[r], arr[i]
                DrawUtils.draw_list(draw_instance, {i: (0,255,0), r : (255,0,0)}, True)
                yield True
        
        while not is_sorted(arr):
            yield from shuffle(arr)

        
        
        