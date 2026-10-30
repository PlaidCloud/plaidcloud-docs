---
title: Étapes Document
description: Gérez les documents dans les workflows PlaidCloud avec des étapes de conversion, de copie, de renommage, de suppression de fichiers et d'opérations sur les PDF.
sidebar:
  label: Étapes Document
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Étapes de workflow pour agir sur les fichiers stockés dans des comptes de documents. Utilisez-les pour déplacer, transformer et convertir des documents en parallèle de vos workflows de données.

## Opérations sur les fichiers

- [Copy document file](/fr/reference/workflow-steps/document/copy-document-file/) · [Copy document directory](/fr/reference/workflow-steps/document/copy-document-directory/)
- [Create document directory](/fr/reference/workflow-steps/document/create-document-directory/)
- [Delete document file](/fr/reference/workflow-steps/document/delete-document-file/) · [Delete document directory](/fr/reference/workflow-steps/document/delete-document-directory/)
- [Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/) — écrit une table des fichiers d'un dossier
- [Update Excel Cells](/fr/reference/workflow-steps/document/document-excel-update/) — écrit des valeurs dans des cellules choisies d'un classeur, ou les met en forme
- [Fix file extension](/fr/reference/workflow-steps/document/fix-file-extension/)
- [Rename document file](/fr/reference/workflow-steps/document/rename-document-file/) · [Rename document directory](/fr/reference/workflow-steps/document/rename-document-directory/)

Les étapes de copie et de renommage considèrent une source absente comme normale. Lorsque le fichier, ou le dossier à copier ou à renommer, est absent, ou que le dossier est vide, l'étape ne fait rien, se termine par un avertissement indiquant le chemin, et le workflow continue. Une exécution planifiée sur un dossier sans fichier ce jour-là n'échoue plus.

## Chiffrement

- [Encrypt file · Decrypt file](/fr/reference/workflow-steps/document/encrypt-decrypt-file/) — AES, Blowfish ou mot de passe de classeur Excel

## Opérations sur les PDF

- [Compress PDF](/fr/reference/workflow-steps/document/compress-pdf/)
- [Convert image to PDF](/fr/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or image to JPEG](/fr/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/)

## Opérations sur les images

- [Crop image to headshot](/fr/reference/workflow-steps/document/crop-image-to-headshot/)

## Opérations sur le texte

- [Concatenate files](/fr/reference/workflow-steps/document/concatenate-files/) — réunit plusieurs fichiers en un seul
- [Document text substitution](/fr/reference/workflow-steps/document/document-text-substitution/) — recherche et remplacement dans un document

## Conversion d'encodage

- [Convert document encoding](/fr/reference/workflow-steps/document/convert-document-encoding/) — choix de l'encodage cible
- [Convert document encoding to ASCII](/fr/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert document encoding to UTF-16](/fr/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert document encoding to UTF-8](/fr/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Voir aussi

- [Convert Dashboard to PDF](/fr/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files](/fr/reference/workflow-steps/document/document-delete-old-files/)
- [Comptes de documents](/fr/guides/documents/adding-accounts/) — connectez des comptes de documents avant d'utiliser ces étapes
- [Guide des documents](/fr/guides/documents/) — procédures pas à pas orientées tâches pour les mêmes opérations
