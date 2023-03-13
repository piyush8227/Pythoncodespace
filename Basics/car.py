''' 
Author: Piyush
Description: Student registration application
'''
import pickle

std = {}

def std_register():
    global std

    reg_no = input('Enter Registration No: ')
    sname = input("Enter the student name: ")
    sage = input('Enter the age of student: ')

    std[reg_no] = {'name': sname, 'age': sage}

    f = open('std.dat','wb')
    pickle.dump(std, f)

std_register()

def std_info():
    f = open('std.dat','rb')
    sss = pickle.load(f)
    print(sss)
# print(std)
std_info()