from typing import Iterable
from utils.bst import Tree
from utils.reader import read_list_int
from utils.benchmark import run_func
from utils.generate import generate_data_from_stats, get_stats, generate_more_data_from_data


def naive(data: Iterable[int], target: int) -> int:
    for a in data:
        for b in data:
            if a + b == target:
                return a * b


def naive_sorted(data: Iterable[int], target: int) -> int:
    sorted_data = sorted(data)
    for i, a in enumerate(sorted_data):
        for b in sorted_data[i + 1 :]:
            if a + b == target:
                return a * b


def naive_sorted_reverse(data: Iterable[int], target: int) -> int:
    sorted_data = sorted(data)
    for i, a in enumerate(sorted_data):
        remaining_data = sorted_data[i + 1 :]
        for k in range(len(remaining_data)):
            if a + remaining_data[-k] == target:
                return a * remaining_data[-k]


def binary_tree(data: Iterable[int], target: int) -> int:
    sorted_data = sorted(data)
    tree = Tree()
    tree.populate_tree(sorted_data)
    for e in sorted_data:
        diff = target - e
        if tree.find(diff):
            return e * diff


def hashmap(data: Iterable[int], target: int) -> int:
    mapper = {}
    for e in data:
        mapper[target - e] = True
    for k in data:
        if mapper.get(k, None) is not None:
            return k * target - k


def two_pointer(data: Iterable[int], target: int) -> int:
    data = sorted(data)
    i = 0
    j = len(data) - 1

    while i != j:
        if data[i] + data[j] == target:
            return data[i] * data[j]
        elif data[i] + data[j] < target:
            i += 1
        elif data[i] + data[j] > target:
            j -= 1
        else:
            return None


if __name__ == "__main__":
    data = read_list_int(1)
    data = generate_more_data_from_data(data, len(data) * 200)
    data = generate_data_from_stats(20_000, 2000, 10_000)
    stats = get_stats(data)
    print(stats)
    run_func(naive_sorted, data, 2020)
    run_func(naive_sorted_reverse, data, 2020)
    run_func(binary_tree, data, 2020)
    run_func(hashmap, data, 2020)
    run_func(two_pointer, data, 2020)
    # run_func(naive, data, 2020)
