---
title: Ajouter un compte Google Drive
description: Ajoutez un compte de stockage Google Drive à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage cloud Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Configuration de Google Drive

Ces étapes doivent être effectuées dans la console Google Cloud pour créer un compte de service que PlaidCloud peut utiliser pour accéder à Google Drive.

### Créer un projet Google Cloud

1. Connectez-vous à la [console Google Cloud](https://console.cloud.google.com)
2. Créez un projet ou sélectionnez-en un existant

### Activer l'API Google Drive

1. Accédez à **APIs & Services > Library**
2. Recherchez **Google Drive API**
3. Sélectionnez-la et cliquez sur **Enable**

### Créer un compte de service

1. Accédez à **APIs & Services > Credentials**
2. Sélectionnez **+ Create Credentials > Service account**
3. Saisissez un nom pour le compte de service (p. ex. `plaidcloud-drive`)
4. Sélectionnez **Create and Continue**
5. Si vous le souhaitez, accordez des rôles (p. ex. **Viewer** pour la lecture seule, ou **Editor** pour la lecture et l'écriture). Sélectionnez **Continue**.
6. Sélectionnez **Done**

### Générer une clé de compte de service

1. Dans la liste **Service Accounts**, sélectionnez le compte de service que vous venez de créer
2. Accédez à l'onglet **Keys**
3. Sélectionnez **Add Key > Create new key**
4. Choisissez le format **JSON** et sélectionnez **Create**
5. Un fichier de clé JSON est téléchargé. Conservez ce fichier en lieu sûr — il contient les identifiants que PlaidCloud utilisera.

### Partager le contenu de Drive avec le compte de service

1. Copiez l'adresse e-mail du compte de service (p. ex. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. Dans Google Drive, partagez avec cette adresse e-mail le ou les dossiers auxquels PlaidCloud doit accéder, en accordant l'accès **Editor**

Vous devriez maintenant disposer de tout ce qu'il faut pour ajouter votre compte Google Drive à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents résidera
3. Accédez à `Document > Manage Accounts`
4. Cliquez sur le bouton `+ New Account`
5. Sélectionnez `Google Drive` comme Type de service
6. Renseignez un nom et une description
7. Saisissez le chemin du dossier partagé dans le champ **Chemin de départ**, ou laissez-le vide pour accéder à tout le contenu partagé
8. Sélectionnez un **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, laissez `Private`.
9. Collez l'intégralité du contenu du fichier de clé JSON dans le champ Identifiants OAuth2 JSON sous Identifiants d'authentification
10. Cliquez sur le bouton Enregistrer et votre nouveau compte de documents est actif
