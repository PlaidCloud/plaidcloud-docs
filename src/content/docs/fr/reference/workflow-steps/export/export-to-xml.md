---
title: Étape Export to XML
description: Exportez des données sous forme de fichiers XML depuis une étape de workflow PlaidCloud pour l'échange de données structurées et l'intégration de systèmes.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Description

Écrit une table de projet PlaidCloud dans un compte de documents sous la forme d'un fichier XML. À utiliser lorsque les systèmes en aval exigent une entrée XML, ce qui est courant avec les anciennes intégrations d'entreprise, les déclarations administratives ou certains formats d'échange de données propres à un secteur.

La structure XML reflète la table : un élément par ligne, des éléments enfants pour chaque colonne. Pour mieux contrôler la structure, utilisez une approche par modèle avec [Document Text Substitution](/fr/reference/workflow-steps/document/document-text-substitution/) sur un fichier modèle.

## Si le fichier existe

Sous **Si le fichier existe**, **Un fichier qui existe déjà** (`if_exists`) détermine ce qui se passe lorsque le fichier existe déjà. **L'écraser** (`overwrite`, par défaut) remplace un fichier déjà présent ; **Faire échouer l'étape sans rien écrire** (`fail`) arrête l'étape sans rien écrire lorsqu'un fichier qu'elle écrirait existe déjà.
