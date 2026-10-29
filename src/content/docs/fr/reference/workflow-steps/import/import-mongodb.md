---
title: Importer depuis MongoDB
description: Lisez une collection MongoDB, ou le résultat d'un pipeline d'agrégation, dans une table PlaidCloud avec une étape de workflow.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Description

Lit les documents d'une collection MongoDB dans une table de projet, avec une ligne par document. Utilisez un filtre pour ne lire que les documents voulus, ou un pipeline d'agrégation pour les remodeler dans MongoDB avant leur enregistrement. L'étape accède à MongoDB via une [connexion MongoDB](/fr/reference/connectors/databases/mongodb/).

## Source et cible

| Paramètre | Obligatoire | Fonction |
| --- | --- | --- |
| Connexion MongoDB | Oui | La connexion à utiliser pour la lecture. |
| Base de données | Non | La base de données à lire. Laissez vide pour utiliser la **Base de données par défaut** de la connexion. |
| Collection | Oui | La collection à lire. |
| Table cible | Oui | La table dans laquelle les documents sont enregistrés. Ce doit être une table, pas une vue. |

## Requête

| Paramètre | Fonction |
| --- | --- |
| Filtre (JSON) | Un filtre de requête MongoDB sous forme d'objet JSON, par exemple `{"status": "open"}`. Seuls les documents correspondants sont lus. |
| Pipeline d'agrégation (JSON) | Un pipeline d'agrégation sous forme de tableau JSON, par exemple `[{"$match": {"status": "open"}}]`. Lorsqu'il est défini, la collection est agrégée au lieu d'être filtrée. Un pipeline contenant une étape `$out` ou `$merge` est refusé, car il écrirait dans MongoDB. |
| Limite de lignes (0 = toutes) | Le nombre maximal de documents à lire. `0` les lit tous. |
| Limite de durée (secondes) | La durée pendant laquelle MongoDB peut effectuer la lecture avant de l'arrêter. |
| Documents échantillonnés pour les colonnes | Lorsque l'étape ne déclare aucune colonne, le nombre de documents, pris depuis le début, qui déterminent les colonnes et leurs types : chaque champ de premier niveau qu'ils contiennent devient une colonne. La valeur par défaut est 1000. |

Le filtre et le pipeline acceptent des variables de workflow écrites sous la forme `{name}`, par exemple `{"region": "{region}"}`. La valeur de chaque variable est insérée comme une seule chaîne ou un seul nombre JSON, de sorte qu'une variable ne peut pas ajouter de clés ni d'opérateurs à la requête. Une variable non définie arrête l'étape avec une erreur qui la nomme.

## Mappage des colonnes

Mappez chaque champ de document sur une colonne de la table cible dans l'onglet de mappage. Une colonne lit le champ de document de même nom. Une collection inexistante se termine avec un avertissement et laisse la table cible vide.

## Voir aussi

- [Exporter vers MongoDB](/fr/reference/workflow-steps/export/export-mongodb/)
- [Connexion MongoDB](/fr/reference/connectors/databases/mongodb/)
