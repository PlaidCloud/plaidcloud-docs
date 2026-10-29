---
title: Ajouter de nouveaux comptes de documents
description: "Connectez à PlaidCloud un stockage de documents cloud et sur site : S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV, et plus encore."
sidebar:
  label: Ajouter de nouveaux comptes de documents
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Connectez à PlaidCloud un stockage de documents cloud et sur site : S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV, et plus encore. Chaque fournisseur a ses propres identifiants et son propre flux de connexion.

L'option la plus rapide est un **Bucket géré par PlaidCloud** : PlaidCloud met en place et exploite le stockage pour vous, et il vous suffit de choisir un nom, sans rien d'autre à configurer. Pour connecter un stockage que vous possédez déjà, choisissez le fournisseur correspondant ci-dessous.

## Les secrets enregistrés sont en écriture seule

Le secret d'un compte, c'est-à-dire le champ intitulé **Clé privée / Mot de passe** ou, selon le type de compte, **Clé d'accès secrète**, **Clé du compte**, **Secret client**, **Jeton d'accès**, **Mot de passe**, **Clé JSON de l'utilisateur système** ou **Identifiants OAuth2 JSON**, est en écriture seule, tout comme la **clé privée RSA** d'un compte SFTP. Une fois enregistrés, ils ne sont plus jamais affichés, ni dans le formulaire, ni dans l'API, ni pour un assistant IA. Lorsque vous modifiez un compte, le champ est vide, avec l'indication *Collez la valeur ; laissez vide lors de la modification pour conserver celle qui est enregistrée.* Laissez-le vide pour conserver le secret enregistré, ou collez-en un nouveau pour le remplacer.

Modifier l'endroit où un compte se connecte exige de saisir de nouveau son secret. Si vous modifiez la première partie du **Chemin de départ** (pour un stockage cloud, le bucket ou le conteneur), l'**Hôte ou adresse IP** ou le **Port de connexion SSH** d'un compte SFTP, ou l'**ID de locataire OneDrive** d'un compte OneDrive, collez également le secret, faute de quoi l'enregistrement est refusé avec le message *Changing where the account connects needs its secret entered again*. Cela empêche toute personne pouvant modifier un compte sans avoir jamais vu son secret d'envoyer ce secret vers un serveur de son choix.

Un assistant IA connecté via le connecteur MCP de PlaidCloud peut également créer et mettre à jour des comptes, avec un type de stockage, des identifiants et un chemin de départ. Les identifiants sont en écriture seule et masqués lorsque le compte est relu. Pour un exemple détaillé, consultez [Ajouter un compte OneDrive / SharePoint](/fr/guides/documents/adding-accounts/add-onedrive-account/#créer-le-compte-avec-un-assistant-ia).
