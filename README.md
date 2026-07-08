# Analysis Alpha-Beta Pruning

Guía en español, desde cero, para estudiar **minimax**, **negamax** y **poda alfa-beta** con análisis formal inspirado en el paper de Knuth y Moore, *An Analysis of Alpha-Beta Pruning*.

## Archivos principales

- `docs/guia-alpha-beta-pruning.tex`: guía completa en LaTeX con colores suaves, diagramas TikZ, demostraciones por inducción, notación matemática y ejemplos con 3 en raya, ajedrez y damas.
- `src/alpha_beta.py`: implementación didáctica en Python de minimax, negamax, alfa-beta, 3 en raya y árboles de ejemplo.

## Compilar la guía

Desde la raíz del repositorio:

```bash
pdflatex -interaction=nonstopmode docs/guia-alpha-beta-pruning.tex
pdflatex -interaction=nonstopmode docs/guia-alpha-beta-pruning.tex
```

El segundo pase ayuda a estabilizar referencias internas.

## Ejecutar el código

```bash
python src/alpha_beta.py
```

El script imprime comparaciones entre minimax completo y alfa-beta sobre árboles pequeños, además de una demostración de 3 en raya.

## Objetivo pedagógico

La guía no asume conocimientos previos. Primero define juegos, posiciones, árboles, valores terminales, funciones de evaluación, máximo, mínimo, cotas e inducción. Luego deriva minimax, negamax y alfa-beta paso a paso, explica los invariantes y demuestra por qué la poda no cambia el resultado.