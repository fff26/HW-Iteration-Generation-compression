from iterator import FlatIterator
from generator import flat_generator
from iterator_recursion import DeepFlatIterator
from generator_recursion import deep_flat_generator


if __name__ == "__main__":
    # 1.1
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False], 
        [1, 2, None],
    ]
    iterator = FlatIterator(nested_list)
    for item in iterator:
        print(item)

    # 1.2
    flat_list = [item for item in iterator]
    print(flat_list)

    # 2
    for item in flat_generator(nested_list):
        print(item)

    # 3.1
    nested_list_2 = [
    ['a', 'b', 'c'], 
    ['d', ['e', 'f']],
    [[['g', ['r', 33]]], 'h'],
    'i'
    ]

    # 3.2
    for item in DeepFlatIterator(nested_list_2):
        print(item)

    # 4
    for item in deep_flat_generator(nested_list_2):
        print(item)