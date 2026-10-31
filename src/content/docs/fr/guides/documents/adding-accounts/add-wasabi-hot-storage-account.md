---
title: Ajouter un compte Wasabi Hot Storage
description: Ajoutez un compte Wasabi Hot Storage à PlaidCloud pour importer et exporter des fichiers de données à l'aide d'un stockage cloud économique.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Configuration de Wasabi Hot Storage


Ces étapes doivent être réalisées dans la console Wasabi Hot Storage.


1. Connectez-vous à un compte Wasabi Hot Storage ou créez-en un.
2. Accédez à `Buckets` dans la console.
3. Créez un bucket par défaut ou de test.
4. Accédez à Users dans la console.
5. Sélectionnez le bouton `Create User`.
6. Lorsque vous y êtes invité, saisissez un nom d'utilisateur et sélectionnez un utilisateur `Programmatic (create API key)`.
7. Ignorez l'affectation à un groupe. Sélectionnez le bouton `Next`.
8. Sélectionnez l'icône plus à côté de la stratégie `WasabiFullAccess` pour l'associer à l'utilisateur. Sélectionnez le bouton `Next`.
9. Vérifiez les paramètres de l'utilisateur et sélectionnez `Create User`.
10. Récupérez les clés générées pour l'utilisateur en téléchargeant le fichier CSV ou en les copiant-collant quelque part pour un usage ultérieur. Vous ne pourrez plus récupérer cette clé ; conservez-la donc précieusement. Si vous devez régénérer une clé, revenez simplement à l'étape 5 ci-dessus.

Vous disposez maintenant de tout ce qu'il faut pour ajouter votre compte Wasabi à PlaidCloud Document.



## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud.
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé.
3. Accédez à `Document > Manage Accounts`.
4. Sélectionnez le bouton `+ New Account`.
5. Sélectionnez `Wasabi Hot Storage` comme Type de service.
6. Renseignez un nom et une description.
7. Saisissez le nom du bucket et un préfixe de chemin facultatif dans le champ **Chemin de départ** (par exemple `my-bucket` ou `my-bucket/data`). Le premier segment du chemin est le nom du bucket.
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Collez la **Access Key** créée à l'étape 10 ci-dessus dans le champ ID de clé d'accès sous Identifiants d'authentification.
10. Collez la **Secret Key** créée à l'étape 10 ci-dessus dans le champ Clé d'accès secrète sous Identifiants d'authentification.
11. Saisissez la **Région** si votre compte Wasabi utilise une région spécifique ; sinon, laissez le champ vide.
12. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel.
