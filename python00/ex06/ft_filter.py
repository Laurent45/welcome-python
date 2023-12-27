
class filter:
    def __init__(self, generator):
        self._generator = generator

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)


def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is None:
        return filter(e for e in iterable if bool(e) is True)
    return filter(e for e in iterable if function(e))
