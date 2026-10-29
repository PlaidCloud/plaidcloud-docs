---
title: Ajouter un compte Azure Data Lake Gen2
description: Ajoutez un compte Azure Data Lake Storage Gen2 à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage à espace de noms hiérarchique sur Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Configuration d'Azure Data Lake Gen2

Azure Data Lake Storage Gen2 repose sur Azure Blob Storage avec un espace de noms hiérarchique activé. Ces étapes doivent être effectuées dans le portail Azure.

1. Connectez-vous au [portail Azure](https://portal.azure.com)
2. Accédez à **Storage accounts** et sélectionnez ou créez un compte de stockage pour lequel **Hierarchical namespace** est activé
3. Dans la barre latérale gauche, sous **Security + networking**, sélectionnez **Access keys**
4. Copiez le **Storage account name** et l'une des valeurs **Key**. Conservez les deux pour la configuration de PlaidCloud Document ci-dessous.
5. Accédez à **Containers** sous **Data storage** et créez un système de fichiers (conteneur) s'il n'en existe pas déjà. Notez le nom du système de fichiers.

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte Azure Data Lake Gen2 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Azure Data Lake Gen2` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le nom du système de fichiers et un préfixe de chemin facultatif dans le champ **Chemin de départ** (p. ex. `my-filesystem/data`). Le premier segment du chemin est le nom du système de fichiers.
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Collez le **Storage account name** dans le champ Nom du compte sous Identifiants d'authentification
10. Collez la **Key** dans le champ Clé du compte sous Identifiants d'authentification
11. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
