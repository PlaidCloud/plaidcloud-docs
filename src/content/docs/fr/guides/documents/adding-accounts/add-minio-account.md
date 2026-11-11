---
title: Ajouter un compte MinIO
description: Ajoutez un compte de stockage MinIO à PlaidCloud pour importer et exporter des fichiers de données à l'aide d'un stockage d'objets auto-hébergé compatible S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Configuration de MinIO

Ces étapes doivent être réalisées dans la console MinIO ou à l'aide de la CLI `mc`.

1. Connectez-vous à la console MinIO (par ex. `https://your-minio-host:9001`)
2. Accédez à **Buckets** et créez un bucket s'il n'en existe pas encore. Notez le nom du bucket.
3. Accédez à **Identity > Users** (ou **Access Keys**)
4. Créez un utilisateur ou un compte de service disposant d'un accès en lecture et écriture au bucket cible
5. Copiez la **clé d'accès** et la **clé secrète** générées pour l'utilisateur. Conservez-les pour la configuration de PlaidCloud Document ci-dessous.
6. Notez l'URL du point de terminaison MinIO (par ex. `https://play.min.io` ou `https://minio.yourcompany.com`)

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte MinIO à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `MinIO` comme Type de service
6. Saisissez un nom et une description
7. Dans le champ **Chemin de départ**, saisissez l'URL de votre point de terminaison MinIO suivie du nom du bucket et d'un préfixe facultatif : `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Saisissez la **Région** si votre déploiement MinIO utilise des régions ; sinon, laissez ce champ vide
9. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
10. Collez la **clé d'accès** dans le champ ID de clé d'accès, sous Identifiants d'authentification
11. Collez la **clé secrète** dans le champ Clé d'accès secrète, sous Identifiants d'authentification
12. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel
