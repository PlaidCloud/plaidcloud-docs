---
title: Połączenia
description: Konfiguruj połączenia PlaidCloud i zarządzaj nimi — zapisane konfiguracje, które umożliwiają przepływom pracy dostęp do zewnętrznych baz danych, magazynów w chmurze, systemów ERP i interfejsów REST API.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**Połączenie** to zapisana konfiguracja, która umożliwia PlaidCloud dostęp do systemu zewnętrznego — bazy danych, konta magazynu w chmurze, systemu ERP lub interfejsu REST API. Kroki przepływu pracy, które muszą odczytywać dane z tego systemu lub zapisywać do niego, odwołują się do połączenia, dzięki czemu poświadczenia i szczegóły punktu końcowego znajdują się w jednym miejscu.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Wiele kroków przepływu pracy odwołuje się do jednego zapisanego połączenia, które przechowuje poświadczenia i punkt końcowy w jednym miejscu i łączy się z systemem zewnętrznym — bazą danych, magazynem w chmurze, systemem ERP lub interfejsem REST API." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">kroki przepływu pracy</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Krok importu</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Krok eksportu</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Krok wyszukiwania</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Połączenie</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">poświadczenia + punkt końcowy, raz</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">system zewnętrzny</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">baza danych · magazyn · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Skonfiguruj połączenie raz; każdy krok, który odczytuje dane z systemu zewnętrznego lub zapisuje do niego, wskazuje na to połączenie, więc poświadczenia i szczegóły punktu końcowego nie są powielane w krokach.</figcaption>
</figure>

## Przewodniki

- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/) — tworzenie, edycja, testowanie i kontrola dostępu do połączenia oraz konfiguracja dla poszczególnych środowisk.
- [Używanie własnej hurtowni danych](/pl/guides/connections/external-lakehouse/) — samodzielne podłączenie własnej hurtowni Snowflake lub Databricks, logowanie własną tożsamością, zarządzanie kilkoma hurtowniami i podgląd kosztu każdego uruchomienia.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — połączenie z własnym zarządzanym serwerem Git obszaru roboczego bez adresu serwera i poświadczeń oraz automatyzacja kompilacji aplikacji Panel na jego podstawie.
- [Klonowanie połączenia](/pl/guides/connections/clone-connection/) — duplikowanie istniejącego połączenia dla nowego środowiska lub tenanta.
- [Data Foundation: Common Finance Model](/pl/guides/projects/data-foundation/) — Common Finance Model łączy dane ERP z wielu systemów i instancji ERP w jeden model z jednym planem kont, jednym zestawem jednostek i jedną walutą raportowania, który odczytują raporty, metryki i asystenci AI.
- Dostęp do Data Foundation, po jednej stronie dla każdego systemu, dla administratora, który przyznaje PlaidCloud dostęp do odczytu, wraz z informacją, co odesłać: [NetSuite](/pl/guides/connections/netsuite-access-for-data-foundation/), [SAP S/4HANA](/pl/guides/connections/sap-s4hana-access-for-data-foundation/), [SAP ECC](/pl/guides/connections/sap-ecc-access-for-data-foundation/), [SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud-access-for-data-foundation/), [Oracle E-Business Suite](/pl/guides/connections/oracle-ebs-access-for-data-foundation/), [Oracle Fusion](/pl/guides/connections/oracle-fusion-access-for-data-foundation/), [Dynamics 365 Finance and Operations](/pl/guides/connections/dynamics-365-fo-access-for-data-foundation/), [Business Central](/pl/guides/connections/business-central-access-for-data-foundation/), [Sage Intacct](/pl/guides/connections/sage-intacct-access-for-data-foundation/), [QuickBooks](/pl/guides/connections/quickbooks-access-for-data-foundation/), [Xero](/pl/guides/connections/xero-access-for-data-foundation/), [Workday](/pl/guides/connections/workday-access-for-data-foundation/), [Salesforce](/pl/guides/connections/salesforce-access-for-data-foundation/). [Macierz pokrycia Data Foundation](/pl/reference/data-foundation-coverage-matrix/) pokazuje, które zbiory danych dostarcza każdy system.
- [Źródła Singer](/pl/guides/connections/singer-sources/) — połączenie ze źródłami takimi jak Stripe, GitHub, Slack i BigQuery za pomocą tapów Singer, a następnie import ich danych do tabel projektu.
- [Połączenie z NetSuite](/pl/guides/connections/netsuite/) — konfiguracja połączenia z NetSuite i pobieranie danych finansowych i operacyjnych za pomocą SuiteQL.
- [Import danych finansowych z NetSuite](/pl/guides/connections/import-netsuite-financials/) — pobieranie sald, szczegółów księgi głównej i danych głównych za pomocą gotowych kroków importu NetSuite, bez pisania SuiteQL.
- [Księgowanie zapisu dziennika w NetSuite](/pl/guides/connections/post-netsuite-journal-entries/) — mapowanie tabel nagłówków i pozycji, podgląd i księgowanie zapisów dziennika w NetSuite.
- [Połączenie z Acumatica](/pl/guides/connections/acumatica/) — konfiguracja połączenia z Acumatica, import encji oraz księgowanie transakcji dziennika, faktur, rachunków i płatności.
- [Połączenie z Business Central](/pl/guides/connections/business-central/) — konfiguracja połączenia z Business Central przez Azure AD, import encji OData i księgowanie pozycji dziennika głównego.
- [Połączenie z Dynamics 365 Finance & Operations](/pl/guides/connections/dynamics-365-fo/) — konfiguracja połączenia z D365 F&O przez Azure AD, import encji OData/DMF i księgowanie zapisów dziennika.
- [Połączenie z Oracle Fusion](/pl/guides/connections/oracle-fusion/) — konfiguracja połączenia z Oracle Fusion, import sald księgi głównej i partii dziennika oraz księgowanie dzienników przez FBDI.
- [Połączenie z Workday Financials](/pl/guides/connections/workday-financials/) — konfiguracja połączenia z Workday Financials z użytkownikiem systemu integracji, import raportu RaaS i księgowanie zapisów dziennika.
- [Połączenie z SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/) — konfiguracja bezpośredniego połączenia z S/4HANA Cloud przez OAuth2, import zestawienia obrotów i sald oraz pozycji zapisów dziennika, a także księgowanie zapisów dziennika przez SOAP.
- [Doraźne wyodrębnienia z SAP ECC / S/4HANA](/pl/guides/connections/sap-adhoc-extract/) — wyszukiwanie w SAP według tabeli, kodu transakcji lub zapisanego zapytania SAP Query, podgląd i planowanie wyodrębnienia oraz ładowanie go do tabeli przez agenta PlaidLink.
- [Połączenie z Sage Intacct](/pl/guides/connections/sage-intacct/) — konfiguracja połączenia z Sage Intacct i pobieranie danych finansowych i księgowych.
- [Połączenie z Xero](/pl/guides/connections/xero/) — autoryzacja organizacji Xero jednym kliknięciem, import encji Accounting API oraz księgowanie zapisów ręcznych, faktur, rachunków, płatności i not kredytowych.
- [Połączenie z Salesforce](/pl/guides/connections/salesforce/) — konfiguracja External Client App i użytkownika Run As w Salesforce, a następnie wyodrębnianie obiektów CRM do tabel projektu.
- [Wyodrębnianie z HFM / FCCS (ad hoc)](/pl/guides/connections/hfm-fccs/) — połączenie z Oracle FCCS i samodzielne pobieranie wycinka danych za pomocą selektora punktu widzenia, bez zgłoszenia do zespołu HFM.
- [Połączenie z TM1](/pl/guides/connections/tm1/) — połączenie z serwerem IBM TM1 / Planning Analytics i odczyt danych kostki według widoku lub MDX, w podziale na okresy.
- [Połączenie z Anaplan](/pl/guides/connections/anaplan/) — połączenie z Anaplan i odczyt zapisanego widoku, uruchomienie istniejącej akcji eksportu lub załadowanie list do wymiaru PlaidCloud. Wyłącznie do odczytu.
- [OneStream dla Data Foundation](/pl/guides/connections/onestream-for-data-foundation/) — co konfiguruje administrator OneStream, aby Data Foundation mógł odczytywać skonsolidowane wyniki przez adapter danych.
- [Połączenie z QuickBooks](/pl/guides/connections/quickbooks/) — wymagania wstępne i obecne ograniczenia dla QuickBooks Online.
- [Przegląd Rejestru księgowań](/pl/guides/connections/posting-register/) — konsola na poziomie tenanta dla działów finansów i księgowości do przeglądania księgowań ERP we wszystkich projektach i połączeniach, które widzą.

## Powiązane

- [Dokumentacja konektorów](/pl/reference/connectors/) — pełny katalog obsługiwanych systemów i pól, których każdy z nich wymaga.
