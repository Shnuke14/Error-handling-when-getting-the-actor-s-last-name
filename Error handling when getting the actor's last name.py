actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    name = actor["name"]
    ## Деление
    name_split = name.split()
    ## Получение последнего элемента в списке
    last_name = name_split[-1]
    return last_name

## Вызов функции
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())