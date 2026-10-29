---
title: Ajouter un compte Bucket géré par PlaidCloud
description: Ajoutez un stockage de fichiers entièrement géré à PlaidCloud Document en une seule étape — choisissez un nom et PlaidCloud configure tout pour vous, sans rien à paramétrer.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Un **Bucket géré par PlaidCloud** est le moyen le plus rapide d'ajouter du stockage de fichiers à Document. PlaidCloud crée et exploite le stockage pour vous — rien à configurer au préalable et aucun identifiant à gérer. Il vous suffit de lui donner un nom.

Utilisez un Bucket géré par PlaidCloud lorsque vous souhaitez un nouvel espace autonome pour conserver des fichiers Document. Pour connecter un stockage que vous possédez et gérez déjà vous-même, choisissez plutôt l'un des autres fournisseurs de la page [Ajouter de nouveaux comptes de documents](/fr/guides/documents/adding-accounts/).

## Configuration

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `PlaidCloud Managed Bucket` comme Type de service
6. Renseignez un nom et une description facultative
7. Saisissez un **Nom du bucket**. Les noms doivent comporter de 3 à 63 caractères, n'utiliser que des lettres minuscules, des chiffres, des points ou des tirets, et commencer et se terminer par une lettre ou un chiffre. Le nom doit être **unique à l'échelle mondiale** — s'il est déjà utilisé, il vous sera demandé d'en choisir un autre
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`
9. Cliquez sur le bouton Enregistrer

PlaidCloud configure le stockage et fait de vous son propriétaire. Le compte est immédiatement prêt pour la navigation et le téléversement — il n'y a rien d'autre à configurer.

:::note
Les Buckets gérés par PlaidCloud sont disponibles avec les offres **Business** et **Enterprise**. Si votre offre ne les inclut pas, ou si vous avez atteint la limite de votre offre, le formulaire vous en informe lorsque vous essayez d'en créer un.
:::

## Après la création

- Le nom du bucket est figé une fois créé — il ne peut pas être modifié sur un compte existant.
- La suppression du compte **laisse les fichiers stockés en place** ; une suppression ne détruit donc jamais vos données. Contactez le support si vous avez besoin que le stockage lui-même soit supprimé.
- Un Bucket géré par PlaidCloud se comporte comme n'importe quel autre compte de documents pour le [contrôle d'accès](/fr/guides/documents/account-management/control-document-account-access/), la [propriété](/fr/guides/documents/account-management/managing-document-account-owners/) et la navigation.
