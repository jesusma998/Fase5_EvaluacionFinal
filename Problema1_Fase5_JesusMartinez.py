# Nombre del estudiante: Jesus Fernando Martinez Anaya
# Grupo: [Escribe aquí tu número de grupo]
# Programa: Ingeniería Multimedia
# Código Fuente: autoría propia

print("--- Sistema de Evaluación de Compromiso de Sesiones ---")

# R1: Matriz de datos. 
# Cada fila representa una sesión.
# Columnas: [Duración en minutos, Número de Interacciones, Porcentaje de Asistencia]
matriz_sesiones = [
    [60, 20, 85],  # Sesión 1
    [45, 12, 65],  # Sesión 2
    [30, 5, 40],   # Sesión 3
    [90, 25, 95]   # Sesión 4
]

print("\nProcesando los datos de las sesiones...\n")
print("-" * 50)
print(f"{'Sesión':<10} | {'Duración':<10} | {'Interacciones':<15} | {'Asistencia':<12} | {'Compromiso'}")
print("-" * 50)

# R2 y R3: Recorrer la matriz para evaluar y mostrar resultados
for i in range(len(matriz_sesiones)):
    duracion = matriz_sesiones[i][0]
    interacciones = matriz_sesiones[i][1]
    asistencia = matriz_sesiones[i][2]
    
    # Evaluar el nivel de compromiso (ajusta estos valores si la guía exige otros específicos)
    if duracion >= 60 and interacciones >= 15 and asistencia >= 80:
        nivel_compromiso = "Alto"
    elif duracion >= 45 and interacciones >= 10 and asistencia >= 60:
        nivel_compromiso = "Medio"
    else:
        nivel_compromiso = "Bajo"
        
    # Imprimir la fila con el formato adecuado
    print(f"Sesión {i+1:<3} | {duracion:<10} | {interacciones:<15} | {asistencia:<12}% | {nivel_compromiso}")

print("-" * 50)
print("--- Fin del reporte ---")