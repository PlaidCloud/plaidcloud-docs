---
title: Ajouter un compte Backblaze B2
description: Ajoutez un compte de stockage Backblaze B2 à PlaidCloud pour importer et exporter des fichiers de données à l'aide d'un stockage d'objets cloud économique.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Configuration de Backblaze B2

Ces étapes doivent être réalisées dans la console Backblaze B2.

1. Connectez-vous à la [console Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Accédez à **Buckets** et créez un bucket s'il n'en existe pas encore. Notez le nom du bucket.
3. Accédez à **App Keys**
4. Sélectionnez **Add a New Application Key**
5. Donnez un nom à la clé, sélectionnez le bucket auquel elle doit avoir accès et choisissez les autorisations appropriées (lecture et écriture)
6. Sélectionnez **Create New Key**
7. Copiez le **keyID** (votre clé d'accès) et l'**applicationKey** (votre clé secrète). Conservez-les pour la configuration de PlaidCloud Document ci-dessous. La clé d'application ne s'affiche qu'une seule fois.
8. Notez le **point de terminaison S3** correspondant à la région de votre bucket. Il suit le modèle `https://s3.{region}.backblazeb2.com` (par ex. `https://s3.us-west-004.backblazeb2.com`). Vous le trouverez sur la page de détails du bucket.

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte Backblaze B2 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Backblaze B2` comme Type de service
6. Saisissez un nom et une description
7. Dans le champ **Chemin de départ**, saisissez votre point de terminaison compatible S3 suivi du nom du bucket : `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Saisissez la **Région** de votre bucket (par ex. `us-west-004`)
9. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
10. Collez le **keyID** dans le champ ID de clé d'accès, sous Identifiants d'authentification
11. Collez l'**applicationKey** dans le champ Clé d'accès secrète, sous Identifiants d'authentification
12. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel
