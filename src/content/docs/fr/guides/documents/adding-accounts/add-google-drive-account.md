---
title: Ajouter un compte Google Drive
description: Ajoutez un compte de stockage Google Drive à PlaidCloud pour importer et exporter des fichiers de données à l'aide du stockage cloud Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Configuration de Google Drive

Ces étapes doivent être réalisées dans la console Google Cloud afin de créer un compte de service que PlaidCloud pourra utiliser pour accéder à Google Drive.

### Créer un projet Google Cloud

1. Connectez-vous à la [console Google Cloud](https://console.cloud.google.com)
2. Créez un projet ou sélectionnez un projet existant

### Activer l'API Google Drive

1. Accédez à **APIs & Services > Library**
2. Recherchez **Google Drive API**
3. Sélectionnez-la et cliquez sur **Activer**

### Créer un compte de service

1. Accédez à **APIs & Services > Credentials**
2. Sélectionnez **+ Create Credentials > Service account**
3. Saisissez un nom pour le compte de service (par ex. `plaidcloud-drive`)
4. Sélectionnez **Create and Continue**
5. Attribuez éventuellement des rôles (par ex. **Lecteur** pour un accès en lecture seule, ou **Éditeur** pour un accès en lecture et écriture). Sélectionnez **Continuer**.
6. Sélectionnez **Terminé**

### Générer une clé de compte de service

1. Dans la liste **Service Accounts**, sélectionnez le compte de service que vous venez de créer
2. Accédez à l'onglet **Keys**
3. Sélectionnez **Add Key > Create new key**
4. Choisissez le format **JSON** et sélectionnez **Créer**
5. Un fichier de clé JSON est téléchargé. Conservez ce fichier en lieu sûr : il contient les identifiants que PlaidCloud utilisera.

### Partager le contenu de Drive avec le compte de service

1. Copiez l'adresse e-mail du compte de service (par ex. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. Dans Google Drive, partagez avec cette adresse e-mail le ou les dossiers auxquels PlaidCloud doit accéder, en accordant l'accès **Éditeur**. Pour utiliser un Drive partagé, ajoutez plutôt le compte de service comme membre de ce Drive.

Vous disposez maintenant de tout le nécessaire pour ajouter votre compte Google Drive à PlaidCloud Document.


## Configuration de PlaidCloud Document

1. Connectez-vous à PlaidCloud
2. Sélectionnez l'espace de travail dans lequel le nouveau compte de documents sera créé
3. Accédez à `Document > Manage`
4. Sélectionnez le bouton **Nouveau compte**
5. Sélectionnez `Google Drive` comme Type de service
6. Saisissez un nom et une description
7. Saisissez le chemin du dossier partagé dans le champ **Chemin de départ**, ou laissez-le vide pour accéder à l'ensemble du contenu partagé
8. Sélectionnez le **Modèle de sécurité** adapté à votre cas d'usage. En cas de doute, conservez `Private`.
9. Collez l'intégralité du contenu du fichier de clé JSON dans le champ de clé privée du compte, sous Identifiants d'authentification
10. Sélectionnez le bouton Enregistrer : votre nouveau compte de documents est opérationnel

## Utiliser le compte dans les workflows

Un compte Google Drive fonctionne dans les workflows comme dans le navigateur Document. Les étapes peuvent lister, importer, exporter, copier, déplacer, renommer et supprimer des fichiers, et créer des dossiers.

- **Emplacements.** Les emplacements de premier niveau du compte sont les dossiers partagés avec le compte de service et les Drives partagés dont il est membre. Les chemins sont des noms de dossiers, comme `Finance/Reports/2026`. Si deux dossiers partagés ou Drives partagés portent le même nom, le compte refuse d'ouvrir ce nom. Renommez ou cessez de partager tous les éléments sauf un.
- **Google Sheets.** Un Google Sheet est lu sous la forme d'un export `.xlsx` et apparaît sous le nom `Name.xlsx`. Les autres fichiers Google Workspace, tels que Docs et Slides, ne peuvent pas être lus.
- **Nouveaux fichiers dans Mon Drive.** Un compte de service n'a pas de stockage propre : dans un dossier qui se trouve dans le Mon Drive personnel d'un utilisateur, il peut écraser un fichier existant mais pas en créer un nouveau. Créez d'abord le fichier à cet endroit, ou utilisez un dossier d'un Drive partagé, qui accepte les nouveaux fichiers et dossiers.
- **Dossiers manquants.** Un dossier qui n'existe pas est listé comme vide au lieu de provoquer une erreur.
- **Limitation de débit.** PlaidCloud réessaie automatiquement lorsque Google limite le débit d'une requête ou renvoie une erreur temporaire.
