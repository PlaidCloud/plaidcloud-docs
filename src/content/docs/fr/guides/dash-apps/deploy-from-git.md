---
title: Déployer une application Dash depuis PlaidCloud Git
description: "Le parcours complet pour servir une application Plotly Dash dans PlaidCloud : placez votre code dans un dépôt PlaidCloud Git, connectez-le avec une connexion gérée sans identifiants, puis publiez-le en ligne."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Voici le parcours complet, du code de l'application Dash sur votre machine jusqu'à une URL en ligne, avec **[PlaidCloud Git](/fr/guides/git/)**, le service Git géré intégré à votre espace de travail, comme source. Comme PlaidCloud Git est géré, la connexion depuis laquelle votre application se déploie ne nécessite **aucune URL de serveur, aucun nom d'utilisateur ni aucun jeton** : PlaidCloud s'authentifie en votre nom.

Il y a cinq étapes :

1. Écrire une application Dash minimale.
2. La placer dans un dépôt PlaidCloud Git.
3. Créer une connexion PlaidCloud Git gérée.
4. Publier une application Dash qui pointe vers le dépôt.
5. Ouvrir l'application servie, et consulter les journaux de génération si elle ne démarre pas.

Ce pas-à-pas est presque identique à [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) : les deux sont des applications Python côté serveur, construites à partir de Git et servies de la même manière. La différence tient au code de l'application elle-même et à un champ de la boîte de dialogue de publication.

## Avant de commencer

