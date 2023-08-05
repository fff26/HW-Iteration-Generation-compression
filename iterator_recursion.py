class DeepFlatIterator:
    
    def __init__(self, nested_list):
        self.nested_list = nested_list
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.nested_list:
            current = self.nested_list[0]
            self.nested_list = self.nested_list[1:]
            if isinstance(current, list):
                self.nested_list = current + self.nested_list
                continue
            else:
                return current
        raise StopIteration