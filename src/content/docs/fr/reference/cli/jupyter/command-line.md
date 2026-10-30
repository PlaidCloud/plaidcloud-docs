---
title: Ligne de commande
description: Utilisez l'interface en ligne de commande de PlaidCloud pour automatiser des tâches, exécuter des scripts et interagir avec les ressources PlaidCloud depuis un terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud utilise des requêtes JSON-RPC standard et peut être utilisé avec toute application capable d'émettre ces requêtes.


Pour simplifier les choses, un package Python facilite la connexion et l'exécution des appels d'API.


## Installation requise

Depuis un terminal, exécutez la commande suivante :

```bash
pip install plaidcloud-rpc
```


## Utiliser l'objet Simplerpc pour effectuer une requête

Pour effectuer une requête avec le package `plaidcloud-rpc`, utilisez l'objet `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Une fois l'objet `SimpleRPC` instancié, vous pouvez émettre des requêtes RPC vers PlaidCloud. Cet exemple demande les métadonnées d'une table.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## Quelles API sont disponibles ?

De nombreuses API permettent de contrôler presque tous les aspects de PlaidCloud. La référence interactive de l'API est servie par tenant, dans chaque espace de travail PlaidCloud : ouvrez votre espace de travail et accédez au menu de documentation de l'API pour consulter le catalogue des points de terminaison en direct.


## Obtenir un jeton OAuth

Consultez [Configuration d'OAuth](/fr/reference/cli/jupyter/oauth-setup/) pour savoir comment obtenir un jeton OAuth et configurer le système pour l'authentification automatisée.
