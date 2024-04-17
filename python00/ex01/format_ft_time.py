"""
    The purpose of this exercise is to get the current time and parse it.
    The output will look like this:

    $>python format_ft_time.py | cat -e
    Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
    Oct 21 2022$
    $>

    About standard format specifier: https://docs.python.org/3/library/string.html#formatspec 
"""

from datetime import datetime

date_time = datetime.now()

print(
    f"Seconds since January 1, 1970: {date_time.timestamp():,.4f} or {date_time.timestamp():#.3} in scientific notation"
)
print(f"{date_time:%b %d %Y}")
