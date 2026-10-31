---
title: Convert PDF or Image to JPEG
description: "Convertissez des pages PDF ou des images au format JPEG dans une étape de workflow PlaidCloud pour obtenir une sortie compatible avec le web et traiter des images."
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Convertit un PDF ou une image en JPEG. La première page d'un PDF devient le JPEG ; une image est réencodée, et une image comportant plusieurs pages ou trames, comme un TIFF numérisé, est convertie à partir de la première.

## Entrées

- **Fichier ou répertoire d'entrée** : un PDF ou une image (PNG, GIF, TIFF, JPEG ou HEIC), ou un dossier de fichiers de ce type, dans un compte de documents.
- **Fichier ou répertoire de sortie** : l'emplacement où le JPEG est écrit.

## Sortie

Un JPEG par fichier d'entrée. Pour un dossier, le JPEG de chaque fichier est écrit dans un dossier portant le nom du chemin de sortie, sans son extension, sous le propre nom du fichier source.

## Remarques

- Un fichier de tout autre type fait échouer l'étape, en nommant les types acceptés.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- Le chemin de sortie ne peut pas être le chemin d'entrée.

## Usages courants

- Générer des images d'aperçu pour l'affichage sur le web
- Produire des versions image seule de PDF pour des systèmes qui ne gèrent pas le format PDF

## Voir aussi

- [Convert image to PDF](/fr/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/fr/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/fr/reference/workflow-steps/document/crop-image-to-headshot/)
