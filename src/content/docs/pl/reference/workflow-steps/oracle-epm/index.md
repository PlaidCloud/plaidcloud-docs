---
title: Kroki Oracle EPM (HFM / FCCS)
description: Kroki przepływu pracy do samoobsługowego pobierania wycinka danych ad hoc z Oracle FCCS przez połączenie HFM/FCCS — zbuduj punkt widzenia, uruchom go i załaduj wynik jako tabelę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

Kroki przepływu pracy odczytujące dane z Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) przez [połączenie HFM/FCCS](/pl/guides/connections/hfm-fccs/). Użytkownik finansowy buduje punkt widzenia w formularzu kroku, uruchamia go, a zwrócona siatka trafia automatycznie do tabeli projektu — bez zgłoszenia do zespołu HFM i bez wiedzy o konsolidacji.

## Kroki

- [HFM/FCCS: odczytaj dane (ad hoc)](/pl/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — samoobsługowe pobranie wycinka danych za pomocą selektora punktu widzenia; buforuje powtórne pobrania, jest gotowy na zabezpieczenia na poziomie wierszy i można go awansować do zaplanowanego cyklicznego ładowania.

## Powiązane

- [Wyodrębnianie z HFM / FCCS (przewodnik)](/pl/guides/connections/hfm-fccs/)
- [Konektor HFM / FCCS](/pl/reference/connectors/rest/hfm-fccs/)
