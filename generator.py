def flat_generator(nested_list):

    for inner_list in nested_list:
        for item in inner_list:
            yield item