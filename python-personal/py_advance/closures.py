#Funcion superior recive arg, desde nums(arg)
def nums(num:int)-> int: 
#Funcion anidada recibe paramentro de variable cuya asignacion es un funcion
#division_by_5 = nums(5) arg-> para func superior
#print(division_by_5(100)) arg-> para funcion anidada

        def divided_by(n:int):
            assert num != 0, 'Zero Division Error'
            return n / num
        return divided_by

def run():
    division_by_3 = nums(3)
    print(division_by_3(18))

    division_by_5 = nums(5)
    print(division_by_5(100))

    division_by_18 = nums(18)
    print(division_by_18(54))
    

if __name__ == '__main__':
    run()