---
titulo: Revisión integral de la guía
ultima_revision: 2026-11-05
estado: borrador
confianza: mixta
fuentes: [S01, S03, S07, S08, S09, S10, S11, S17, S22, S23, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S43, S44, S45, S46, S47, S48, S51, S53, S56]
---

# Revisión integral de la guía

Fecha de corte: 2026-11-05. Se revisó todo el contenido público, las checklists, la plantilla, las tablas, la calculadora, el validador y el registro de fuentes. También se preparó una adaptación privada sin incorporarla al repositorio.

Este informe documenta un repaso editorial y técnico reproducible. No certifica instalaciones, potabilidad, adecuación nutricional ni funcionamiento de servicios de emergencia. La guía sigue en borrador.

## Resultado y prioridades

| Prioridad editorial | Hallazgo | Tratamiento |
|---|---|---|
| Inmediata | «Afuera o con ventilación» podía habilitar combustión peligrosa en interiores | Generadores solo al exterior; nunca en garaje abierto. Se distinguen de artefactos domésticos instalados correctamente [S41, S08]. |
| Inmediata | Dosis de lavandina publicada con una contradicción de traducción sin resolver | Se leyó el CDC en inglés y se priorizó etiqueta, aptitud y pauta sanitaria argentina [S39, S40, S51]. |
| Inmediata | Indicación general de desconectar y mover una garrafa con pérdida | Se retiró. Ante olor fuerte se prioriza evacuar, evitar chispas y pedir asistencia [S46]. |
| Inmediata | Agacharse al aire libre presentado como protección ante rayos | Se retiró; se prioriza refugio cerrado. La discrepancia oficial queda abierta en P15 [S44, S45]. |
| Alta | Distancia a una fuente de agua tratada como criterio suficiente para una letrina | Se retiró el procedimiento doméstico urbano. La fuente extranjera tampoco lo autoriza y exige otras condiciones [S10]. |
| Alta | Reserva de agua tratada como suficiente también para higiene | Se corrigió el alcance de la base y se separaron otros consumos [S30, S31]. |
| Alta | Canasta energética y suplementos podían leerse como dieta suficiente | Se conserva solo el ejemplo aritmético, sin validación nutricional. Se retira la compra rutinaria de suplementos (`RECOMENDACIÓN EDITORIAL`; P08). |
| Alta | Resumen de latas distinto de la suma de la tabla | Ahora suma filas ya redondeadas; se agregaron casos de regresión [S56]. |

## Qué se considera correcto y con qué límites

| Tema | Evaluación |
|---|---|
| Agua: base de cálculo | La pauta japonesa incluye bebida y comidas; no todo el consumo de higiene. Las cuentas para la familia tipo son reproducibles [S31, S56]. |
| Agua: tratamientos | Clarificar antes del tratamiento, hervir, proteger el almacenamiento y distinguir contaminación química están respaldados. Se incorpora el carácter absoluto del tamaño de poro [S39, S48]. |
| Comida: cadena de frío | Se mantienen los límites con equipos cerrados: heladera hasta 4 horas, freezer lleno 48 horas y medio lleno 24 horas. No son garantías para un equipo abierto o alimentos ya calentados [S03]. |
| Monóxido | La descripción y los síntomas enumerados coinciden con CPSC; se conservan sin diagnosticar a una persona [S11]. |
| Saneamiento temporal | Recipiente estable, bolsas gruesas, absorbente, tapa, lavado de manos y resguardo de residuos tienen respaldo. La disposición final requiere autorización local [S10]. |
| Salud | Reserva de medicación acordada con profesionales, material básico de botiquín y adaptación por necesidades individuales cuentan con referencias primarias [S38, S53]. |
| Plan familiar | Asignar tareas, reconocer riesgos, acordar encuentros y practicar la salida coincide con SINAGIR [S37]. |
| Comunicación | Radio y contactos en papel se mantienen como opciones. Ningún canal se promete disponible durante una crisis (`RECOMENDACIÓN EDITORIAL`). |
| Contexto internacional | Se contrastan los países e instituciones incluidos con sus documentos, sin presentar una advertencia mundial simultánea [S29, S30, S31, S32, S33, S34, S35, S36, S38]. |
| Privacidad y formato | Se conserva Markdown sin recursos remotos necesarios para leerlo. La copia privada queda ignorada y la plantilla pública no contiene información real (`RECOMENDACIÓN EDITORIAL`; controles documentales en [S56]). |

