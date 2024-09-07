import random

class ListUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_array(nums, min_val, max_val):
        array = []
        
        for _ in range(nums - 1):
            value = random.randint(min_val, max_val)
            array.append(value)

        return array