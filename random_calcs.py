# import modules
import random

# class
class Program:
    def run_program(self, random_number = [1, 20], quant_calcs = 1):
        # title
        print('=' * 30)
        print(f'{"CALCULOS":^30}')
        print('=' * 30)
        c = 0
        while True:
            # verify quantity times the user want to run the program
            if quant_calcs == c:
                break
            # random calcs
            basics_calcs = ['+', '-', '*', '/']
            calc = random.choice(basics_calcs)

            # verify what calc will be do
            if calc == '/':
                while True:
                    number1 = random.randint(random_number[0], random_number[1])
                    number2 = random.randint(random_number[0], random_number[1])
                    if number1 > number2:
                        if number1 % number2 == 0:
                            break

                result = number1 / number2 
                print(f'{number1} / {number2} = ?')
                print('=' * 30)
            else:
                number1 = random.randint(random_number[0], random_number[1])
                number2 = random.randint(random_number[0], random_number[1])

                if calc == '+':
                    result = number1 + number2
                    print(f'{number1} + {number2} = ?')

                elif calc == '-':
                    result = number1 - number2
                    print(f'{number1} - {number2} = ?')

                elif calc == '*':
                    result = number1 * number2
                    print(f'{number1} x {number2} = ?')

            result_user = int(input('Resultado: '))
            
            # verify if the user win or not
            print('=' * 30)
            if result_user == result:
                print(f'Você ACERTOU! O resultado é {result}.')
            else:
                print(f'Você ERROU! O resultado é {result}.')
            print('=' * 30)
            c += 1

