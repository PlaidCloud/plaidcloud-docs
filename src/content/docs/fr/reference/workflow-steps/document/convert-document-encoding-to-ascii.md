---
title: Convert Document Encoding to ASCII
description: "Convertissez l'encodage d'un fichier de document en ASCII dans une étape de workflow PlaidCloud pour garantir la compatibilité avec les systèmes qui exigent du texte ASCII."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-ascii.md
---

## Description

Réécrit un fichier texte en ASCII pur. C'est particulièrement utile lorsque la source d'information mélange plusieurs encodages ou que d'autres outils ne prennent pas en charge certains encodages.

## Fonctionnement

- L'encodage de la source est détecté. Un fichier UTF-8 est lu en UTF-8, et les caractères Windows qui y ont été collés (par exemple les guillemets typographiques de Word ou d'Excel) sont conservés intacts, quel qu'en soit le nombre. Un fichier dans un autre encodage est lu dans l'encodage détecté à partir de sa première partie qui n'est pas du UTF-8 valide.
- Les lettres accentuées conservent leur lettre de base (`café` devient `cafe`), et les caractères sans équivalent ASCII sont supprimés.
- Une ligne qui ne contient qu'un guillemet double est rattachée à la fin de la ligne qui la précède.
- Un fichier dont l'encodage ne peut pas être détecté fait échouer l'étape, en nommant le fichier.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.

## Exemples

Sélectionnez le fichier d'entrée et parcourez l'emplacement pour le trouver. Sélectionnez l'emplacement de sortie voulu et parcourez-le pour choisir l'emplacement du fichier. Enregistrez et exécutez.
