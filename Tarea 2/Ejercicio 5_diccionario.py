# Ejercicio 6 - manipulación de un diccionario.
# Primero defino unas variablas llamadas "nombre_estudiante" y "promedio_notas".
# Les doy valores por medio del diccionario origen.
# Finalmente creo el diccionario solicitado.

# Definición del diccionario origen.

sampleDict = {
    'class': {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
                "math": 90
            },
        }
    }
}

nombre_estudiante = sampleDict["class"]["student"]["name"]
print("El nombre del estudiante es: ", nombre_estudiante)

promedio_notas = (sampleDict["class"]["student"]["marks"]["physics"] + sampleDict["class"]["student"]["marks"]["history"] + sampleDict["class"]["student"]["marks"]["math"])/3
print("Su promedio de notas es: ", promedio_notas)

nuevoDict = { 
    "nombre": nombre_estudiante, 
    "promedio notas": promedio_notas 
}
print(nuevoDict)
