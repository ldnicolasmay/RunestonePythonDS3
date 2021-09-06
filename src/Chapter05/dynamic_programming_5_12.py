from typing import Dict, List


def make_change_1(amount: int, denoms_list: List[int]) -> int:
    if amount in denoms_list:
        return 1
    else:
        # min(
        #     1 + foo(amount - 1, denominations),
        #     1 + foo(amount - 5, denominations),
        #     1 + foo(amount - 10, denominations),
        #     1 + foo(amount - 25, denominations)
        # )
        counts = [
            1 + make_change_1(amount - c, denoms_list)
            for c in denoms_list if c <= amount
        ]
        return min(counts)


# print(foo(63, [1, 5, 10, 25]))


def memoized_make_change(
    amount: int,
    denoms_list: List[int],
    lookup_table: Dict[int, int]
) -> int:
    # print(lookup_table)
    if amount in denoms_list:
        lookup_table[amount] = 1
        return lookup_table[amount]
    else:
        if amount in lookup_table:
            return lookup_table[amount]
        else:
            counts = [
                1 + memoized_make_change(amount - c, denoms_list, lookup_table)
                for c in denoms_list if c <= amount
            ]
            lookup_table[amount] = min(counts)
            return min(counts)


# print(memoized_make_change(63, [1, 5, 10, 25], {}))


def make_change_lookup_table(
    amount: int,
    denoms_list: List[int],
    lookup_table: Dict[int, int],
) -> Dict[int, int]:
    for a in range(1, amount + 1):
        if a in denoms_list:
            lookup_table[a] = 1
        else:
            counts = [
                1 + lookup_table[a - c] for c in denoms_list if c <= a
            ]
            min_counts = min(counts)
            lookup_table[a] = min_counts

    return lookup_table


def make_change_3(
    amount: int,
    denoms_list: List[int],
    lookup_table: Dict[int, int]
) -> int:
    lookup_table = make_change_lookup_table(amount, denoms_list, lookup_table)

    return lookup_table[amount]


# print(make_change_3(101, [1, 5, 10, 25], {}))


def make_change_4(
    amount: int,
    denoms_list: List[int],
    lookup_table: Dict[int, int],
) -> List[int]:
    lookup_table = make_change_lookup_table(amount, denoms_list, lookup_table)
    current_amount = amount
    coins_list = []

    while current_amount > 0:
        print(f"current_amount={current_amount}")
        if lookup_table[current_amount] == 1:
            coins_list.append(current_amount)
            current_amount = current_amount - current_amount
        else:
            current_denom_counts = dict(
                (denom, lookup_table[current_amount - denom]) for denom in denoms_list
                if denom <= current_amount
            )
            print(f"current_denom_counts={current_denom_counts}")

            min_denom_count = dict(
                (denom, count) for denom, count in current_denom_counts.items()
                if denom == min(current_denom_counts, key=current_denom_counts.get)
            )
            print(f"min_denom_count={min_denom_count}")

            min_denom = list(min_denom_count.keys())[0]
            coins_list.append(min_denom)
            current_amount = current_amount - min_denom

    return coins_list


print(f"lookup_table={make_change_4(63, [1, 5, 10, 25], {})}")
