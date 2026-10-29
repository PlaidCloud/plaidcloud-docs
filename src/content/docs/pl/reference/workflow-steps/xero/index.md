---
title: Kroki Xero
description: Kroki przepływu pracy, które odczytują dane z Xero i zapisują je w Xero za pośrednictwem połączenia Xero — importują encje Accounting API oraz księgują ręczne zapisy dziennika, faktury, rachunki, płatności i noty kredytowe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/xero/index.md
---

Kroki przepływu pracy, które odczytują dane z Xero i zapisują je w Xero za pośrednictwem [połączenia Xero](/pl/guides/connections/xero/). Krok importu pobiera encje Accounting API Xero bez konieczności pisania zapytania; krok księgowania księguje ręczne zapisy dziennika, faktury, rachunki, płatności i noty kredytowe za pośrednictwem wspólnego potoku zapisu ERP w PlaidCloud.

## Kroki

- [Xero: importuj encję](/pl/reference/workflow-steps/xero/import-xero-entity/) — konta, kontakty, faktury, noty kredytowe, płatności, ręczne zapisy dziennika, transakcje bankowe, pozycje, kategorie śledzenia, stawki podatkowe i waluty.
- [Xero: zaksięguj dokument](/pl/reference/workflow-steps/xero/xero-post/) — księguje ręczne zapisy dziennika, faktury, rachunki, płatności i noty kredytowe.

## Powiązane

- [Konektor REST Xero](/pl/reference/connectors/rest/xero/)
- [Połącz z Xero](/pl/guides/connections/xero/)
- [Przeglądaj historię księgowania ERP](/pl/guides/connections/erp-post-history/)
