---
title: Lecture des données et utilisateur connecté
description: "Connectez une application Panel côté serveur à PlaidCloud en tant que personne qui la consulte : lisez les données d'un projet et utilisez l'identité du lecteur pour un comportement par utilisateur et la sécurité au niveau des lignes."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Une application Panel serveur peut lire vos données PlaidCloud, et elle le fait **en tant que personne qui la consulte**. Lorsqu'une personne ouvre l'application, PlaidCloud la connecte avec la même authentification unique que le reste de la plateforme, et chaque appel de votre application s'exécute avec **les propres autorisations de ce lecteur**. Il n'y a pas de compte de service partagé, et l'application ne peut jamais voir des données que le lecteur ne pourrait pas voir lui-même.

Cela s'applique uniquement aux applications **Server**. Les applications WASM s'exécutent entièrement dans le navigateur et n'ont pas de connexion côté serveur.

## Se connecter à PlaidCloud

Utilisez `PlaidConnection` en nommant le projet dont vous voulez lire les données :

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

C'est toute la configuration nécessaire. Vous n'avez **pas** à fournir de jeton, de nom d'utilisateur ni de mot de passe : la connexion s'authentifie automatiquement en tant que lecteur connecté. Vous trouverez l'identifiant de votre projet dans l'URL du projet ou sur sa page de paramètres.

> **Nommez votre projet.** Une application publiée avec un projet dans le sélecteur **Projet** lit ce projet par défaut, et l'[API de données](/fr/guides/panel-apps/data-api/) l'utilise pour `table("name")`. Pour une application sans projet, transmettez `project_id` à `PlaidConnection` comme ci-dessus ; un `PlaidConnection()` nu n'a aucun projet à lire.

### Lire une table

Avec une connexion, chargez une table dans un DataFrame pandas à partir de son nom :

```python
df = conn.get_dataframe("Sales Ledger")
```

Comme la connexion est celle du lecteur, elle ne renvoie que les lignes que celui-ci est autorisé à voir, et elle lève une erreur d'autorisation s'il n'a aucun accès au projet.

> **Lisez les tables par leur nom, sans écrire de SQL.** Sur un projet où un administrateur a activé l'[Accès aux lignes](/fr/administration/access/managing-security-groups-and-assignments/#accès-aux-lignes-et-requêtes-que-vous-écrivez-vous-même), la lecture par nom applique les droits de lignes de chaque lecteur, tandis qu'une requête composée par votre application est refusée pour toute personne qui n'est pas Architecte du projet : il n'existe pas de table unique que les droits puissent filtrer. Lire par nom permet à votre application de fonctionner dans les deux cas.

## Identifier le lecteur

Pour adapter ce que l'application affiche à **la personne qui la consulte** (un message d'accueil personnalisé, un onglet masqué ou la sécurité au niveau des lignes), lisez l'utilisateur connecté depuis Panel :

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` est l'adresse e-mail du lecteur, issue de sa connexion vérifiée : vous pouvez lui faire confiance comme identité. `pn.state.access_token` est son jeton d'accès brut, utile si vous devez décoder des revendications de groupe ou de rôle pour des règles plus fines.

### Sécurité au niveau des lignes

Combinez les deux : lisez le lecteur, puis filtrez chaque requête en fonction de lui. Par exemple, pour montrer à chaque responsable régional uniquement sa propre région :

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Comme la connexion applique déjà les autorisations du lecteur sur le projet, ce filtrage est un façonnage *supplémentaire* par-dessus ce qu'il est autorisé à voir, et non un substitut au contrôle d'accès propre à PlaidCloud.

> **Effectuez les appels de données depuis le flux principal de l'application.** Le lecteur connecté est disponible pendant que le code de votre application s'exécute pour sa session (c'est là que s'exécute le travail de `.servable()`). Si vous déportez un appel bloquant vers un thread d'arrière-plan, utilisez `asyncio.to_thread` : un pool de threads brut ne transmet pas l'identité de la session, et la connexion échouera bruyamment plutôt que de lire de mauvaises données.

## Applications publiques

Si vous avez publié avec **Autoriser l'accès public**, l'application est servie sans connexion : il n'y a donc aucun lecteur pour qui agir, `pn.state.user` est vide et un `PlaidConnection()` n'a personne à authentifier. Limitez les applications publiques à des données sans risque pour tout le monde, ou laissez l'accès public désactivé pour que les lecteurs se connectent et que le modèle par utilisateur décrit ci-dessus s'applique.
