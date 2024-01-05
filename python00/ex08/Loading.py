
def ft_tqdm(lst: range) -> None:
    # your code here
    total = len(lst)
    count = 0
    pourcentage = 0
    spaces = " " * 30

    print(f"{pourcentage}%|[{spaces}]| {count}/{total}", end="\r")
    for _ in lst:
        yield
        count += 1
        pourcentage = count * 100 // total
        print(f"{pourcentage}%|[{spaces}]| {count}/{total}", end="\r")
    return
