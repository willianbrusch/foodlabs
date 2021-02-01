# RECIPES API

Use this URL as base to requests:

> `http://127.0.0.1:8000/`

## Endpoints:

### POST /recipes/

- don't need authentication

> #### request body:
>
>```
> {
>   "name": "Brigadeiro de Champanhe",
>   "description": "É um brigadeiro  gourmet",
>   "instructions": "Junte espumante ao chocolate branco e deixe ferver",
>   "tags": [
>     {
>       "name": "doce"
>     },
>     {
>       "name": "gourmet"
>     }
>   ],
>   "ingredient_set": [
> 		{
>       "name": "chocolate branco",
>       "unit": "g",
>       "amount": 300
>     },
>     {
>       "name": "espumante",
>       "unit": "mL",
>       "amount": 100
>     }
>   ]
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 2,
>   "name": "Brigadeiro de Champanhe",
>   "description": "É um brigadeiro  gourmet",
>   "instructions": "Junte espumante ao chocolate branco e deixe ferver",
>   "tags": [
>     {
>       "name": "doce"
>     },
>     {
>       "name": "gourmet"
>     }
>   ],
>   "ingredient_set": [
> 		{
>       "name": "chocolate branco",
>       "unit": "g",
>       "amount": 300
>     },
>     {
>       "name": "espumante",
>       "unit": "mL",
>       "amount": 100
>     }
>   ]
> }
>```

### DELETE /recipes/<int:recipe_id>

- don't need authentication

- **If everything goes right:** http status code: 204

> #### no response body

- **If something went wrong:** http status code: 404

> #### no response body

### GET /recipes/

- don't need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
>```
> [
>   {
>     "id": 1,
>     "name": "Brigadeiro de Champanhe",
>     "description": "É um brigadeiro gourmet",
>     "instructions": "Junte espumante ao  chocolate branco e deixe ferver",
>     "tags": [
>       {
>         "name": "doce"
>       },
>       {
>         "name": "gourmet"
>       }
>     ],
>     "ingredient_set": [
>       {
>         "name": "chocolate branco",
>         "unit": "g",
>         "amount": 300
>       },
>       {
>         "name": "espumante",
>         "unit": "mL",
>         "amount": 100
>       }
>     ]
>   },
>   {
>     "id": 2,
>     "name": "Pudim",
>     "description": "Sobremesa simples e > deliciosa",
>     "instructions": "Bata bem os ovos no > liquidificador. Acrescente o leite condensado e o leite. Bata novamente. > Asse em forno médio por 45 minutos, deixe esfriar e desenforme.",
>     "tags": [
>       {
>         "name": "doce"
>       },
>       {
>         "name": "fácil"
>       }
>     ],
>     "ingredient_set": [
>       {
>         "name": "leite condensado",
>         "unit": "lata",
>         "amount": 1
>       },
>       {
>         "name": "leite",
>         "unit": "lata",
>         "amount": 1
>       },
>       {
>         "name": "ovos",
>         "unit": "unidade",
>         "amount": 3
>       }
>     ]
>   }
> ]
>```

### GET /recipes/<int:recipes_id>

- don't need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
>```
> {
>     "id": 2,
>     "name": "Pudim",
>     "description": "Sobremesa simples e deliciosa",
>     "instructions": "Bata bem os ovos no liquidificador. Acrescente o leite condensado e o leite. Bata novamente. Asse em forno médio por 45 minutos, deixe esfriar e desenforme.",
>     "tags": [
>       {
>         "name": "doce"
>       },
>       {
>         "name": "fácil"
>       }
>     ],
>     "ingredient_set": [
>       {
>         "name": "leite condensado",
>         "unit": "lata",
>         "amount": 1
>       },
>       {
>         "name": "leite",
>         "unit": "lata",
>         "amount": 1
>       },
>       {
>         "name": "ovos",
>         "unit": "unidade",
>         "amount": 3
>       }
>     ]
>   }
>```


