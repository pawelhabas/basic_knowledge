#   KeyError

data: dict[str, str] = {'name': 'Bob',
                        'job': 'Programmer',
                        'salary': 120}

try:
    print(data['name'])
    print(data.get('birth_date', 'Unknown birth date'))
    print(data['age'])

except KeyError as e:
    print('>>> KeyError occurred:\n', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- " * 8)
