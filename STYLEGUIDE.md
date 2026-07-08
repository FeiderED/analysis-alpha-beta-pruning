# Guía editorial del libro

Este repositorio se desarrollará como un libro universitario, no como una colección de apuntes. La prioridad es que cada capítulo sea matemáticamente correcto, pedagógicamente claro y visualmente consistente.

## Regla principal

Todo contenido nuevo debe ubicarse en `book/` y debe contribuir a una de estas capas:

1. **Capa matemática:** definiciones, notación, lemas, proposiciones, teoremas, corolarios, demostraciones e invariantes.
2. **Capa visual:** tableros, árboles, diagramas, tablas de evolución de valores, mapas conceptuales y figuras TikZ.
3. **Capa narrativa:** intuición, motivación, errores comunes, resúmenes y conexiones entre capítulos.

Un capítulo no se considera completo si solo tiene una de estas capas.

## Estilo de redacción

- Escribir en español claro y académico.
- No asumir conocimientos previos cuando se introduce un concepto por primera vez.
- Antes de una definición importante, explicar por qué esa definición existe.
- Antes de un teorema, explicar qué problema resuelve.
- Después de una demostración formal, agregar una interpretación intuitiva.
- Evitar frases como "es obvio" o "claramente" cuando el lector todavía no tiene fundamentos.
- Mantener una progresión: intuición → formalización → ejemplo → prueba → interpretación.

## Convención de capítulos

Cuando aplique, cada capítulo seguirá esta estructura:

1. Motivación.
2. Objetivos del capítulo.
3. Intuición inicial.
4. Notación necesaria.
5. Definiciones.
6. Ejemplos resueltos.
7. Lemas y proposiciones.
8. Teoremas.
9. Demostraciones paso a paso.
10. Interpretación intuitiva.
11. Errores comunes.
12. Resumen.
13. Ejercicios.
14. Conexión con el siguiente capítulo.

## Convención matemática

- Usar `\States` para el conjunto de estados.
- Usar `\Moves` para el conjunto de movimientos.
- Usar `\Legal(s)` para movimientos legales desde un estado.
- Usar `\Succ(s,a)` para el sucesor de `s` al aplicar `a`.
- Usar `\Children(s)` para el conjunto de hijos de `s`.
- Usar `\Utility(s)` para utilidad terminal.
- Usar `V(s)` para valor Minimax.
- Usar `\alpha` y `\beta` solo como cotas de Alpha-Beta, no como valores arbitrarios.

## Convención visual

Toda figura debe tener una razón pedagógica. No se agregan diagramas decorativos.

Cada árbol o tablero debe responder explícitamente:

- ¿Qué estado representa?
- ¿Quién mueve?
- ¿Qué movimientos legales existen?
- ¿Cuál es la profundidad del nodo?
- ¿Cuál es el valor si ya se conoce?
- ¿Qué ocurre con `\alpha` y `\beta` si el ejemplo está en Alpha-Beta?

## Ejemplos de juegos

Los ejemplos de tres en raya, conecta 4, damas y ajedrez deben desarrollarse nodo por nodo. Para cada nodo relevante se debe incluir:

- identificador del estado;
- tablero o representación equivalente;
- jugador que mueve;
- movimientos legales;
- hijos generados;
- utilidad o evaluación, si corresponde;
- retropropagación Minimax;
- evolución de cotas Alpha-Beta, si corresponde;
- justificación de cada poda.

## Código

El cuerpo principal del libro no debe contener código. Si se agrega código más adelante, debe ir en apéndices o en una carpeta independiente, no dentro de los capítulos centrales.
