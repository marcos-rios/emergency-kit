#!/usr/bin/env python3
"""Valida la estructura y las convenciones de la guía.

Uso:
    python3 scripts/validar.py

Sale con código 1 si encuentra errores. Solo usa la biblioteca estándar.
"""

import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Archivos de la raíz que no son de contenido y no llevan frontmatter.
META = {"AGENTS.md", "CHANGELOG.md", "PENDIENTES.md", "fuentes.md"}
EXCLUIR_DIRS = {".git", "mi-plan", "dist", "__pycache__"}

CLAVES_FRONTMATTER = ["titulo", "ultima_revision", "estado", "confianza", "fuentes"]
CONFIANZAS = {"verificada", "mixta", "editorial"}
MAX_LINEAS = 300

RE_ID_FUENTE = re.compile(r"\bS\d\d\b")
RE_FILA_FUENTE = re.compile(r"^\|\s*(S\d\d)\s*\|", re.MULTILINE)
RE_ENLACE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
RE_IMAGEN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
RE_PENDIENTE = re.compile(r"^>\s*\*\*PENDIENTE:\*\*(.*)$", re.MULTILINE)
RE_ID_PENDIENTE = re.compile(r"\bP\d\d\b")
RE_ENTRADA_PENDIENTE = re.compile(r"^- \[[ xX]\] \*\*(P\d\d)\.\*\*(.*)$", re.MULTILINE)
RE_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Rangos de emojis y pictogramas habituales.
RANGOS_EMOJI = [
    (0x1F000, 0x1FAFF),
    (0x2600, 0x27BF),
    (0x2B00, 0x2BFF),
    (0x231A, 0x231B),
    (0x23E9, 0x23FA),
    (0xFE0F, 0xFE0F),
    (0x200D, 0x200D),
]

PALABRAS_VACIAS = {
    "de", "la", "el", "en", "y", "a", "los", "las", "del", "que", "por", "con",
    "no", "se", "un", "una", "o", "para", "al", "es", "lo", "ver", "falta",
    "verificar", "pendiente", "pendientes", "sin",
}


class Reporte:
    def __init__(self):
        self.errores = []
        self.avisos = []

    def error(self, archivo, mensaje):
        self.errores.append(f"ERROR   {archivo}: {mensaje}")

    def aviso(self, archivo, mensaje):
        self.avisos.append(f"AVISO   {archivo}: {mensaje}")


def rel(ruta):
    return ruta.relative_to(RAIZ).as_posix()


def todos_los_md():
    archivos = []
    for ruta in sorted(RAIZ.rglob("*.md")):
        partes = set(ruta.relative_to(RAIZ).parts[:-1])
        if partes & EXCLUIR_DIRS:
            continue
        archivos.append(ruta)
    return archivos


def archivos_de_contenido():
    raiz = [p for p in sorted(RAIZ.glob("*.md")) if p.name not in META]
    checklists = sorted((RAIZ / "checklists").glob("*.md"))
    return raiz + checklists


def leer(ruta):
    return ruta.read_text(encoding="utf-8")


def parsear_frontmatter(texto):
    lineas = texto.split("\n")
    if not lineas or lineas[0].strip() != "---":
        return None
    datos = {}
    for linea in lineas[1:]:
        if linea.strip() == "---":
            return datos
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip()
    return None


def sin_bloques_de_codigo(texto):
    return re.sub(r"```.*?```", "", texto, flags=re.DOTALL)


def validar_frontmatter(ruta, texto, ids_fuentes, reporte):
    datos = parsear_frontmatter(texto)
    if datos is None:
        reporte.error(rel(ruta), "falta el frontmatter entre líneas '---'")
        return
    for clave in CLAVES_FRONTMATTER:
        if clave not in datos:
            reporte.error(rel(ruta), f"falta la clave '{clave}' en el frontmatter")
    if "ultima_revision" in datos and not RE_FECHA.match(datos["ultima_revision"]):
        reporte.error(rel(ruta), "ultima_revision no tiene formato AAAA-MM-DD")
    if "confianza" in datos and datos["confianza"] not in CONFIANZAS:
        reporte.error(rel(ruta), f"confianza inválida: '{datos['confianza']}'")
    if "fuentes" in datos:
        valor = datos["fuentes"]
        if not (valor.startswith("[") and valor.endswith("]")):
            reporte.error(rel(ruta), "fuentes debe ser una lista entre corchetes")
        for id_fuente in RE_ID_FUENTE.findall(valor):
            if id_fuente not in ids_fuentes:
                reporte.error(rel(ruta), f"el frontmatter cita {id_fuente}, que no está en fuentes.md")
    if "\n## Fuentes" not in texto:
        reporte.error(rel(ruta), "falta la sección '## Fuentes'")


def validar_enlaces(ruta, texto, reporte):
    texto = sin_bloques_de_codigo(texto)
    for destino in RE_IMAGEN.findall(texto):
        if re.match(r"^[a-z]+://", destino):
            reporte.error(rel(ruta), f"imagen remota no permitida: {destino}")
    for destino in RE_ENLACE.findall(texto):
        if re.match(r"^(https?|mailto):", destino) or destino.startswith("#"):
            continue
        objetivo = destino.split("#", 1)[0]
        if not objetivo:
            continue
        if not (ruta.parent / objetivo).resolve().exists():
            reporte.error(rel(ruta), f"enlace roto: {destino}")


