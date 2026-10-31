---
title: Kroki przepływu pracy
description: Każdy typ kroku przepływu pracy w PlaidCloud — import, eksport, transformacje, alokacje, wymiary, dokumenty, powiadomienia i więcej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Kroki przepływu pracy to elementy składowe automatyzacji w PlaidCloud. Każdy krok wykonuje jedną operację (import CSV, złączenie dwóch tabel, wysłanie powiadomienia), a kroki są składane w przepływy pracy uruchamiane kolejno, równolegle, warunkowo lub w pętlach.

## Kategorie

### Przepływ danych

- [Import](/pl/reference/workflow-steps/import/) — pobieraj dane z CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, źródeł Singer i innych
- [Eksport](/pl/reference/workflow-steps/export/) — wysyłaj dane do CSV, XML, SQL, Excel, Arkuszy Google, Parquet, ORC, MongoDB, Kafka, archiwum tabel i innych

### Transformacje tabel

- [Tabele](/pl/reference/workflow-steps/tables/) — złączenia, unie, filtry, wyszukiwania, tabele przestawne, rozwinięcia, ukierunkowane aktualizacje, nadawanie uprawnień Dostęp do wierszy z tabeli źródłowej, przywracanie do wybranego momentu
- [Operacje wspólne](/pl/reference/workflow-steps/common/) — wspólne wzorce mapowania i filtrowania danych

### Dane geoprzestrzenne

- [Dane geoprzestrzenne](/pl/reference/workflow-steps/spatial/) — import i eksport plików przestrzennych, bufor, dopasowanie, pomiary, zmiana odwzorowania i budowanie geometrii; pełne pokrycie narzędzi przestrzennych Alteryx

### Modelowanie

- [Alokacja](/pl/reference/workflow-steps/allocation/) — rozdzielanie według kluczy alokacji, alokacje podziałowe, tagowanie według reguł
- [Wymiary](/pl/reference/workflow-steps/dimensions/) — ładowanie, sortowanie, czyszczenie i eksport oraz zarządzanie hierarchiami
- [Optymalizacja](/pl/reference/workflow-steps/optimization/) — kroki solvera liniowego i mieszanego całkowitoliczbowego
- [Uczenie maszynowe](/pl/reference/workflow-steps/machine-learning/) — trenuj modele, w tym XGBoost i learnery KNIME, i oceniaj nimi tabele

### Dokumenty i pliki

- [Dokument](/pl/reference/workflow-steps/document/) — operacje na plikach, listowanie katalogów, szyfrowanie, obsługa PDF, przetwarzanie obrazów, konwersja kodowania, aktualizacje komórek Excel
- [Tekst i dokumenty](/pl/reference/workflow-steps/text-documents/) — wyodrębnianie tekstu z PDF, OCR obrazów, odczyt i zapis blobów, sentyment, modelowanie tematów, chmury słów

### Komunikacja

- [Powiadomienia](/pl/reference/workflow-steps/notifications/) — e-mail, Slack, Teams, SMS, webhook, Twitter, dziennik
- [Raporty](/pl/reference/workflow-steps/reports/) — generuj pojedyncze lub wsadowe raporty PDF z szablonów RML

### Sterowanie przepływem pracy

- [Sterowanie przepływem pracy](/pl/reference/workflow-steps/workflow-control/) — zmienne, pętle, przepływy podrzędne, makra, obsługa błędów, asercja liczby wierszy
- [Ogólne](/pl/reference/workflow-steps/general/) — krok LLM, pass, wait, transformacja zdefiniowana przez użytkownika, uruchamianie zdalnego Pythona, Wykonawca Alteryx
- [Makra pakietowe](/pl/reference/workflow-steps/macros/) — odpowiedniki makr pakietowych Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integracje korporacyjne

- [Agent](/pl/reference/workflow-steps/agent/) — operacje agenta PlaidLink dla zasobów lokalnych
- [NetSuite](/pl/reference/workflow-steps/netsuite/) — importuj salda, szczegóły księgi głównej, dane główne lub własne [zapytanie SuiteQL](/pl/reference/workflow-steps/netsuite/import-suiteql-query/); księguj zapisy dziennika w NetSuite
- [Acumatica](/pl/reference/workflow-steps/acumatica/) — importuj encje główne i transakcyjne; księguj transakcje dziennika, faktury, rachunki i płatności
- [Business Central](/pl/reference/workflow-steps/business-central/) — importuj encje OData; księguj wiersze dziennika ogólnego
- [Xero](/pl/reference/workflow-steps/xero/) — importuj encje Accounting API; księguj ręczne zapisy dziennika, faktury, rachunki, płatności i noty kredytowe
- [Dynamics 365 F&O](/pl/reference/workflow-steps/dynamics-365-fo/) — importuj encje OData/DMF; księguj zapisy dziennika
- [Oracle Fusion](/pl/reference/workflow-steps/oracle-fusion/) — importuj salda księgi głównej i partie zapisów dziennika; księguj zapisy dziennika przez FBDI
- [Oracle EPM (HFM / FCCS)](/pl/reference/workflow-steps/oracle-epm/) — samodzielnie pobieraj doraźny wycinek danych z Oracle FCCS za pomocą selektora punktu widzenia; opcjonalne cykliczne ładowanie według harmonogramu
- [Oracle Essbase](/pl/reference/workflow-steps/essbase/) — uruchamiaj zapytanie MDX na żywo względem kostki lub ładuj zarys wymiaru jako wymiar PlaidCloud; bezpośrednio z chmury
- [IBM TM1 / Planning Analytics](/pl/reference/workflow-steps/ibm-planning-analytics/) — odczytuj kostkę według zapisanego widoku lub MDX albo hierarchię wymiaru; bezpośrednio z chmury lub przez agenta lokalnego
- [Anaplan](/pl/reference/workflow-steps/anaplan/) — odczytuj zapisany widok, uruchamiaj istniejącą akcję eksportu lub ładuj jedną lub więcej list do wymiaru PlaidCloud; bezpośrednio z chmury, tylko odczyt
- [Workday Financials](/pl/reference/workflow-steps/workday-financials/) — importuj raport RaaS; księguj zapisy księgowe
- [Salesforce](/pl/reference/workflow-steps/salesforce/) — wyodrębniaj dowolny standardowy lub niestandardowy obiekt CRM do tabeli projektu przez Bulk API 2.0, z obiektem i listą pól odczytanymi z organizacji
- [Sage Intacct](/pl/reference/workflow-steps/sage-intacct/) — importuj salda, rachunki AP, zapytania doraźne i obiekty księgi głównej/wymiarów; księguj zapisy dziennika
- [SAP S/4HANA Cloud](/pl/reference/workflow-steps/s4hana-cloud/) — importuj zestawienie obrotów i sald oraz pozycje zapisów dziennika przez OData; księguj zapisy dziennika przez SOAP
- [SAP](/pl/reference/workflow-steps/sap/) — wywołania RFC SAP ECC / S/4HANA
- [SAP-PCM](/pl/reference/workflow-steps/sap-pcm/) — sterowanie modelem SAP Profitability and Cost Management