- Ouvrez **Git** depuis votre espace de travail pour confirmer que vous pouvez accéder à PlaidCloud Git. Par défaut, l'organisation de votre espace de travail comprend un dépôt **`apps`**, qui convient aussi naturellement aux applications Dash.
- Installez `git` en local si vous voulez envoyer du code depuis votre machine (vous pouvez aussi ajouter des fichiers dans l'interface web de Git).

## 1. Écrire une application Dash minimale

Votre application a besoin d'un **point d'entrée**, c'est-à-dire un fichier Python qui construit une application Dash et expose son serveur Flask, ainsi que, facultativement, d'un fichier **`requirements.txt`** pour les paquets supplémentaires, à la racine du dépôt ou à côté de votre point d'entrée.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Créez `app.py` :

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

C'est une application complète. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` et les bibliothèques clientes PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) sont préinstallés ; ne listez donc dans `requirements.txt` que les paquets *supplémentaires*. Ne passez pas `requests_pathname_prefix` ni `url_base_pathname` à `Dash(__name__)` : la plateforme définit automatiquement le préfixe d'URL via `DASH_URL_BASE_PATHNAME`, et définir les deux provoque une erreur de configuration au démarrage. Pour le contrat complet de l'application et les fonctions d'accès aux données, consultez [le contrat de l'application](/fr/guides/dash-apps/#contrat-de-lapplication) et [Lire les données et l'utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/).

## 2. Placer votre application dans un dépôt PlaidCloud Git

Utilisez le dépôt **`apps`** existant de votre espace de travail, ou [créez-en un nouveau](/fr/guides/git/repositories/#créer-un-dépôt). Ensuite, placez-y votre code.

Comme vous vous connectez via PlaidCloud, votre compte Git n'a pas de mot de passe distinct : [générez un jeton d'accès personnel](/fr/guides/git/repositories/#générer-un-jeton-daccès-personnel) (**votre avatar → Paramètres → Applications**) avec les portées de **lecture** et d'**écriture** sur le dépôt, et utilisez-le comme mot de passe lorsque Git le demande. Copiez l'URL de clonage **HTTPS** du dépôt depuis son bouton **Code**, puis :

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Notez le chemin du dépôt, `<org>/apps`, où `<org>` est le nom de l'organisation de votre espace de travail. Vous saisirez ce chemin à l'étape suivante. Les détails complets sur le clonage, les commits et les envois figurent dans [Dépôts](/fr/guides/git/repositories/).

> **Le jeton ci-dessus sert uniquement à *vous* permettre d'envoyer du code.** La connexion que vous créez ensuite est gérée et ne nécessite aucun jeton : ne confondez pas les deux.

## 3. Créer une connexion PlaidCloud Git gérée

Une **connexion** indique à un déploiement Dash où se trouve son code. Pour PlaidCloud Git, la connexion est *gérée* : PlaidCloud fournit l'hôte et les identifiants, et vous ne saisissez donc que la cible du dépôt. C'est le même type de connexion que celui utilisé par une application Panel serveur.

1. Ouvrez **Outils > Connexions**, cliquez sur **Nouvelle connexion**, puis choisissez **PlaidCloud Git**.
2. Donnez à la connexion un **Nom du compte** (par exemple, `Apps Repo`).
3. Définissez **Chemin du dépôt** sur `<org>/apps` (le chemin que vous avez noté à l'étape 2) et **Branche par défaut** sur `main`. Laissez **Chemin de départ** vide, sauf si vos applications se trouvent dans un sous-répertoire.
4. Cliquez sur **Créer**.

Il n'y a aucun champ URL du serveur, Utilisateur, Mot de passe ou SSL/SSH : PlaidCloud Git est géré, la plateforme prend donc en charge l'hôte et l'authentification. Pour le formulaire complet, y compris l'**Utilisation** et le **Modèle de sécurité** de la connexion (qui, dans l'espace de travail, peut l'utiliser), consultez [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/).

## 4. Publier l'application Dash

Faites maintenant pointer un déploiement Dash vers cette connexion.

1. Ouvrez **Mes applications Panel** et cliquez sur **Nouvelle application Dash**.
2. Sous **Paramètres du répertoire**, définissez un **Nom de l'application** et un **Slug d'URL**. Le slug est l'URL et le nom interne de l'application ; utilisez donc des lettres minuscules, des chiffres et des tirets, en commençant par une lettre, avec 40 caractères au maximum (par exemple, `hello-dash`). Un **Mémo** facultatif décrit l'application.
3. Sous **Connexion Git et observateur de publication** :
   - **Connexion Git** : la connexion PlaidCloud Git que vous avez créée à l'étape 3.
   - **Branche** : `main`. Les envois vers cette branche régénèrent et redéploient automatiquement l'application.
   - **Point d'entrée** : `app.py`.
4. Sous **Exécution**, choisissez le **CPU**, la **Mémoire** et la fenêtre d'**Inactivité (minutes)**. Cochez **Autoriser l'accès public** uniquement si l'application doit être accessible sans connexion. Il n'y a pas de paramètre **Conception** : c'est une option propre à Panel.
5. Sous **Avancé (diffusion intégrée)** : facultatif. Laissez vide, sauf si vous intégrez l'application dans un autre site.
6. Cliquez sur **Publier**.

## 5. Ouvrir l'application et lire les journaux si elle ne démarre pas

Après la publication, l'application est **générée** : PlaidCloud clone la branche, installe votre `requirements.txt` et construit une image de conteneur à partir de l'image `platform-dash-base`. Son **Statut** s'affiche dans la liste **Mes applications Panel** et se met à jour automatiquement.

- Lorsque le Statut est **Prêt**, ouvrez l'application à l'adresse `https://<your-tenant-host>/serve/<slug>/`. La première requête après une période d'inactivité la démarre, en affichant brièvement un écran de chargement PlaidCloud.
- Si la génération échoue, ouvrez l'application et consultez ses journaux de **Génération** : une dépendance manquante ou une erreur d'import y apparaît. Consultez [Utiliser une application Dash](/fr/guides/dash-apps/using/) pour la signification de chaque statut, la lecture des journaux et le déclenchement d'une régénération.

Désormais, **chaque envoi vers la branche de la connexion régénère et redéploie automatiquement l'application** : modifiez `app.py`, exécutez `git push`, et votre changement est mis en ligne. (Sauf si l'application est **verrouillée** : dans ce cas, les envois sont ignorés jusqu'à son déverrouillage ; voir [Utiliser une application Dash](/fr/guides/dash-apps/using/#verrouiller-une-application).)

## Étapes suivantes

- [Lire les données et l'utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/) : interrogez les données PlaidCloud en tant que personne qui consulte l'application.
- [Utiliser une application Dash](/fr/guides/dash-apps/using/) : statut de génération, journaux, verrouillage et suppression de l'application.
- [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/) : le formulaire de connexion complet, l'utilisation et le modèle de sécurité.
- [Dépôts](/fr/guides/git/repositories/) : branches, jetons et collaboration dans PlaidCloud Git.
