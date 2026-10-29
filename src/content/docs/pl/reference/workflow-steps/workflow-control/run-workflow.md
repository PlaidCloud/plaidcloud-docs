---
title: Uruchom przepływ pracy
description: Uruchamia istniejący przepływ pracy z poziomu kroku przepływu pracy PlaidCloud, aby łączyć wykonywanie przepływów pracy i budować potoki przetwarzania obejmujące wiele przepływów pracy.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Opis

Uruchamia inny przepływ pracy w ramach wykonywania bieżącego przepływu pracy. Użyj tego kroku do łączenia przepływów pracy w łańcuch, gdy jeden proces logicznie zależy od innego — na przykład przepływ pracy „zamknięcie miesiąca” wywołuje przepływ pracy „załaduj dane rzeczywiste”, następnie przepływ pracy „uruchom alokacje”, a potem przepływ pracy „opublikuj pulpity”.

Wywołany przepływ pracy działa niezależnie — może znajdować się w tym samym projekcie lub w innym. Domyślnie wywołujący przepływ pracy jest kontynuowany bez oczekiwania; ustaw opcję **Wait until processing completes**, jeśli kolejne kroki w przepływie wywołującym zależą od zakończenia wywołanego przepływu pracy.



## Przepływ pracy do uruchomienia


Najpierw wybierz projekt zawierający przepływ pracy, który ma zostać uruchomiony, z menu rozwijanego **Projekt**.



Następnie wybierz konkretny przepływ pracy do uruchomienia z menu rozwijanego **Przepływ pracy**.



Dostępna jest również opcja **Wait until processing completes before continuing.** Zaznaczenie tego pola wyboru wstrzyma wykonywanie bieżącego przepływu pracy do czasu zakończenia wykonywania wywołanego przepływu pracy. Domyślnie ta opcja jest wyłączona, co oznacza, że bieżący przepływ pracy, w którym znajduje się ta transformacja, będzie kontynuował przetwarzanie równolegle z wywołanym przepływem pracy.







## Przykłady

Brak przykładów...
