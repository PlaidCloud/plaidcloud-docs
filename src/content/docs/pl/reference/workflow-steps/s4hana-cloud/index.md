---
title: Kroki SAP S/4HANA Cloud
description: Kroki przepływu pracy, które odczytują dane z SAP S/4HANA Cloud Public Edition i zapisują je do niego przez połączenie S/4HANA Cloud — import zestawienia obrotów i sald oraz pozycji zapisów dziennika, a także księgowanie zapisów dziennika.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Kroki przepływu pracy, które odczytują dane z SAP S/4HANA Cloud Public Edition i zapisują je do niego przez [połączenie S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/). Krok importu pobiera dane zestawienia obrotów i sald lub pozycji zapisów dziennika bez konieczności pisania zapytań OData; krok księgowania księguje zapisy dziennika przez wspólny potok zapisu ERP w PlaidCloud.

## Kroki

- [Import S/4HANA Entity](/pl/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) — dane zestawienia obrotów i sald oraz pozycji zapisów dziennika, z filtrami po stronie serwera.
- [S/4HANA: Post Journal Entry](/pl/reference/workflow-steps/s4hana-cloud/s4hana-post/) — księgowanie zapisów dziennika przez SOAP, z zaksięgowanym zapisem odwracającym do korekt.

## Powiązane

- [Konektor REST SAP S/4HANA Cloud](/pl/reference/connectors/rest/s4hana-cloud/)
- [Połączenie z SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
