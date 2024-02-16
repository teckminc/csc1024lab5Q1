'''
Do not remove any text from these comments
1.	Write a Python program using the while loop to get an 
input of five number from the user then store the input 
into a list called my_list in incremental order. 
Following is the sample output of the program.

Enter a number: 1.111
Enter a number: 3.333
Enter a number: 2.222
Enter a number: 4.444
Enter a number: 5.555
my_list = [1.111, 2.222, 3.333, 4.444, 5.555]

Function to use: float(), input(), print(), list.append(), list.sort()
Operators: <=, +
Structure: while
'''
def main():
    my_list = []
    count = 1
    while count <= 5:
        num = float(input("Enter a number: "))
        my_list.append(num)
        count = count + 1

    my_list.sort()
    print("my_list =" , my_list)
    return 0

