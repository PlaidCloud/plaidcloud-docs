---
title: Forecast
description: Generate time series forecasts from a project table and write predicted values to an output table.
sidebar:
  order: 6
---

## Description

The **Forecast** step reads a time series from an input table, fits a forecasting model, and writes future predicted values to an output table. Use it when you have historical values by date and want the workflow to produce a repeatable forecast.

## Configuration

### Forecast Parameters

* **Input Table** *(required)* — the table that contains the historical time series.
* **Output Table** *(required)* — the table where forecast rows are written.
* **Date Column** *(required)* — the mapped target column that contains the date or timestamp for each observation. The default is `ds`.
* **Value Column** *(required)* — the mapped target column that contains the numeric value to forecast.
* **Series Columns** *(optional)* — mapped target columns that identify separate series within the same table, such as customer, product, region, or account.
* **Frequency** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly`, or `Quarterly`. Use an explicit frequency when the input dates are sparse or irregular.
* **Horizon** — number of future periods to forecast. The default is 12.
* **Model** — `Automatic` by default. You can also select `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive`, or `AutoTheta`.

### Table Data Selection

Use the table data selection tab to shape the input table before forecasting. The mapped target columns must include the **Date Column**, **Value Column**, and any **Series Columns**.

Use **Inspect Source** to populate the mapping from the selected input table. You can populate both sides of the mapping, only the source side, or only the target side before adjusting the columns.

Saving is refused until the mapping has source columns — *Source columns are required: use Populate to read them from the input table.* — and while its target columns leave out the **Date Column**, the **Value Column** or a **Series Column**.

### Data Filters

Use the filters tab to limit rows, apply conditions, aggregate input data, or slice the result before the forecast runs.

## Behavior

The step creates or updates the configured output table with forecast rows for the selected horizon. When you configure **Series Columns**, PlaidCloud forecasts each series separately and includes the series values in the output.

## ARIMA Models, Fitting, and Diagnostics

An AI assistant or the REST API can also set these keys:

* `forecast_model` — besides the models above (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`), `arima`, `sarima` and `sarimax` fit the order you give: `order` is `[p, d, q]`, `seasonal_order` is `[P, D, Q, s]` (`sarima`, `sarimax`), and `exog_columns` names the exogenous regressor columns (`sarimax`).
* `mode` — `forecast` (default) writes the forecast of every series. `fit` fits one series with `arima`, `sarima` or `sarimax` and writes the model as a table. `apply` writes the forecasts of the model table named by `model_frame`; for a `sarimax` model, the input table holds the future regressors.
* `log_transform` — fit on the natural log of the values. With `apply`, whether the forecasts are returned from the log scale.
* `diagnostics` — write one table instead of a forecast: `residuals` or `coefficients` of the model in `model_frame`, `autocorrelation` (ACF and PACF) or `residual_stats` of the input value column, or `ljung_box`, the Q statistic and p-value for each lag of the model's residuals, else of the input value column. `max_lag` (default 40) is the largest lag for `autocorrelation` and `ljung_box`, and `dynamic` makes `residuals` use dynamic in-sample prediction.
* `interval_levels` — the prediction interval levels; `95` is the only level.
* `knime_config` — set by the KNIME converter to run a KNIME time series preparation node instead of a forecast: `aggregate_granularity` aggregates the values to a year, quarter, month, week, day, hour, minute or second, and `align_timestamps` aligns them to a period.

## Resources

Forecast processing runs in a separate job. Enable **Advanced Resource Management** only when the forecast needs more CPU or memory than the default request. Increasing resource requests can delay Forecast starts while capacity is scheduled. Set `cpu` (1 to 7, default 1) and `memory` (8 to 56 GiB, default 8) with it.
