import re


class Split:
    def __init__(self, split, is_static):
        self.original = split
        self.positive = split[0] == "+"
        split = split[1:]
        self.is_static = is_static

        if self.is_static:
            split = int(split)
            self.minimum: int = split
            self.maximum: int = split
            self.mean: float = split
            self.amount: int = 1
        else:
            amount, size = re.split("d", split)
            amount = int(amount)
            size = int(size)
            self.mean: float = (size + 1) / 2 * amount
            self.minimum: int = amount
            self.maximum: int = size * amount
            self.amount: int = amount


def dice_calculator(dice_notation: str):
    dice_notation = dice_notation.replace(" ", "")
    if dice_notation[0] not in ["+", "-"]:
        dice_notation = f"+{dice_notation}"

    splits_raw = re.findall("[+-][^+-]+", dice_notation)

    splits = []
    for split in splits_raw:
        if split[1:].isnumeric():
            splits.append(Split(split, True))
        else:
            splits.append(Split(split, False))

    return split_merger(splits)


def split_merger(splits: list[Split]):
    global_min = 0
    global_max = 0

    global_mean = 0

    for split in splits:
        if split.positive:
            global_min += split.minimum
            global_max += split.maximum
            global_mean += split.mean
        else:
            global_min -= split.maximum
            global_max -= split.minimum
            global_mean -= split.mean

    return global_min, global_max, global_mean


pass
