---
title: Ajouter un compte Google Cloud Storage
description: Ajoutez un compte Google Cloud Storage à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets cloud de Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Configuration de Google Cloud


Ces étapes doivent être effectuées dans Google Cloud Platform


1. Connectez-vous à un compte Google Cloud Platform ou créez-en un
2. Sélectionnez ou créez un projet dans lequel résidera le compte Google Cloud Storage
3. Accédez à `Cloud Storage > Browser` dans la console Google Cloud Platform
4. Créez un bucket par défaut ou de test
5. Aller à `IAM & Admin > Service Accounts` dans la console Google Cloud Platform
6. Cliquez sur le bouton `+ Create Service Account`
7. Renseignez les informations du compte de service et créez le compte
8. Repérez le compte de service que vous venez de créer dans la liste des comptes de service et sélectionnez `Manage Keys` dans le menu contextuel à droite
9. Dans le menu `Add Key`, sélectionnez `Create a Key`
10. Lorsque vous y êtes invité, sélectionnez le format JSON pour la clé. La clé est alors générée et téléchargée automatiquement sur votre ordinateur. Vous ne pourrez plus récupérer cette clé ; conservez-la donc précieusement. Si vous devez régénérer une clé, retournez simplement à l'étape 8 ci-dessus.
11. Accédez à `IAM & Admin > IAM` dans la console Google Cloud Platform
12. Repérez le compte de service que vous venez de créer et cliquez sur l'icône de modification des autorisations
13. Ajoutez les droits `Storage Admin` et `Storage Transfer Admin` au compte de service et enregistrez. Remarque : des droits moins permissifs peuvent être attribués, mais cela aura un impact sur les fonctionnalités disponibles via Document.

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte GCS à PlaidCloud Document.



## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Google Cloud Storage` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le nom du bucket et un préfixe de chemin facultatif dans le champ **Chemin de départ** (p. ex. `my-bucket` ou `my-bucket/data`). Le premier segment du chemin est le nom du bucket.
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Ouvrez le fichier de clé JSON du compte de service que vous avez téléchargé à l'étape 10 ci-dessus et copiez-en l'intégralité du contenu
10. Collez le contenu dans le champ **Clé JSON de l'utilisateur système** sous Identifiants d'authentification
11. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif

Une clé de compte de service valide est requise. L'enregistrement du compte sans clé, ou avec un élément qui n'est pas une clé de compte de service Google, est refusé avec le message « GCS document accounts require a valid service-account key. ». Un compte existant enregistré sans clé valide cesse de fonctionner tant que vous n'avez pas collé une clé dans le champ **Clé JSON de l'utilisateur système**.
