# Aqui se realiza lo que angel haga en el video

#¿Qué son las Funciones Lambda?

#Las funciones lambda, también conocidas como funciones anónimas, 
#son funciones pequeñas y sin nombre que pueden definirse en una línea de código.

#¿Cuales son sus ventajas?

#Son útiles para definir funciones pequeñas y simples en el lugar donde se necesitan

#Pueden ser utilizadas como argumentos de otras funciones de orden superior, como map(), filter() y sorted():

#Ayudan a escribir código más conciso y expresivo al eliminar la necesidad de definir funciones separadas con nombres

# Definimos una función lambda para mezclar ingredientes
mezclar_ingredientes = lambda ing1, ing2: f'Mezclando {ing1} con {ing2}'

# Utilizamos la función lambda para mezclar ingredientes
resultado = mezclar_ingredientes("harina", "azúcar")

# Imprimimos el resultado
print(resultado)  # Esto imprimirá "Mezclando harina con azúcar"

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una función lambda para filtrar los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimimos el resultado
print(numeros_pares)  # Esto imprimirá [2, 4, 6, 8, 10]