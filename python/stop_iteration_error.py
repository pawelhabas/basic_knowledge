#   StopIteration

from typing import Generator


def number_generator() -> Generator[int, None, None]:
    for i in range(2):
        yield i


try:
    my_gen: Generator[int, None, None] = number_generator()
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
except StopIteration as e:
    print('>>> StopIteration occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)
