---
title: Ładowanie i wyładowywanie wymiarów
description: Ładuj i wyładowuj dane wymiarów w PlaidCloud, w tym importy zbiorcze, odświeżanie danych i synchronizację z zewnętrznymi źródłami danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

Wymiary można utrzymywać za pomocą operacji przepływu pracy, ładując dane. Dodatkowo dane wymiarowe można spłaszczyć do danych tabelarycznych i zapisać w tabelach. Jest to często przydatne do wzbogacania danych raportowych i analitycznych.


## Ładowanie wymiarów

Ponieważ wymiary reprezentują hierarchiczne struktury danych, proces ładowania musi przekazywać relacje zawarte w danych. PlaidCloud obsługuje dwie różne struktury danych do ładowania wymiarów:
 * Nadrzędny–podrzędny — dane są ułożone pionowo, a kolumna *nadrzędna* i kolumna *podrzędna* określają element nadrzędny każdego elementu podrzędnego w całej strukturze
 * Poziomy — dane są ułożone poziomo, a każda kolumna reprezentuje poziom hierarchii od lewej do prawej

 Oprócz struktury w procesie ładowania można uwzględnić inne informacje o wymiarze, takie jak wartości, aliasy i właściwości.

 Ładowanie poziomów (płaskie) przyjmuje domyślną konsolidację, którą otrzymuje każdy węzeł pośredni tworzony przez ładowanie, i może wskazywać kolumnę liścia: wtedy to ta kolumna decyduje, który węzeł przechowuje aliasy, właściwości i wartości wiersza; w przeciwnym razie liściem jest ostatni wypełniony poziom.

 Domyślny typ konsolidacji ładowania nadrzędny–podrzędny dotyczy każdego wiersza, którego własna konsolidacja jest pusta lub nierozpoznana, więc musi być jednym z prawidłowych typów, nawet jeśli tabela wskazuje także kolumnę konsolidacji. Hierarchia, do której kieruje ładowanie, nie może mieć takiej samej nazwy jak kolumna mapowana przez ładowanie: kolumna o takiej nazwie jest odczytywana jako hierarchia, do której należy każdy wiersz, więc ładowanie wskazujące oba jest odrzucane, zamiast przyjąć jedną interpretację i zignorować drugą.

 Ładowanie aliasów, właściwości lub wartości sprawdza członka z każdego wiersza przed zapisaniem czegokolwiek. Jeśli któryś wiersz wskazuje członka, którego wymiar nie zawiera, ładowanie kończy się niepowodzeniem i zgłasza te nazwy, a nic z tego ładowania nie zostaje zapisane. Załaduj najpierw strukturę lub uwzględnij brakujących członków w niej, a następnie załaduj atrybuty.

 Więcej informacji zawiera krok przepływu pracy [Dimension Load](/pl/reference/workflow-steps/dimensions/dimension-load).


## Wyładowywanie (eksportowanie) wymiarów

Eksportowanie wymiarów do tabel obsługuje dwa podejścia do struktury:
 * Nadrzędny–podrzędny — dane są ułożone pionowo, a kolumna *nadrzędna* i kolumna *podrzędna* określają element nadrzędny każdego elementu podrzędnego w całej strukturze
 * Poziomy — dane są ułożone poziomo, a każda kolumna reprezentuje poziom hierarchii od lewej do prawej

Do spłaszczonych danych tabelarycznych można także dołączyć właściwości i wartości.

 Więcej informacji zawiera krok przepływu pracy [Dimension Export](/pl/reference/workflow-steps/dimensions/dimension-export).
