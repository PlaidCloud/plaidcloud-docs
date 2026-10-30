---
title: Prévision
description: Générez des prévisions de séries temporelles à partir d'une table de projet et écrivez les valeurs prédites dans une table de sortie.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Description

L'étape **Prévision** lit une série temporelle dans une table d'entrée, ajuste un modèle de prévision et écrit les valeurs prédites futures dans une table de sortie. Utilisez-la lorsque vous disposez de valeurs historiques par date et que vous voulez que le workflow produise une prévision reproductible.

## Configuration

### Paramètres de prévision

* **Table d'entrée** *(obligatoire)* — la table qui contient la série temporelle historique.
* **Table de sortie** *(obligatoire)* — la table dans laquelle les lignes de prévision sont écrites.
* **Colonne de date** *(obligatoire)* — la colonne cible mappée qui contient la date ou l'horodatage de chaque observation. La valeur par défaut est `ds`.
* **Colonne de valeur** *(obligatoire)* — la colonne cible mappée qui contient la valeur numérique à prévoir.
* **Colonnes de série** *(facultatif)* — les colonnes cibles mappées qui identifient des séries distinctes au sein d'une même table, comme le client, le produit, la région ou le compte.
* **Fréquence** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` ou `Quarterly`. Utilisez une fréquence explicite lorsque les dates d'entrée sont clairsemées ou irrégulières.
* **Horizon** — nombre de périodes futures à prévoir. La valeur par défaut est 12.
* **Modèle** — `Automatic` par défaut. Vous pouvez aussi sélectionner `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` ou `AutoTheta`.

### Sélection des données de la table

Utilisez l'onglet de sélection des données de la table pour mettre en forme la table d'entrée avant la prévision. Les colonnes cibles mappées doivent inclure la **Colonne de date**, la **Colonne de valeur** et les éventuelles **Colonnes de série**.

Utilisez **Inspecter la source** pour remplir le mappage à partir de la table d'entrée sélectionnée. Vous pouvez remplir les deux côtés du mappage, seulement le côté source ou seulement le côté cible avant d'ajuster les colonnes.

L'enregistrement est refusé tant que le mappage n'a pas de colonnes sources — *Source columns are required: use Populate to read them from the input table.* — et tant que ses colonnes cibles omettent la **Colonne de date**, la **Colonne de valeur** ou une **Colonne de série**.

### Filtres de données

Utilisez l'onglet des filtres pour limiter les lignes, appliquer des conditions, agréger les données d'entrée ou découper le résultat avant l'exécution de la prévision.

## Comportement

L'étape crée ou met à jour la table de sortie configurée avec les lignes de prévision pour l'horizon sélectionné. Lorsque vous configurez des **Colonnes de série**, PlaidCloud prévoit chaque série séparément et inclut les valeurs de série dans la sortie.

## Modèles ARIMA, ajustement et diagnostics

La section **Paramètres du modèle** comporte les champs suivants :

* **Modèle** (`forecast_model`) — outre les modèles ci-dessus (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`), **ARIMA**, **ARIMA saisonnier (SARIMA)** et **ARIMA saisonnier avec régresseurs (SARIMAX)** (`arima`, `sarima`, `sarimax`) ajustent l'ordre que vous indiquez : **Ordre ARIMA (p, d, q)** (`order`) vaut `[p, d, q]`, **Ordre saisonnier (P, D, Q, m)** (`seasonal_order`) vaut `[P, D, Q, s]` (`sarima`, `sarimax`), et **Colonnes de régresseurs** (`exog_columns`) nomme les colonnes de régresseurs exogènes (`sarimax`).
* **Mode** (`mode`) — `forecast` (par défaut) écrit la prévision de chaque série. `fit` ajuste une série avec `arima`, `sarima` ou `sarimax` et écrit le modèle sous forme de table. `apply` écrit les prévisions du modèle de la table nommée par **Table du modèle** (`model_frame`) ; pour un modèle `sarimax`, la table d'entrée contient les régresseurs futurs.
* **Ajuster le logarithme des valeurs** (`log_transform`) — ajuste sur le logarithme népérien des valeurs. Avec `apply`, indique si les prévisions sont renvoyées depuis l'échelle logarithmique.
* **Écrire plutôt les diagnostics** (`diagnostics`) — écrit une table au lieu d'une prévision : `residuals` ou `coefficients` du modèle de `model_frame`, `autocorrelation` (ACF et PACF) ou `residual_stats` de la colonne de valeur d'entrée, ou `ljung_box`, la statistique Q et la valeur p pour chaque décalage des résidus du modèle, sinon de la colonne de valeur d'entrée. **Décalage max.** (`max_lag`, 40 par défaut) est le plus grand décalage pour `autocorrelation` et `ljung_box`, et **Prévoir dynamiquement (réinjecter les prédictions)** (`dynamic`) fait utiliser à `residuals` la prédiction dynamique sur l'échantillon.
* **Nœud de séries temporelles KNIME** (`knime_config`) — exécute un nœud KNIME de préparation de séries temporelles au lieu d'une prévision : `aggregate_granularity` agrège les valeurs à l'année, au trimestre, au mois, à la semaine, au jour, à l'heure, à la minute ou à la seconde, et `align_timestamps` les aligne sur une période.

Un assistant IA ou l'API REST peut aussi définir `interval_levels`, les niveaux des intervalles de prédiction ; `95` est le seul niveau.

## Ressources

Le traitement de la prévision s'exécute dans une tâche distincte. Activez la **Gestion avancée des ressources** uniquement lorsque la prévision a besoin de plus de CPU ou de mémoire que la demande par défaut. L'augmentation des demandes de ressources peut retarder le démarrage des prévisions pendant que la capacité est planifiée. Définissez `cpu` (de 1 à 7, 1 par défaut) et `memory` (de 8 à 56 Gio, 8 par défaut) avec cette option.
