#   NameError

try:
    print(non_existing_variable)

except NameError as e:
    print('>>> NameError occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)
