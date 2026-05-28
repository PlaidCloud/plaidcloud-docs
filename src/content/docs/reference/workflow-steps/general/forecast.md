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

### Data Filters

Use the filters tab to limit rows, apply conditions, aggregate input data, or slice the result before the forecast runs.

## Behavior

The step creates or updates the configured output table with forecast rows for the selected horizon. When you configure **Series Columns**, PlaidCloud forecasts each series separately and includes the series values in the output.

## Resources

Forecast processing runs in a separate job. Enable **Advanced Resource Management** only when the forecast needs more CPU or memory than the default request. Increasing resource requests can delay Forecast starts while capacity is scheduled.
