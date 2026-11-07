---
title: Ligne de commande
description: Utilisez l'interface en ligne de commande de PlaidCloud pour automatiser des tâches, exécuter des scripts et interagir avec les ressources PlaidCloud depuis un terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud dispose d'une API REST utilisable par toute application capable d'envoyer des requêtes HTTP. Pour simplifier les choses, le package Python `plaidcloud-rpc` gère pour vous les détails de connexion et de requête.

:::caution[JSON-RPC est obsolète]
JSON-RPC est obsolète et sera supprimé dans une publication ultérieure. Utilisez `plaidcloud-rpc` 1.25.0 ou ultérieure, qui envoie vos appels à l'API REST, et développez les nouvelles intégrations avec l'API REST. Consultez [JSON-RPC est obsolète](#json-rpc-est-obsolète).
:::


## Installation requise

Depuis un terminal, exécutez la commande suivante :

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Utiliser l'objet SimpleRPC pour envoyer une requête

Pour effectuer une requête avec le package `plaidcloud-rpc`, utilisez l'objet `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Une fois l'objet `SimpleRPC` instancié, vous pouvez envoyer des requêtes à PlaidCloud. Cet exemple demande les métadonnées d'une table.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` envoie chaque appel à l'API REST sous `/rest/v1/` sur l'hôte de votre espace de travail, avec le même jeton. Un appel que l'API REST ne couvre pas encore, ou un appel vers un espace de travail encore sur une publication antérieure, utilise JSON-RPC à la place : le même code fonctionne donc dans les deux cas. Un appel en échec lève `RPCError` dans les deux cas.


## Appeler directement l'API REST

`call_rest` envoie une requête à n'importe quel point de terminaison de l'API REST avec le même jeton, les mêmes paramètres TLS et les mêmes nouvelles tentatives que `SimpleRPC`. Indiquez la méthode HTTP, le chemin sous `/rest/v1/` et, si besoin, `params` pour la chaîne de requête et `body` pour un corps de requête JSON.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Il renvoie la réponse JSON décodée, ou `None` lorsque la réponse n'a pas de corps. Toute réponse autre qu'un succès lève `RPCError`, avec le statut HTTP comme `code`.


## JSON-RPC est obsolète

JSON-RPC est obsolète et sera supprimé dans une publication ultérieure. Les versions de `plaidcloud-rpc` antérieures à 1.25.0 envoient tous leurs appels via JSON-RPC et cesseront donc de fonctionner lors de sa suppression. Passez à la version 1.25.0 ou ultérieure ; votre code `SimpleRPC` n'a pas besoin d'être modifié. Développez les nouvelles intégrations avec l'API REST.


## Quelles API sont disponibles ?

De nombreuses API permettent de contrôler presque tous les aspects de PlaidCloud. La référence interactive de l'API est servie par tenant, dans chaque espace de travail PlaidCloud : ouvrez votre espace de travail et accédez au menu de documentation de l'API pour consulter le catalogue des points de terminaison en direct.


## Obtenir un jeton OAuth

Consultez [Configuration d'OAuth](/fr/reference/cli/jupyter/oauth-setup/) pour savoir comment obtenir un jeton OAuth et configurer le système pour l'authentification automatisée.
