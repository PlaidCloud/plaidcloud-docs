---
title: Prognoza
description: Generuj prognozy szeregów czasowych z tabeli projektu i zapisuj przewidywane wartości w tabeli wyjściowej.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Opis

Krok **Prognoza** odczytuje szereg czasowy z tabeli wejściowej, dopasowuje model prognostyczny i zapisuje przyszłe przewidywane wartości w tabeli wyjściowej. Używaj go, gdy masz historyczne wartości według dat i chcesz, aby przepływ pracy tworzył powtarzalną prognozę.

## Konfiguracja

### Parametry prognozy

* **Tabela wejściowa** *(wymagane)* — tabela zawierająca historyczny szereg czasowy.
* **Tabela wyjściowa** *(wymagane)* — tabela, do której zapisywane są wiersze prognozy.
* **Kolumna daty** *(wymagane)* — zmapowana kolumna docelowa zawierająca datę lub znacznik czasu każdej obserwacji. Domyślnie `ds`.
* **Kolumna wartości** *(wymagane)* — zmapowana kolumna docelowa zawierająca wartość liczbową do prognozowania.
* **Kolumny serii** *(opcjonalne)* — zmapowane kolumny docelowe identyfikujące oddzielne serie w tej samej tabeli, takie jak klient, produkt, region lub konto.
* **Częstotliwość** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` lub `Quarterly`. Użyj jawnej częstotliwości, gdy daty wejściowe są rzadkie lub nieregularne.
* **Horyzont** — liczba przyszłych okresów do prognozowania. Domyślnie 12.
* **Model** — domyślnie `Automatic`. Możesz też wybrać `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` lub `AutoTheta`.

### Wybór danych tabeli

Użyj karty wyboru danych tabeli, aby ukształtować tabelę wejściową przed prognozowaniem. Zmapowane kolumny docelowe muszą obejmować **Kolumna daty**, **Kolumna wartości** oraz wszystkie **Kolumny serii**.

Użyj **Sprawdź źródło**, aby wypełnić mapowanie na podstawie wybranej tabeli wejściowej. Przed dostosowaniem kolumn możesz wypełnić obie strony mapowania, tylko stronę źródłową lub tylko docelową.

Zapis jest odrzucany, dopóki mapowanie nie ma kolumn źródłowych — *Source columns are required: use Populate to read them from the input table.* — oraz gdy jego kolumny docelowe pomijają **Kolumna daty**, **Kolumna wartości** lub **Kolumny serii**.

### Filtry danych

Użyj karty filtrów, aby ograniczyć wiersze, zastosować warunki, zagregować dane wejściowe lub wyciąć fragment wyniku przed uruchomieniem prognozy.

## Działanie

Krok tworzy lub aktualizuje skonfigurowaną tabelę wyjściową o wiersze prognozy dla wybranego horyzontu. Gdy skonfigurujesz **Kolumny serii**, PlaidCloud prognozuje każdą serię osobno i dołącza do wyniku wartości serii.

## Modele ARIMA, dopasowanie i diagnostyka

Sekcja **Ustawienia modelu** zawiera następujące pola:

* **Model** (`forecast_model`) — oprócz modeli wymienionych wyżej (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`) modele **ARIMA**, **Sezonowy ARIMA (SARIMA)** i **Sezonowy ARIMA z regresorami (SARIMAX)** (`arima`, `sarima`, `sarimax`) dopasowują podany przez Ciebie rząd, przy czym **Rząd ARIMA (p, d, q)** (`order`) to `[p, d, q]`, **Rząd sezonowy (P, D, Q, m)** (`seasonal_order`) to `[P, D, Q, s]` (`sarima`, `sarimax`), a **Kolumny regresorów** (`exog_columns`) wskazują egzogeniczne kolumny regresorów (`sarimax`).
* **Tryb** (`mode`) — `forecast` (domyślnie) zapisuje prognozę każdej serii. `fit` dopasowuje jedną serię za pomocą `arima`, `sarima` lub `sarimax` i zapisuje model jako tabelę. `apply` zapisuje prognozy modelu z tabeli wskazanej w polu **Tabela modelu** (`model_frame`); dla modelu `sarimax` tabela wejściowa zawiera przyszłe regresory.
* **Dopasuj logarytm wartości** (`log_transform`) — dopasowuje na naturalnym logarytmie wartości. Przy `apply` określa, czy prognozy są zwracane ze skali logarytmicznej.
* **Zamiast tego zapisz diagnostykę** (`diagnostics`) — zapisuje jedną tabelę zamiast prognozy: `residuals` lub `coefficients` modelu z `model_frame`, `autocorrelation` (ACF i PACF) lub `residual_stats` kolumny wartości wejściowej albo `ljung_box`, czyli statystykę Q i wartość p dla każdego opóźnienia reszt modelu, a w przeciwnym razie kolumny wartości wejściowej. **Maks. opóźnienie** (`max_lag`, domyślnie 40) to największe opóźnienie dla `autocorrelation` i `ljung_box`, a **Prognozuj dynamicznie (przekazuj prognozy z powrotem)** (`dynamic`) sprawia, że `residuals` używa dynamicznej predykcji wewnątrz próby.
* **Węzeł szeregów czasowych KNIME** (`knime_config`) — uruchamia węzeł przygotowania szeregów czasowych KNIME zamiast prognozy: `aggregate_granularity` agreguje wartości do roku, kwartału, miesiąca, tygodnia, dnia, godziny, minuty lub sekundy, a `align_timestamps` wyrównuje je do okresu.

Asystent AI lub REST API mogą też ustawić `interval_levels`, czyli poziomy przedziałów predykcji; jedynym poziomem jest `95`.

## Zasoby

Przetwarzanie prognozy działa w osobnym zadaniu. Włącz **Zaawansowane zarządzanie zasobami** tylko wtedy, gdy prognoza potrzebuje więcej CPU lub pamięci niż w żądaniu domyślnym. Zwiększenie żądań zasobów może opóźnić starty Prognozy w czasie, gdy planowana jest pojemność. Ustaw przy tym `cpu` (od 1 do 7, domyślnie 1) i `memory` (od 8 do 56 GiB, domyślnie 8).
