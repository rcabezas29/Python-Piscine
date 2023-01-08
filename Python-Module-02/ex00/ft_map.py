def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    def iteration():
        for it in iterable:
            yield function_to_apply(it)
        
    if not hasattr(iterable, '__iter__') or not callable(function_to_apply):
        return None
    
    return iteration()
    
def addition(n):
    return n + n

numbers = [1, 2, 3, 4]
result = ft_map(addition, numbers)
print(list(result))