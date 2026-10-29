---
title: Calculate PCM Model
description: Uruchamiaj obliczenia modelu SAP PCM z kroku przepływu pracy PlaidCloud, aby wykonywać zadania przetwarzania rentowności i alokacji kosztów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Opis



Uruchamia silnik obliczeniowy w modelu SAP Profitability and Cost Management (PCM). Użyj go w przepływie pracy, aby wykonać obliczenia kosztów po tym, jak wcześniejsze ładowania danych wypełnią dane wejściowe modelu (przypisania, klucze, dane źródłowe).

Obliczenia są asynchroniczne po stronie serwera PCM; w razie potrzeby przerwania długotrwałych obliczeń połącz z [Stop PCM Model Calculation](/pl/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/).


## Nasze kwalifikacje


PlaidCloud jest oficjalnym partnerem SAP i preferowanym dostawcą usług związanych z projektowaniem i wdrażaniem modeli SAP PCM.







## Przykłady


Wybierz z listy rozwijanej Agent do użycia, wpisz nazwę modelu w polu „Nazwa modelu”, zaznacz pole wyboru „Wait for Calculation to Complete” (jeśli chcesz), a następnie kliknij „Save and Run Step”.
