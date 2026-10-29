---
title: Ajouter un compte DigitalOcean Spaces
description: Ajoutez un compte de stockage DigitalOcean Spaces à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage d'objets compatible S3 de DigitalOcean.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Configuration de DigitalOcean Spaces

Ces étapes doivent être effectuées dans le panneau de contrôle DigitalOcean.

1. Connectez-vous au [panneau de contrôle DigitalOcean](https://cloud.digitalocean.com)
2. Accédez à **Spaces Object Storage** dans la barre latérale gauche
3. Créez un Space s'il n'en existe pas déjà. Notez le nom du Space et la région (p. ex. `nyc3`).
4. Accédez à **API > Spaces Keys** (dans la section Tokens)
5. Sélectionnez **Generate New Key**
6. Donnez un nom à la clé
7. Copiez la **Key** (clé d'accès) et le **Secret**. Conservez les deux pour la configuration de PlaidCloud Document ci-dessous. Le secret n'est affiché qu'une seule fois.
8. Notez l'URL du point de terminaison de la région de votre Space. Elle suit le modèle `https://{region}.digitaloceanspaces.com` (p. ex. `https://nyc3.digitaloceanspaces.com`)

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte DigitalOcean Spaces à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `DigitalOcean Spaces` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le **Chemin de départ** sous la forme de l'URL du point de terminaison suivie du nom du Space : `https://nyc3.digitaloceanspaces.com/my-space`
8. Saisissez la **Région** (p. ex. `nyc3`, `sfo3`, `ams3`)
9. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
10. Collez la **Key** dans le champ ID de clé d'accès sous Identifiants d'authentification
11. Collez le **Secret** dans le champ Clé d'accès secrète sous Identifiants d'authentification
12. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
