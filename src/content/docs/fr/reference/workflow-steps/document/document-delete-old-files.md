---
title: Étape Delete Old Files
description: Supprimez les fichiers d'un compte de documents plus anciens ou plus récents qu'un âge donné, avec une liste d'essai avant toute suppression.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Description

Supprime des fichiers d'un compte de documents en fonction de leur âge. Utilisez-la pour éviter qu'un dossier d'exportation ou de dépôt ne grossisse sans limite : supprimez les extractions de la veille ou videz les archives de plus d'un an.

## Configuration

### Fichiers à supprimer

- **Chemin du fichier** — le compte de documents et le dossier dans lesquels travailler.
- **Âge** — un nombre suivi d'une unité : minutes, heures, jours, mois ou années.
- **Avant ou après** — supprime les fichiers modifiés pour la dernière fois **avant** la date limite (le sens habituel du nettoyage) ou **après** celle-ci.
- **Récursif** — désactivé par défaut. Activez-le pour inclure les sous-dossiers.
- **Table des résultats du test** — la table dans laquelle le bouton **Tester** de l'éditeur d'étape écrit
  son aperçu des fichiers correspondants.

<Aside type="caution" title="Prévisualisez avec Tester, pas en exécutant l'étape">
  L'aperçu provient du bouton **Tester** pendant que vous modifiez l'étape.
  L'exécution de l'étape dans un workflow supprime toujours les fichiers : il n'existe pas de mode d'essai,
  et la table des résultats du test ne l'en détourne pas. La suppression est irréversible, et un
  chemin erroné avec **Récursif** activé touche plus de fichiers que prévu ; vérifiez donc
  l'aperçu avant de planifier l'étape.
</Aside>

## Voir aussi

- [Étapes Document](/fr/reference/workflow-steps/document/)
- [Delete Document File](/fr/reference/workflow-steps/document/delete-document-file/)
- [Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/)
