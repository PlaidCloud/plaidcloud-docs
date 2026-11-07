---
title: Kroki przepływu pracy
description: Każdy typ kroku przepływu pracy w PlaidCloud — import, eksport, transformacje, alokacje, wymiary, dokumenty, powiadomienia i więcej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Kroki przepływu pracy to elementy składowe automatyzacji w PlaidCloud. Każdy krok wykonuje jedną operację (import pliku CSV, złączenie dwóch tabel, wysłanie powiadomienia), a kroki łączy się w przepływy pracy, które działają kolejno, równolegle, warunkowo lub w pętlach.

## Kategorie

### Przenoszenie danych

- [Import](/pl/reference/workflow-steps/import/) — pobieranie danych z CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, źródeł Singer i innych
- [Eksport](/pl/reference/workflow-steps/export/) — wysyłanie danych do CSV, XML, SQL, Excel, Arkuszy Google, Parquet, ORC, MongoDB, Kafka, archiwum tabel i innych

### Transformacje tabel

- [Tabele](/pl/reference/workflow-steps/tables/) — złączenia, sumy zbiorów, filtry, wyszukiwania, tabele przestawne, rozpakowywanie (melt), ukierunkowane aktualizacje, uprawnienia Dostęp do wierszy z tabeli źródłowej, przywracanie do punktu w czasie
- [Operacje wspólne](/pl/reference/workflow-steps/common/) — współdzielone wzorce mapowania i filtrowania danych

### Dane geoprzestrzenne

- [Dane geoprzestrzenne](/pl/reference/workflow-steps/spatial/) — import i eksport plików przestrzennych, bufor, dopasowanie, pomiar, zmiana odwzorowania i budowa geometrii; pełne pokrycie narzędzi przestrzennych Alteryx

### Modelowanie

- [Alokacja](/pl/reference/workflow-steps/allocation/) — rozdzielanie oparte na kluczach, alokacje dzielone, tagowanie według reguł
- [Wymiary](/pl/reference/workflow-steps/dimensions/) — ładowanie, sortowanie, czyszczenie, eksport i zarządzanie hierarchiami
- [Optymalizacja](/pl/reference/workflow-steps/optimization/) — kroki solvera liniowego i mieszanego całkowitoliczbowego
- [Uczenie maszynowe](/pl/reference/workflow-steps/machine-learning/) — trenowanie modeli, w tym XGBoost i uczących KNIME, oraz ocenianie nimi tabel

### Dokumenty i pliki

- [Dokumenty](/pl/reference/workflow-steps/document/) — operacje na plikach, lista katalogu, szyfrowanie, obsługa PDF, przetwarzanie obrazów, konwersja kodowania, aktualizacja komórek Excel
- [Tekst i dokumenty](/pl/reference/workflow-steps/text-documents/) — wyodrębnianie tekstu z PDF, OCR obrazów, odczyt i zapis blobów, analiza sentymentu, modelowanie tematów, chmury słów

### Komunikacja

- [Powiadomienia](/pl/reference/workflow-steps/notifications/) — e-mail, Slack, Teams, SMS, webhook, Twitter, dziennik
- [Raporty](/pl/reference/workflow-steps/reports/) — generowanie pojedynczych lub wsadowych raportów PDF z szablonów RML

### Sterowanie przepływem pracy

- [Sterowanie przepływem pracy](/pl/reference/workflow-steps/workflow-control/) — zmienne, pętle, podprzepływy pracy, makra, obsługa błędów, asercja liczby wierszy
- [Ogólne](/pl/reference/workflow-steps/general/) — krok LLM, Pass, Czekaj, transformacja zdefiniowana przez użytkownika, uruchamianie zdalnego Pythona, Wykonawca Alteryx
- [Makra pakietowe](/pl/reference/workflow-steps/macros/) — odpowiedniki makr pakietowych Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integracje korporacyjne

- [Agent](/pl/reference/workflow-steps/agent/) — operacje agenta PlaidLink dla zasobów lokalnych
- [NetSuite](/pl/reference/workflow-steps/netsuite/) — import sald, szczegółów księgi głównej, danych głównych lub własnego [zapytania SuiteQL](/pl/reference/workflow-steps/netsuite/import-suiteql-query/); księgowanie zapisów dziennika w NetSuite
- [Acumatica](/pl/reference/workflow-steps/acumatica/) — import encji głównych i transakcyjnych; księgowanie transakcji dziennika, faktur, rachunków i płatności
- [Business Central](/pl/reference/workflow-steps/business-central/) — import encji OData; księgowanie pozycji dziennika głównego
- [Xero](/pl/reference/workflow-steps/xero/) — import encji Accounting API; księgowanie dzienników ręcznych, faktur, rachunków, płatności i not kredytowych
- [Dynamics 365 F&O](/pl/reference/workflow-steps/dynamics-365-fo/) — import encji OData/DMF; księgowanie zapisów dziennika
- [Oracle Fusion](/pl/reference/workflow-steps/oracle-fusion/) — import sald księgi głównej i partii zapisów dziennika; księgowanie zapisów dziennika przez FBDI
- [Oracle EPM (HFM / FCCS)](/pl/reference/workflow-steps/oracle-epm/) — samodzielne pobieranie doraźnego wycinka danych z Oracle FCCS za pomocą selektora punktu widzenia; opcjonalne cykliczne ładowanie według harmonogramu
- [Oracle Essbase](/pl/reference/workflow-steps/essbase/) — uruchomienie zapytania MDX na żywo względem kostki lub załadowanie konspektu wymiaru jako wymiaru PlaidCloud; bezpośrednio w chmurze
- [IBM TM1 / Planning Analytics](/pl/reference/workflow-steps/ibm-planning-analytics/) — odczyt kostki według zapisanego widoku lub MDX albo hierarchii wymiaru; bezpośrednio w chmurze lub przez lokalnego agenta
- [Anaplan](/pl/reference/workflow-steps/anaplan/) — odczyt zapisanego widoku, uruchomienie istniejącej akcji eksportu lub załadowanie jednej lub kilku list do wymiaru PlaidCloud; bezpośrednio w chmurze, tylko do odczytu
- [OneStream](/pl/reference/workflow-steps/onestream/) — odczyt adaptera danych, jedno wywołanie na element konsolidacji, do tabeli; tylko do odczytu
- [Workday Financials](/pl/reference/workflow-steps/workday-financials/) — import raportu RaaS; księgowanie dzienników księgowych
- [Salesforce](/pl/reference/workflow-steps/salesforce/) — wyodrębnianie dowolnego standardowego lub niestandardowego obiektu CRM do tabeli projektu przez Bulk API 2.0, z listą obiektów i pól odczytywaną z organizacji
- [Sage Intacct](/pl/reference/workflow-steps/sage-intacct/) — import sald, rachunków AP, zapytań doraźnych oraz obiektów księgi głównej i wymiarów; księgowanie zapisów dziennika
- [SAP S/4HANA Cloud](/pl/reference/workflow-steps/s4hana-cloud/) — import zestawienia obrotów i sald oraz pozycji zapisów dziennika przez OData; księgowanie zapisów dziennika przez SOAP
- [SAP](/pl/reference/workflow-steps/sap/) — wywołania RFC SAP ECC / S/4HANA
- [SAP-PCM](/pl/reference/workflow-steps/sap-pcm/) — sterowanie modelem SAP Profitability and Cost Management
