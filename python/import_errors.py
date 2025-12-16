#   ImportError, ModuleNotFoundError

try:
    import math

except ModuleNotFoundError as e:
    print('>>> ModuleNotFoundError occurred:\n', e)
except ImportError as e:
    print('>>> ImportError occurred:\n', e)
except Exception as e:
    print(type(e), e)
else:
    print('>>> Module import success')
finally:
    print("-*- "*8)

try:
    from math import not_existing_element

except ModuleNotFoundError as e:
    print('>>> ModuleNotFoundError occurred:\n', e)
except ImportError as e:
    print('>>> ImportError occurred:\n', e)
except Exception as e:
    print(type(e), e)
else:
    print('>>> Module import success')
finally:
    print("-*- "*8)

try:
    import not_existing_element

except ModuleNotFoundError as e:
    print('>>> ModuleNotFoundError occurred:\n', e)
except ImportError as e:
    print('>>> ImportError occurred:\n', e)
except Exception as e:
    print(type(e), e)
else:
    print('>>> Module import success')
finally:
    print("-*- "*8)

try:
    from not_existing_module import not_existing_element

except ModuleNotFoundError as e:
    print('>>> ModuleNotFoundError occurred:\n', e)
except ImportError as e:
    print('>>> ImportError occurred:\n', e)
except Exception as e:
    print(type(e), e)
else:
    print('>>> Module import success')
finally:
    print("-*- "*8)
