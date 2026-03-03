def reverseList(li):
    if isinstance(li, list):
        li.reverse()
        return li
    else:
        return f'{li} is not a list'
    
    
import random as R
li = [ R.randint(10, 99) for _ in range(11)]
print(li)
revLi = reverseList(li)
print(revLi)

revLi = reverseList("Hello!")
print(revLi)