## Repaso por archivo

Las decisiones de alcance y prioridad de esta tabla son `RECOMENDACIÓN EDITORIAL`. Las fuentes de cada corrección están en el capítulo enlazado y en las tablas anteriores.

| Archivo o grupo | Diagnóstico y cambio realizado | Qué falta |
|---|---|---|
| [README](README.md) | Contexto actualizado; diferencia recomendaciones oficiales y antecedentes periodísticos; precaución al cortar servicios | Conteo internacional P14 y fuentes inaccesibles P13 |
| [Agua](01-agua.md) | Corrige alcance del volumen, etiqueta local, hervido, poro absoluto y mantenimiento del tanque | Dimensionamiento real de la vivienda P17 |
| [Comida](02-comida.md) | Conserva cadena de frío; agrega límites del orden de consumo, dieta y selección de productos | Nutrición y validación de canastas P08 |
| [Energía y cocina](03-energia-y-cocina.md) | Separa tipos de combustión, retira traslado de envases con pérdida y promesas de autonomía | Normativa local GLP P01; dimensionamiento P17 |
| [Saneamiento](04-saneamiento.md) | Mantiene opción temporal; retira letrina urbana y criterio de distancia aislado | Disposición local de residuos P04 |
| [Salud](05-salud.md) | Usa botiquín oficial, evita compra genérica de medicamentos y agrega contingencia para frío/energía | Necesidades individuales, solo en el plan privado |
| [Comunicación](06-comunicacion.md) | Corrige actualización periódica de antecedentes y evita garantía de canales | Handies P02; servicio satelital P03 |
| [Seguridad y vecinos](07-seguridad-y-vecinos.md) | Mantiene privacidad y cooperación; retira afirmación de eficacia absoluta y rondas de barrio | Adecuar red de ayuda sin exponer a las personas |
| [Evacuación](08-evacuacion.md) | Condiciona cortes a seguridad; diferencia carga transportable y reserva de casa | Ruta, destino y accesibilidad P16/P17 |
| [Argentina](09-argentina.md) | Reemplaza dependencia de comunicados históricos por páginas generales; revisa teléfonos y rayos | Confirmación municipal P16 y discrepancia P15 |
| [Modo largo plazo](10-modo-largo-plazo.md) | Mantiene carácter opcional; tanque como hipótesis, dieta sin validación y sin suplementos universales | Nutrición P08 y condiciones reales P17 |
| [Compras](compras.md) | Corrige prestaciones de filtros, lavandina y criterio de energía; sin promesa de autonomía | Priorizar según inventario privado |
| [Checklist de 72 horas](checklists/72-horas.md) | Alinea agua, cocina exterior, medicación y operación segura de servicios | Inventario y capacidades reales |
| [Checklist de 30 días](checklists/30-dias.md) | Corrige tanque, filtros, suplementos y letrina | No usar como dieta completa: P08 |
| [Mochila](checklists/mochila.md) | Refuerza reparto y prueba de la carga, separada de la reserva de casa | Probarla según capacidades de cada integrante |
| [Auto](checklists/auto.md) | Conserva kit y rutas; elimina la excepción implícita del garaje abierto | Solo aplica si se dispone de vehículo |
| [Calculadoras](calculadoras/README.md) y CSV | Aclaran hipótesis, higiene aparte y límites nutricionales; se retira compra genérica de analgésicos | Validación nutricional P08 |
| [Calculadora](calculadoras/calcular.py) | Corrige escala para períodos cortos y resumen de latas | No dimensiona higiene, energía ni dietas |
| [Validador](scripts/validar.py) | Agrega coherencia de IDs por cuerpo/frontmatter/bibliografía, sección final, enlaces telefónicos y pendientes cerrados | No verifica verdad sanitaria, legal ni actualidad de enlaces externos |
| [Plantilla](plantillas/mi-plan.md) | Agrega datos de agua y energía, y límites de operación de servicios | Completar solo la copia privada |
| [Fuentes](fuentes.md), [pendientes](PENDIENTES.md) e [historial](CHANGELOG.md) | Registran consultas nuevas, cierres parciales y problemas abiertos | Reconsulta y revisión periódica |

## Cambios de contexto confirmados

