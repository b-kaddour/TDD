"""
Test de la classe Container
"""

#import
import unittest

#Modification du lien relatif (remonter dans le dossier parent)
import sys
sys.path.append("..")

#importation de la class a tester
from src.container import Container

#Class test qui herite de unittest.TestCase
class TestContainer(unittest.TestCase):
    """
    Méthode de TDD
    """
    #Methode permettant de préparer les données utilisés lors de different test
    def setUp(self):
        #on oublie pas le self. pour le declarer au sein de la class de test
        # type / durability / capacity ml / capacity_max ml /
        self.c = Container("Bouteille", 30, 50, 100)

    def test_container_is_instance(self):
    # def_test_container_is_created(self) similaire

        self.assertIsInstance(self.c, Container)

    def test_durability_after_drink(self):
        # le joueur boit et le contenant doi perdre 1 point de durabilité
        # quantité bu
        temp_durability = self.c.durability
        self.c.drink(25)
        #la durabilité doit baisser
        self.assertEqual(self.c.durability, temp_durability-1)

    def test_durability_after_fill_in(self):
        # le joueur remplit le contenant doi perdre 0.5 point de durabilité
        temp_durability= self.c.durability
        #on souhaite remplir le contenant a son maximum
        temp_fillin=self.c.capacity_max - self.c.capacity
        self.c.fill(temp_fillin)
        self.assertEqual(self.c.durability,temp_durability-0.5)

    def test_is_broken(self):
        #on modifie la durabilié (ou sinon fait un for...)
        self.c.durability = 1
        self.c.drink(25)
        #on verifie que la durabilité est bien a 0 pour moins de 0
        self.assertLessEqual(self.c.durability, 0)


if __name__ == "__main__":
    unittest.main()
