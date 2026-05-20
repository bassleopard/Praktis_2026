import time


# Рекурсивний підхід
def climb_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)


# Ітеративний підхід
def climb_iterative(n: int) -> int:
    if n <= 1:
        return 1

    a, b = 1, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Значення n для тестування
test_values = [10, 20, 30, 35]

print(f"{'n':<5} {'Recursive':<15} {'Iterative':<15}")

for n in test_values:

    # Час рекурсивного алгоритму
    start = time.perf_counter()
    rec_result = climb_recursive(n)
    rec_time = time.perf_counter() - start

    # Час ітеративного алгоритму
    start = time.perf_counter()
    iter_result = climb_iterative(n)
    iter_time = time.perf_counter() - start

    print(f"{n:<5} {rec_time:<15.6f} {iter_time:<15.6f}")