---
title: Compress PDF
description: "Compressez des fichiers PDF dans une étape de workflow PlaidCloud pour réduire leur taille tout en préservant la qualité des documents et en économisant de l'espace de stockage."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Réduit la taille d'un PDF stocké dans un compte de documents. Utile pour alléger de gros documents numérisés avant de les archiver, de les joindre à des notifications ou de les déplacer entre comptes de documents.

## Entrées

- **Fichier ou répertoire d'entrée** : un PDF, ou un dossier de PDF, dans un compte de documents.
- **Fichier ou répertoire de sortie** : l'emplacement où le PDF compressé est écrit.

## Fonctionnement

Le PDF est réécrit avec ses images ramenées à la résolution d'écran (72 ppp) et ses polices intégrées sous forme de sous-ensembles, ce qui peut réduire considérablement la taille des documents numérisés ; le texte reste net. Les pages sont ajustées au format US Letter.

## Sortie

Un PDF compressé au chemin de sortie. Pour un dossier, chaque PDF est écrit sous le chemin de sortie, en conservant sa place relative au dossier d'entrée.

## Remarques

- Le chemin de sortie ne peut pas être le chemin d'entrée, de sorte que la source n'est jamais écrasée.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- Un PDF qui ne peut pas être compressé fait échouer l'étape, en nommant le fichier et la raison.

## Usages courants

- Réduire la taille de factures, de reçus ou de contrats numérisés avant un stockage à long terme
- Réduire la taille d'un PDF avant de l'envoyer par e-mail ou de le joindre à des notifications
- Préparer des documents pour les téléverser vers des systèmes en aval dont la taille est limitée

## Voir aussi

- [Convert PDF or image to JPEG](/fr/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guide des documents](/fr/guides/documents/)
