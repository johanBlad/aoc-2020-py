
def read_list_int(task: int):
    with open(f"input/{task}.in", "r") as f:
        return [int(e.strip()) for e in f.readlines()] 