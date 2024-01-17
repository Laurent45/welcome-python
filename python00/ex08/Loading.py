"""
    The purpose of this exercise is to copy the tqdm function with the yield operator

"""

BAR_SIZE = 180
FILL_CHAR = "="
SPACE_CHAR = " "


def ft_tqdm(lst: range) -> None:
    # your code here
    total = len(lst)

    for i in range(0, total):
        percentage = i * 100 // total
        fill_rate = BAR_SIZE * percentage // 100
        print(f"{percentage}%|[{FILL_CHAR * fill_rate}{SPACE_CHAR * (BAR_SIZE - fill_rate)}]| {i}/{total}", end="\r")
        yield
    print(f"100%|[{FILL_CHAR * (BAR_SIZE - 1)}>]| {total}/{total}", end="")
