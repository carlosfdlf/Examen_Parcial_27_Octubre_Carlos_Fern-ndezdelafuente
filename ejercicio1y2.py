class Alumno():
    
    def __init__(self, nombre, nota):
        
        self.nombre = nombre
        self.nota = nota
        
        print(f"Se acaba de crear un alumno {self.nombre} con un {self.nota} de nota")
        
        def __str__ (self):
            return "self.nombre {}, self.nota {}".format (self.nombre, self.nota)
        
    def calificacion ():
        if Alumno.nota >= 5:
            print ("El alumno ha aprobado")
        else: 
            print("El alumno ha suspendido")        
        
        
alumno = Alumno("Carlos", "6")
alumnos = [["Carlos", 6], ["Javier", 9], ["Magdalena", 3], ["Francisco", 7]]
print(str(alumno))
print(str(alumnos))

Alumno.calificacion("6")
for alumno in alumnos:
    Alumno.calificacion(alumno)





