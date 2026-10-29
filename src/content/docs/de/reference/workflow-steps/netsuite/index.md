---
title: NetSuite-Schritte
description: NetSuite-Workflow-Schritte – Salden, Hauptbuchdetails, Stammdaten oder Ihre eigene SuiteQL-Abfrage importieren und Journalbuchungen über Ihre NetSuite-Verbindung buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Workflow-Schritte, die über Ihre [NetSuite-Verbindung](/de/guides/connections/netsuite/) aus NetSuite lesen und dorthin schreiben. Die vorgefertigten Importschritte sind der einfachste Weg, gängige Finanz- und Referenzdaten abzurufen – wählen Sie eine Verbindung, eine Zieltabelle und einen Datumsbereich oder Datensatztyp, ganz ohne SuiteQL.

## Importschritte

- [NetSuite: Salden importieren](/de/reference/workflow-steps/netsuite/import-balances/) – Kontensalden (eine Saldenliste) für einen Datumsbereich und eine Tochtergesellschaft.
- [NetSuite: Hauptbuchdetails importieren](/de/reference/workflow-steps/netsuite/import-gl-detail/) – Hauptbuch-Transaktionszeilen für einen Datumsbereich und eine Tochtergesellschaft.
- [NetSuite: Stammdaten importieren](/de/reference/workflow-steps/netsuite/import-master-data/) – Stammdatenlisten: Konten, Tochtergesellschaften, Abteilungen, Klassen, Standorte, Lieferanten oder Kunden.
- [NetSuite: SuiteQL-Abfrage importieren](/de/reference/workflow-steps/netsuite/import-suiteql-query/) – führen Sie Ihre eigene SuiteQL-Abfrage aus und laden Sie das Ergebnis in eine typisierte Tabelle, wobei Datumsfenster und Paging für Sie erledigt werden.

## Buchungsschritte

- [Post NetSuite Journal Entry](/de/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) – bucht Journalbuchungen aus Kopf- und Positionstabellen zurück nach NetSuite.

## Individuelle Abrufe

Für Daten, die die vorgefertigten Importschritte nicht abdecken – eine individuelle Abfrage oder ein NetSuite-Datensatz ohne vorgefertigten Schritt –, verwenden Sie [NetSuite: SuiteQL-Abfrage importieren](/de/reference/workflow-steps/netsuite/import-suiteql-query/) mit Ihrem eigenen SuiteQL. Ausgangspunkte finden Sie unter [NetSuite-SuiteQL-Abfragebeispiele](/de/guides/connections/netsuite-financial-queries/).

## Verwandte Themen

- [NetSuite-REST-Konnektor](/de/reference/connectors/rest/netsuite/)
- [Mit NetSuite verbinden](/de/guides/connections/netsuite/)
- [NetSuite-Finanzdaten importieren](/de/guides/connections/import-netsuite-financials/)
