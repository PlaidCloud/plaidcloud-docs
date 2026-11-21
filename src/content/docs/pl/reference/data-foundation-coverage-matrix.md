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
| **Pełny¹** | Odczytywany bezpośrednio, gdy system go przechowuje. System bez tych danych nie zatrzymuje ładowania. Połączenie bez dostępu do nich pozostawia ten zbiór danych pusty lub powoduje niepowodzenie tylko tego zbioru danych, a reszta zostaje załadowana. |
| **Plik** | System nie dostarcza tego zbioru danych. Dodaj go jako plik. |

## SAP, Oracle i Dynamics 365

| Zbiór danych | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Jednostki | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Kalendarz fiskalny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Plan kont | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Działy | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Centra zysku | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Pełny¹ |
| Lokalizacje | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Projekty | Plik | Plik | Plik | Plik | Plik | Plik |
| Przedstawiciele handlowi | Plik | Plik | Plik | Plik | Plik | Plik |
| Produkty | Pełny | Pełny | Pełny | Pełny¹ | Pełny¹ | Pełny |
| Klienci | Pełny | Pełny | Pełny | Pełny¹ | Pełny¹ | Pełny |
| Dostawcy | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Księga główna | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Bilans próbny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Saldo na koniec miesiąca | Plik | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Plik |
| Salda bankowe | Plik | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ |
| Pozycje sprzedaży | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Lejek sprzedaży | Plik | Plik | Plik | Plik | Plik | Plik |
| Pozycje faktur zakupu | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Zamówienia zakupu | Pełny¹ | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Plik |
| Pozycje otwarte | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Płatności | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Stany magazynowe | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Koszty standardowe | Pełny¹ | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Plik |
| Środki trwałe | Pełny¹ | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Plik |
| Ruchy środków trwałych | Pełny¹ | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Plik |
| Budżet | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Klucze alokacji | Pełny¹ | Pełny¹ | Plik | Plik | Plik | Plik |
| Kursy walut | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Wartości segmentów | Plik | Plik | Plik | Plik | Plik | Plik |
| CO-PA według wyceny | Pełny¹ | Pełny¹ | Plik | Plik | Plik | Plik |

## Systemy finansowe średniej wielkości i chmurowe

| Zbiór danych | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jednostki | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Kalendarz fiskalny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Plan kont | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Działy | Pełny | Pełny¹ | Pełny | Plik | Pełny¹ | Pełny | Pełny |
| Centra zysku | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Pełny¹ |
| Lokalizacje | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Plik | Pełny¹ |
| Projekty | Plik | Plik | Pełny¹ | Plik | Plik | Plik | Plik |
| Przedstawiciele handlowi | Plik | Plik | Plik | Plik | Plik | Plik | Pełny¹ |
| Produkty | Pełny | Plik | Pełny | Pełny¹ | Pełny¹ | Pełny¹ | Pełny |
| Klienci | Pełny | Plik | Pełny | Pełny¹ | Pełny¹ | Pełny¹ | Pełny |
| Dostawcy | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Księga główna | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Bilans próbny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny | Pełny |
| Saldo na koniec miesiąca | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Plik |
| Salda bankowe | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Pozycje sprzedaży | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny |
| Lejek sprzedaży | Plik | Plik | Plik | Plik | Plik | Plik | Plik |
| Pozycje faktur zakupu | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Pozycje otwarte | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Płatności | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Zamówienia zakupu | Plik | Plik | Plik | Plik | Plik | Plik | Plik |
| Stany magazynowe | Pełny¹ | Plik | Plik | Pełny¹ | Plik | Plik | Pełny¹ |
| Koszty standardowe | Plik | Plik | Plik | Plik | Plik | Plik | Plik |
| Środki trwałe | Plik | Plik | Plik | Plik | Plik | Plik | Plik |
| Ruchy środków trwałych | Plik | Plik | Plik | Plik | Plik | Plik | Plik |
| Budżet | Pełny¹ | Plik | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ | Pełny¹ |
| Klucze alokacji | Pełny¹ | Plik | Pełny¹ | Plik | Plik | Pełny¹ | Pełny |
| Kursy walut | Pełny | Plik | Pełny | Pełny¹ | Plik | Pełny | Pełny¹ |
| Wartości segmentów | Plik | Plik | Plik | Plik | Plik | Pełny¹ | Pełny¹ |
| CO-PA według wyceny | Plik | Plik | Plik | Plik | Plik | Plik | Plik |

## Źródła CRM, konsolidacji i planowania

