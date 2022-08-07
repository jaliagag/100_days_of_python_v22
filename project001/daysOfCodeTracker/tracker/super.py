#from django.test import TestCase

# Create your tests here.

# https://www.youtube.com/watch?v=0xt806gLghg

class Persona():
    def __init__(self,apePat,apeMat,nombre):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nombre

    def showme(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Estudiante(Persona):

    # esto solo así nos va a dar un error
    # TypeError: __init__() takes 2 positional arguments but 4 were given
    #def __init__(self, profesion):
    #    self.prof = profesion
    # tenemos que usar un super que va a heredar el constructor de la clase padre
    def __init__(self, apePat, apeMat, nombre, profesion):
        super().__init__(apePat,apeMat,nombre)
        self.prof = profesion

estu1 = Estudiante("aliaga","giacosa","josé", "devesecops")
# nos muestra el lugar en memoria
# print(estu1)
# llamamos a la función showme
print(estu1.showme())
print(estu1.prof)
