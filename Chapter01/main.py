from fraction import Fraction

def run():
    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)
    f3 = f1 + f2  # 3/4
    f4 = f1 + f1  # 1/2

    print(f"f1={f1}")
    print(f"f2={f2}")
    print(f"f3={f3}")
    print(f"f4={f4}")

    print(f"{f1} == {f4}: {f1 == f4}")
    print(f"{f2} == {f4}: {f2 == f4}")
    print(f"{Fraction(1, 2)} == {Fraction(2, 4)}:", end=" ")
    print(f"{Fraction(1, 2) == Fraction(2, 4)}")

    print(f"{f1} != {f4}: {f1 != f4}")
    print(f"{f2} != {f4}: {f2 != f4}")

    print(f"{f2} - {f1} = {f2 - f1}")
    print(f"{f1} - {f2} = {f1 - f2}")

    print(f"{f1} * {f2} = {f1 * f2}")

    print(f"{f1} / {f2} = {f1 / f2}")

    print(f"{f1} < {f2} = {f1 < f2}")
    print(f"{f2} < {f1} = {f2 < f1}")
    print(f"{f1} < {f1} = {f1 < f1}")

    print(f"{f1} <= {f2} = {f1 <= f2}")
    print(f"{f2} <= {f1} = {f2 <= f1}")
    print(f"{f1} <= {f1} = {f1 <= f1}")

    print(f"{f1} >= {f2} = {f1 >= f2}")
    print(f"{f2} >= {f1} = {f2 >= f1}")
    print(f"{f1} >= {f1} = {f1 >= f1}")


if __name__ == "__main__":
    run()

