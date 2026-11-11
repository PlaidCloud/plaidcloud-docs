---
title: Ajouter un compte de bucket géré par PlaidCloud
description: Ajoutez en une seule étape un stockage de fichiers entièrement géré à PlaidCloud Document. Choisissez un nom et PlaidCloud configure tout pour vous, sans rien à paramétrer.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Un **Bucket géré par PlaidCloud** est le moyen le plus rapide d'ajouter du stockage de fichiers à Document. PlaidCloud crée et exploite le stockage pour vous : rien à configurer au préalable et aucun identifiant à gérer. Il vous suffit de lui donner un nom.

Utilisez un bucket géré par PlaidCloud lorsque vous souhaitez disposer d'un nouvel emplacement autonome pour conserver vos fichiers Document. Pour connecter un stockage que vous possédez et gérez vous-même, choisissez plutôt l'un des autres fournisseurs de la page [Ajout de nouveaux comptes de documents](/fr/guides/documents/adding-accounts/).

## Configuration

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `PlaidCloud Managed Bucket` comme Type de service
6. Saisissez un nom et, éventuellement, une description
7. Saisissez un **Nom du bucket**. Le nom doit comporter de 3 à 63 caractères, n'utiliser que des lettres minuscules, des chiffres, des points ou des traits d'union, et commencer et se terminer par une lettre ou un chiffre. Il doit être **unique au niveau mondial** : s'il est déjà utilisé, vous serez invité à en choisir un autre
8. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`
9. Sélectionnez le bouton Enregistrer

PlaidCloud configure le stockage et vous en désigne propriétaire. Le compte est immédiatement prêt pour la navigation et le téléversement de fichiers : il n'y a rien d'autre à configurer.

:::note
Les buckets gérés par PlaidCloud sont disponibles avec les offres **Business** et **Enterprise**. Si votre offre ne les inclut pas, ou si vous avez atteint la limite de votre offre, le formulaire vous l'indique lorsque vous essayez d'en créer un.
:::

## Après la création

- Le nom du bucket est définitif une fois le bucket créé : il ne peut pas être modifié sur un compte existant.
- La suppression du compte **laisse les fichiers stockés en place** : une suppression ne détruit donc jamais vos données. Contactez le support si vous avez besoin de supprimer le stockage lui-même.
- Un bucket géré par PlaidCloud se comporte comme n'importe quel autre compte de documents pour le [contrôle d'accès](/fr/guides/documents/account-management/control-document-account-access/), la [propriété](/fr/guides/documents/account-management/managing-document-account-owners/) et la navigation.
