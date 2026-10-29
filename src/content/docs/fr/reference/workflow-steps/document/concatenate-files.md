---
title: Concatenate Files
description: "Concaténez plusieurs fichiers en un seul dans une étape de workflow PlaidCloud pour combiner des sorties de texte, de CSV ou d'autres documents."
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Combine deux fichiers ou plus d'un compte de documents en un seul fichier de sortie. Fonctionne octet par octet : utile pour les formats texte brut (CSV, fichiers journaux, JSON Lines) où une simple concaténation produit une sortie valide.

## Entrées

- **Fichiers source** : liste des fichiers à concaténer, dans l'ordre
- **Chemin de sortie** : destination du fichier combiné
- **Séparateur** : séquence d'octets facultative insérée entre les fichiers source (souvent un saut de ligne)

## Sortie

Un seul fichier contenant le contenu de tous les fichiers source dans l'ordre indiqué, joints par le séparateur configuré.

Un fichier source qui n'existe pas est exclu du fichier combiné, et l'étape se termine avec un avertissement qui le nomme, de sorte que le workflow se poursuit.

## Usages courants

- Combiner des fichiers journaux quotidiens en une archive mensuelle
- Fusionner des fichiers CSV qui partagent un même schéma (supprimez les en-têtes de tous sauf du premier)
- Joindre des exports JSON Lines issus de plusieurs sources avant le traitement

## À éviter pour

- Les PDF : utilisez plutôt [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/)
- Les formats binaires avec en-têtes (XLSX, ZIP, fichiers image) : la concaténation d'octets ne produira pas de fichier valide

## Voir aussi

- [Merge multiple PDFs](/fr/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guide des documents](/fr/guides/documents/)
