from typing import Iterable
from random import randint, shuffle, sample
from itertools import chain


def get_stats(data: Iterable[int]) -> dict:
    n = len(data)
    mean = sum(data) / n
    variance = sum([((e - mean) ** 2) for e in data]) / n
    std = variance ** 0.5
    return {
        "n": n,
        "mean": mean,
        "variance": variance,
        "std": std,
    }


def concat_shuffle_clean(*args):
    chained = list(set(chain(*args)))
    shuffle(chained)
    return chained


def get_target_partials(target: int):
    p1 = randint(1, target)
    p2 = target - p1
    return [p1, p2]


def generate_data_from_stats(mean: int, std: int, desired_size: int, spread: int = 1.2):
    return [
        int(mean + randint(int(-std * spread * 10000), int(std* spread * 10000)) / 10000)
        for i in range(desired_size)
    ]


def generate_more_data_from_data(
    data: Iterable[int], desired_size: int, spread: int = 1.2, keep_original=True
):
    stats = get_stats(data)

    std = stats.get("std")
    mean = stats.get("mean")
    gen_data = generate_data_from_stats(mean, std, desired_size, spread=spread)
    if keep_original is True:
        return concat_shuffle_clean(data, gen_data)
    else:
        return list(set(gen_data))
