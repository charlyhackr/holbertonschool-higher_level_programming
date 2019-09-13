#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    todas_dir = dir(hidden_4)
    avoid = "__"
    for num in range(0, len(todas_dir)):
        if avoid not in todas_dir[num]:
            print(todas_dir[num])
