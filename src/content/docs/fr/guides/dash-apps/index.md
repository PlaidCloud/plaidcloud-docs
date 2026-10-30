---
title: Applications Dash
description: Créez et déployez des applications de données Plotly Dash côté serveur dans PlaidCloud, publiées depuis un dépôt Git et servies avec authentification par utilisateur et mise à l'échelle à zéro, à parité avec les applications Panel serveur.
sidebar:
  label: Applications Dash
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Les applications Dash vous permettent de publier des applications interactives [Plotly Dash](https://dash.plotly.com/) (callbacks, graphiques et grilles de données (`dash-ag-grid`, `dash-mantine-components`)) directement depuis PlaidCloud. Vous les gérez depuis l'écran **Mes applications Panel**, aux côtés de vos applications Panel, où chaque ligne indique son runtime, son état de build et son URL.

## Place de Dash

Une application Dash est hébergée exactement comme une **application Panel serveur** : vous indiquez à PlaidCloud une branche d'un dépôt Git, il compile votre code dans un conteneur, et le conteneur reste inactif à zéro réplica, se réveille à la première requête, répond, puis revient à zéro lorsqu'il est inactif. Il n'existe pas de runtime « WASM » distinct pour Dash : toute application Dash est une application serveur.

Choisissez une application Dash lorsque votre application est écrite avec Plotly Dash plutôt qu'avec HoloViz Panel, par exemple si vous avez déjà une base de code Dash, ou si votre équipe préfère le modèle de callbacks de Dash et l'écosystème `dash-ag-grid` / `dash-mantine-components`. Si vous partez de zéro et n'avez pas de préférence, consultez [Applications Panel](/fr/guides/panel-apps/) pour l'alternative.

Tout ce qu'obtient une application Panel serveur, une application Dash l'obtient aussi :

- **Identité par utilisateur.** Chaque lecteur se connecte via l'authentification unique de la plateforme, et chaque appel que l'application effectue pour lire des données s'exécute en tant que *ce lecteur*, selon le même modèle que [Lecture des données et utilisateur connecté](/fr/guides/panel-apps/accessing-data/), avec l'API d'aide propre à Dash. Consultez [Lecture des données et utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/).
- **Mise à l'échelle à zéro.** L'application passe à zéro réplica après sa fenêtre d'inactivité configurée et se réveille à la requête suivante, avec un bref écran de chargement PlaidCloud pendant un démarrage à froid. Consultez [Utiliser une application Dash](/fr/guides/dash-apps/using/#ouvrir-une-application-dash).
- **Reconstructions automatiques.** Chaque push vers la branche connectée reconstruit et redéploie l'application.
- **Journaux d'exécution et de build**, chacun étiqueté avec le lecteur dont la session a produit la ligne.

Deux choses qu'une application Dash n'a **pas**, par conception, et qui correspondent à ce qui manque aussi à une application Panel :

- **Pas de paramètre de conception/thème.** L'option **Conception** de la boîte de dialogue de publication Panel (FAST ou Par défaut) est propre à Panel : les applications Dash se stylisent entièrement via les composants que vous choisissez (`dash-mantine-components`, CSS personnalisé, etc.), donc le formulaire de publication n'a pas de champ équivalent.
- **Pas de liste d'accès par application.** L'accès repose sur la barrière SSO de l'espace de travail : toute personne connectée à votre locataire peut ouvrir l'application (ou, si vous activez **Autoriser l'accès public**, n'importe qui). Il n'existe pas de couche ACL distincte par application, quel que soit le type d'application.

## Contrat de l'application

Le fichier d'entrée d'une application Dash doit s'appeler `app.py` et exposer un `server` : c'est tout le contrat.

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Nommez le fichier `app.py`.** Le lanceur de PlaidCloud importe votre application comme le module `app` et lit son objet `server` ; quel que soit le chemin que vous définissez dans **Point d'entrée** (racine du dépôt ou sous-dossier), le fichier situé à ce chemin doit s'appeler `app.py`.
- **Exposez `server = app.server`** au niveau du module. C'est l'objet que la plateforme importe.
- **Vous n'avez pas à câbler la connexion vous-même.** La plateforme protège automatiquement chaque requête par une authentification unique par utilisateur : vous n'avez pas besoin d'appeler `init_auth` ni d'importer `plaidcloud_dash` pour obtenir l'identité. (Une application plus ancienne qui *appelle* `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` continue de fonctionner sans changement : cet appel est idempotent, il coexiste donc avec le câblage propre à la plateforme.)
- **Ne définissez ni `requests_pathname_prefix` ni `url_base_pathname` dans `Dash(__name__)`.** Toute application Dash est servie sous un préfixe d'URL obligatoire (`/serve/<slug>/`), et la plateforme le définit pour vous via la variable d'environnement `DASH_URL_BASE_PATHNAME`, qui est la variable de configuration native de Dash, lue avant tout argument du constructeur. Passer aussi le préfixe explicitement entre en conflit avec la configuration propre à Dash, et l'application ne démarre pas.
- **`Entry Point` peut pointer vers un sous-dossier.** Avant de démarrer l'application, l'hôte définit le répertoire de travail du conteneur sur le dossier du fichier d'entrée : les imports de fichiers voisins dans le même dossier (`import data`) et les chemins de fichiers relatifs de votre application se résolvent donc par rapport à ce dossier, comme si vous exécutiez `python app.py` depuis l'intérieur.
- **Ne lisez pas de données à l'import.** Effectuez vos lectures PlaidCloud dans des callbacks, pas au niveau du module. Consultez [Lecture des données et utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/). Le module de votre application s'exécute une seule fois, au démarrage du conteneur, avant qu'un lecteur se soit connecté ; une lecture de connexion ou de table à ce moment-là n'a aucun lecteur au nom duquel agir et fait échouer l'application au démarrage.

PlaidCloud exécute votre application sous **gunicorn multithread**, ce qui lui permet de servir des lecteurs simultanés depuis un seul processus : vous n'avez rien de plus à faire pour que plusieurs personnes utilisent l'application en même temps.

## Choisir entre Panel et Dash

| | Applications Panel | Applications Dash |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Runtimes | WASM (dans le navigateur) ou serveur | Serveur uniquement |
| Modèle d'identité | SSO par utilisateur (applications serveur) | SSO par utilisateur |
| Mise à l'échelle à zéro | Applications serveur uniquement | Oui |
| Paramètre de conception/thème | Oui (FAST / Par défaut) | Non : stylisation via vos propres composants |
| Liste d'accès par application | Non : barrière SSO de l'espace de travail | Non : barrière SSO de l'espace de travail |

## Étapes suivantes

- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) : le parcours complet du dépôt à l'application servie, avec une connexion gérée sans identifiants.
- [Lecture des données et utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/) : interrogez les données PlaidCloud en tant que personne qui consulte l'application.
- [Utiliser une application Dash](/fr/guides/dash-apps/using/) : état du build, ouverture de l'application, journaux et suppression.
