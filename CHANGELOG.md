# Changelog

Todos los cambios relevantes de esta guía se registran en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el proyecto usa [versionado semántico](https://semver.org/lang/es/).

## [Sin publicar]

## [0.1.0] - 2026-11-02

### Agregado

- Estructura inicial del repositorio.
- Contenido en borrador: agua, comida, energía y cocina, saneamiento, salud, comunicación, seguridad y vecinos, evacuación, Argentina, modo largo plazo y compras.
- Checklists de 72 horas, 30 días, mochila y auto.
- Calculadora de cantidades (`calculadoras/calcular.py`) y tablas CSV.
- Plantilla del plan familiar (`plantillas/mi-plan.md`); el plan real vive en `mi-plan/`, ignorado por git.
- Script de validación (`scripts/validar.py`).
- Fuentes S01 a S28 y lista de pendientes P01 a P13.

### Verificación de fuentes

El agente abrió las 28 URLs el 2026-11-02. Resultado en [fuentes.md](fuentes.md):

- ok: S03, S05, S06, S08, S10, S11, S13, S15, S16, S19, S20, S25, S26, S28.
- ok, con observaciones: S01, S02, S04, S09, S12, S14, S18, S21, S24, S27.
- no accesible: S07 (HTTP 402), S17 (HTTP 429), S22 (HTTP 403).
- contenido distinto: S23 (página en sueco; la edición en inglés está en otra ruta).

Diferencias con el material de partida, registradas sin reemplazarlas en silencio:

- Dosis de lavandina del CDC en español: "1 cuarto de litro" frente a 8 gotas por galón. Se mantiene 2 gotas por litro y se abre P11.
- Fecha de la campaña británica: 22 de octubre (S26) frente a 23 de octubre (S27). Se abre P12.
- Garrafas (S12): la ubicación exterior y alejada de aberturas es para el cilindro de 45 kg; para las garrafas de 10 y 15 kg el folleto pide un lugar ventilado. El contenido distingue los dos casos.
- Contención del fuego (S09): la fuente menciona piedras o un tambor de metal, no ladrillos. Se quitaron los ladrillos.
- Teléfono 103 (S04): se incluyó solo la descripción que aparece en la página.
- Primeros auxilios: el enlace del Ministerio de Salud se cita como S25 (la página que corresponde), enlazada desde S04.
