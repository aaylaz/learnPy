

class loop_tracker:

    """Loops through an iterable and keeps count"""

    def __init__(self, aniterator):
        self.aniterator = iter(aniterator)
        self.index = 0
        self.empty = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.aniterator)
        self.index += 1
        return item

    def __len__(self):
        return self.index

    def is_empty(self):
        if self.empty == 0:
            return False
        else:
            return True







