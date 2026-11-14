---
title: Déployer une application Panel depuis PlaidCloud Git
description: "Le parcours complet pour servir une application HoloViz Panel dans PlaidCloud : placez votre code dans un dépôt PlaidCloud Git, connectez-le avec une connexion gérée sans identifiants et publiez-le en ligne."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Voici le parcours complet, du code de l'application Panel sur votre machine jusqu'à une URL en ligne, en utilisant **[PlaidCloud Git](/fr/guides/git/)**, le service Git géré intégré à votre espace de travail, comme source. PlaidCloud Git étant géré, la connexion depuis laquelle votre application se déploie n'a **besoin ni d'URL de serveur, ni de nom d'utilisateur, ni de jeton** : PlaidCloud s'authentifie en votre nom.

Il y a cinq étapes :

1. Écrire une application Panel minimale.
2. La placer dans un dépôt PlaidCloud Git.
3. Créer une connexion PlaidCloud Git gérée.
4. Publier une application serveur qui pointe vers le dépôt.
5. Ouvrir l'application servie, et lire les journaux de construction si elle ne démarre pas.

Chaque étape renvoie au guide détaillé correspondant ; cette page les assemble en un seul parcours.

## Avant de commencer

- Ouvrez **Git** depuis votre espace de travail pour confirmer que vous pouvez accéder à PlaidCloud Git. Par défaut, l'organisation de votre espace de travail comprend un dépôt **`apps`** (et un dépôt **`udfs`**), qui est l'endroit naturel pour les applications Panel.
- Installez `git` en local si vous voulez pousser du code depuis votre machine (vous pouvez aussi ajouter des fichiers dans l'interface web de Git).

## 1. Écrire une application Panel minimale

Votre application a besoin d'un **point d'entrée** (un fichier Python qui construit une application Panel et la marque `.servable()`) et, facultativement, d'un fichier **`requirements.txt`** pour les paquets supplémentaires, soit à la racine du dépôt, soit à côté de votre point d'entrée.

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Créez `app.py` :

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

C'est une application complète : l'appel `.servable()` est ce que PlaidCloud sert. `panel`, `bokeh` et les bibliothèques clientes PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) sont préinstallés ; ne listez donc dans `requirements.txt` que les paquets *supplémentaires*. Pour des exemples plus riches, les dépendances et la gestion des thèmes clair/sombre, voir [Créer une application Panel](/fr/guides/panel-apps/creating/).

## 2. Placer votre application dans un dépôt PlaidCloud Git

