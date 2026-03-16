# Calculadora Geométrica en Python

## Descripción

Este proyecto es una **calculadora geométrica interactiva en consola**, desarrollada en **Python**, que permite calcular diferentes propiedades de figuras **2D y 3D**.

El programa utiliza **menús interactivos**, **validación de errores** y **validaciones geométricas** para evitar cálculos imposibles o incoherentes.

El usuario puede elegir una figura y luego seleccionar qué desea calcular, como área, perímetro, volumen u otros valores geométricos.

---

## Características

* Menú interactivo en consola
* Navegación entre menús (volver atrás)
* Validación de datos de entrada
* Prevención de errores matemáticos
* Soporte para múltiples figuras geométricas

---

## Figuras soportadas

### Figuras 2D

**Triángulo**

* Área
* Perímetro
* Ángulo faltante

**Cuadrado**

* Área
* Perímetro

**Círculo**

* Área
* Perímetro
* Diámetro

**Trapecio**

* Área
* Perímetro

**Triángulo rectángulo**

* Hipotenusa
* Cateto
* Ángulo faltante

---

### Figuras 3D

**Cubo**

* Área superficial
* Volumen

**Cono**

* Área
* Volumen

**Cilindro**

* Área
* Volumen

**Esfera**

* Área
* Volumen

---

## Validaciones implementadas

El programa incluye varias validaciones para evitar resultados incorrectos:

* No se permiten números negativos.
* Los lados de un triángulo deben cumplir la **regla del triángulo**.
* Los ángulos de un triángulo no pueden sumar 180° o más.
* En el trapecio, la **base menor no puede ser mayor que la base mayor**.
* En el triángulo rectángulo, el **cateto no puede ser mayor que la hipotenusa**.
* En el cono, la **generatriz debe ser mayor que el radio**.

---

## Tecnologías utilizadas

* Python 3
* Programación estructurada
* Ciclos `while`
* Condicionales `if / elif`
* Validación de entradas con `try/except`

---

## Cómo ejecutar el programa

1. Clona el repositorio:

```
git clone https://github.com/CarlosAp0515/calculadora-geometrica.git
```

2. Entra en la carpeta del proyecto:

```
cd calculadora-geometrica
```

3. Ejecuta el programa:

```
python calculadora.py
```

---

## Objetivo del proyecto

Este proyecto fue desarrollado como práctica para aprender:

* estructuras de control en Python
* validación de datos
* lógica matemática aplicada
* organización de programas con menús

---

## Autor

**Carlos Aponte**

Proyecto educativo de programación en Python.
