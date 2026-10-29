---
title: Ajouter un compte Azure Blob Storage
description: Ajoutez un compte Azure Blob Storage à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets cloud de Microsoft Azure.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Configuration d'Azure Blob Storage

Ces étapes doivent être effectuées dans le portail Azure.

1. Connectez-vous au [portail Azure](https://portal.azure.com)
2. Accédez à **Storage accounts** et sélectionnez ou créez un compte de stockage
3. Dans la barre latérale gauche, sous **Security + networking**, sélectionnez **Access keys**
4. Copiez le **Storage account name** et l'une des valeurs **Key**. Conservez les deux pour la configuration de PlaidCloud Document ci-dessous.
5. Accédez à **Containers** sous **Data storage** et créez un conteneur s'il n'en existe pas déjà. Notez le nom du conteneur.

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte Azure Blob Storage à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Azure Blob Storage` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le nom du conteneur et un préfixe de chemin facultatif dans le champ **Chemin de départ** (p. ex. `my-container/data`). Le premier segment du chemin est le nom du conteneur.
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Collez le **Storage account name** dans le champ Nom du compte sous Identifiants d'authentification
10. Collez la **Key** dans le champ Clé du compte sous Identifiants d'authentification
11. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
