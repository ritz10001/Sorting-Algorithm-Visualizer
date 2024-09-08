from draw_utils import DrawUtils

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
            j = i -1
            while j>=0 and arr[j] > val:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1
            arr[j+1] = val
            DrawUtils.draw_list(draw_instance, {j: (0,255,0), j+1 : (255,0,0)}, True)
            yield True
        return arr

                    