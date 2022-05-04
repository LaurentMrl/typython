from Sprite import Sprite


def compareTypes(args, defaultArgs):

    newArgs = args[len(args)-len(defaultArgs):]

    for index in range(len(newArgs)):

        if defaultArgs[index]!=None and type(newArgs[index])!=(defaultArgs[index]):

            raise Exception(f"Error à l'argument numéro {index}, on demande {(defaultArgs[index])} alors qu'on à reçu un type {type(newArgs[index])}")



def myfunc(sah,ui=None, text=Sprite, nbr=int):

    mesArgs=list(locals().values())

    defaultArgs=myfunc.__defaults__

    compareTypes(mesArgs, defaultArgs)



test = Sprite(sp_img_path="",sp_animation="")

myfunc("oui", text=test, nbr=30)