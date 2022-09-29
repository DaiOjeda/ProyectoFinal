from django.test import TestCase
from django.urls import reverse

from AppCommunity.models import Grupo

class GrupoTestCase(TestCase):
    def SetUp(self):
        Grupo.objects.create(camada=15, nombre_lider="Daiana", apellido_lider="Ojeda")
        Grupo.objects.create(camada=16, nombre_lider="Lucas", apellido_lider="Garcia")

    def test_prueba(self):
        g1 = Grupo.objects.get(camada=15)
        g2 = Grupo.objects.get(camada=16)
        self.assertEqual(g1.nombre_lider, "Daiana")
        self.assertEqual(g2.nombre_lider, "Lucas")

class ViewTests(TestCase):
    def test_inicio(self):
        response = self.client.get(reverse('AppCommunityInicio'))
        self.assertEqual(response.status_code, 100)
        self.assertEqual(response, "No hay nada para mostrar")

