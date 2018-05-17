from enum import Enum
from timeit import repeat


def main():
    d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    if m is None:
        print("That's not a move!")
        return

    print(m)

    # ******** less pythonic ********
    if m == Moves.North or m == Moves.South or m == Moves.West or \
            m == Moves.East:
        print("That's a direct move.")
    else:
        print("That's a diagonal move.")

    # ******** more pythonic ********
    if m in {Moves.North, Moves.South, Moves.West, Moves.East}:
        print("That's a direct move.")
    else:
        print("That's a diagonal move.")

    time_for_loop(m)


class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()
        if text == 'w':
            return Moves.West
        if text == 'e':
            return Moves.East
        if text == 's':
            return Moves.South
        if text == 'n':
            return Moves.North

        if text == 'nw':
            return Moves.NorthWest
        if text == 'sw':
            return Moves.SouthWest
        if text == 'ne':
            return Moves.NorthEast
        if text == 'se':
            return Moves.SouthEast

        return None


def time_for_loop(move: Moves):
    """
    Display the cpu time required to execute various types of for loops.
    :param move: integer describing move
    """
    g = {'m': move}
    statements = {
        # 'test_name': (timer_statement, timer_globals),
        'or': ('m == 0 or m == 1 or m == 2 or m == 3', g),
        'set': ('m in range(3)', g),
        'global': ('m in direction', {**{'direction': range(3)}, **g}),
    }

    times = {}
    for name, args in statements.items():
        kwargs = {k: v for k, v in zip(('stmt', 'globals'), args)}
        times[name] = min(repeat(repeat=3, **kwargs))

    sorted_times = sorted(times.items(), key=lambda x: x[1])
    sorted_times = [x for row in sorted_times for x in row]
    fmt = '{:<%d} :  ' % max(map(len, times))
    print(((fmt + '{:.3f}\n') * 3).format(*sorted_times))


if __name__ == '__main__':
    main()
