from django.test import TestCase
from rest_framework.test import APIClient


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.recipe_data = {
            "name": "Brigadeiro de Champanhe",
            "description": "É um brigadeiro gourmet",
            "instructions": "Junte espumante ao chocolate branco e deixe ferver",
            "tags": [
                {"name": "doce"},
                {"name": "gourmet"}
            ],
            "ingredient_set": [
                {
                    "name": "chocolate branco",
                    "unit": "g",
                    "amount": 300
                },
                {
                    "name": "espumante",
                    "unit": "mL",
                    "amount": 100
                }
            ]
        }

        self.recipe_data_2 = {
            "name": "Pudim",
            "description": "Sobremesa simples e deliciosa",
            "instructions": "Bata bem os ovos no liquidificador. Acrescente o leite condensado e o leite. Bata novamente. Asse em forno médio por 45 minutos, deixe esfriar e desenforme.",
            "tags": [
                {
                    "name": "doce"
                },
                {
                    "name": "fácil"
                }
            ],
            "ingredient_set": [
                {
                    "name": "leite condensado",
                    "unit": "lata",
                    "amount": 1
                },
                {
                    "name": "leite",
                    "unit": "lata",
                    "amount": 1
                },
                {
                    "name": "ovos",
                    "unit": "unidade",
                    "amount": 3
                }
            ]
        }

    def test_recipe_post(self):
        get_response = self.client.get('/recipes/')
        self.assertEqual(get_response.data, [])

        post_response = self.client.post(
            '/recipes/', self.recipe_data, format='json')

        self.assertDictContainsSubset({'id': 1}, post_response.json())
        self.assertDictContainsSubset(self.recipe_data, post_response.json())
        self.assertEqual(post_response.status_code, 201)

    def test_get_all_recipes(self):
        empty_response = self.client.get('/recipes/')
        self.assertEqual(empty_response.data, [])

        not_found_response = self.client.get('/recipes/1/')
        self.assertEqual(not_found_response.status_code, 404)

        post_response = self.client.post(
            '/recipes/', self.recipe_data, format='json')

        self.assertDictContainsSubset({'id': 1}, post_response.json())
        self.assertDictContainsSubset(self.recipe_data, post_response.json())
        self.assertEqual(post_response.status_code, 201)

        post_response = self.client.post(
            '/recipes/', self.recipe_data, format='json')

    def test_filter_recipes(self):
        post_response = self.client.post(
            '/recipes/', self.recipe_data, format='json')

        post_response_2 = self.client.post(
            '/recipes/', self.recipe_data_2, format='json')

        self.assertDictContainsSubset({'id': 2}, post_response_2.json())
        self.assertDictContainsSubset(
            self.recipe_data_2, post_response_2.json())
        self.assertEqual(post_response_2.status_code, 201)

        get_response = self.client.get('/recipes/2/')
        self.assertDictEqual(get_response.data, post_response_2.data)

        get_all_response = self.client.get('/recipes/')
        self.assertEqual(len(get_all_response.data), 2)

    def test_delete_recipe(self):
        post_response = self.client.post(
            '/recipes/', self.recipe_data, format='json')

        self.assertDictContainsSubset({'id': 1}, post_response.json())
        self.assertDictContainsSubset(self.recipe_data, post_response.json())
        self.assertEqual(post_response.status_code, 201)

        get_response = self.client.get('/recipes/1/')
        self.assertDictEqual(get_response.data, post_response.data)

        delete_response = self.client.delete('/recipes/1/')
        self.assertEqual(delete_response.status_code, 204)

        get_response = self.client.get('/recipes/1/')
        self.assertEqual(get_response.status_code, 404)
