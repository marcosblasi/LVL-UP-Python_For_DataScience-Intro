
def function(parameter1:str, parameter2:str):

    message = 'Hello ' + str(parameter1) + str(parameter2)
    return message


variable = function('This is Python course ', 'LVL_UP')

text = 'Welcome ' + variable

print(text)

# --------------------------------------------------------------------- #

def cat_ev(name:str, age:int):

    if age < 8:
        cat = 'inferiors'
        message = f'{name} you are in category: {cat}'

    elif 8 < age < 12:
        cat = 'intermediate'
        message = f'{name} you are in category: {cat}'

    else: 
        cat = 'superiors'
        message = f'{name} you are in category: {cat}' 

    return message

evaluation = cat_ev('Marcos', 30)

print(evaluation)

# --------------------------------------------------------------------- #

list_a = []

def str_ev(
        article_list:list
        ):
    
    """Function that receives a list of articles and saves it in a list wheter they 
       accomplish a certain condition or not"""

    for element in article_list:

        if element[0] == 'a' or element[0] == 'A':

            list_a.append(element)

        else:

            pass
    
    return list_a

articles = str_ev(['Armario', 'Silla', 'Ropero', 'arbol'])

print(articles)


