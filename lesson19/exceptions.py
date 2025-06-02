class CustomError(Exception):
    pass

x = 2
try:
    raise CustomError('am a custom exception')

    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError('Only string are allowed')
except NameError:
    print('an error occured')
except ZeroDivisionError:
    print('do not divide by zero')
except Exception as error:
    print(error)
else:
    print('no error found')
finally:
    print('it will always execute')