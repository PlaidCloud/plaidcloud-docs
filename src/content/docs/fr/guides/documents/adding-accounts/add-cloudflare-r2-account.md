---
title: Ajouter un compte Cloudflare R2
description: Ajoutez un compte de stockage Cloudflare R2 à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets de Cloudflare, sans frais de sortie.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Configuration de Cloudflare R2

Ces étapes doivent être réalisées dans le tableau de bord Cloudflare.

1. Connectez-vous au [tableau de bord Cloudflare](https://dash.cloudflare.com)
2. Sélectionnez votre compte, puis accédez à **R2 Object Storage** dans la barre latérale gauche
3. Créez un bucket s'il n'en existe pas encore. Notez le nom du bucket.
4. Accédez à **R2 Object Storage > Manage R2 API Tokens**
5. Sélectionnez **Create API Token**
6. Donnez un nom au jeton, sélectionnez le ou les buckets auxquels il doit avoir accès et choisissez les autorisations **Object Read & Write**
7. Sélectionnez **Create API Token**
8. Copiez l'**ID de clé d'accès** et la **Clé d'accès secrète**. Conservez-les pour la configuration de PlaidCloud Document ci-dessous. Le secret ne s'affiche qu'une seule fois.
9. Notez le **point de terminaison de l'API S3** de votre compte. Il suit le modèle `https://{account_id}.r2.cloudflarestorage.com` et s'affiche sur la page de vue d'ensemble de R2.

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte Cloudflare R2 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Cloudflare R2` comme Type de service
6. Saisissez un nom et une description
7. Dans le champ **Chemin de départ**, saisissez votre point de terminaison R2 suivi du nom du bucket : `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. Le champ **Région** peut être défini sur `auto` ou laissé vide : R2 sélectionne automatiquement la région la plus proche
9. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
10. Collez l'**ID de clé d'accès** dans le champ ID de clé d'accès, sous Identifiants d'authentification
11. Collez la **Clé d'accès secrète** dans le champ Clé d'accès secrète, sous Identifiants d'authentification
12. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel
