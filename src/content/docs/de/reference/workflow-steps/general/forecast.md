---
title: Prognose
description: Erstellen Sie Zeitreihenprognosen aus einer Projekttabelle und schreiben Sie die vorhergesagten Werte in eine Ausgabetabelle.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Beschreibung

Der Schritt **Prognose** liest eine Zeitreihe aus einer Eingabetabelle, passt ein Prognosemodell an und schreibt künftige Vorhersagewerte in eine Ausgabetabelle. Verwenden Sie ihn, wenn Sie historische Werte nach Datum haben und der Workflow eine wiederholbare Prognose erzeugen soll.

## Konfiguration

### Prognoseparameter

* **Eingabetabelle** *(erforderlich)* — die Tabelle mit der historischen Zeitreihe.
* **Ausgabetabelle** *(erforderlich)* — die Tabelle, in die die Prognosezeilen geschrieben werden.
* **Datumsspalte** *(erforderlich)* — die zugeordnete Zielspalte, die das Datum oder den Zeitstempel jeder Beobachtung enthält. Der Standardwert ist `ds`.
* **Wertspalte** *(erforderlich)* — die zugeordnete Zielspalte, die den numerischen Wert enthält, der prognostiziert werden soll.
* **Serienspalten** *(optional)* — zugeordnete Zielspalten, die einzelne Serien innerhalb derselben Tabelle kennzeichnen, etwa Kunde, Produkt, Region oder Konto.
* **Häufigkeit** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` oder `Quarterly`. Verwenden Sie eine explizite Häufigkeit, wenn die Eingabedaten spärlich oder unregelmäßig sind.
* **Prognosehorizont** — Anzahl der künftigen Perioden, die prognostiziert werden. Der Standardwert ist 12.
* **Modell** — standardmäßig `Automatic`. Sie können auch `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` oder `AutoTheta` auswählen.

### Tabellendatenauswahl

Verwenden Sie die Registerkarte für die Tabellendatenauswahl, um die Eingabetabelle vor der Prognose zu formen. Die zugeordneten Zielspalten müssen die **Datumsspalte**, die **Wertspalte** und alle **Serienspalten** enthalten.

Verwenden Sie **Quelle untersuchen**, um die Zuordnung aus der ausgewählten Eingabetabelle zu füllen. Sie können beide Seiten der Zuordnung, nur die Quellseite oder nur die Zielseite füllen, bevor Sie die Spalten anpassen.

Das Speichern wird abgelehnt, solange die Zuordnung keine Quellspalten hat — *Source columns are required: use Populate to read them from the input table.* — und solange ihre Zielspalten die **Datumsspalte**, die **Wertspalte** oder eine **Serienspalte** auslassen.

### Datenfilter

Verwenden Sie die Registerkarte für Filter, um Zeilen zu begrenzen, Bedingungen anzuwenden, Eingabedaten zusammenzufassen oder das Ergebnis aufzuteilen, bevor die Prognose ausgeführt wird.

## Verhalten

Der Schritt erstellt oder aktualisiert die konfigurierte Ausgabetabelle mit Prognosezeilen für den gewählten Horizont. Wenn Sie **Serienspalten** konfigurieren, prognostiziert PlaidCloud jede Serie separat und nimmt die Serienwerte in die Ausgabe auf.

## ARIMA-Modelle, Anpassung und Diagnosen

Der Abschnitt **Modelleinstellungen** hat diese Felder:

* **Modell** (`forecast_model`) — neben den oben genannten Modellen (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`) passen **ARIMA**, **Saisonales ARIMA (SARIMA)** und **Saisonales ARIMA mit Regressoren (SARIMAX)** (`arima`, `sarima`, `sarimax`) die von Ihnen angegebene Ordnung an. Dabei ist **ARIMA-Ordnung (p, d, q)** (`order`) gleich `[p, d, q]`, **Saisonale Ordnung (P, D, Q, m)** (`seasonal_order`) gleich `[P, D, Q, s]` (`sarima`, `sarimax`), und **Regressorspalten** (`exog_columns`) benennt die exogenen Regressorspalten (`sarimax`).
* **Modus** (`mode`) — `forecast` (Standard) schreibt die Prognose jeder Serie. `fit` passt eine Serie mit `arima`, `sarima` oder `sarimax` an und schreibt das Modell als Tabelle. `apply` schreibt die Prognosen der Modelltabelle, die unter **Modelltabelle** (`model_frame`) angegeben ist. Bei einem `sarimax`-Modell enthält die Eingabetabelle die künftigen Regressoren.
* **Den Logarithmus der Werte anpassen** (`log_transform`) — passt anhand des natürlichen Logarithmus der Werte an. Bei `apply` bestimmt es, ob die Prognosen von der Log-Skala zurückgegeben werden.
* **Stattdessen Diagnosen schreiben** (`diagnostics`) — schreibt statt einer Prognose eine Tabelle: `residuals` oder `coefficients` des Modells in `model_frame`, `autocorrelation` (ACF und PACF) oder `residual_stats` der Eingabe-Wertspalte, oder `ljung_box`, die Q-Statistik und den p-Wert für jeden Lag der Residuen des Modells, sonst der Eingabe-Wertspalte. **Max. Lag** (`max_lag`, Standard 40) ist der größte Lag für `autocorrelation` und `ljung_box`, und **Dynamisch prognostizieren (Prognosen zurückführen)** (`dynamic`) lässt `residuals` die dynamische In-Sample-Vorhersage verwenden.
* **KNIME-Zeitreihenknoten** (`knime_config`) — führt statt einer Prognose einen KNIME-Knoten zur Zeitreihenaufbereitung aus: `aggregate_granularity` aggregiert die Werte auf ein Jahr, Quartal, einen Monat, eine Woche, einen Tag, eine Stunde, Minute oder Sekunde, und `align_timestamps` richtet sie an einer Periode aus.

Ein KI-Assistent oder die REST-API kann außerdem `interval_levels` festlegen, die Stufen der Vorhersageintervalle. `95` ist die einzige Stufe.

## Ressourcen

Die Prognoseverarbeitung läuft in einem separaten Job. Aktivieren Sie die **Erweiterte Ressourcenverwaltung** nur, wenn die Prognose mehr CPU oder Arbeitsspeicher benötigt als die Standardanforderung. Höhere Ressourcenanforderungen können den Start von Prognosen verzögern, während Kapazität eingeplant wird. Legen Sie damit `cpu` (1 bis 7, Standard 1) und `memory` (8 bis 56 GiB, Standard 8) fest.
