def ListAsCommaSeperatedString(lst: list) -> str:
    mainStr: str = ""
    for i,item in enumerate(lst):
        if(i == 0):
             mainStr += f'{item}'
        else:
            mainStr += f', {item}'
    return mainStr

spam = ['apples', 'bananas', 'tofu', 'cats']
newStr = ListAsCommaSeperatedString(spam)
print(newStr)
