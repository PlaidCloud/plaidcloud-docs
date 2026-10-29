---
title: Étape Document Text Substitution
description: Effectuez des remplacements de texte par recherche et remplacement dans des documents au sein d'une étape de workflow PlaidCloud pour transformer automatiquement le contenu.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Description

Recherche et remplacement dans un fichier texte. Remplacez des chaînes ou des espaces réservés précis par de nouvelles valeurs, ce qui est utile pour créer des modèles (remplacer un espace réservé tel que `CUSTOMER_NAME` par un nom réel) ou pour assainir du texte (supprimer ou masquer des chaînes précises).

Fonctionne sur des fichiers texte UTF-8 (TXT, CSV, JSON, XML, HTML, RML) de toute taille. Un fichier qui n'est pas du texte UTF-8, comme un PDF ou un document Office, fait échouer l'étape.

## Entrées

- **Fichier ou répertoire d'entrée** — le fichier, ou un dossier de fichiers, à modifier.
- **Fichier ou répertoire de destination** — l'emplacement où le résultat est écrit. Le résultat est toujours écrit dans le compte de documents de l'entrée ; la destination définit le chemin.
- **Compression** — Aucune compression, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib) pour la sortie. Snappy et LZ4 sont écrits au format en blocs lu par Spark et Hadoop, et LZO sous forme de fichier `lzop`.
- **Ordre des opérations de remplacement de texte** — une ligne par remplacement, chacune indiquant le texte d'origine et son remplacement. Vous pouvez utiliser des variables dans le remplacement.

## Fonctionnement

- Les remplacements s'exécutent de haut en bas, et chacun travaille sur le résultat de ceux qui le précèdent : un remplacement peut donc modifier du texte introduit par une ligne antérieure.
- La correspondance est exacte et sensible à la casse, et chaque occurrence est remplacée.
- Une ligne dont le texte d'origine est vide est ignorée.
- Pour un dossier, chaque fichier est écrit dans un dossier portant le nom de la destination, sans son extension, sous le nom propre du fichier.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine par un avertissement indiquant le chemin, ne traite rien, et le workflow continue.

## Exemples

| Original | Remplacement | `Dear CUSTOMER_NAME,` devient |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
