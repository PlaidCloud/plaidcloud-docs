---
title: Ajouter un compte Backblaze B2
description: Ajoutez un compte de stockage Backblaze B2 à PlaidCloud pour importer et exporter des fichiers de données à l'aide d'un stockage d'objets cloud économique.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Configuration de Backblaze B2

Ces étapes doivent être effectuées dans la console Backblaze B2.

1. Connectez-vous à la [console Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Accédez à **Buckets** et créez un bucket s'il n'en existe pas déjà. Notez le nom du bucket.
3. Accédez à **App Keys**
4. Sélectionnez **Add a New Application Key**
5. Donnez un nom à la clé, sélectionnez le bucket auquel elle doit avoir accès et choisissez les autorisations appropriées (lecture et écriture)
6. Sélectionnez **Create New Key**
7. Copiez le **keyID** (c'est votre clé d'accès) et l'**applicationKey** (c'est votre clé secrète). Conservez les deux pour la configuration de PlaidCloud Document ci-dessous. L'application key n'est affichée qu'une seule fois.
8. Notez le **S3 Endpoint** de la région de votre bucket. Il suit le modèle `https://s3.{region}.backblazeb2.com` (p. ex. `https://s3.us-west-004.backblazeb2.com`). Vous le trouverez sur la page de détails du bucket.

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte Backblaze B2 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Backblaze B2` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le **Chemin de départ** sous la forme de votre point de terminaison compatible S3 suivi du nom du bucket : `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Saisissez la **Région** de votre bucket (p. ex. `us-west-004`)
9. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
10. Collez le **keyID** dans le champ ID de clé d'accès sous Identifiants d'authentification
11. Collez l'**applicationKey** dans le champ Clé d'accès secrète sous Identifiants d'authentification
12. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
