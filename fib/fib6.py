from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range (1, n):
        last, next = next, last + next
        yield next

if __name__ == "__main__":
    for i in fib6(6):
        print(i)
