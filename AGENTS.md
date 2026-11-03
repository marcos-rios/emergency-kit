# Instrucciones para agentes

Guía de preparación familiar ante crisis, adaptada a Argentina, en Markdown plano. Antes de editar, leé este archivo completo.

## Reglas

1. **Veracidad.** Todo dato numérico, normativo o técnico termina con un ID de fuente (`[S02]`) o con `ESTIMACIÓN` (cálculo propio, con la cuenta) o `RECOMENDACIÓN EDITORIAL` (criterio de la guía). Si no está verificado, no se afirma: se marca `> **PENDIENTE:** ...` en el texto, con su ID (`P01`), y se agrega a [PENDIENTES.md](PENDIENTES.md).
2. **Seguridad.** Toda combustión (hornallas, parrillas, braseros, generadores) solo al aire libre o con ventilación. Nunca gasolina para encender fuego. Nada de dosis de medicamentos: derivar a médico o farmacéutico. Nada sobre armas, violencia ni explosivos.
3. **Privacidad.** Ningún dato personal real. La guía habla de una "familia tipo de 4 personas (2 adultos y 2 chicos)". Los datos reales van en `mi-plan/`, que está en `.gitignore`. El repo solo trae la plantilla de `plantillas/`.
4. **Offline-first.** Markdown plano, enlaces relativos, sin JavaScript, sin CDN, sin imágenes remotas.
5. **Honestidad sobre el escenario.** Sin alarmismo. La nota que aclara que las guías oficiales hablan de 3 a 10 días aparece una sola vez en el README y en `10-modo-largo-plazo.md`.
6. **Tono.** Español rioplatense con voseo, registro neutral y profesional. Sin coloquialismos, sin emojis, frases cortas.
7. **Aviso.** La guía no reemplaza a las autoridades ni el consejo médico. Las cantidades de comida son orientativas.
8. **Sin precios ni marcas** (salvo las instituciones citadas como fuente). No copiar texto literal de las fuentes: parafrasear y citar el ID. Sin dependencias externas: solo biblioteca estándar de Python.

## Convenciones

- Cada `.md` de contenido (raíz y `checklists/`) empieza con este frontmatter:

  ```
  ---
  titulo: Agua
  ultima_revision: 2026-11-02
  estado: borrador
  confianza: mixta
  fuentes: [S02, S01]
  ---
  ```

  `confianza`: `verificada` (todo con fuente), `mixta` (fuentes y estimaciones) o `editorial`.
- Cada archivo de contenido termina con `## Fuentes`, con los IDs usados y su título.
- Enlaces internos relativos: `[Agua](01-agua.md)`.
- Tablas para teléfonos, métodos y cantidades. Casillas `- [ ]` para checklists.
- Máximo de unas 300 líneas por archivo.
- Fuentes nuevas: agregá la fila a [fuentes.md](fuentes.md) con estado y fecha de consulta.
- Cambios: actualizá `ultima_revision` y anotá en [CHANGELOG.md](CHANGELOG.md).
- Commits en español, estilo Conventional Commits: `docs(agua): agrega métodos de potabilización`.

## Validación

Antes de cada commit:

```sh
python3 scripts/validar.py
```

Controla frontmatter, enlaces relativos, IDs de fuentes (en los dos sentidos), emojis y caracteres de control, correspondencia de los `PENDIENTE` con [PENDIENTES.md](PENDIENTES.md) y que `mi-plan/` esté en `.gitignore`. Sale con código 1 si hay errores.

Calculadora:

```sh
python3 calculadoras/calcular.py --personas 4 --dias 3
```

Casos de prueba que debe reproducir: 4 personas y 3 días, 36 L y 2 bidones; 4 y 7, 84 L y 5 bidones; 2 y 7, 42 L y 3 bidones.
