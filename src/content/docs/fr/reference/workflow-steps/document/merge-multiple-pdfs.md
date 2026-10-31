---
title: Étape Merge Multiple PDFs
description: Fusionnez plusieurs fichiers PDF en un seul document dans une étape de workflow PlaidCloud pour assembler et consolider des rapports.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Réunit les PDF d'un dossier en un seul PDF. Contrairement à [Concatenate files](/fr/reference/workflow-steps/document/concatenate-files/), cette étape comprend le format PDF et produit un document fusionné valide.

## Entrées

- **Répertoire d'entrée** — le dossier dont les PDF sont fusionnés, dans un compte de documents. Vous pouvez indiquer à la place une archive unique, comme un ZIP de PDF, et les PDF qu'elle contient sont fusionnés.
- **Fichier fusionné de sortie** — l'emplacement où le PDF fusionné est écrit.

## Fonctionnement

- Les PDF sont fusionnés dans l'ordre de leur chemin, les nombres étant pris selon leur valeur (`page2.pdf` précède `page10.pdf`) ; numérotez-les donc pour contrôler l'ordre. Chacun conserve ses propres pages dans l'ordre.
- Seuls les fichiers nommés `.pdf` sont fusionnés. Tout le reste du dossier est ignoré, et une archive présente dans le dossier n'est pas ouverte.
- Les fichiers des sous-dossiers sont inclus lorsque le compte de documents les liste : les comptes S3, Wasabi et Google Cloud Storage listent toute l'arborescence du dossier, tandis que les comptes OneDrive, SFTP et Azure ne listent que le premier niveau.
- 100 PDF au maximum sont fusionnés ; au-delà, l'étape échoue.

## Sortie

Un seul PDF au chemin de sortie, contenant toutes les pages de tous les PDF fusionnés.

## Remarques

- Un dossier sans PDF, ou inexistant, termine l'étape par un avertissement indiquant le dossier, ne fusionne rien, et le workflow continue.
- Le chemin de sortie ne peut pas être le chemin d'entrée.

## Cas d'usage courants

- Assembler des rapports mensuels à partir de PDF de rapports individuels
- Combiner une page de garde, un corps de texte et des annexes en un seul livrable
- Regrouper des factures générées dans une archive par client ou par période

## Voir aussi

- [Compress PDF](/fr/reference/workflow-steps/document/compress-pdf/) — réduit la taille du résultat fusionné
- [Convert image to PDF](/fr/reference/workflow-steps/document/convert-image-to-pdf/) — transforme des images en PDF avant la fusion
