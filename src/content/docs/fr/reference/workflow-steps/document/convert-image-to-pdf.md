---
title: Convert Image to PDF
description: "Convertissez des fichiers image en documents PDF dans une étape de workflow PlaidCloud pour obtenir une sortie de documents standardisée et des formats prêts pour l'archivage."
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Transforme une image (PNG, GIF, TIFF, JPEG ou HEIC) en PDF d'une page, ou réajuste un PDF existant à un format de page standard.

## Entrées

- **Fichier ou répertoire d'entrée** : une image ou un PDF, ou un dossier de fichiers de ce type, dans un compte de documents.
- **Destination** : l'emplacement où le PDF est écrit.
- **Taille de page** : US Letter, US Legal, A3, A4 ou A5.
- **Compression** : **Lossy** ramène les images à la résolution d'écran et peut réduire considérablement le fichier ; **Lossless**, la valeur par défaut, conserve exactement les données d'image.

## Fonctionnement

- Une image est placée sur une page du format choisi, mise à l'échelle pour y tenir sans modifier ses proportions. Une image comportant plusieurs pages ou trames, comme un TIFF numérisé, est convertie à partir de la première.
- Avec **Lossy**, le résultat est ensuite compressé, et un PDF en entrée est ajusté au format de page choisi pendant la compression.
- Avec **Lossless**, un PDF en entrée est transmis tel quel et conserve son propre format de page.

## Sortie

Un PDF par fichier d'entrée. Pour un dossier, le PDF de chaque fichier est écrit dans un dossier portant le nom de la destination, sans son extension, sous le propre nom du fichier source. Pour en combiner plusieurs dans un seul document, faites suivre cette étape de [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/).

## Remarques

- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- La destination ne peut pas être le chemin d'entrée.

## Usages courants

- Standardiser des images de reçus ou de factures dans un format d'archivage
- Préparer des images servant de preuve pour des systèmes qui n'acceptent que des PDF en entrée

## Voir aussi

- [Convert PDF or image to JPEG](/fr/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/fr/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/)
