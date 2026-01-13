import functools
import time


def my_timer(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result

    return wrapper


def line_separator():
    print('>>><<<' * 8)


if __name__ == '__main__':
    line_separator()