def validar_caracteres(ruta, texto, reporte):
    for numero, linea in enumerate(texto.split("\n"), start=1):
        for caracter in linea:
            codigo = ord(caracter)
            if caracter != "\t" and unicodedata.category(caracter) == "Cc":
                reporte.error(rel(ruta), f"línea {numero}: carácter de control U+{codigo:04X}")
            elif any(desde <= codigo <= hasta for desde, hasta in RANGOS_EMOJI):
                reporte.error(rel(ruta), f"línea {numero}: emoji o pictograma U+{codigo:04X}")


def palabras(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return {p for p in re.findall(r"[a-z0-9]+", texto) if len(p) > 2 and p not in PALABRAS_VACIAS}


def validar_pendientes(contenido, reporte):
    ruta_pendientes = RAIZ / "PENDIENTES.md"
    if not ruta_pendientes.exists():
        reporte.error("PENDIENTES.md", "no existe")
        return
    entradas = {pid: texto for pid, texto in RE_ENTRADA_PENDIENTE.findall(leer(ruta_pendientes))}
    if not entradas:
        reporte.error("PENDIENTES.md", "no tiene entradas con formato '- [ ] **P01.** ...'")
        return

    referenciados = set()
    total = 0
    for ruta in contenido:
        for texto in RE_PENDIENTE.findall(leer(ruta)):
            total += 1
            ids = RE_ID_PENDIENTE.findall(texto)
            if not ids:
                reporte.error(rel(ruta), f"PENDIENTE sin referencia a PENDIENTES.md (P01, P02...): {texto.strip()[:60]}")
                continue
            for pid in ids:
                if pid not in entradas:
                    reporte.error(rel(ruta), f"PENDIENTE cita {pid}, que no está en PENDIENTES.md")
                    continue
                referenciados.add(pid)
                comunes = palabras(texto) & palabras(entradas[pid])
                if len(comunes) < 2:
                    reporte.aviso(rel(ruta), f"el texto del PENDIENTE no se parece a la entrada {pid}")
    if total > len(entradas):
        reporte.error("PENDIENTES.md", f"hay {total} PENDIENTE en el contenido y solo {len(entradas)} entradas")


def validar_fuentes(archivos, reporte):
    ruta_fuentes = RAIZ / "fuentes.md"
    if not ruta_fuentes.exists():
        reporte.error("fuentes.md", "no existe")
        return set()
    ids_fuentes = set(RE_FILA_FUENTE.findall(leer(ruta_fuentes)))
    citados = set()
    for ruta in archivos:
        if ruta.name == "fuentes.md" and ruta.parent == RAIZ:
            continue
        es_meta = ruta.parent == RAIZ and ruta.name in META
        for id_fuente in RE_ID_FUENTE.findall(leer(ruta)):
            if id_fuente not in ids_fuentes:
                reporte.error(rel(ruta), f"cita {id_fuente}, que no está en fuentes.md")
            elif not es_meta:
                citados.add(id_fuente)
    # Las menciones en archivos de gestión (PENDIENTES, CHANGELOG) no cuentan como uso.
    for id_fuente in sorted(ids_fuentes - citados):
        reporte.error("fuentes.md", f"{id_fuente} no se cita en ningún archivo de contenido")
    return ids_fuentes


def validar_gitignore(reporte):
    ruta = RAIZ / ".gitignore"
    if not ruta.exists():
        reporte.error(".gitignore", "no existe")
        return
    lineas = {l.strip() for l in leer(ruta).splitlines()}
    if not lineas & {"mi-plan/", "mi-plan", "/mi-plan/", "/mi-plan"}:
        reporte.error(".gitignore", "no ignora mi-plan/")


def main():
    reporte = Reporte()
    archivos = todos_los_md()
    contenido = archivos_de_contenido()

    ids_fuentes = validar_fuentes(archivos, reporte)
    for ruta in contenido:
        texto = leer(ruta)
        validar_frontmatter(ruta, texto, ids_fuentes, reporte)
        if texto.count("\n") > MAX_LINEAS:
            reporte.aviso(rel(ruta), f"supera las {MAX_LINEAS} líneas")
    for ruta in archivos:
        texto = leer(ruta)
        validar_enlaces(ruta, texto, reporte)
        validar_caracteres(ruta, texto, reporte)
    validar_pendientes(contenido, reporte)
    validar_gitignore(reporte)

    for linea in reporte.avisos + reporte.errores:
        print(linea)
    print()
    print(f"Archivos Markdown revisados: {len(archivos)} ({len(contenido)} de contenido)")
    print(f"Fuentes registradas: {len(ids_fuentes)}")
    print(f"Avisos: {len(reporte.avisos)}")
    print(f"Errores: {len(reporte.errores)}")
    return 1 if reporte.errores else 0


if __name__ == "__main__":
    sys.exit(main())
