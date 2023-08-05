def deep_flat_generator(nested_list):
    
    for item in nested_list:
        if isinstance(item, list):
            yield from deep_flat_generator(item)
        else:
            yield item
            
nested_list = [
    ['a', 'b', 'c'],
    ['d', ['e', 'f']], 
    [[['g']], 'h'],
    'i'
]

for item in deep_flat_generator(nested_list):
    print(item)