- El comunicado británico está fechado el 22 de octubre de 2026 y aclara la continuidad de consejos previos [S29].
- Japón publicó su pedido nacional y puso en marcha la agencia el 2 de noviembre de 2026 [S31, S32].
- Se incorpora la estrategia europea presentada el 26 de marzo de 2025, con objetivo de pautas para al menos 72 horas de autosuficiencia [S33].
- Alemania, Suecia y Noruega se describen desde BBK, MCF y DSB, sin depender del resumen periodístico inicial [S34, S35, S36].
- La reserva de 2 semanas en casa se atribuye a la Cruz Roja Americana, sin convertirla en recomendación federal estadounidense [S38].

## Preguntas resueltas y asuntos abiertos

| ID | Estado después del repaso |
|---|---|
| P01 | Abierto: orientación oficial sobre formatos no reemplaza los límites municipales de almacenamiento [S47]. |
| P02 | Abierto: no se publican frecuencias supuestamente libres sin verificar normativa de ENACOM. |
| P03 | Abierto: no se presume disponibilidad de mensajería satelital en un celular concreto. |
| P04 | Abierto: disposición sanitaria municipal pendiente; no hay receta de letrina urbana [S10]. |
| P05 | Cerrado para la dependencia de los comunicados históricos; se usan páginas generales. Rayos continúa en P15 [S43, S44]. |
| P06 | Parcial: Berlín leído; falta completar los folletos S22 y S23. No se equipara acceso con lectura. |
| P07 | Cerrado mediante pauta local y etiqueta del producto; no se define concentración universal [S40, S51]. |
| P08 | Abierto: sin validación nutricional ni fuente confirmada de kcal por unidad. |
| P09 | Abierto por decisión del titular: licencia pendiente. |
| P10 | Abierto: revisión periódica y actualización anticipada ante cambios. |
| P11 | Cerrado: contraste del CDC en inglés permite identificar el error de traducción [S39]. |
| P12 | Cerrado: fecha británica respaldada por el comunicado oficial [S29]. |
| P13 | Abierto: acceso fallido o cuerpo no recuperado en S01, S07, S09 y S17. |
| P14 | Abierto: conteo de países sin lista oficial trazable confirmada. |
| P15 | Abierto: discrepancia entre SINAGIR y NWS documentada [S44, S45]. |
| P16 | Abierto: canales municipales, sitios de evacuación y accesibilidad. |
| P17 | Abierto: volumen utilizable de agua, energía y necesidades particulares. Solo se completa en privado. |

## Fuentes

- S01: Ready.gov: Build a Kit.
- S03: CDC: desechar alimentos después de un apagón.
- S07: Servicio Meteorológico Nacional: alertas.
- S08: Gobierno de Mendoza: estufas, garrafas, salamandras y braseros.
- S09: Texas A&M AgriLife: cocinar cuando se corta la luz.
- S10: King County: cómo armar un inodoro de emergencia.
- S11: CPSC: calefactores portátiles y equipo de camping.
- S17: The New York Sun: 33 países piden acopiar suministros.
- S22: Cruz Roja Americana: guía de preparación (PDF, español).
- S23: Suecia (MCF): «If crisis or war comes», edición en inglés.
- S29: Cabinet Office: publicación de Be Ready.
- S30: Reino Unido: checklist Be Ready.
- S31: Japón: pedido de preparación preventiva.
- S32: Japón: puesta en marcha de la agencia de gestión de desastres.
- S33: Comisión Europea: Preparedness Union Strategy.
- S34: BBK: Stockpiling.
- S35: MCF: Home preparedness.
- S36: DSB: preguntas frecuentes de preparación doméstica.
- S37: SINAGIR: Plan Familiar de Emergencias.
- S38: Cruz Roja Americana: Survival Kit Supplies.
- S39: CDC: How to Make Water Safe in an Emergency.
- S40: ANMAT: Agua segura y salud.
- S41: CPSC: Generators and Engine-Driven Tools.
- S43: SINAGIR: qué hacer en caso de lluvias intensas.
- S44: SINAGIR: qué hacer en caso de tormentas.
- S45: NWS: Lightning Myths and Facts.
- S46: SINAGIR: qué hacer en caso de fuga de gas.
- S47: Secretaría de Energía: uso responsable de las garrafas.
- S48: CDC: How to Create an Emergency Water Supply.
- S51: SENASA: alimentos y agua ante emergencias y cortes de luz.
- S53: Ministerio de Salud: botiquín de primeros auxilios.
- S56: Pruebas locales de calculadora y validador.
