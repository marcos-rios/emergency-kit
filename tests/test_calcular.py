"""Regresiones de cantidades y consistencia de la salida pública."""
import contextlib
import io
import unittest

from calculadoras import calcular as calc


class CalculadoraTest(unittest.TestCase):
    def test_casos_documentados(self):
        for personas, dias, litros, bidones in [(4, 3, 36, 2), (4, 7, 84, 5), (2, 7, 42, 3)]:
            with self.subTest(personas=personas, dias=dias):
                filas = {f['item']: f['cantidad'] for f in calc.calcular(personas, dias)}
                self.assertEqual(filas['Agua potable'], str(litros))
                self.assertEqual(filas['Bidones de 20 L'], str(bidones))

    def test_un_dia_no_recibe_la_reserva_entera_de_tres(self):
        for dias, latas_por_fila in [(1, '2'), (2, '4')]:
            with self.subTest(dias=dias):
                filas = {f['item']: f['cantidad'] for f in calc.calcular(4, dias)}
                self.assertEqual(filas['Atún caballa o sardinas en lata'], latas_por_fila)
                self.assertEqual(filas['Legumbres choclo o arvejas en lata'], latas_por_fila)

    def test_resumen_incluye_redondeos_de_cada_fila(self):
        for personas, dias, latas in [(1, 1, 2), (1, 3, 4), (3, 7, 22)]:
            with self.subTest(personas=personas, dias=dias):
                salida = io.StringIO()
                with contextlib.redirect_stdout(salida):
                    self.assertEqual(calc.main(['--personas', str(personas), '--dias', str(dias)]), 0)
                self.assertIn(f'Latas en total: {latas} ', salida.getvalue())
                self.assertIn('higiene y otros usos', salida.getvalue())

    def test_cli_rechaza_cantidades_no_positivas(self):
        for opcion in ['--personas', '--dias']:
            args = ['--personas', '4', '--dias', '3']
            args[args.index(opcion) + 1] = '0'
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                calc.main(args)
            self.assertEqual(error.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
