---
title: Convert Document Encoding to UTF-8
description: "Convertissez l'encodage d'un fichier de document en UTF-8 dans une étape de workflow PlaidCloud pour une large compatibilité avec les systèmes et applications modernes."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## Description

Réécrit un fichier texte en UTF-8. C'est particulièrement utile lorsque la source d'information mélange plusieurs encodages ou que d'autres outils ne prennent pas en charge certains encodages.

## Fonctionnement

- L'encodage de la source est détecté. Un fichier UTF-8 est lu en UTF-8, et les caractères Windows qui y ont été collés (par exemple les guillemets typographiques de Word ou d'Excel) sont conservés intacts, quel qu'en soit le nombre. Un fichier dans un autre encodage est lu dans l'encodage détecté à partir de sa première partie qui n'est pas du UTF-8 valide.
- Le texte est écrit tel quel : les lettres accentuées, les symboles et les autres caractères sont conservés exactement comme ils étaient.
- Un fichier dont l'encodage ne peut pas être détecté fait échouer l'étape, en nommant le fichier.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.

## Exemples

Sélectionnez le fichier d'entrée et parcourez l'emplacement pour le trouver. Sélectionnez l'emplacement de sortie voulu, puis parcourez-le pour choisir l'emplacement du fichier. Enregistrez et exécutez.
