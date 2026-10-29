---
title: Uruchamianie zakresu kroków w przepływie pracy
description: Uruchom wybrany zakres kroków w przepływie pracy PlaidCloud, aby selektywnie wykonać części potoku przetwarzania danych.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Uruchamianie pojedynczych kroków jest przydatne, ale czasem warto też uruchomić podzbiory całego przepływu pracy na potrzeby tworzenia, testowania lub rozwiązywania problemów. Aby uruchomić podzbiór kroków, zaznacz wszystkie kroki, które chcesz uruchomić, i wybierz **Uruchom wybrane kroki** z menu **Akcje** u góry hierarchii kroków przepływu pracy. Spowoduje to zwykłe przetwarzanie przepływu pracy, które rozpocznie się od początku wybranych kroków i zakończy po ukończeniu ostatniego wybranego kroku.

Jeśli ostatni wybrany krok znajduje się w grupie ustawionej na [**Execute in Parallel**](/pl/guides/workflows/controlling-parallel-execution/), uruchomienie czeka też na zakończenie każdego innego wybranego kroku w tej grupie, zanim się zatrzyma.
