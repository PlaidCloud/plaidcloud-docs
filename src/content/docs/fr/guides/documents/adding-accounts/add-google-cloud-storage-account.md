---
title: Ajouter un compte Google Cloud Storage
description: Ajoutez un compte Google Cloud Storage à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets cloud de Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Configuration de Google Cloud


Ces étapes doivent être réalisées dans Google Cloud Platform


1. Connectez-vous à un compte Google Cloud Platform ou créez-en un
2. Sélectionnez ou créez un projet dans lequel le compte Google Cloud Storage sera créé
3. Accédez à `Cloud Storage > Browser` dans la console Google Cloud Platform
4. Créez un bucket par défaut ou de test
5. Accédez à `IAM & Admin > Service Accounts` dans la console Google Cloud Platform
6. Sélectionnez le bouton `+ Create Service Account`
7. Renseignez les informations du compte de service et créez le compte
8. Repérez le compte de service que vous venez de créer dans la liste des comptes de service et sélectionnez `Manage Keys` dans le menu contextuel à droite
9. Dans le menu `Add Key`, sélectionnez `Create a Key`
10. À l'invite, sélectionnez le format JSON pour la clé. La clé est alors générée et téléchargée automatiquement sur votre ordinateur. Vous ne pourrez plus récupérer cette clé par la suite : conservez-la précieusement. Pour régénérer une clé, revenez simplement à l'étape 8 ci-dessus.
11. Accédez à `IAM & Admin > IAM` dans la console Google Cloud Platform
12. Repérez le compte de service que vous venez de créer et cliquez sur l'icône de modification des autorisations
13. Ajoutez les droits `Storage Admin` et `Storage Transfer Admin` au compte de service, puis enregistrez. Vous pouvez attribuer des droits plus restrictifs, mais cela limitera les fonctionnalités disponibles dans Document.

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte GCS à PlaidCloud Document.



## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Google Cloud Storage` comme Type de service
6. Saisissez un nom et une description
7. Saisissez le nom du bucket et un préfixe de chemin facultatif dans le champ **Chemin de départ** (par ex. `my-bucket` ou `my-bucket/data`). Le premier segment du chemin correspond au nom du bucket.
8. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
9. Ouvrez le fichier de clé JSON du compte de service téléchargé à l'étape 10 ci-dessus et copiez l'intégralité de son contenu
10. Collez ce contenu dans le champ **Clé JSON de l'utilisateur système**, sous Identifiants d'authentification
11. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel

Une clé de compte de service valide est obligatoire. L'enregistrement d'un compte sans clé, ou avec un contenu qui n'est pas une clé de compte de service Google, est refusé avec le message « GCS document accounts require a valid service-account key. » Un compte existant enregistré sans clé valide cesse de fonctionner jusqu'à ce que vous en colliez une dans le champ **Clé JSON de l'utilisateur système**.
