---
title: Déployer une application Dash depuis PlaidCloud Git
description: Le parcours complet pour diffuser une application Plotly Dash dans PlaidCloud — placez votre code dans un dépôt PlaidCloud Git, connectez-le avec une connexion gérée sans identifiants, puis publiez-le en ligne.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Voici le parcours complet, du code de votre application Dash sur votre machine jusqu'à une URL en ligne, avec **[PlaidCloud Git](/fr/guides/git/)** — le service Git géré intégré à votre espace de travail — comme source. PlaidCloud Git étant géré, la connexion depuis laquelle votre application se déploie n'exige **ni URL de serveur, ni nom d'utilisateur, ni jeton** : PlaidCloud s'authentifie en votre nom.

Il y a cinq étapes :

1. Écrire une application Dash minimale.
2. La placer dans un dépôt PlaidCloud Git.
3. Créer une connexion PlaidCloud Git gérée.
4. Publier une application Dash qui pointe vers le dépôt.
5. Ouvrir l'application diffusée — et consulter les journaux de construction si elle ne démarre pas.

Cette procédure est presque identique à [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) — ce sont deux applications Python côté serveur, construites à partir de Git et diffusées de la même manière. La différence tient au code de l'application elle-même et à un champ de la boîte de dialogue de publication.

## Avant de commencer

