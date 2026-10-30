---
title: Upiększanie (formatowanie) kodu w edytorach
description: Użyj przycisku Upiększ lub skrótu Shift+Alt+F, aby automatycznie sformatować kod SQL, JSON i wyrażeń w edytorach kroków przepływu pracy PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Upiększanie kodu w edytorach

Kilka edytorów kroków przepływu pracy korzysta z edytora kodu — kroki SQL (Frame Extract SQL, Remote Execute SQL, Remote Direct SQL, Remote Export SQL i Import SQL), **Result schema** (JSON) kroku LLM oraz Edytor wyrażeń używany w obszarach przepływów.

Każdy z tych edytorów ma przycisk **Upiększ**, który formatuje kod w miejscu — dodaje wcięcia i spójnie go układa, aby był łatwiejszy do czytania i przeglądu. Możesz też nacisnąć **Shift+Alt+F** (**Shift+Option+F** w systemie macOS), gdy kursor znajduje się w edytorze.

## Co jest formatowane

- **SQL** — przekształcany w czytelny, wielowierszowy układ: jedna klauzula w wierszu, wyrównane `CASE` / `WHEN` i rozbite zagnieżdżone funkcje. Zmienne projektu i tokeny szablonu, takie jak `{variable}`, `{{ ... }}` i `{% ... %}`, są zachowywane dokładnie.
- **JSON** — z ponownymi wcięciami o szerokości dwóch spacji (na przykład Result schema kroku LLM).
- **Wyrażenia** — wyrażenia PlaidCloud są formatowane standardowym formatowaniem Pythona: spójne odstępy wokół operatorów i przecinków oraz podziały wierszy w długich wyrażeniach.

## Warto wiedzieć

- Upiększanie nigdy nie zmienia działania kodu — tylko jego układ. Słowa kluczowe i identyfikatory SQL zachowują oryginalną wielkość liter.
- Jeśli kodu nie można przeanalizować (błąd składni), Upiększ pozostawia go bez zmian i wyświetla krótki komunikat, więc nigdy nie tracisz pracy.
- Formatowanie jest stosowane jako pojedynczy krok — naciśnij **Ctrl+Z** (**Cmd+Z** w systemie macOS), aby je cofnąć.
