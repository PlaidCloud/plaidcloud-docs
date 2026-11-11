---
title: Ajouter un compte Linode Object Storage
description: Ajoutez un compte Linode (Akamai) Object Storage à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage cloud compatible S3 de Linode.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Configuration de Linode Object Storage

Ces étapes doivent être réalisées dans le Linode Cloud Manager.

1. Connectez-vous au [Linode Cloud Manager](https://cloud.linode.com)
2. Accédez à **Object Storage** dans la barre latérale gauche
3. Créez un bucket s'il n'en existe pas encore. Notez le nom du bucket (appelé **libellé**) et sa région (par ex. `us-east-1`).
4. Accédez à **Object Storage > Access Keys**
5. Sélectionnez **Create Access Key**
6. Donnez un libellé à la clé et sélectionnez le ou les buckets auxquels elle doit avoir accès, avec des autorisations de lecture et d'écriture
7. Sélectionnez **Create Access Key**
8. Copiez la **clé d'accès** et la **clé secrète**. Conservez-les pour la configuration de PlaidCloud Document ci-dessous. Le secret ne s'affiche qu'une seule fois.
9. Notez l'URL du point de terminaison correspondant à la région de votre bucket. Elle suit le modèle `https://{region}.linodeobjects.com` (par ex. `https://us-east-1.linodeobjects.com`)

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte Linode Object Storage à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Linode Object Storage` comme Type de service
6. Saisissez un nom et une description
7. Dans le champ **Chemin de départ**, saisissez l'URL du point de terminaison suivie du nom du bucket : `https://us-east-1.linodeobjects.com/my-bucket`
8. Saisissez la **Région** (par ex. `us-east-1`)
9. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
10. Collez la **clé d'accès** dans le champ ID de clé d'accès, sous Identifiants d'authentification
11. Collez la **clé secrète** dans le champ Clé d'accès secrète, sous Identifiants d'authentification
12. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel
