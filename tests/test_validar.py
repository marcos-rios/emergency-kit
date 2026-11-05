"""Casos que antes podían pasar sin bibliografía coherente."""
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from scripts import validar


class ValidadorTest(unittest.TestCase):
    def texto(self, cuerpo, lista='S01', bibliografia='S01'):
        return ('---\ntitulo: Prueba\nultima_revision: 2026-11-05\nestado: borrador\n'
                f'confianza: mixta\nfuentes: [{lista}]\n---\n\n# Prueba\n{cuerpo}\n'
                f'## Fuentes\n\n- {bibliografia}: Título.\n')

    def revisar(self, texto):
        reporte = validar.Reporte()
        validar.validar_frontmatter(validar.RAIZ / 'prueba.md', texto, {'S01', 'S02'}, reporte)
        return reporte.errores

    def test_fuente_solo_en_bibliografia_no_cuenta_como_uso(self):
        self.assertTrue(self.revisar(self.texto('Texto editorial.')))

    def test_cita_del_cuerpo_debe_estar_en_frontmatter_y_bibliografia(self):
        self.assertTrue(self.revisar(self.texto('Dato [S02].')))
        self.assertFalse(self.revisar(self.texto('Dato [S01].')))

    def test_fuentes_debe_ser_la_ultima_seccion(self):
        self.assertTrue(self.revisar(self.texto('Dato [S01].') + '\n## Otra sección\nTexto.'))

    def test_telefono_no_es_un_archivo_relativo(self):
        reporte = validar.Reporte()
        validar.validar_enlaces(Path('prueba.md'), '[Teléfono](tel:+540000000000)', reporte)
        self.assertEqual(reporte.errores, [])

    def test_no_se_puede_marcar_pendiente_un_asunto_cerrado(self):
        with tempfile.TemporaryDirectory() as carpeta:
            raiz = Path(carpeta)
            (raiz / 'PENDIENTES.md').write_text('- [x] **P01.** Agua segura verificada.\n')
            contenido = raiz / 'agua.md'
            contenido.write_text('> **PENDIENTE:** agua segura por verificar, P01.\n')
            reporte = validar.Reporte()
            with patch.object(validar, 'RAIZ', raiz):
                validar.validar_pendientes([contenido], reporte)
            self.assertTrue(any('ya está cerrado' in error for error in reporte.errores))


if __name__ == '__main__':
    unittest.main()
