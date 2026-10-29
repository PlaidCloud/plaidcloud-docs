---
title: Mise à niveau
description: Mettez à niveau votre agent PlaidLink vers la dernière version pour bénéficier des nouvelles fonctionnalités, des correctifs de sécurité et d'une meilleure compatibilité système.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Une mise à niveau manuelle de PlaidLink peut être nécessaire si l'agent ne dispose pas des privilèges suffisants pour se mettre à jour lui-même lors de la publication de nouvelles versions, ou si vous préférez procéder manuellement.

## Télécharger l'agent

Consultez les versions publiées sur [PlaidCloud.com](https://plaidcloud.com/) pour **PlaidLink**.

## Arrêter l'agent actuel

Saisissez **`Services`** dans la barre de recherche de Windows et ouvrez le gestionnaire de services. Dans la liste des services, repérez **`PlaidCloud Agent`**.

Effectuez un clic droit sur le service **`PlaidCloud Agent`** et sélectionnez *Stop*.  Une fois le service arrêté, passez à l'étape suivante.

## Extraire l'agent

Accédez à l'emplacement actuel de l'agent installé.

```bash
C:\Users\<Username here>\src\
```

Renommez le dossier d'installation actuel afin qu'il ne soit plus référencé.  Par exemple : `Plaidlink_Old_12122022`

Extrayez le fichier zip téléchargé pour l'installer à cet emplacement. En général, cet emplacement est le suivant :

```bash
C:\Users\<Username here>\src\plaidlink
```

## Démarrer l'agent

Revenez à la fenêtre *Services*.  Effectuez un clic droit sur le service **`PlaidCloud Agent`** et sélectionnez *Start*.

Saisissez **`Services`** dans la barre de recherche de Windows et ouvrez le gestionnaire de services. Dans la liste des services, repérez **`PlaidCloud Agent`**.

Effectuez un clic droit sur le service et sélectionnez **`Start`**.  Lorsque l'agent passe à l'état **`Running`**, il est de nouveau opérationnel sur la nouvelle version.
