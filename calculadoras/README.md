---
titulo: Calculadoras
ultima_revision: 2026-11-05
estado: borrador
confianza: mixta
fuentes: [S31]
---

# Calculadoras

Todo lo que sale de esta carpeta es `ESTIMACIÓN`: cantidades orientativas, no indicaciones oficiales.

## Archivos

| Archivo | Contenido |
|---|---|
| [cantidades.csv](cantidades.csv) | Reserva de 3 y 7 días para una familia de 4 personas |
| [largo-plazo.csv](largo-plazo.csv) | Canasta mensual por persona para el [modo largo plazo](../10-modo-largo-plazo.md) |
| [calcular.py](calcular.py) | Escala `cantidades.csv` a cualquier cantidad de personas y días |

Los CSV están codificados en UTF-8 y usan coma como separador.

## Uso de la calculadora

Requiere Python 3. No usa dependencias externas.

```sh
python3 calculadoras/calcular.py --personas 4 --dias 3
```

### Reglas

- Agua: personas × días × 3 L para bebida y preparación de comidas [S31]. Higiene y otros consumos van aparte.
- Bidones de 20 L: agua / 20, redondeado hacia arriba.
- Comidas: personas × días × 3.
- Latas en total: suma de las filas de latas ya redondeadas. El resumen y la tabla usan el mismo total. Es una estimación de inventario, no una dieta.
- Filas con `escala=si`:
  - hasta 3 días, se usa `base_3d / 3 × días`;
  - 7 días, se usa `base_7d`;
  - otra cantidad de días, `base_7d / 7 × días`;
  - el resultado se multiplica por `personas / 4` y se redondea hacia arriba (con un decimal si la unidad es kg).
- Filas con `escala=no`: se copian sin cambios, incluidos los textos como "lo que ya tengas". Hasta 3 días se toma `base_3d`; con más días, `base_7d`.

La calculadora no estima cuánto dura una dieta ni asegura que estas cantidades cubran las necesidades de cada integrante.

### Casos de prueba

| Personas | Días | Agua | Bidones |
|---|---|---|---|
| 4 | 3 | 36 L | 2 |
| 4 | 7 | 84 L | 5 |
| 2 | 7 | 42 L | 3 |

## Canasta de largo plazo

`largo-plazo.csv` lista la canasta mensual por persona. Total aritmético bajo los supuestos de la tabla: 60.205 kcal; unas 2.000 kcal por día (`ESTIMACIÓN`: 60.205 / 30 = 2.006,8).

Supuesto: las kcal por unidad son valores de referencia sin fuente nutricional verificada para alimentos crudos y secos (arroz, legumbres, harina, fideos y azúcar por kg; aceite por litro). Cada marca y variedad tiene valores distintos: revisá la tabla nutricional del envase. La suma aritmética no prueba adecuación nutricional. Las cantidades no fueron validadas por un profesional de nutrición (ver P08 en [PENDIENTES](../PENDIENTES.md)).

> **PENDIENTE:** falta verificar los valores energéticos de los alimentos y validar nutricionalmente la canasta. Ver P08 en [PENDIENTES](../PENDIENTES.md).

## Fuentes

- S31: Japón: pedido de preparación preventiva.
