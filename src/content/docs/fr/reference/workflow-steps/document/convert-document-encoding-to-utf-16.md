---
title: Convert Document Encoding to UTF-16
description: "Convertissez l'encodage d'un fichier de document en UTF-16 dans une étape de workflow PlaidCloud pour prendre en charge les jeux de caractères multioctets et le texte Unicode."
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Description

Réécrit un fichier texte en UTF-16. Utile lorsqu'un système en aval exige de l'UTF-16, ou lorsqu'une source mélange des encodages que d'autres outils rejettent.

## Entrées

- **Fichier ou répertoire d'entrée** : le fichier texte, ou le dossier de fichiers texte, à convertir.
- **Destination** : l'emplacement où le fichier converti est écrit.
- **Compression** : Aucune compression, Zip, GZip ou BZip2 pour la sortie.
- **Boutisme (ordre des octets)** : Petit-boutiste ou Gros-boutiste.
- **Include BOM** : cochez cette case pour commencer le fichier par une marque d'ordre des octets (`FF FE` en petit-boutiste, `FE FF` en gros-boutiste). Laissez-la décochée pour n'avoir aucune marque.

## Fonctionnement

- L'encodage de la source est détecté. Un fichier UTF-8 est lu en UTF-8, et les caractères Windows qui y ont été collés (par exemple les guillemets typographiques de Word ou d'Excel) sont conservés intacts, quel qu'en soit le nombre. Un fichier dans un autre encodage est lu dans l'encodage détecté à partir de sa première partie qui n'est pas du UTF-8 valide.
- Le texte est écrit tel quel : les lettres accentuées, les symboles et les autres caractères sont conservés exactement comme ils étaient.
- Un fichier dont l'encodage ne peut pas être détecté fait échouer l'étape, en nommant le fichier.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- Pour un dossier, chaque fichier est converti et écrit dans la destination sous son propre nom. Les fichiers des sous-dossiers sont écrits dans la destination elle-même, et non dans des sous-dossiers correspondants.

## Exemples

Sélectionnez le fichier d'entrée et parcourez l'emplacement pour le trouver. Sélectionnez l'emplacement de sortie voulu, choisissez l'ordre des octets et cochez **Include BOM** si le système destinataire en attend une. Enregistrez et exécutez.
