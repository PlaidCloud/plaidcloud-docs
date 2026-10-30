---
title: Crop Image to Headshot
description: "Recadrez des images en portrait carré dans une étape de workflow PlaidCloud pour obtenir des portraits standardisés dans les annuaires et les badges."
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Recadre une image en un carré centré et la met à l'échelle en un JPEG de 500 × 500 pixels. Utile pour normaliser des annuaires d'employés ou de membres dont les photos source ont des proportions variables.

## Entrées

- **Fichier ou répertoire d'entrée** : une image, ou un dossier d'images, dans un compte de documents.
- **Fichier ou répertoire de sortie** : l'emplacement où le portrait est écrit.

## Sortie

Un JPEG de 500 × 500 recadré au centre de la source. Pour un dossier, le portrait de chaque fichier est écrit dans un dossier portant le nom du chemin de sortie, sans son extension.

## Remarques

- Le recadrage est effectué au centre de l'image ; il ne cherche pas de visage, donc cadrez les photos source avec le sujet au centre.
- Un fichier qui ne peut pas être lu comme une image est copié tel quel vers la sortie au lieu de faire échouer l'étape.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- Le chemin de sortie ne peut pas être le chemin d'entrée.

## Usages courants

- Standardiser les photos d'un annuaire d'employés
- Générer des images d'avatar homogènes pour un portail interne
- Recadrer des photos pour des badges d'identification et des accréditations

## Voir aussi

- [Convert PDF or image to JPEG](/fr/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/fr/reference/workflow-steps/document/fix-file-extension/)
