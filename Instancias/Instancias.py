class Coordenada:
    #Este es el constructor
    def __init__(self, x, y):
        #Variables para las coordenadas     
        self.x = x
        self.y = y
    #Este es un metodo llamado distancia
    def distancia(self, otra_coordenada):
        #Para definir la instancia vamos a usar el metodo euclidiano
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        #0.5 hace referencia a la raiz cuadrada del numero de coordenadas
        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    #Instacias
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)
    #Estamos imprimiendo la diferencias entre las coordenadas
    print(coord_1.distancia(coord_2))
    #isinstance esto es para ver si alguna de las coord_1 es instancia de la Cordenada
    print(isinstance(coord_1, Coordenada))

