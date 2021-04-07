# variabilityModelGenerator

Esta herramienta, denominada Generador Automatico de Modelos de Variabilidad, permite
generar diferentes modelos compuestos por servicios, dependencias de variabilidad e
inconsistencias en forma aleatoria. La misma, esta basada en los elementos, relaciones e
interacciones definidas en el modelado SeVaTax 

Para Ejecutar

Definir los parametros en generator.py y ejecutar 

Cantidad de Servicios (SQ): Indica la cantidad de servicios diferentes que deben
contener los modelos de variabilidad.
 Complejidad de las Relaciones (RC): Indica la cantidad de dependencias (requiere,
excluye y usa) que deben incluirse.

 Profundidad de Modelo (MP): Indica el numero maximo de niveles de puntos
variantes correlativos que pueden incluirse en cada modelo de variabilidad desde
la raiz hasta las hojas. 

Cantidad de Inconsistencias (IQ): Indica la cantidad de inconsistencias que
pueden ser agregadas.

ejemplo 

SQ = 30
RC = 5
MP = 4
IQ = 10



