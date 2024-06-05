class Coche:
    # atributos de la clase
   color = ""
   marca = ""
   kmH = 0
   
   #TODO:PREGUNTARLE AL PROFE PARA QUE SON LOS METODOS DE LA CLASE Y QUE ESTAN HACIENDO EN ESTE EJERCICIO
   # metodos de la clase
   def acelerar(self):
       self.kmH += 10

    # ------------ METODOS GETTERS -----------------   
    # los gets tiene la funcion unica y exclusivamente funcionalidad
    # -- de devolver el valor de un atributo   
    # get traducido es = a Obtener
    
   def getKmH(self):
       return self.kmH
   
   def getMarca(self):
       return self.marca
   
   def getColor(self):
       return self.color
   
   # ----------------- METODOS SETTERS -----------------
   # los sets tiene la funcion unica y exclusivamente funcionalidad
   # de modificar el valor de un atributo
   # set traducido es = a Establecer
   
   def setKmH(self, kilometros):
       self.kmH = kilometros 
       
   def setMarca(self , Marca):
       self.marca =  Marca    
    
   def setColor(self , Color):
        self.color = Color   

       
       
"""coche1 = Coche() # instanciar la clase Coche (crear la copia)
coche1.setMarca("Ford")

for i in range(5):

    coche1.acelerar()
    
print(f"el coche1 tiene una velocidad de {coche1.getKmH()} km/h")
print(f"el coche1 tiene una marca de {coche1.getMarca()}")

coche2 = Coche()

for i in range(7):
    coche2.acelerar()
    
print(f"el coche2 tiene una velocidad de {coche2.getKmH()} km/h")"""


#Personalizacion de coches en el taller
#crear una instancia de coche
mi_coche = Coche() # instanciando (creando una copia)

#Establecer el color inicial del coche 
mi_coche.setColor("rojo")

# Mostrar el color inicial del coche 
print(f"Color inicial del coche: {mi_coche.getColor()}")

# el cliente decide cambiar el color del coche 
nuevo_color = "Negro"
mi_coche.setColor(nuevo_color)

# Mostrar el color final del coche 
print(f"Color final del coche: {mi_coche.getColor()}")





    
   

       
    
    