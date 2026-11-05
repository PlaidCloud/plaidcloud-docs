---
title: Połączenia
description: Konfiguruj połączenia PlaidCloud i zarządzaj nimi — zapisanymi konfiguracjami, dzięki którym przepływy pracy docierają do zewnętrznych baz danych, magazynów w chmurze, systemów ERP i interfejsów REST API.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**Połączenie** to zapisana konfiguracja, dzięki której PlaidCloud łączy się z systemem zewnętrznym — bazą danych, kontem magazynu w chmurze, systemem ERP lub interfejsem REST API. Kroki przepływu pracy, które muszą odczytywać dane z tego systemu lub zapisywać je w nim, odwołują się do połączenia, dzięki czemu poświadczenia i szczegóły punktu końcowego są przechowywane w jednym miejscu.

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
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">baza · magazyn · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Skonfiguruj połączenie raz; każdy krok, który odczytuje dane z systemu zewnętrznego lub zapisuje je w nim, wskazuje na to połączenie, więc poświadczenia i szczegóły punktu końcowego nie są powielane w krokach.</figcaption>
</figure>

## Przewodniki

- [Tworzenie połączeń i zarządzanie nimi](/pl/guides/connections/create-connection/) — tworzenie, edycja i testowanie połączenia, kontrola dostępu do niego oraz konfiguracja dla poszczególnych środowisk.
- [Korzystanie z własnej hurtowni danych](/pl/guides/connections/external-lakehouse/) — samodzielne połączenie własnej hurtowni Snowflake lub Databricks, logowanie własną tożsamością, zarządzanie kilkoma hurtowniami i podgląd kosztu każdego uruchomienia.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — połączenie z zarządzanym serwerem Git Twojego obszaru roboczego bez adresu serwera i poświadczeń oraz automatyzacja budowania aplikacji Panel na jego podstawie.
- [Klonowanie połączenia](/pl/guides/connections/clone-connection/) — duplikowanie istniejącego połączenia dla nowego środowiska lub tenanta.
- [Data Foundation: Common Finance Model](/pl/guides/projects/data-foundation/) — Common Finance Model łączy dane ERP z wielu systemów i instancji ERP w jeden model z jednym planem kont, jednym zestawem jednostek i jedną walutą raportowania, z którego korzystają raporty, metryki i asystenci AI.
- [Źródła Singer](/pl/guides/connections/singer-sources/) — połącz się ze źródłami takimi jak Stripe, GitHub, Slack i BigQuery za pomocą tapów Singer, a następnie importuj ich dane do tabel projektu.
- [Połączenie NetSuite](/pl/guides/connections/netsuite/) — skonfiguruj połączenie z NetSuite i pobieraj dane finansowe i operacyjne za pomocą SuiteQL.
- [Dostęp do NetSuite dla Data Foundation](/pl/guides/connections/netsuite-access-for-data-foundation/) — co przygotowuje administrator NetSuite, aby Data Foundation mogło odczytywać NetSuite bezpośrednio, i co należy mu odesłać.
- [Importowanie danych finansowych z NetSuite](/pl/guides/connections/import-netsuite-financials/) — pobieraj salda, szczegóły księgi głównej i dane główne za pomocą gotowych kroków importu NetSuite, bez pisania SuiteQL.
- [Księgowanie zapisu dziennika w NetSuite](/pl/guides/connections/post-netsuite-journal-entries/) — mapowanie tabel nagłówków i pozycji, podgląd i księgowanie zapisów dziennika w NetSuite.
- [Połącz z Acumatica](/pl/guides/connections/acumatica/) — skonfiguruj połączenie z Acumatica, importuj encje i księguj transakcje dziennika, faktury, rachunki i płatności.
- [Połącz z Business Central](/pl/guides/connections/business-central/) — skonfiguruj połączenie z Business Central przez Azure AD, importuj encje OData i księguj pozycje dziennika głównego.
- [Połącz z Dynamics 365 Finance & Operations](/pl/guides/connections/dynamics-365-fo/) — skonfiguruj połączenie z D365 F&O przez Azure AD, importuj encje OData/DMF i księguj zapisy dziennika.
- [Połącz z Oracle Fusion](/pl/guides/connections/oracle-fusion/) — skonfiguruj połączenie z Oracle Fusion, importuj salda księgi głównej i partie zapisów dziennika oraz księguj dzienniki przez FBDI.
- [Połącz z Workday Financials](/pl/guides/connections/workday-financials/) — skonfiguruj połączenie z Workday Financials z użytkownikiem systemu integracji, importuj raport RaaS i księguj zapisy dziennika.
- [Połącz z SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/) — skonfiguruj bezpośrednie połączenie z S/4HANA Cloud przez OAuth2, importuj zestawienie obrotów i sald oraz pozycje zapisów dziennika i księguj zapisy dziennika przez SOAP.
- [Doraźne wyodrębnianie danych z SAP ECC / S/4HANA](/pl/guides/connections/sap-adhoc-extract/) — wyszukuj w SAP według tabeli, kodu transakcji lub zapisanego zapytania SAP Query, wyświetl podgląd i zaplanuj wyodrębnienie oraz załaduj je do tabeli przez agenta PlaidLink.
- [Połącz z Sage Intacct](/pl/guides/connections/sage-intacct/) — skonfiguruj połączenie z Sage Intacct i pobieraj dane finansowe i księgowe.
- [Połącz z Xero](/pl/guides/connections/xero/) — autoryzuj organizację Xero jednym kliknięciem, importuj encje Accounting API i księguj dzienniki ręczne, faktury, rachunki, płatności i noty kredytowe.
- [Połącz z Salesforce](/pl/guides/connections/salesforce/) — skonfiguruj Salesforce External Client App i użytkownika Run As, a następnie wyodrębniaj obiekty CRM do tabel projektu.
- [Wyodrębnianie z HFM / FCCS (doraźne)](/pl/guides/connections/hfm-fccs/) — połącz się z Oracle FCCS i samodzielnie pobierz wycinek danych za pomocą selektora punktu widzenia, bez zgłoszenia do zespołu HFM.
- [Połącz z TM1](/pl/guides/connections/tm1/) — połącz się z serwerem IBM TM1 / Planning Analytics i odczytuj dane kostki według widoku lub MDX, w podziale na okresy.
- [Połącz z Anaplan](/pl/guides/connections/anaplan/) — połącz się z Anaplan i odczytaj zapisany widok, uruchom istniejącą akcję eksportu lub załaduj listy do wymiaru PlaidCloud. Tylko odczyt.
- [OneStream dla Data Foundation](/pl/guides/connections/onestream-for-data-foundation/) — co przygotowuje administrator OneStream, aby Data Foundation mogło odczytywać skonsolidowane wyniki przez adapter danych.
- [Połącz z QuickBooks](/pl/guides/connections/quickbooks/) — wymagania wstępne i obecne ograniczenia QuickBooks Online.
- [Przegląd rejestru księgowań](/pl/guides/connections/posting-register/) — konsola na poziomie tenanta, w której dział finansów i księgowości przegląda księgowania ERP ze wszystkich widocznych dla niego projektów i połączeń.

## Powiązane

- [Dokumentacja konektorów](/pl/reference/connectors/) — pełny katalog obsługiwanych systemów i pól, których każdy z nich wymaga.
