---
title: Étapes d'importation
description: Étapes de workflow qui amènent des données de sources externes dans des tables de projet.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Étapes de workflow qui amènent des données de sources externes dans des tables de projet.

Une importation de fichier vérifie la requête qui charge sa table cible avant de s'exécuter. Une requête qui contient autre chose qu'une simple instruction SQL sur des colonnes typées est refusée avant que la table cible ne soit créée, remplacée ou chargée, de sorte que la table reste exactement dans son état initial.

Un fichier source manquant n'est pas une erreur. L'importation avertit en indiquant le chemin et laisse la table cible vide avec ses colonnes déclarées, de sorte que les étapes suivantes lisent zéro ligne. Cela s'applique aux importations CSV, Excel, JSON, largeur fixe, YXDB, dBASE, ORC, Avro, Parquet, XML et extraction Db2. Une importation XML avec balises ne crée une table vide que pour chaque balise qui déclare des champs. Les importations d'archive et Access avertissent aussi, mais elles ne déclarent aucune colonne et ne créent donc aucune table. Une importation d'archive qui trouve ses fichiers par une recherche de documents n'émet aucun avertissement de fichier manquant.

Il en va de même avant l'exécution d'une étape. **Renseigner** sur le mappage d'une importation de fichier, ainsi que la lecture des colonnes d'un fichier via l'API REST ou un assistant IA, répondent *Rien à remplir* (une liste de colonnes vide via l'API) avec un avertissement qui nomme le chemin lorsque le fichier est absent ou vide, au lieu d'une erreur. Importer un fichier manquant dans une nouvelle table ou une nouvelle étape depuis Documents ne crée rien, marque le fichier comme **ignoré** et affiche un avertissement qui nomme le chemin.

## Étapes

- [Importer depuis Access](/fr/reference/workflow-steps/import/import-access/)
- [Importer Alteryx YXDB](/fr/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Importer l'archive](/fr/reference/workflow-steps/import/import-archive/)
- [Importer depuis Avro](/fr/reference/workflow-steps/import/import-avro/)
- [Importer depuis CSV](/fr/reference/workflow-steps/import/import-csv/)
- [Importer Delta Lake](/fr/reference/workflow-steps/import/import-delta/)
- [Importer l'extraction DB2](/fr/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE](/fr/reference/workflow-steps/import/import-dbf/)
- [Importer depuis Excel](/fr/reference/workflow-steps/import/import-excel/)
- [Import Delimited](/fr/reference/workflow-steps/import/import-delimited/)
- [Importer les tables de base de données externe](/fr/reference/workflow-steps/import/import-external-database-tables/)
- [Importer à largeur fixe](/fr/reference/workflow-steps/import/import-fixed-width/)
- [Import Google BigQuery](/fr/reference/workflow-steps/import/import-google-bigquery/)
- [Importer depuis Google Sheets](/fr/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF](/fr/reference/workflow-steps/import/import-hdf/)
- [Importer depuis JSON](/fr/reference/workflow-steps/import/import-json/)
- [Importer depuis Kafka](/fr/reference/workflow-steps/import/import-kafka/)
- [Importer depuis Monday](/fr/reference/workflow-steps/import/import-monday/)
- [Importer depuis MongoDB](/fr/reference/workflow-steps/import/import-mongodb/)
- [Importer ORC](/fr/reference/workflow-steps/import/import-orc/)
- [Importer depuis Parquet](/fr/reference/workflow-steps/import/import-parquet/)
- [Import Project Table](/fr/reference/workflow-steps/import/import-project-table/)
- [Import Quandl](/fr/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source](/fr/reference/workflow-steps/import/import-singer/)
- [Import SPSS](/fr/reference/workflow-steps/import/import-spss/)
- [Importer depuis SQL](/fr/reference/workflow-steps/import/import-sql/)
- [Import Stata](/fr/reference/workflow-steps/import/import-stata/)
- [Importer depuis XML](/fr/reference/workflow-steps/import/import-xml/)
- [Restaurer les tables](/fr/reference/workflow-steps/import/restore-tables/)
