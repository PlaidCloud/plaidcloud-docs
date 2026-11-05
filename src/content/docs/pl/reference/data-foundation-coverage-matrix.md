---
title: Data Foundation Coverage Matrix
description: Który zbiór danych Common Finance Model dostarcza bezpośrednio każdy system, z którym łączy się Data Foundation, a który dodajesz jako plik.
sidebar:
  label: Pokrycie Data Foundation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation odczytuje bezpośrednio każdy podłączony system ERP i każdą instancję do jednego Common Finance Model. Pliki uzupełniają wszystko, czego system nie przechowuje, więc każdy z poniższych zbiorów danych można też dostarczyć jako plik.

## Legenda

| Oznaczenie | Znaczenie |
| --- | --- |
| **Pełny** | Data Foundation odczytuje zbiór danych bezpośrednio z systemu. |
| **Pełny¹** | Odczytywany bezpośrednio, gdy system go przechowuje. System bez tych danych lub połączenie bez dostępu do nich nie zatrzymuje ładowania. |
| **Plik** | System nie dostarcza tego zbioru danych. Dodaj go jako plik. |

## SAP, Oracle i Dynamics 365

| Zbiór danych | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Jednostki | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Kalendarz fiskalny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Plan kont | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Działy | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Centra zysku | Pełny¹ | Pełny¹ | Plik | Plik | Plik | Plik |
| Produkty | Pełny | Pełny | Pełny | Pełny¹ | Pełny¹ | Pełny |
| Klienci | Pełny | Pełny | Pełny | Pełny¹ | Pełny¹ | Pełny |
| Księga główna | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Bilans próbny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Pozycje sprzedaży | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Lejek sprzedaży | Plik | Plik | Plik | Plik | Plik | Plik |
| Stany magazynowe | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Plik | Pełny¹ |
| Budżet | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Plik | Pełny¹ |
| Klucze alokacji | Pełny¹ | Pełny¹ | Plik | Plik | Plik | Plik |
| Kursy walut | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Wartości segmentów | Plik | Plik | Plik | Plik | Plik | Plik |
| CO-PA według wyceny | Plik | Plik | Plik | Plik | Plik | Plik |

## Systemy finansowe średniej wielkości i chmurowe

| Zbiór danych | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Jednostki | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Kalendarz fiskalny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Plan kont | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Działy | Pełny | Pełny | Pełny¹ | Pełny | Pełny | Pełny |
| Centra zysku | Plik | Plik | Plik | Plik | Plik | Plik |
| Produkty | Pełny | Pełny | Pełny¹ | Pełny | Pełny¹ | Pełny |
| Klienci | Pełny | Pełny | Pełny¹ | Pełny | Pełny¹ | Pełny |
| Księga główna | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Bilans próbny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Pozycje sprzedaży | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny |
| Lejek sprzedaży | Plik | Plik | Plik | Plik | Plik | Plik |
| Stany magazynowe | Plik | Plik | Pełny¹ | Plik | Plik | Pełny¹ |
| Budżet | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Pełny¹ |
| Klucze alokacji | Pełny¹ | Pełny¹ | Plik | Plik | Pełny¹ | Pełny |
| Kursy walut | Pełny | Pełny | Pełny¹ | Plik | Pełny | Pełny¹ |
| Wartości segmentów | Plik | Plik | Plik | Plik | Pełny¹ | Pełny |
| CO-PA według wyceny | Plik | Plik | Plik | Plik | Plik | Plik |

## Źródła CRM, konsolidacji i planowania

| Zbiór danych | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Jednostki | Plik | Plik | Plik |
| Kalendarz fiskalny | Plik | Plik | Plik |
| Plan kont | Plik | Plik | Plik |
| Działy | Plik | Plik | Plik |
| Centra zysku | Plik | Plik | Plik |
| Produkty | Pełny¹ | Plik | Plik |
| Klienci | Pełny¹ | Plik | Plik |
| Księga główna | Plik | Plik | Plik |
| Bilans próbny | Plik | Plik | Plik |
| Pozycje sprzedaży | Plik | Plik | Plik |
| Lejek sprzedaży | Pełny¹ | Plik | Plik |
| Stany magazynowe | Plik | Plik | Plik |
| Budżet | Plik | Pełny | Pełny |
| Klucze alokacji | Plik | Plik | Plik |
| Kursy walut | Plik | Plik | Plik |
| Wartości segmentów | Plik | Plik | Plik |
| CO-PA według wyceny | Plik | Plik | Plik |

## Uwagi według systemu

- **Salesforce** to źródło CRM. Dostarcza klientów, produkty i lejek sprzedaży, nigdy księgę.
- **OneStream** to źródło wyników. Dostarcza wyłącznie zbiór danych budżetu, wprowadzając Twoje skonsolidowane wyniki, aby Data Foundation mogło uzgodnić z nimi rachunek zysków i strat grupy.
- **Anaplan** to źródło planu. Dostarcza wyłącznie zbiór danych budżetu, z planu Budget, Forecast lub Consolidated.
- **SAP S/4HANA i SAP ECC** odczytują te same dane główne. ECC odczytuje księgę z pozycji księgowości finansowej i controllingu, a obroty z tabel sum księgi głównej. Centra zysku są odczytywane, gdy system je przechowuje. Pozycje sprzedaży to dokumenty rozliczeniowe, a nie CO-PA.
- **CO-PA według wyceny** nie jest odczytywane bezpośrednio z żadnego systemu. Dodaj je jako plik.
- **Workday** nie ma bezpośredniej usługi dziennika ani sald. Data Foundation udostępnia raporty do zbudowania i je odczytuje. Wartości segmentów (worktagi), klienci, produkty, pozycje sprzedaży i klucze dotyczące liczby pracowników pochodzą z opcjonalnych raportów. Budżety pozostają plikami.
- **Xero** nie dostarcza kursów walut. Dodaj je jako plik, jeśli Twoje jednostki używają więcej niż jednej waluty.
- **QuickBooks Online** odczytuje działy, klientów, produkty, kursy walut, budżety, stany magazynowe i pozycje sprzedaży, gdy plik firmy je zawiera.
- **NetSuite** odczytuje segmenty niestandardowe jako wartości segmentów. Kursy walut i stany magazynowe są odczytywane, gdy konto je oferuje, a budżety, gdy konto używa NetSuite Budgets, a rola może je odczytać.

## Powiązane

- [Data Foundation](/pl/guides/projects/data-foundation/)
- [Rozpocznij pracę z Data Foundation](/pl/guides/projects/data-foundation-getting-started/)
- [Dodaj pliki z danymi spoza ERP](/pl/guides/projects/data-foundation/#dodaj-pliki-z-danymi-spoza-erp)
- Przewodniki po dostępie dla połączeń:
  - [NetSuite](/pl/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/pl/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/pl/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/pl/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/pl/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/pl/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/pl/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/pl/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/pl/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pl/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pl/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pl/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pl/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pl/guides/connections/anaplan/#anaplan-jako-źródło-dla-data-foundation)
