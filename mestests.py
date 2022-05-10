# from Sprite import Sprite

# def compareTypes(args, defaultArgs):
#     newArgs = args[len(args)-len(defaultArgs):]
#     for index in range(len(newArgs)):
#         if defaultArgs[index] is not None and type(newArgs[index])!=(defaultArgs[index]):
#             raise Exception(f"Error à l'argument numéro {index}, on demande {(defaultArgs[index])} alors qu'on à reçu un type {type(newArgs[index])}")

# def myfunc(sah, ui=None, text=Sprite, nbr=int):
#     mesArgs=list(locals().values())
#     defaultArgs=myfunc.__defaults__
#     compareTypes(mesArgs, defaultArgs)

# test = Sprite(sp_img_path="",sp_animation="")
# myfunc("oui", text=test, nbr=30)

from Sprite import Sprite
from typing import Union, get_origin

def compareTypes(args, defaultArgs):
    newArgs = args[len(args)-len(defaultArgs):]
    for index in range(len(newArgs)):
        if get_origin(defaultArgs[index]) is Union:
            isSameType=False
            unionTypes=defaultArgs[index].__args__
            for typeInUnion in range(len(unionTypes)):
                if unionTypes[index-1] is not None and type(newArgs[index])==unionTypes[typeInUnion]:
                    isSameType=True
            if isSameType==False:
                raise Exception(f"Error à l'argument typé numéro {index+1} on demande un Union type {unionTypes} alors qu'on à reçu un type {type(newArgs[index])}")
        elif defaultArgs[index] is not None and type(newArgs[index])!=(defaultArgs[index]):
            raise Exception(f"Error à l'argument typé numéro {index+1}, on demande {(defaultArgs[index])} alors qu'on à reçu un type {type(newArgs[index])}")

def myfunc(sah, ui=None, text=int|str, nbr=int):
    mesArgs=list(locals().values())
    defaultArgs=myfunc.__defaults__
    compareTypes(mesArgs, defaultArgs)

test = Sprite(sp_img_path="",sp_animation="")
myfunc("oui", text="oui", nbr="oui")