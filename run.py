# import modules
from random_calcs import Program
import os


# funcions
def clear():
    os.system('clear') or None


def title(msg='', s='='):
    print(s*30)
    print(f'{msg:^30}')
    print(s*30)


# quantity of calcs
title(msg='QUANTIDADE')
quant = int(input('Quantas contas deseja fazer? '))
clear()

# run program
program = Program()
program.run_program(quant_calcs=quant)

