class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.current_index = 0
        self.current_iterator = iter(self.nested_list[0])
        return self

    def __next__(self):
        try:
            return next(self.current_iterator)
        except StopIteration:
            self.current_index += 1
            if self.current_index == len(self.nested_list):
                raise StopIteration
            else:
                self.current_iterator = iter(self.nested_list[self.current_index])
                return next(self.current_iterator)