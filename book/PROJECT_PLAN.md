# Plan maestro del libro

## Visión

Construir una obra extensa, rigurosa y autocontenida sobre Alpha-Beta Pruning, desde fundamentos matemáticos hasta análisis formal del paper de Knuth y Moore.

El libro debe poder ser leído por una persona que parte desde cero y debe terminar permitiéndole comprender demostraciones formales, análisis de complejidad y ejemplos reales de juegos.

## Volumen I: Fundamentos matemáticos

Objetivo: preparar al lector para entender árboles de juego, recursividad, inducción, invariantes y complejidad.

Capítulos previstos:

1. ¿Qué significa jugar racionalmente?
2. Conjuntos y notación básica.
3. Funciones y relaciones.
4. Órdenes, máximos y mínimos.
5. Recursividad matemática.
6. Inducción matemática.
7. Árboles y grafos.
8. Complejidad computacional.
9. Invariantes de algoritmos.

## Volumen II: Juegos y búsqueda adversaria

Objetivo: formalizar juegos finitos, estados, movimientos, árboles de juego y utilidad.

Capítulos previstos:

1. Juegos bipersonales de suma cero.
2. Estados, acciones, sucesores e historias.
3. Terminalidad y utilidad.
4. Árboles de juego completos.
5. Árboles de profundidad limitada.
6. Evaluación heurística.
7. Explosión combinatoria.
8. Primeros ejemplos con tres en raya.

## Volumen III: Minimax, Negamax, Branch and Bound y Alpha-Beta

Objetivo: desarrollar los algoritmos centrales con rigor matemático.

Capítulos previstos:

1. Construcción matemática de Minimax.
2. Corrección de Minimax.
3. Negamax y equivalencia formal.
4. Demostración de `G(p)=-F(p)`.
5. Branch and Bound.
6. Alpha-Beta como búsqueda con cotas.
7. Invariantes de Alpha-Beta.
8. Corrección formal de Alpha-Beta.
9. Análisis de complejidad.
10. Teoremas principales del paper de Knuth y Moore.

## Volumen IV: Casos de estudio y aplicaciones

Objetivo: construir árboles de juego reales y explicar cada paso.

Casos previstos:

1. Tres en raya completo.
2. Conecta 4.
3. Damas.
4. Ajedrez.
5. Comparación entre órdenes de movimientos.
6. Ejemplos donde Alpha-Beta no poda.
7. Ejemplos donde Alpha-Beta poda agresivamente.
8. Tablas de evolución de `alpha` y `beta`.
9. Técnicas modernas: move ordering, transposition tables, iterative deepening, principal variation search y MCTS.

## Criterios de finalización de un capítulo

Un capítulo se considera terminado solo si contiene:

- objetivos claros;
- motivación;
- definiciones necesarias;
- ejemplos resueltos;
- errores comunes;
- ejercicios;
- resumen;
- conexión con el capítulo siguiente;
- revisión de consistencia de notación.

## Orden de trabajo recomendado

1. Consolidar la arquitectura editorial.
2. Redactar completamente el Capítulo 0.
3. Reforzar fundamentos matemáticos.
4. Ampliar árboles de juego.
5. Construir el caso de tres en raya con mucho detalle.
6. Recién después, volver a Minimax y Alpha-Beta.
