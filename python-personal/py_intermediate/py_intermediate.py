#Curso de Python Intermedio: Comprehensions, 
#Lambdas y Manejo de Errores
#Profesor: Facundo García Marto    

# # Listas y Diccionarios -> Apuntes

# def run():
#     list_comp = [i for i in range(10000) if i % 36 == 0 ]
#     print(list_comp)

# if __name__ == '__main__':
#     run()
# #Lista de Divisibles por 4,6,9 con comprehension List
# #----------------------------------------------------------
# import numpy as np

# def run():
#     d={i:round(np.sqrt(i),2) for i in range(1,4)}
#     print(d)

# if __name__ == '__main__':
#     run()

# #Dictionary Comprehensions    
# #---------------------------------------------------------
# def run():
#     var = lambda l : [i for i in l if i % 3 == 0]
#     print(var([1,2,3,4,5,6,7,8,9,10]))
# if __name__ == '__main__':
#     run()

# #Lambda Functions - Apuntes
# #--------------------------------------------------------------

# # #Manejor Lambdas/ High Order Functions y Comprehensions

# DATA = [
#     {
#         'name': 'Facundo',
#         'age': 72,
#         'organization': 'Platzi',
#         'position': 'Technical Coach',
#         'language': 'python',
#     },
#     {
#         'name': 'Luisana',
#         'age': 33,
#         'organization': 'Globant',
#         'position': 'UX Designer',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Héctor',
#         'age': 19,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'ruby',
#     },
#     {
#         'name': 'Gabriel',
#         'age': 20,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Isabella',
#         'age': 30,
#         'organization': 'Platzi',
#         'position': 'QA Manager',
#         'language': 'java',
#     },
#     {
#         'name': 'Karo',
#         'age': 23,
#         'organization': 'Everis',
#         'position': 'Backend Developer',
#         'language': 'python',
#     },
#     {
#         'name': 'Ariel',
#         'age': 32,
#         'organization': 'Rappi',
#         'position': 'Support',
#         'language': '',
#     },
#     {
#         'name': 'Juan',
#         'age': 17,
#         'organization': '',
#         'position': 'Student',
#         'language': 'go',
#     },
#     {
#         'name': 'Pablo',
#         'age': 32,
#         'organization': 'Master',
#         'position': 'Human Resources Manager',
#         'language': 'python',
#     },
#     {
#         'name': 'Lorena',
#         'age': 56,
#         'organization': 'Python Organization',
#         'position': 'Language Maker',
#         'language': 'python',
#     },
# ]

# def run():
#     # student_dev = [ st['name'] for st in DATA if st['language'] == 'python' ]
#     # for i in student_dev:
#     #     print(i)
#     # adults = list(filter(lambda arg : arg['language'] == 'python' ,DATA))
#     # adults = list(map(lambda arg : arg['name'], adults))
#     # old_people = list(map(lambda arg : {**arg , **{'old': arg['age'] > 18}} , DATA))
#     #iterable = list(filter(lambda worker : worker['age'] > 18 ,DATA))
#     #iterable = list(map(lambda worker : worker['age'] ,iterable))
#     iterable = [{**worker,** {'old':worker['age'] > 18}} for worker in DATA]

#     for worker in iterable:
#         print(worker['name'],' ',worker['age'],' ',worker['old'])

# if __name__ == '__main__':
#     run()   
# --------------------------------------------------------------
#Manejo de Exceptions 

# def concat(num):
    
    
#     for i in range (1,num+1):
#         print('I 💖 # '+str(i))

# def run():
#     user_num = input('Ingrese una palabra: ')
#     assert int(user_num) > 0 , 'Solo ingresa Numeros Positivos'
#     assert user_num.isnumeric() ,'Solo ingresa Numeros'
    
#     concat(int(user_num))

# if __name__ == '__main__':
#     run()

# #Apertura de Archivos con Open With
# #----------------------------------------------------------------------------------------------
# def run():
#     names=[]
#     with open('./file.csv','r',encoding='utf-8') as f:
#         for line in f:
#            names.append(line.strip())

#     with open('./file.txt','a',encoding='utf-8') as file:
#         for lines in names:
#             file.write(lines + ' Taste 👍')
#             file.write('\n')
        

# if __name__=='__main__':
#     run()
#----------------------------------------------------------------------------------------






