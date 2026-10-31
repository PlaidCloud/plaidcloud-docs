---
title: Kontynuacja po błędzie
description: Skonfiguruj kroki przepływu pracy PlaidCloud tak, aby kontynuowały wykonywanie po błędzie, co pozwala uruchomić kolejne kroki mimo wcześniejszych niepowodzeń.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

Kroki przepływu pracy można ustawić tak, aby kontynuowały przetwarzanie nawet w razie błędu. Może to być przydatne w warunkach uruchamiania przepływu pracy lub gdy dane są dostępne sporadycznie. Jeśli krok zakończy się błędem, zostanie on zapisany jako błąd, ale przepływ pracy będzie nadal przetwarzany.



Aby ustawić tę opcję, otwórz formularz kroku z tabeli przepływu pracy — kliknij ikonę koła zębatego lub kliknij krok prawym przyciskiem myszy i wybierz **Edytuj szczegóły kroku** — a następnie przejdź do karty **Ogólne**. Ustaw **Akcja do wykonania w razie błędu** na **Kontynuuj**. Po zapisaniu zaktualizowanego kroku błędy tego kroku nie będą powodować zatrzymania przepływu pracy.



Kroki ustawione na kontynuację po błędzie mają specjalny wskaźnik w tabeli hierarchii kroków przepływu pracy.
