---
title: Étape Fix File Extension
description: Corrigez les extensions de fichier dans une étape de workflow PlaidCloud en détectant le type réel du fichier et en le renommant avec l'extension appropriée.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Lit le contenu réel d'un fichier et, lorsqu'il contredit son extension, le renomme avec l'extension que son type porte normalement : un PDF enregistré en `.dat` devient `.pdf`. Utile lorsqu'un système source transmet des fichiers dont les extensions sont erronées ou manquantes.

## Entrées

- **Fichier ou répertoire d'entrée** — un fichier, ou un dossier dont chaque fichier est contrôlé, dans un compte de documents. Les fichiers sont renommés sur place ; il n'y a donc pas d'emplacement de sortie.

## Fonctionnement

L'étape identifie le type de chaque fichier à partir de son contenu, et ne renomme le fichier que si son nom actuel n'a pas d'extension, en a une provisoire (`.dat`, `.tmp` ou `.bin`), ou désigne un autre type que l'étape reconnaît.

Les types reconnus sont les suivants : PDF ; images JPEG, PNG, GIF, TIFF, BMP, WebP et HEIC ; documents Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) et PowerPoint (`.pptx`) ; archives ZIP et GZip ; et CSV, JSON, HTML, XML et texte brut.

Un fichier conserve son nom dans les cas suivants :

- son extension correspond déjà à son contenu : `.jpg` et `.jpeg` conviennent tous deux à un JPEG, `.tif` et `.tiff` à un TIFF ;
- son extension n'est pas reconnue par l'étape, comme `.sql`, `.log` ou `.ai`, car le contenu seul ne permet pas de distinguer un script SQL de tout autre texte, ni un fichier Illustrator d'un PDF ;
- il contient du texte brut sous une extension de texte telle que `.csv`, `.tsv` ou `.json` ;
- il contient un format de texte sous l'extension d'un autre (XML dans un fichier `.html`, CSV dans un fichier `.json`), car le contenu ne permet pas de les distinguer de façon fiable. Seul un fichier `.txt`, ou sans extension ou avec une extension provisoire, est renommé vers un format de texte ;
- c'est un fichier ZIP nommé comme un document Office, puisque les fichiers `.xlsx`, `.docx` et `.pptx` sont en réalité des fichiers ZIP ;
- son type ne peut pas être déterminé, comme pour un fichier vide.

Une archive est jugée d'après son propre contenu : ses éléments ne sont ni ouverts ni renommés. Les fichiers dont le nom commence par `.` sont ignorés.

## Exemples

| Fichier | Contenu | Résultat |
|---|---|---|
| `invoice.dat` | PDF | renommé `invoice.pdf` |
| `photo.png` | JPEG | renommé `photo.jpg` |
| `export.txt` | CSV | renommé `export.csv` |
| `readme` | texte brut | renommé `readme.txt` |
| `query.sql` | texte brut | inchangé |
| `budget.xlsx` | ZIP | inchangé |

## Remarques

- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine par un avertissement indiquant le chemin, ne traite rien, et le workflow continue.

## Voir aussi

- [Concatenate files](/fr/reference/workflow-steps/document/concatenate-files/)
- [Guide des documents](/fr/guides/documents/)
