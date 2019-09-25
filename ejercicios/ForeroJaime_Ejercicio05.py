
#A partir de la implementación de la clase Balon tal como se muestra en el video resuelva los siguiente puntos.

#* (20 puntos) Incluya dos nuevos atributos a la clase Balon para describir la velocidad y posicion inicial en "x". El metodo __init__ debe actualizarse para que estos dos atributos se puedan inicializar de la misma manera que los atributos asociados al eje "y".

#* (20 puntos) Actualice el método calculaFuerza para calcular la fuerza en el eje "x".

#* (20 puntos) Actualice el método muevete para calcular el cambio de posición y velocidad en el eje "x".

#* (20 puntos) Actualice el método imprime para imprimir en pantalla el tiempo, las posiciones "x", "y" y las velocidades en "x" y "y". Esos cinco valores se deben imprimir en ese orden.

#* (20 puntos) El código debe inicializarse con "x0=1.0", "y0=1.0", velocidad inicial en "x" de 0.4 y velocidad inicial en "y" de 0.2 y "t" igual a 0.0. Con esas condiciones iniciales el código debe imprimir en pantalla el tiempo, posiciones y velocidades mientras "t" sea menor a 1.5, tomando "DeltaT"=0.005.

class Balon:
    g = 9.8
    def __init__(self, x0, y0, vx0, vy0, m0):
        self.x = x0
        self.y = y0
        self.vx = vx0
        self.vy = vy0
        self.m = m0
    def calculaFuerza(self):
        self.Fx = 0.0
        self.Fy = -self.m * Balon.g
    def muevete(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += self.Fx * dt/self.m
        self.vy += self.Fy * dt/self.m
    def imprime(self, t):
        print(t, self.x, self.y, self.vx, self.vy)

pelota = Balon(1.0, 1.0, 0.4, 0.2, 0.453)
pelota.calculaFuerza()
t = 0.0
Deltat = 0.005
while t < 1.5:
    pelota.imprime(t)
    pelota.muevete(Deltat)
    t += Deltat
