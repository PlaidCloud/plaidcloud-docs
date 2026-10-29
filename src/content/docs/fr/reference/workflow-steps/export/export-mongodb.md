---
title: Exporter vers MongoDB
description: Écrivez une table PlaidCloud dans une collection MongoDB sous forme de documents insérés, remplacés, mis à jour ou upsertés.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Description

Écrit chaque ligne d'une table de projet dans une collection MongoDB sous forme de document. La collection est créée si elle n'existe pas. L'étape accède à MongoDB via une [connexion MongoDB](/fr/reference/connectors/databases/mongodb/).

## Source et cible

| Paramètre | Obligatoire | Rôle |
| --- | --- | --- |
| Table source | Oui | La table à écrire. |
| Connexion MongoDB | Oui | La connexion par laquelle écrire. |
| Base de données | Non | La base de données dans laquelle écrire. Laissez vide pour utiliser la **Base de données par défaut** de la connexion. |
| Collection | Oui | La collection dans laquelle écrire. |

## Options d'écriture

| Paramètre | Rôle |
| --- | --- |
| Mode d'écriture | **Insérer un document par ligne** (valeur par défaut), **Remplacer le document correspondant**, **Mettre à jour les champs du document correspondant**, **Remplacer le document correspondant, ou insérer**, ou **Mettre à jour les champs du document correspondant, ou insérer**. |
| Colonnes de correspondance | Les colonnes, séparées par des virgules, qui identifient un document. Obligatoire pour tous les modes sauf l'insertion. |
| Supprimer tous les documents de la collection avant l'écriture | Vide d'abord la collection, de sorte qu'elle ne contienne que les lignes de cette exécution. |
| S'arrêter à la première écriture en échec | S'arrête au premier document que MongoDB refuse. Décochez pour poursuivre avec les autres. |
| Attendre que l'écriture atteigne le journal | Attend que MongoDB ait écrit chaque lot dans son journal. |
| Write Concern | Vide pour celui de la connexion, un nombre de serveurs, ou `majority`. |
| Documents par requête | Le nombre de documents envoyés dans chaque requête. |

L'insertion ajoute de nouveau les documents à chaque exécution de l'étape. Les modes qui remplacent ou mettent à jour laissent la collection identique quel que soit le nombre d'exécutions de l'étape ; utilisez l'un d'eux lorsqu'un workflow peut s'exécuter deux fois sur les mêmes lignes.

## Voir aussi

- [Importer depuis MongoDB](/fr/reference/workflow-steps/import/import-mongodb/)
- [Connexion MongoDB](/fr/reference/connectors/databases/mongodb/)
