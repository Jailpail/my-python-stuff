import colorama


class one:
    pass


class two:
    print("colorama.Cursor is an interesting function  because it sounds cool , i have absolutely 0 idea what it does ")
    pass
joemama= two
print("is class two instance of class one? ",isinstance(two, one))
print("Is class two subclass of joemama? ",issubclass(two,joemama))
print("Is class one subclass to class joemama ( totally not class two )?",issubclass(one,joemama))
print("Is colorama instance of joemama?",isinstance(colorama,joemama))
print("Colorama functions in format ['function']:  ",dir(colorama))