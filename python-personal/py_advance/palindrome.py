from typing import List

def is_prime(num:int)->bool:
    result:List[int] = [i for i in range(2,num) if num % i == 0] 
    return len(result) == 0

def run():
    user_num:int = int(input('Ingresa una Numero: '))
    print(is_prime('a'))

if __name__ == '__main__':
    run()

