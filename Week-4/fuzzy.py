'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    'Triples input_a, subtracts input_b, then adds input_c'
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    'Returns True or False based on truthfulness of the question'
    if question == True:
        return True

def main():
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    newAnswer = choices(True)
    print(newAnswer)

if __name__ == '__main__':
    main()
