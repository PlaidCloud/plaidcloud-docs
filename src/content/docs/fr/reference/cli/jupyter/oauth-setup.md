---
title: Jetons OAuth
description: Configurez des jetons OAuth pour accéder à l'API PlaidCloud et authentifier les Notebooks Jupyter, les outils CLI et les connexions d'applications personnalisées.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud utilise des requêtes JSON-RPC standard et peut être utilisé avec toute application capable d'émettre ces requêtes.  Les requêtes sont sécurisées par des jetons OAuth.


## Obtenir un jeton OAuth

Les jetons OAuth sont générés depuis l'application PlaidCloud. Pour afficher la liste des jetons OAuth qui vous sont attribués et en générer de nouveaux, accédez à `Analyze > Tools > Registered Systems`.

Vous pouvez alors consulter les jetons existants ou en créer un nouveau.

## Télécharger le fichier de configuration OAuth de PlaidCloud
Sélectionnez « Register a New System ».

Remplissez le formulaire et notez le nom saisi afin de le retrouver dans la liste.

Une fois le système créé, ouvrez son enregistrement en cliquant sur l'icône en forme d'engrenage.  Le texte du fichier de configuration s'affiche.  

REMARQUE : veillez à sélectionner, dans la liste déroulante en haut, le projet pour lequel vous souhaitez utiliser cette connexion.  L'identifiant unique du projet sera ajouté à la configuration.

Copiez ce texte dans un fichier plaid.conf situé sur votre système.  Placez-le dans le répertoire .plaid.

## Créer un fichier de configuration en local
Créez un répertoire un niveau au-dessus du répertoire de votre notebook, ou de l'endroit où vous prévoyez d'utiliser la ligne de commande.  Nommez ce répertoire `.plaid`.

Dans le répertoire `.plaid`, créez un fichier nommé `plaid.conf` et collez-y le contenu copié précédemment.  Enregistrez le fichier : vous pourrez alors vous connecter à l'aide des utilitaires PlaidCloud et des méthodes RPC.


## Utilisations avancées

Il est pratique de placer le dossier `.plaid` près de son point d'utilisation, mais il peut en réalité se trouver n'importe où dans l'arborescence parente.  Le processus d'initialisation remonte l'arborescence jusqu'à trouver le répertoire `.plaid`.

Placer le répertoire `.plaid` plus haut peut être utile si plusieurs opérations ont besoin d'y accéder mais ne peuvent pas coexister dans les mêmes arborescences de niveau inférieur.


## Spécification facultative des chemins
Si vous utilisez une installation locale de Jupyter Notebook ou travaillez en ligne de commande, vous pouvez, grâce aux outils utilitaires, exporter des données, des fichiers Excel et d'autres éléments, ainsi que lire des données locales dans des dataframes.  Pour cela, un fichier paths.yaml est nécessaire.

En plus du fichier `plaid.conf`, créez un fichier `paths.yaml`.  Le fichier `paths.yaml` doit se trouver au même niveau que `plaid.conf`, dans le répertoire `.plaid`.  Il doit contenir les informations de chemin suivantes :

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
