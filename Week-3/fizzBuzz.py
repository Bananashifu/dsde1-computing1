for i in range(100):
    if i % 3 == 0:
        if i % 5 == 0:
            print('fizz-buzz')
        else:
            print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(str(i))