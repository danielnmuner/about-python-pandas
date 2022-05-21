# from datetime import datetime


# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         initial_time = datetime.now()
#         func(*args, **kwargs)
#         final_time = datetime.now()
#         time_elapsed = final_time - initial_time
#         print(f'Pasaron {time_elapsed.total_seconds()} segundos')
#     return wrapper


# @execution_time
# def random_func():
#     for _ in range(1, 10000000):
#         pass


# random_func()
#---------------------------------------------------------------------
# #Rock Paper Sisors con decoradores

# import random

# def run():
#     options = 'Rock'
#     user_option = 'Rock'
    
#     def cpu_result(func):
#         def wrapper(*args,**kwagrs):
#             func(*args,**kwagrs)
#             option = ['Rock','Paper','Sisors']
#             cpu_option = random.choice(option)
#             if cpu_option == 'Paper' and user_option == 'Sisors' or  cpu_option == 'Rock' and user_option == 'Paper' or cpu_option == 'Sisors' and user_option == 'Rock':
#                 print('You Won!')
#             elif cpu_option == user_option:
#                 print('You are Tied!')
#             else: 
#                 print('Loser')
#         return wrapper



#     @cpu_result
#     def user_result(option:str):
#         print(f'User chose {option}')


#     user_result(user_option)


# if __name__=='__main__':
#     run()