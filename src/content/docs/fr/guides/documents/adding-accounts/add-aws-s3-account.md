---
title: Ajouter un compte AWS S3
description: Ajoutez un compte de stockage AWS S3 à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets cloud d'Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Configuration d'AWS S3

Ces étapes doivent être effectuées dans la console AWS.

1. Connectez-vous à un compte Amazon Web Services (AWS) ou créez-en un
2. Accédez à `All services > Storage > S3` dans la console
3. Créez un bucket par défaut ou de test. Notez le nom du bucket et la région (p. ex. `us-east-1`).
4. Accédez à `All Services > Security Identity & Compliance > IAM > Users` dans la console
5. Cliquez sur le bouton `Create User`
6. Lorsque vous y êtes invité, saisissez un nom d'utilisateur et sélectionnez uniquement `Access Key - Programmatic access`. Cliquez sur le bouton `Next: Permissions`.
7. Sélectionnez la case d'option `Attach existing policies directly`
8. Dans la zone de recherche du filtre, saisissez `s3`. Lorsque la liste se réduit aux éléments liés à S3, sélectionnez `AmazonS3FullAccess` en cochant la case à sa gauche. Cliquez sur le bouton `Next: Tags`.
9. Ignorez cette étape en cliquant sur le bouton `Next: Review`
10. Vérifiez les paramètres de l'utilisateur et sélectionnez `Create user`
11. Récupérez les clés générées pour l'utilisateur en téléchargeant le CSV ou en les copiant-collant quelque part pour un usage ultérieur. Vous ne pourrez plus récupérer cette clé ; conservez-la donc précieusement. Si vous devez régénérer une clé, retournez simplement à l'étape 5 ci-dessus.

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte S3 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Amazon S3` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le nom du bucket et un préfixe de chemin facultatif dans le champ **Chemin de départ** (p. ex. `my-bucket` ou `my-bucket/data`). Le premier segment du chemin est le nom du bucket.
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Collez la **clé d'accès** créée à l'étape 11 ci-dessus dans le champ ID de clé d'accès sous Identifiants d'authentification
10. Collez la **clé secrète** créée à l'étape 11 ci-dessus dans le champ Clé d'accès secrète sous Identifiants d'authentification
11. Saisissez la **Région** de votre bucket (p. ex. `us-east-1`, `eu-west-1`). Si le champ est laissé vide, la valeur par défaut est `us-east-2`.
12. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
