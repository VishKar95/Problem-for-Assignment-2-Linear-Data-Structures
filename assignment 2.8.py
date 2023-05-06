def reverse_string(string):
    stack = []
    # push all characters onto the stack
    for char in string:
        stack.append(char)
    
    reversed_string = ''
    # pop all characters from the stack to get the reversed string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
string = 'Hello, world!'
print(reverse_string(string))  # output: '!dlrow ,olleH'
