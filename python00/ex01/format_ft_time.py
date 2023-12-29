"""
    The purpose of this exercice is to get the current time and parse it.
    The output will look like this:

    $>python format_ft_time.py | cat -e
    Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
    Oct 21 2022$
    $>

    About standard format specifier: https://docs.python.org/3/library/string.html#formatspec 
"""

from time import time
from time import strftime
from time import localtime

time = time()

print(f"Seconds since January 1, 1970: {time:,.4f} or {time:#.3} in scientific notation")
print(strftime("%b %d %Y", localtime(time)))
