---
title: Ajouter un compte Azure Data Lake Gen2
description: Ajoutez un compte Azure Data Lake Storage Gen2 à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage à espace de noms hiérarchique d'Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Configuration d'Azure Data Lake Gen2

Azure Data Lake Storage Gen2 repose sur Azure Blob Storage avec un espace de noms hiérarchique activé. Ces étapes doivent être réalisées dans le portail Azure.

1. Connectez-vous au [portail Azure](https://portal.azure.com)
2. Accédez à **Storage accounts**, puis sélectionnez ou créez un compte de stockage dont l'option **Hierarchical namespace** est activée
3. Dans la barre latérale gauche, sous **Security + networking**, sélectionnez **Access keys**
4. Copiez le **Storage account name** et l'une des valeurs **Clé**. Conservez-les pour la configuration de PlaidCloud Document ci-dessous.
5. Accédez à **Containers** sous **Data storage** et créez un système de fichiers (conteneur) s'il n'en existe pas encore. Notez le nom du système de fichiers.

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte Azure Data Lake Gen2 à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Azure Data Lake Gen2` comme Type de service
6. Saisissez un nom et une description
7. Saisissez le nom du système de fichiers et un préfixe de chemin facultatif dans le champ **Chemin de départ** (par ex. `my-filesystem/data`). Le premier segment du chemin correspond au nom du système de fichiers.
8. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
9. Collez le **Storage account name** dans le champ Nom du compte, sous Identifiants d'authentification
10. Collez la **Clé** dans le champ Clé du compte, sous Identifiants d'authentification
11. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel
