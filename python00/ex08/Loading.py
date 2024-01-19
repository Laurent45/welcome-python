"""
    The purpose of this exercise is to copy the tqdm function with the yield operator

"""


def ft_tqdm(lst: range) -> None:
    # your code here
    bar_size = 180
    fill_char = "="
    space_char = " "
    total = len(lst)

    for i in range(0, total):
        percentage = i * 100 // total
        fill_rate = bar_size * percentage // 100
        print(f"{percentage}%|[{fill_char * fill_rate}{space_char * (bar_size - fill_rate)}]| {i}/{total}", end="\r")
        yield
    print(f"100%|[{fill_char * (bar_size - 1)}>]| {total}/{total}", end="")