- Ouvrez **Git** depuis votre espace de travail pour vérifier que vous pouvez accéder à PlaidCloud Git. Par défaut, l'organisation de votre espace de travail comprend un dépôt **`apps`** — le lieu naturel pour les applications Dash également.
- Installez `git` en local si vous souhaitez envoyer du code depuis votre machine (vous pouvez aussi ajouter des fichiers dans l'interface web de Git).

## 1. Écrire une application Dash minimale

Votre application a besoin d'un **point d'entrée** — un fichier Python qui construit une application Dash et expose son serveur Flask — et, éventuellement, d'un fichier **`requirements.txt`** pour des paquets supplémentaires, à la racine du dépôt ou à côté de votre point d'entrée.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Créez `app.py` :

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

C'est une application complète. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` et les bibliothèques clientes PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) sont préinstallés ; ne listez donc dans `requirements.txt` que les paquets *supplémentaires*. Ne passez pas `requests_pathname_prefix` ni `url_base_pathname` à `Dash(__name__)` — la plateforme définit automatiquement le préfixe d'URL via `DASH_URL_BASE_PATHNAME`, et définir les deux provoque une erreur de configuration au démarrage. Pour le contrat complet de l'application et les utilitaires d'accès aux données, consultez [le contrat d'application](/fr/guides/dash-apps/#contrat-de-lapplication) et [Lire les données et l'utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/).

## 2. Placer votre application dans un dépôt PlaidCloud Git

Utilisez le dépôt **`apps`** existant de votre espace de travail, ou [créez-en un nouveau](/fr/guides/git/repositories/#créer-un-dépôt). Ensuite, placez-y votre code.

Comme vous vous connectez via PlaidCloud, votre compte Git n'a pas de mot de passe distinct — [générez un jeton d'accès personnel](/fr/guides/git/repositories/#générer-un-jeton-daccès-personnel) (**votre avatar → Paramètres → Applications**) avec l'autorisation **write:repository**, et utilisez-le comme mot de passe lorsque Git vous le demande. Envoyer du code vers `apps` exige l'accès **Contributeur** ; demandez à un administrateur de l'espace de travail de vous ajouter à **Git Contributors** si l'onglet **Git** indique que vous avez l'accès Lecture. Sélectionnez **Copy clone URL** sur le dépôt dans l'onglet **Git**, puis :

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Notez le chemin du dépôt — `<org>/apps` — où `<org>` est le nom de l'organisation de votre espace de travail. Vous saisirez ce chemin à l'étape suivante. Les détails complets du clonage, des commits et des envois figurent dans [Dépôts](/fr/guides/git/repositories/).

> **Le jeton ci-dessus ne sert qu'à *vous* permettre d'envoyer du code.** La connexion que vous créez ensuite est gérée et n'a pas besoin de jeton — ne confondez pas les deux.

## 3. Créer une connexion PlaidCloud Git gérée

Une **connexion** indique à un déploiement Dash où se trouve son code. Pour PlaidCloud Git, la connexion est *gérée* — PlaidCloud fournit l'hôte et les identifiants, de sorte que vous ne saisissez que la cible du dépôt. C'est le même type de connexion que celui utilisé par une application Panel serveur.

1. Ouvrez **Tools > Connections**, cliquez sur **Nouvelle connexion**, puis choisissez **PlaidCloud Git**.
2. Donnez à la connexion un **Nom du compte** (par exemple, `Apps Repo`).
3. Définissez **Repository Path** sur `<org>/apps` — le chemin que vous avez noté à l'étape 2 — et **Branche par défaut** sur `main`. Laissez **Chemin de départ** vide, sauf si vos applications se trouvent dans un sous-répertoire.
4. Cliquez sur **Créer**.

Il n'y a aucun champ URL du serveur, Utilisateur, Mot de passe ou SSL/SSH — PlaidCloud Git étant géré, la plateforme se charge de l'hôte et de l'authentification. Pour le formulaire complet, y compris l'**Utilisation** et le **Modèle de sécurité** de la connexion (qui, dans l'espace de travail, peut l'utiliser), consultez [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/).

## 4. Publier l'application Dash

Faites maintenant pointer un déploiement Dash vers cette connexion.

1. Ouvrez **Mes applications Panel** et cliquez sur **Nouvelle application Dash**.
2. Sous **Paramètres du répertoire**, définissez un **Nom de l'application** et un **Slug d'URL** — le slug est l'URL et le nom interne de l'application ; utilisez donc des lettres minuscules, des chiffres et des tirets, en commençant par une lettre, avec 40 caractères au maximum (par exemple, `hello-dash`). Un **Mémo** facultatif décrit l'application.
3. Sous **Connexion Git et observateur de publication** :
   - **Connexion Git** — la connexion PlaidCloud Git que vous avez créée à l'étape 3.
   - **Branche** — `main`. Les envois vers cette branche reconstruisent et redéploient automatiquement l'application.
   - **Point d'entrée** — `app.py`.
4. Sous **Exécution**, choisissez le **CPU**, la **Mémoire** et la fenêtre d'**Inactivité (minutes)**. Cochez **Autoriser l'accès public** uniquement si l'application doit être accessible sans connexion. Il n'y a pas de paramètre **Conception** — c'est une option propre à Panel.
5. Sous **Avancé (diffusion intégrée)** — facultatif. Laissez-le vide, sauf si vous intégrez l'application dans un autre site.
6. Cliquez sur **Publier**.

## 5. Ouvrir l'application — et lire les journaux si elle ne démarre pas

Une fois publiée, l'application est **construite** : PlaidCloud clone la branche, installe votre `requirements.txt` et construit une image de conteneur à partir de l'image `platform-dash-base`. Son **Statut** apparaît dans la liste **Mes applications Panel** et se met à jour automatiquement.

- Lorsque le statut est **Prêt**, ouvrez l'application à l'adresse `https://<your-tenant-host>/serve/<slug>/`. La première requête après une période d'inactivité la relance, en affichant brièvement un écran de chargement PlaidCloud.
- Si la construction échoue, ouvrez l'application et consultez ses journaux de construction — une dépendance manquante ou une erreur d'importation y apparaît. Consultez [Utiliser une application Dash](/fr/guides/dash-apps/using/) pour connaître la signification de chaque statut, la façon de lire les journaux et celle de déclencher une reconstruction.

Désormais, **chaque envoi vers la branche de la connexion reconstruit et redéploie automatiquement l'application** — modifiez `app.py`, exécutez `git push`, et votre changement est mis en ligne. (Sauf si l'application est **verrouillée** ; dans ce cas, les envois sont ignorés tant que vous ne la déverrouillez pas — consultez [Utiliser une application Dash](/fr/guides/dash-apps/using/#verrouiller-une-application).)

## Étapes suivantes

- [Lire les données et l'utilisateur connecté dans une application Dash](/fr/guides/dash-apps/accessing-data/) — interrogez les données PlaidCloud en tant que personne qui consulte l'application.
- [Utiliser une application Dash](/fr/guides/dash-apps/using/) — statut de construction, journaux, verrouillage et suppression de l'application.
- [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/) — le formulaire de connexion complet, l'utilisation et le modèle de sécurité.
- [Dépôts](/fr/guides/git/repositories/) — branches, jetons et collaboration dans PlaidCloud Git.