Utilisez le dépôt **`apps`** existant de votre espace de travail, ou [créez-en un nouveau](/fr/guides/git/repositories/#créer-un-dépôt). Ensuite, placez-y votre code. Les applications que vous créez dans [Panel Studio](/fr/guides/panel-apps/studio/#où-se-trouve-votre-application) sont déjà des dossiers dans `apps` ; vous les y trouverez donc à côté des vôtres.

Comme vous vous connectez via PlaidCloud, votre compte Git n'a pas de mot de passe distinct : [générez un jeton d'accès personnel](/fr/guides/git/repositories/#générer-un-jeton-daccès-personnel) (**votre avatar → Settings → Applications**) avec l'autorisation **write:repository**, et utilisez-le comme mot de passe lorsque Git vous le demande. Pousser vers `apps` nécessite l'accès **Contributor** ; demandez à un administrateur de l'espace de travail de vous ajouter à **Git Contributors** si l'onglet **Git** vous affiche comme **Lecteur**. Utilisez le bouton de copie à côté de l'adresse de clonage du dépôt dans l'onglet **Git**, puis :

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notez le chemin du dépôt, `<org>/apps`, où `<org>` est le nom de l'organisation de votre espace de travail. Vous saisirez ce chemin à l'étape suivante. Les détails complets du clonage, du commit et du push se trouvent dans [Dépôts](/fr/guides/git/repositories/).

> **Le jeton ne sert ici qu'à *vous* permettre de pousser du code.** La connexion que vous créez ensuite est gérée et n'a besoin d'aucun jeton : ne confondez pas les deux.

## 3. Créer une connexion PlaidCloud Git gérée

Une **connexion** indique à un déploiement Panel où se trouve son code. Pour PlaidCloud Git, la connexion est *gérée* : PlaidCloud fournit l'hôte et les identifiants ; vous ne saisissez donc que la cible du dépôt.

1. Ouvrez **Tools > Connections**, cliquez sur **Nouvelle connexion** et choisissez **PlaidCloud Git**.
2. Donnez à la connexion un **Nom du compte** (par exemple `Apps Repo`).
3. Définissez **Repository Path** sur `<org>/apps` (le chemin que vous avez noté à l'étape 2) et **Branche par défaut** sur `main`. Laissez **Chemin de départ** vide, sauf si vos applications se trouvent dans un sous-répertoire.
4. Cliquez sur **Créer**.

Il n'y a aucun champ URL du serveur, utilisateur, mot de passe ou SSL/SSH : PlaidCloud Git étant géré, la plateforme prend en charge l'hôte et l'authentification. Pour le formulaire complet, y compris l'**Utilisation** et le **Modèle de sécurité** de la connexion (qui, dans l'espace de travail, peut l'utiliser), voir [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/).

> **Vous utilisez une ancienne version de l'espace de travail ?** Si le formulaire affiche encore une URL de serveur ou des champs d'identifiants, laissez-les simplement vides : la plateforme s'authentifie en votre nom dans les deux cas.

## 4. Publier l'application serveur

Dirigez maintenant un déploiement serveur vers cette connexion.

1. Ouvrez **Applications** et choisissez **Nouvelle application** > **Côté serveur**.
2. Sous **Paramètres du répertoire**, définissez un **Nom de l'application** et un **Slug d'URL** : le slug est l'URL et le nom interne de l'application ; utilisez donc des lettres minuscules, des chiffres et des tirets, en commençant par une lettre, 40 caractères au maximum (par exemple `hello-panel`).
3. Sous **Connexion Git et observateur de publication** :
   - **Connexion Git** : la connexion PlaidCloud Git que vous avez créée à l'étape 3.
   - **Branche** : `main`. Les push sur cette branche reconstruisent et redéploient automatiquement l'application.
   - **Point d'entrée** : `app.py`.
4. Sous **Exécution**, choisissez le **CPU**, la **Mémoire**, la **Conception** (**FAST** pour le look moderne de PlaidCloud) et la fenêtre d'**Inactivité**. Cochez **Autoriser l'accès public** uniquement si l'application doit être accessible sans connexion.
5. Cliquez sur **Publier**.

Chaque champ de cette boîte de dialogue est décrit dans [Créer une application Panel](/fr/guides/panel-apps/creating/#publier-lapplication).

## 5. Ouvrir l'application, et lire les journaux si elle ne démarre pas

Après la publication, l'application est **construite** : PlaidCloud clone la branche, installe votre `requirements.txt` (celui de la racine du dépôt et celui du dossier de votre application, s'ils existent) et construit une image de conteneur. Son **Statut** s'affiche dans la liste **Applications** et se met à jour automatiquement.

- Lorsque le statut est **Prêt**, ouvrez l'application à l'adresse `https://<your-tenant-host>/serve/<slug>/`. La première requête après une période d'inactivité la relance (~15 secondes).
- Si la construction échoue, ouvrez l'application et consultez ses journaux de **construction** : une dépendance manquante ou une erreur d'importation y apparaît. Voir [Utiliser une application Panel](/fr/guides/panel-apps/using/) pour la signification de chaque statut, la façon de lire les journaux et celle de déclencher une reconstruction.

Dès lors, **chaque push sur la branche de la connexion reconstruit et redéploie automatiquement l'application** : modifiez `app.py`, faites `git push`, et votre changement est en ligne. (Sauf si l'application est **verrouillée**, voir [Verrouiller une application](/fr/guides/panel-apps/using/#verrouiller-une-application), auquel cas les push sont ignorés jusqu'à son déverrouillage.)

## Étapes suivantes

- [Créer une application Panel](/fr/guides/panel-apps/creating/) : exemples plus riches, dépendances et gestion des thèmes clair/sombre
- [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/) : le formulaire de connexion complet, l'utilisation et le modèle de sécurité
- [Lire les données et l'utilisateur connecté](/fr/guides/panel-apps/accessing-data/) : interrogez les données PlaidCloud en tant que personne qui consulte l'application
- [Dépôts](/fr/guides/git/repositories/) : branches, jetons et collaboration dans PlaidCloud Git