| Zbiór danych | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Jednostki | Plik | Plik | Plik |
| Kalendarz fiskalny | Pełny¹ | Plik | Plik |
| Plan kont | Plik | Plik | Plik |
| Działy | Plik | Plik | Plik |
| Centra zysku | Plik | Plik | Plik |
| Projekty | Pełny¹ | Plik | Plik |
| Przedstawiciele handlowi | Pełny¹ | Plik | Plik |
| Produkty | Pełny¹ | Plik | Plik |
| Klienci | Pełny¹ | Plik | Plik |
| Księga główna | Plik | Plik | Plik |
| Bilans próbny | Plik | Plik | Plik |
| Pozycje sprzedaży | Plik | Plik | Plik |
| Lejek sprzedaży | Pełny¹ | Plik | Plik |
| Zamówienia sprzedaży | Pełny¹ | Plik | Plik |
| Stany magazynowe | Plik | Plik | Plik |
| Budżet | Plik | Pełny | Pełny |
| Klucze alokacji | Plik | Pełny¹ | Pełny¹ |
| Kursy walut | Plik | Plik | Plik |
| Wartości segmentów | Plik | Plik | Plik |
| CO-PA według wyceny | Plik | Plik | Plik |

## Uwagi według systemu

- **Zamówienia sprzedaży, umowy, przychody przyszłych okresów i ruchy magazynowe** nie są odczytywane z żadnego systemu, z wyjątkiem zamówień z Salesforce. Dodaj je jako pliki.
- **Salesforce** to źródło CRM. Dostarcza klientów, produkty, lejek sprzedaży, przedstawicieli handlowych (użytkowników), kampanie jako projekty, swoje miesiące fiskalne i zamówienia, nigdy księgę. Zamówienia wymagają włączenia Orders w Salesforce. Gdy Salesforce odmówi odczytu zamówień, niepowodzeniem kończą się tylko miesiące zamówień, które zachowują to, co załadowano ostatnio.
- **OneStream** to źródło wyników. Dostarcza zbiór danych budżetu, wprowadzając Twoje skonsolidowane wyniki, aby Data Foundation mogło uzgodnić z nimi rachunek zysków i strat grupy, oraz scenariusz Budget lub Forecast jako plan. Opcjonalny drugi adapter dostarcza planowaną liczbę pracowników i planowane ilości jako klucze alokacji.
- **Anaplan** to źródło planu. Dostarcza zbiór danych budżetu, z planu Budget, Forecast lub Consolidated, oraz klucze alokacji z opcjonalnego drugiego eksportu.
- **SAP S/4HANA i SAP ECC** odczytują te same dane główne, dostawców, faktury zakupu, zamówienia zakupu, pozycje otwarte, płatności, rejestr środków trwałych i koszty standardowe. ECC odczytuje księgę z pozycji księgowości finansowej i controllingu, a obroty i saldo na koniec miesiąca z tabeli sum księgi głównej. Centra zysku i zakłady (lokalizacje) są odczytywane, gdy system je przechowuje. Pozycje sprzedaży to dokumenty rozliczeniowe. CO-PA według wyceny jest odczytywane ze wskazanej tabeli pozycji obszaru wynikowego; jeśli żadna nie jest wskazana, dodaj je jako plik.
- **Oracle E-Business Suite** odczytuje lokalizacje i centra zysku z segmentu planu kont wskazanego dla każdego z nich.
- **Oracle Fusion** odczytuje każdy opcjonalny zbiór danych z osobnego raportu BI Publisher. Niewdrożony raport klientów, produktów, lokalizacji lub dostawców pozostawia ten zbiór danych pusty z ostrzeżeniem; zbiór danych każdego innego raportu kończy się niepowodzeniem i zachowuje to, co załadowano ostatnio; wszystko inne zostaje załadowane.
- **Workday** nie ma bezpośredniej usługi dziennika ani sald. Data Foundation udostępnia raporty do zbudowania i je odczytuje. Wartości segmentów (worktagi), klienci, produkty, dostawcy, pozycje sprzedaży, księgi pomocnicze, salda bankowe, budżety i klucze pochodzą z opcjonalnych raportów, a saldo na koniec miesiąca z salda końcowego raportu sald początkowych.
- **Sage 100** jest odczytywany przez agenta PlaidLink, jedna firma na połączenie. Prowadzi księgi w jednej walucie, więc nie dostarcza kursów walut, a Data Foundation nie odczytuje jego produktów, klientów ani pozycji sprzedaży. Działy są odczytywane z segmentu działu konta, gdy maska konta go zawiera.
- **Xero** nie dostarcza kursów walut. Dodaj je jako plik, jeśli Twoje jednostki używają więcej niż jednej waluty. Działy, lokalizacje i centra zysku to opcje kategorii śledzenia nazwanych dokładnie Department, Site i Profit centre. Xero dopuszcza dwie kategorie śledzenia, więc organizacja ma co najwyżej dwie z tych trzech.
- **QuickBooks Online** nie ma działów: jego lokalizacje (locations) są odczytywane jako lokalizacje, a klasy jako centra zysku. Klienci, produkty, dostawcy, kursy walut, budżety, stany magazynowe, sprzedaż i zakupy są odczytywane, gdy firma je przechowuje, a stany magazynowe tylko wtedy, gdy firma śledzi ilość na stanie.
- **NetSuite** odczytuje segmenty niestandardowe jako wartości segmentów, klasy jako centra zysku, a lokalizacje (locations) jako lokalizacje. Kursy walut i stany magazynowe są odczytywane, gdy konto je oferuje, a budżety, gdy konto używa NetSuite Budgets, a rola może je odczytać.

