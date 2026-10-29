---
title: Zgłoś błąd przepływu pracy
description: Zgłasza niestandardowy błąd w kroku przepływu pracy PlaidCloud, aby uruchomić obsługę błędów i zatrzymać wykonywanie, gdy warunki nie są spełnione.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Opis

Wymusza przejście przepływu pracy w stan błędu z niestandardowym komunikatem. Użyj tego kroku, gdy przepływ pracy ma zakończyć się niepowodzeniem na podstawie warunku danych wykrytego przez wcześniejsze kroki — na przykład „zakończ niepowodzeniem, jeśli liczba wierszy wynosi zero”, „zakończ niepowodzeniem, jeśli kluczowa tabela walidacji zawiera niezmapowane wartości” lub „zakończ niepowodzeniem, jeśli sprawdzenie salda nie uzgadnia się”.

Połącz go z [warunkami kroków](/pl/guides/workflows/step-conditions/), aby błąd był zgłaszany tylko wtedy, gdy coś rzeczywiście jest nie tak. Po uruchomieniu krok natychmiast zatrzymuje przepływ pracy i zapisuje błąd w dzienniku przepływu pracy, co z kolei może uruchomić przepływ pracy naprawczy, jeśli został skonfigurowany.


## Zgłoś błąd przepływu pracy


Krok jest przeznaczony głównie do użycia z warunkami kroków — można go ustawić tak, aby wykonywał się po spełnieniu warunków i zgłaszał błąd w przepływie pracy.
