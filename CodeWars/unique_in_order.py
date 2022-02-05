def unique_in_order(iterable):
    unique = []
    prev = None
    for item in iterable:
         if prev != item:
            unique.append(item)
            prev = item
    return unique
