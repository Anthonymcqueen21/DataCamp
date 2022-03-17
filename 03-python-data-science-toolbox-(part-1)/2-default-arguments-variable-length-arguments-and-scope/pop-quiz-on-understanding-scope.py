'''
Pop quiz on understanding scope
50xp

In this exercise, you will practice what you've learned about scope in functions.
The variable num has been predefined as 5, alongside the following function definitions:

def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)

Try calling func1() and func2() in the shell, then answer the following questions:
-What are the values printed out when you call func1() and func2()?
-What is the value of num in the global scope after calling func1() and func2()?

Possible Answers
func1() prints out 3, func2() prints out 6, and the value of num in the global scope is 3.
func1() prints out 3, func2() prints out 3, and the value of num in the global scope is 3.
func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 10.
func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.
'''
# func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.
