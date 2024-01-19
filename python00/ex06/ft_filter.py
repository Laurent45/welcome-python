class filter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    def __init__(self, function, iterable):
        if function is None:
            self._generator = (e for e in iterable if bool(e) is True)
        else:
            self._generator = (e for e in iterable if function(e))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)
