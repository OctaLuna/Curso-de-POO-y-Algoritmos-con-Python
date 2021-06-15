#Vamos a hacer una Decomposición de un AutoMovil
class AutoMovil:
    #Constructor
    def __init__(self, modelo, marca, color):
        #Estas son nuestras variables de nuestro constructor
        self.modelo = modelo
        self.marca = marca
        self.color = color
        #Le estamos dando un estado, con un variable privada
        self._estado = "en_reposo"
        self._motor = Motor(cilindros=4)

    def Acelerar (self, tipo="despacio"):
        if tipo == "rapida":
            self._motor.Inyecte_gasolina(10)
        else:
            self._motor.Inyecte_gasolina(3)
        self._estado = "en_movimiento"


class Motor:
    #tipo="gasolina" este es un parametro pordefecto, 
    def __init__(self, cilindros, tipo="gasolina"):
        self-cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    def Inyecte_gasolina(self, cantidad)


if __name__ == "__main__":
    pass