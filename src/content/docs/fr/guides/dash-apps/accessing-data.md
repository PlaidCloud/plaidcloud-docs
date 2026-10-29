---
title: Lire les données et l'utilisateur connecté dans une application Dash
description: "Connectez une application Dash à PlaidCloud en tant que personne qui la consulte : lisez les données du projet et utilisez l'identité du lecteur pour un comportement par utilisateur et la sécurité au niveau des lignes."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Une application Dash peut lire vos données PlaidCloud, et elle le fait **en tant que personne qui la consulte**, exactement comme une application Panel serveur. Lorsqu'une personne ouvre l'application, PlaidCloud la connecte avec le même authentification unique que le reste de la plateforme, et chaque appel de votre application s'exécute avec **les propres autorisations de ce lecteur**. Il n'y a aucun compte de service partagé, et l'application ne peut jamais voir des données que le lecteur ne pourrait pas voir lui-même.

Les fonctions utilitaires se trouvent dans `plaidcloud_dash`, qui fait partie de l'image de base Dash :

```python
from plaidcloud_dash import current_user, get_connection
```

## Se connecter à PlaidCloud

Appelez `get_connection()` depuis un rappel (callback) Dash, en nommant le projet dont vous voulez lire les données :

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

C'est toute la configuration nécessaire. Vous ne fournissez **aucun** jeton, nom d'utilisateur ou mot de passe : `get_connection()` s'authentifie automatiquement en tant que lecteur connecté, à l'aide du jeton d'accès de sa session en cours. Vous trouverez l'identifiant de votre projet dans l'URL du projet ou sur sa page de paramètres.

> **Appelez-la depuis un rappel.** `get_connection()` lit le jeton du lecteur dans la session Flask de la requête en cours, qui n'est disponible que pendant qu'un rappel traite la requête de ce lecteur. Si vous déléguez un appel bloquant à un thread d'arrière-plan, un pool de threads brut ne transmettra pas la session : lisez plutôt le jeton dans le rappel et transmettez-le explicitement. Appeler `get_connection()` en dehors d'une requête (ou avec l'authentification désactivée) lève une `RuntimeError` plutôt que de renvoyer silencieusement une connexion sans identité derrière elle.

> **Nommez votre projet dans le code.** La boîte de dialogue de publication ne comporte aucun paramètre de projet : une application Dash lit le projet que vous nommez dans `get_connection(project_id=...)`, comme le `PlaidConnection(project_id=...)` d'une application Panel serveur (voir [Lire les données et l'utilisateur connecté](/fr/guides/panel-apps/accessing-data/)). Un `get_connection()` sans `project_id` convient pour une application qui ne touche jamais aux données du projet (par exemple, une application qui appelle uniquement `current_user()`) ; si vous appelez une opération portant sur un projet avec cette connexion sans identifiant de projet réel et accessible, elle lève `Project Id has not been set`. (Pour lire plusieurs projets, ouvrez une connexion par projet.)

### Lire une table

Avec une connexion, chargez une table dans un DataFrame pandas à partir de son nom :

```python
df = conn.get_dataframe("Sales Ledger")
```

Comme la connexion est celle du lecteur, cet appel ne renvoie que les lignes que le lecteur est autorisé à voir, et lève une erreur d'autorisation s'il n'a aucun accès au projet.

> **Lisez les tables par leur nom, sans écrire de SQL.** Sur un projet où un administrateur a activé l'[Accès aux lignes](/fr/administration/access/managing-security-groups-and-assignments/#accès-aux-lignes-et-requêtes-que-vous-écrivez-vous-même), la lecture par nom applique les droits de ligne de chaque lecteur, alors qu'une requête composée par votre application est refusée pour toute personne qui n'est pas Architecte du projet : il n'existe pas de table unique que les droits puissent filtrer. La lecture par nom garantit le bon fonctionnement de votre application dans les deux cas.

## Lire dans un rappel, jamais à l'import ni à l'échelle du processus

Un seul processus sert tous les lecteurs. L'isolation correcte des données repose sur deux règles :

- **N'ouvrez jamais de connexion et ne lisez jamais de table au niveau du module (au moment de l'import).** Votre `app.py` et les modules qu'il importe s'exécutent **une seule fois**, au démarrage du conteneur, avant que quiconque se soit connecté. Un `get_connection()` ou un `PlaidConnection()` à cet endroit n'a aucun lecteur avec lequel s'authentifier et fait échouer l'application au démarrage (c'est la cause la plus fréquente d'une boucle de plantage « l'application n'a pas démarré »). Gardez chaque lecture à l'intérieur d'un rappel, où la requête d'un lecteur, et donc son jeton de session, est présente.

- **Ne mettez jamais en cache un résultat propre à un lecteur au niveau du module ou du processus.** Le worker gunicorn multithread partage un même processus Python entre tous les lecteurs simultanés ; un DataFrame que vous conservez dans une variable de module, un dictionnaire global ou un `lru_cache` est donc visible de *tous* les autres lecteurs, et les lignes d'une personne fuient dans la vue d'une autre. Calculez les données propres à un lecteur dans le rappel et laissez-les sortir de la portée lorsque le rappel se termine :

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### Données de référence partagées

Si plusieurs lecteurs ont réellement besoin des *mêmes* données de référence (une table de correspondance, une liste de produits), n'essayez pas de les partager au moyen d'un cache au niveau du processus. Accordez ces tables aux utilisateurs de l'application grâce aux [droits d'accès aux lignes et aux autorisations du projet](/fr/administration/access/managing-security-groups-and-assignments/) habituels de PlaidCloud, et laissez chaque lecteur les lire avec son propre `get_connection()`. Tout le monde obtient les mêmes lignes de référence parce qu'ils disposent tous du même accès, et non parce que la lecture d'un lecteur est réutilisée pour un autre.

## Identifier le lecteur

Pour adapter ce que l'application affiche à **la personne qui la consulte** (un message d'accueil personnalisé, un onglet masqué ou la sécurité au niveau des lignes), appelez `current_user()` :

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` renvoie l'identifiant du lecteur connecté (son nom d'utilisateur, à défaut son adresse e-mail, puis l'ID de son compte si aucune revendication de nom d'utilisateur n'est présente), tiré de sa connexion vérifiée ; vous pouvez donc vous y fier comme identité. Elle ne lève jamais d'exception ; appelée avec l'authentification désactivée ou en dehors d'une requête, elle renvoie une chaîne vide.

### Sécurité au niveau des lignes

Combinez les deux : lisez le lecteur, puis filtrez chaque requête en fonction de lui. Par exemple, pour montrer à chaque responsable régional uniquement sa propre région :

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

Comme la connexion applique déjà les autorisations du lecteur sur le projet, ce filtrage est un façonnage *supplémentaire* de ce qu'il est autorisé à voir, et non un substitut au contrôle d'accès propre à PlaidCloud.

## Applications publiques

Si vous avez publié avec **Autoriser l'accès public**, l'application est servie sans connexion : il n'y a donc aucun lecteur au nom duquel agir. `current_user()` renvoie une chaîne vide et `get_connection()` n'a aucun jeton de session avec lequel s'authentifier, si bien qu'elle lève une exception. Limitez les applications publiques à des données sans risque pour tout le monde, ou laissez l'accès public désactivé afin que les lecteurs se connectent et que le modèle par utilisateur décrit ci-dessus s'applique.
