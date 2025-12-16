#   NotImplementedError

def some_function_or_method() -> None:
    raise NotImplementedError


try:
    some_function_or_method()

except NotImplementedError as e:
    print('>>> NotImplementedError occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)
