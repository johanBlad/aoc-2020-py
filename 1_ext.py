from typing import Iterable
from utils.reader import read_list_int
from utils.generate import (
    generate_data_from_stats,
    generate_more_data_from_data,
    concat_shuffle_clean,
    get_stats,
    get_target_partials,
)
from utils.benchmark import run_func

from utils.bst import Tree


def naive_sorted(data: Iterable[int], targets: Iterable[int]) -> dict:
    res = {k: [] for k in targets}

    sorted_data = sorted(data)
    # for t in targets:
    for i, a in enumerate(sorted_data):
        for b in sorted_data[i + 1 :]:
            if a + b in targets:
                res[a + b].append((a, b))
    return res


def binary_search(data: Iterable[int], targets: Iterable[int]) -> dict:
    res = {k: [] for k in targets}
    data = sorted(data)

    def _binary_search(l: Iterable[int], target: int):

        if len(l) == 0:
            return None
        i = len(l) // 2
        mid = l[i]
        if mid == target:
            return target
        elif target < mid:
            _binary_search(l[:i], target)
        else:
            _binary_search(l[i + 1 :], target)

    for e in data:
        for t in targets:
            diff = t - e
            if _binary_search(data, diff):
                res[t].append((e, diff))
    return res


def binary_tree(data: Iterable[int], targets: Iterable[int]) -> dict:
    res = {k: [] for k in targets}

    sorted_data = sorted(data)
    tree = Tree()
    tree.populate_tree(sorted_data)
    h = tree.height()
    print("height", h)

    for e in sorted_data:
        for t in targets:
            diff = t - e
            if tree.find(diff):
                res[t].append((e, diff))
    return res


def main():
    data = read_list_int(1)
    num_targets = 1
    size_data = 7_000_0
    spread = 1.5
    m = 200_00
    std = 2000

    # data = generate_more_data_from_data(data, size_data, spread=spread)
    data = generate_data_from_stats(m, std, size_data, spread=spread)

    targets = generate_more_data_from_data(
        data, num_targets, spread=spread + 0.3, keep_original=False
    )
    targets = [2020]
    partials = [get_target_partials(t) for t in targets]
    data = concat_shuffle_clean(data, *partials)
    print(get_stats(data))
    run_func(binary_tree, data, targets)
    run_func(naive_sorted, data, targets)
    run_func(binary_search, data, targets)

    # for k, v in res.items():
    #     print(k, v)
    # print(len(res.items()))


if __name__ == "__main__":
    main()
