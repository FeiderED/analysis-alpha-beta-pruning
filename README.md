# Análisis formal de Alpha-Beta Pruning

Libro universitario en español sobre **Minimax**, **Negamax**, **Branch and Bound** y **Alpha-Beta Pruning**.

El objetivo es desarrollar el tema con una estructura cercana a CLRS: definiciones formales, notación, lemas, teoremas, corolarios, demostraciones y ejemplos gráficos completamente explicados.

## Enfoque actual

- El cuerpo principal del libro no usa código.
- La prioridad es la formalización matemática.
- Las pruebas se desarrollan paso a paso, sin asumir conocimientos previos.
- Los ejemplos de juegos se explican mediante estados, árboles, utilidad, cotas y poda.
- Los árboles de tres en raya, damas y ajedrez se construyen nodo por nodo.

## Estructura nueva

```text
book/
  main.tex
  preamble.tex
  bibliography.bib
  chapters/
    00-prefacio.tex
    01-fundamentos.tex
    02-arboles-de-juego.tex
    03-minimax-formal.tex
    04-alpha-beta-formal.tex
    05-tres-en-raya-paso-a-paso.tex
    06-damas-y-ajedrez-paso-a-paso.tex
```

La carpeta `docs/` conserva material preliminar anterior. El desarrollo nuevo se hará en `book/`.

## Compilación

```bash
latexmk -pdf book/main.tex
```

También puede compilarse con `pdflatex` en varias pasadas.

## Estado

Inicio del libro formal ampliado. La primera entrega establece el marco editorial y comienza el desarrollo detallado de los ejemplos con árboles de juego, especialmente tres en raya.
