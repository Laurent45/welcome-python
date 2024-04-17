def count_in_list(list: list[str], target: str) -> int:
    return len([s for s in list if s == target])
