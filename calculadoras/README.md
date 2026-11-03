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

- Agua: personas × días × 3 L [S27, S19].
- Bidones de 20 L: agua / 20, redondeado hacia arriba.
- Comidas: personas × días × 3.
- Latas de atún o legumbres en total: personas × días. Es una estimación de esta guía, no un estándar.
- Filas con `escala=si`:
  - hasta 3 días, se usa `base_3d`;
  - 7 días, se usa `base_7d`;
  - otra cantidad de días, `base_7d / 7 × días`;
  - el resultado se multiplica por `personas / 4` y se redondea hacia arriba (con un decimal si la unidad es kg).
- Filas con `escala=no`: se copian sin cambios, incluidos los textos como "lo que ya tengas". Hasta 3 días se toma `base_3d`; con más días, `base_7d`.

### Casos de prueba

| Personas | Días | Agua | Bidones |
|---|---|---|---|
| 4 | 3 | 36 L | 2 |
| 4 | 7 | 84 L | 5 |
| 2 | 7 | 42 L | 3 |

## Canasta de largo plazo

`largo-plazo.csv` lista la canasta mensual por persona. Total: 60.205 kcal, unas 2.000 kcal por día (60.205 / 30).

Supuesto: las kcal por unidad salen de valores típicos de tablas nutricionales para alimentos crudos y secos (arroz, legumbres, harina, fideos y azúcar por kg; aceite por litro). Cada marca y variedad tiene valores distintos: revisá la tabla nutricional del envase. Las cantidades no fueron validadas por un profesional de nutrición (ver P08 en [PENDIENTES](../PENDIENTES.md)).

## Fuentes

- S19: Excélsior, Japón pedirá almacenar agua, comida y suministros.
- S27: Newscord, campaña UK Be Ready, 72 horas.
