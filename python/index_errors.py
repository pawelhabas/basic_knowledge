#   IndexError

names: list[str] = ['Bob', 'James']
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)

try:
    print(names[1])
    print(names[2])

except IndexError as e:
    print('>>> IndexError occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)

try:
    print(numbers[1])
    print(numbers[9])

except IndexError as e:
    print('>>> IndexError occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)
