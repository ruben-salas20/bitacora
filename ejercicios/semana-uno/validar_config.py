# Función que valida batch_size, learning_rate y epochs (batch > 0, lr entre 0 y 1, epochs > 0),
# con mensaje claro por cada error. Tres llamadas de prueba abajo.

def validar_valores(batch, lr, epochs):
    error_messages = ""
    if not batch > 0:
        error_messages += "- El tamaño de batch no puede ser menor o igual a 0\n"
    if not 0 < lr <= 1: # learning rate excluye 0 debido a que no se puede entrenar con un learning rate de 0
        error_messages += "- El learning rate debe estar entre 0 y 1\n"
    if not epochs > 0:
        error_messages += "- El número de epochs no puede ser menor o igual a 0\n"
    if error_messages:
        return error_messages
    return "Valores válidos"

print(validar_valores(32, 0.01, 10))  # Valores válidos
print(validar_valores(0, 0.01, 10))   # Batch no cumple
print(validar_valores(32, 1.5, 10))  # Learning rate no cumple
print(validar_valores(32, 0.01, -5))  # Epochs no cumple
print(validar_valores(0, 1.5, -5))  # Ningun valor cumple