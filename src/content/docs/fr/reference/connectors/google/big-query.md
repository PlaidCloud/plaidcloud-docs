---
title: Connecteur Google BigQuery
description: Configurez une connexion Google BigQuery dans PlaidCloud pour exécuter des requêtes analytiques et intégrer des données à grande échelle dans vos workflows.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Documentation de la connexion
[Documentation de Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## Configuration

Ces champs s'affichent lors de la création ou de la modification de cette connexion. Leur caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou remarques facultatifs sur la connexion. |
| Est active | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |
| Base en lecture seule | Interrupteur | Limite la connexion aux opérations en lecture seule. |
| Type d'accès | Sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Connexion BigQuery

| Champ | Obligatoire | Description |
|---|---|---|
| Projet | Oui | Le projet Google Cloud qui contient le jeu de données. |
| Jeu de données | Oui | Le jeu de données BigQuery à lire et à écrire. |
| Table | Oui | Une table du jeu de données. |

### Identifiants d'authentification

| Champ | Obligatoire | Description |
|---|---|---|
| Clé de compte de service (JSON) | Oui | Collez l'intégralité du fichier de clé JSON d'un compte de service Google autorisé à lire le jeu de données. Ne lui accordez l'accès en écriture que si vous souhaitez écrire dans le jeu de données. La clé est en écriture seule : laissez le champ vide lors d'une modification pour conserver la clé enregistrée. |

La connexion s'authentifie uniquement avec la clé de compte de service que vous lui fournissez. L'étape [Importer depuis SQL](/fr/reference/workflow-steps/import/import-sql/) lit BigQuery via cette connexion, et l'étape [Export External Database Tables](/fr/reference/workflow-steps/export/export-external-tables/) y écrit au moyen d'un job de chargement BigQuery.
