---
title: Étapes d'exportation
description: Étapes de workflow qui écrivent des tables de projet vers des destinations externes — formats de fichier, comptes de documents, bases de données externes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

Étapes de workflow qui écrivent des tables de projet vers des destinations externes — formats de fichier, comptes de documents, bases de données externes.

## Étapes

- [Archiver les tables](/fr/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/fr/reference/workflow-steps/export/export-external-tables/)
- [Exporter vers Kafka](/fr/reference/workflow-steps/export/export-kafka/)
- [Exporter vers MongoDB](/fr/reference/workflow-steps/export/export-mongodb/)
- [Exporter l'archive du projet](/fr/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/fr/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/fr/reference/workflow-steps/export/export-quandl/)
- [Exporter en SQL](/fr/reference/workflow-steps/export/export-sql/)
- [Export Templated](/fr/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/fr/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV](/fr/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel](/fr/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets](/fr/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet](/fr/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF](/fr/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON](/fr/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/fr/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/fr/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/fr/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive](/fr/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML](/fr/reference/workflow-steps/export/export-to-xml/)
- [Comptabiliser des documents](/fr/reference/workflow-steps/export/post-documents/) : comptabilisez une table de documents dans n'importe quel système ERP que vous avez configuré
- [Export de fichier spatial](/fr/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/fr/reference/workflow-steps/export/export-hyper/)

## Colonnes écrites

La plupart des étapes d'export écrivent toutes les colonnes de la table source, telles qu'elles sont au moment de l'exécution de l'étape et dans l'ordre des colonnes de la table, lorsque le Data Mapper ne liste aucune colonne cible, c'est-à-dire lorsque la table de droite de l'onglet **Colonnes** est vide. Une étape à moitié configurée exporte donc toute la table vers sa destination au lieu d'échouer ; vérifiez le Data Mapper avant d'exécuter un export vers une destination externe.

Si aucune colonne n'est mappée et que la table source n'en a aucune, un export CSV, JSON, SQL, Excel, PDF, Google Spreadsheet ou Kafka n'écrit rien et se termine par un avertissement. Dans un export de plusieurs tables, comme XML, Parquet, ORC, Avro ou Excel Sheets, cette table est ignorée avec un avertissement qui la nomme.
