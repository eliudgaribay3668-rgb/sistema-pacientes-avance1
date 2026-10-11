class Paciente:

    # Constructor
    def __init__(self, nombre, edad, diagnostico, numero_expediente):
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico
        self.numero_expediente = numero_expediente
        self.hospitalizado = False

    # Método 1: mostrar la información del paciente
    def mostrar_informacion(self):
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Diagnóstico: {self.diagnostico}")
        print(f"Número de expediente: {self.numero_expediente}")
        print(f"Hospitalizado: {self.hospitalizado}")

    # Método 2: actualizar el diagnóstico
    def actualizar_diagnostico(self, nuevo_diagnostico):
        self.diagnostico = nuevo_diagnostico
        print(f"El diagnóstico de {self.nombre} se actualizó a: {self.diagnostico}")

    # Método 3: hospitalizar al paciente
    def hospitalizar(self):
        self.hospitalizado = True
        print(f"{self.nombre} ha sido hospitalizado correctamente.")

    # Método 4: dar de alta al paciente
    def dar_alta(self):
        self.hospitalizado = False
        print(f"{self.nombre} ha recibido el alta médica.")

# Creación de tres objetos diferentes
paciente1 = Paciente("Nancy Isabel", 20, "Migraña", "EXP-001")
paciente2 = Paciente("Axel López", 19, "Hipertensión", "EXP-002")
paciente3 = Paciente("Santiago Orozco", 20, "Fractura de brazo", "EXP-003")

print("----- PACIENTE 1 -----")
paciente1.mostrar_informacion()
paciente1.actualizar_diagnostico("Migraña crónica")
paciente1.hospitalizar()

print("\n----- PACIENTE 2 -----")
paciente2.mostrar_informacion()
paciente2.hospitalizar()
paciente2.dar_alta()

print("\n----- PACIENTE 3 -----")
paciente3.mostrar_informacion()
paciente3.actualizar_diagnostico("Fractura de brazo en recuperación")

print("\n----- INFORMACIÓN FINAL -----")
paciente1.mostrar_informacion()
print()
paciente2.mostrar_informacion()
print()
paciente3.mostrar_informacion()