## Saldo na koniec miesiąca

Data Foundation odczytuje saldo końcowe, które każdy system sam raportuje na koniec każdego miesiąca (zobacz [Czy liczbom można ufać?](/pl/guides/projects/data-foundation-proof/)), z następujących źródeł:

| System | Źródło salda na koniec miesiąca |
| --- | --- |
| SAP ECC | Tabela sum księgi głównej (`FAGLFLEXT` lub `GLT0` w klasycznej księdze głównej) |
| Oracle E-Business Suite | `GL_BALANCES`, która musi zawierać każdy okres |
| Oracle Fusion | Raport PlaidCloudBalances obejmujący każdy okres |
| Business Central | Zestawienie obrotów i sald na koniec każdego miesiąca |
| Sage Intacct | Salda kont (saldo końcowe każdego miesiąca) |
| QuickBooks Online | Raport Zestawienie obrotów i sald na koniec każdego miesiąca |
| Xero | Raport Zestawienie obrotów i sald na koniec każdego miesiąca |
| Workday | Saldo końcowe raportu sald początkowych (Beginning Balances) |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite i Sage 100 nie raportują osobnego salda, które odczytywałoby Data Foundation. Ładują się i działają jak zwykle. Gdy Business Central odmówi udostępnienia zestawienia obrotów i sald na koniec miesiąca, saldo tego miesiąca kończy się niepowodzeniem i zachowuje to, co załadowano ostatnio.

## Szczegóły zapisów dziennika

Oprócz kwot każdy wiersz księgi głównej zawiera typ zapisu dziennika, datę dokumentu, informację, kto go wprowadził i kiedy, kto go zatwierdził, zapis, który odwraca, oraz podatek, jeśli system je przechowuje. Kalendarz fiskalny zawiera status każdego okresu.

| System | Typ zapisu | Data dokumentu | Wprowadzający i data | Zatwierdzający | Odwrócenie | Podatek | Status okresu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Tak | Tak | Tak | Nie | Nie | Kod | Tak |
| SAP ECC | Tak | Tak | Tak | Nie | Tak | Kod i kwota | Tak |
| SAP S/4HANA Cloud | Tak | Tak | Tak | Nie | Tak | Nie | Nie |
| Oracle E-Business Suite | Tak | Tak | Tak | Tak | Tak | Nie | Tak |
| Oracle Fusion | Tak | Tak | Tak | Tak | Tak | Nie | Tak |
| Dynamics 365 Finance and Operations | Tak | Tak | Tak | Nie | Nie | Nie | Tak |
| Business Central | Tak | Tak | Tak | Nie | Tak | Nie | Tak |
| Sage 100 | Nie | Nie | Nie | Nie | Nie | Nie | Zamknięty po zakończeniu okresu |
| Sage Intacct | Tak | Tak | Tak | Tak | Tak | Nie | Tak |
| QuickBooks Online | Tak | Tak | Tak | Nie | Nie | Nie | Data zamknięcia ksiąg |
| Xero | Tak | Tak | Tylko data | Nie | Nie | Nie | Data blokady |
| Workday | Tak | Tak | Tak | Tak | Tak | Kod i kwota | Tak |
| NetSuite | Tak | Tak | Tak | Nie | Nie | Nie | Tak |

SAP S/4HANA Cloud odczytuje, kto wprowadził zapis dziennika i co on odwraca, z usługi Journal Entry, Sage Intacct z partii zapisów dziennika, a Oracle E-Business Suite odczytuje zatwierdzającego z `GL_JE_BATCHES`. Połączenie, które nie może ich odczytać, pozostawia te kolumny puste.

## Powiązane

- [Data Foundation](/pl/guides/projects/data-foundation/)
- [Rozpocznij pracę z Data Foundation](/pl/guides/projects/data-foundation-getting-started/)
- [Dodaj pliki z danymi spoza ERP](/pl/guides/projects/data-foundation/#dodawanie-plików-z-danymi-spoza-systemu-erp)
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
  - [Sage 100](/pl/guides/connections/sage-100/)
  - [Sage Intacct](/pl/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pl/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pl/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pl/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pl/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pl/guides/connections/anaplan/#anaplan-jako-źródło-dla-data-foundation)
