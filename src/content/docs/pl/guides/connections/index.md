---
title: Połączenia
description: Konfiguruj połączenia PlaidCloud i zarządzaj nimi — zapisanymi konfiguracjami, które umożliwiają przepływom pracy dostęp do zewnętrznych baz danych, magazynów w chmurze, systemów ERP i interfejsów API REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**Połączenie** to zapisana konfiguracja, która umożliwia PlaidCloud dostęp do systemu zewnętrznego — bazy danych, konta magazynu w chmurze, systemu ERP lub interfejsu API REST. Kroki przepływu pracy, które muszą odczytywać dane z tego systemu lub zapisywać je w nim, odwołują się do połączenia, dzięki czemu dane uwierzytelniające i szczegóły punktu końcowego znajdują się w jednym miejscu.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Wiele kroków przepływu pracy odwołuje się do jednego zapisanego połączenia, które przechowuje dane uwierzytelniające i punkt końcowy w jednym miejscu i łączy się z systemem zewnętrznym — bazą danych, magazynem w chmurze, systemem ERP lub interfejsem API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">kroki przepływu pracy</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">krok importu</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">krok eksportu</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">krok wyszukiwania</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Połączenie</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">dane uwierzytelniające + punkt końcowy, raz</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">system zewnętrzny</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">baza danych · magazyn · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Skonfiguruj połączenie raz; każdy krok, który odczytuje dane z systemu zewnętrznego lub zapisuje je w nim, wskazuje to połączenie, więc dane uwierzytelniające i szczegóły punktu końcowego nie są powielane w krokach.</figcaption>
</figure>

## Przewodniki

- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/) — tworzenie, edytowanie i testowanie połączenia, kontrola dostępu do niego oraz konfiguracja dla poszczególnych środowisk.
- [Użyj własnej hurtowni danych](/pl/guides/connections/external-lakehouse/) — samodzielnie połącz własną hurtownię danych Snowflake lub Databricks, loguj się własną tożsamością, zarządzaj wieloma hurtowniami i sprawdzaj, ile kosztuje każde uruchomienie.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — połącz się z zarządzanym serwerem Git swojego obszaru roboczego bez adresu URL serwera i danych uwierzytelniających oraz automatyzuj na jego podstawie kompilacje aplikacji Panel.
- [Klonowanie połączenia](/pl/guides/connections/clone-connection/) — zduplikuj istniejące połączenie na potrzeby nowego środowiska lub tenanta.
- [Data Foundation: Common Finance Model](/pl/guides/projects/data-foundation/) — Common Finance Model łączy dane ERP z wielu systemów i instancji ERP w jeden model z jednym planem kont, jednym zestawem jednostek i jedną walutą raportowania, który odczytują raporty, metryki i asystenci AI.
- [Źródła Singer](/pl/guides/connections/singer-sources/) — łącz się ze źródłami takimi jak Stripe, GitHub, Slack i BigQuery za pomocą tapów Singer, a następnie importuj ich dane do tabel projektu.
- [Połączenie z NetSuite](/pl/guides/connections/netsuite/) — skonfiguruj połączenie NetSuite i pobieraj dane finansowe oraz operacyjne za pomocą SuiteQL.
- [Dostęp NetSuite dla Data Foundation](/pl/guides/connections/netsuite-access-for-data-foundation/) — co konfiguruje administrator NetSuite, aby Data Foundation mogło bezpośrednio odczytywać NetSuite, i co należy odesłać.
- [Importowanie danych finansowych z NetSuite](/pl/guides/connections/import-netsuite-financials/) — pobieraj salda, szczegóły księgi głównej i dane podstawowe za pomocą gotowych kroków importu NetSuite, bez pisania SuiteQL.
- [Księgowanie zapisu dziennika w NetSuite](/pl/guides/connections/post-netsuite-journal-entries/) — zmapuj tabele nagłówków i pozycji, wyświetl podgląd i zaksięguj zapisy dziennika w NetSuite.
- [Połączenie z Acumatica](/pl/guides/connections/acumatica/) — skonfiguruj połączenie Acumatica, importuj jednostki oraz księguj transakcje dziennika, faktury, rachunki i płatności.
- [Połączenie z Business Central](/pl/guides/connections/business-central/) — skonfiguruj połączenie Business Central z Azure AD, importuj jednostki OData i księguj wiersze ogólnego dziennika.
- [Połączenie z Dynamics 365 Finance & Operations](/pl/guides/connections/dynamics-365-fo/) — skonfiguruj połączenie D365 F&O z Azure AD, importuj jednostki OData/DMF i księguj zapisy dziennika.
- [Połączenie z Oracle Fusion](/pl/guides/connections/oracle-fusion/) — skonfiguruj połączenie Oracle Fusion, importuj salda księgi głównej i partie zapisów dziennika oraz księguj dzienniki przez FBDI.
- [Połączenie z Workday Financials](/pl/guides/connections/workday-financials/) — skonfiguruj połączenie Workday Financials z użytkownikiem systemu integracji, importuj raport RaaS i księguj zapisy dziennika.
- [Połączenie z SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/) — skonfiguruj bezpośrednie połączenie z S/4HANA Cloud przez OAuth2, importuj zestawienie obrotów i sald oraz pozycje zapisów dziennika i księguj zapisy dziennika przez SOAP.
- [Wyodrębnianie ad hoc z SAP ECC / S/4HANA](/pl/guides/connections/sap-adhoc-extract/) — przeszukuj SAP według tabeli, kodu transakcji lub zapisanego zapytania SAP Query, wyświetl podgląd i zaplanuj wyodrębnienie, a następnie załaduj je do tabeli przez agenta PlaidLink.
- [Połączenie z Sage Intacct](/pl/guides/connections/sage-intacct/) — skonfiguruj połączenie Sage Intacct i pobieraj dane finansowe oraz księgowe.
- [Połączenie z Xero](/pl/guides/connections/xero/) — autoryzuj organizację Xero jednym kliknięciem, importuj jednostki Accounting API i księguj zapisy ręczne, faktury, rachunki, płatności i noty kredytowe.
- [Połączenie z Salesforce](/pl/guides/connections/salesforce/) — skonfiguruj Salesforce External Client App i użytkownika Run As, a następnie wyodrębnij obiekty CRM do tabel projektu.
- [Wyodrębnianie z HFM / FCCS (ad hoc)](/pl/guides/connections/hfm-fccs/) — połącz się z Oracle FCCS i samodzielnie pobieraj wycinek danych za pomocą selektora punktu widzenia, bez zgłoszenia do zespołu HFM.
- [Połączenie z TM1](/pl/guides/connections/tm1/) — połącz się z serwerem IBM TM1 / Planning Analytics i odczytuj dane kostki według widoku lub MDX, w podziale na okresy.
- [Połączenie z Anaplan](/pl/guides/connections/anaplan/) — połącz się z Anaplan i odczytuj zapisany widok, uruchamiaj istniejącą akcję eksportu lub ładuj listy do wymiaru PlaidCloud. Tylko do odczytu.
- [Połączenie z QuickBooks](/pl/guides/connections/quickbooks/) — wymagania wstępne i obecne ograniczenia dla QuickBooks Online.
- [Przegląd rejestru księgowań](/pl/guides/connections/posting-register/) — konsola na poziomie tenanta dla działów finansów i księgowości do przeglądania księgowań ERP we wszystkich projektach i połączeniach, które widzą.

## Powiązane

- [Dokumentacja referencyjna łączników](/pl/reference/connectors/) — pełny katalog obsługiwanych systemów i pól wymaganych przez każdy z nich.
