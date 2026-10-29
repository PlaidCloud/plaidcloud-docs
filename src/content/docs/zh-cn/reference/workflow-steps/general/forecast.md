---
title: 预测
description: 根据项目表生成时间序列预测，并将预测值写入输出表。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## 说明

**预测**步骤从输入表读取时间序列，拟合预测模型，并将未来的预测值写入输出表。当您有按日期记录的历史值，并希望工作流生成可重复的预测时，请使用此步骤。

## 配置

### 预测参数

* **输入表** *（必填）*——包含历史时间序列的表。
* **输出表** *（必填）*——写入预测行的表。
* **日期列** *（必填）*——已映射的目标列，包含每条观测值的日期或时间戳。默认为 `ds`。
* **值列** *（必填）*——已映射的目标列，包含要预测的数值。
* **序列列** *（可选）*——已映射的目标列，用于在同一张表中标识各个独立的序列，例如客户、产品、区域或科目。
* **频率**——`Auto`、`Hourly`、`Daily`、`Weekly`、`Monthly` 或 `Quarterly`。输入日期稀疏或不规则时，请使用明确的频率。
* **预测范围**——要预测的未来期数。默认为 12。
* **模型**——默认为 `Automatic`。也可选择 `AutoETS`、`AutoARIMA`、`Seasonal Naive`、`Naive` 或 `AutoTheta`。

### 表数据选择

使用表数据选择选项卡，在预测之前整理输入表。已映射的目标列必须包含**日期列**、**值列**和所有**序列列**。

使用**检查源**，根据所选输入表填充映射。在调整各列之前，可以同时填充映射的两侧、仅填充源侧或仅填充目标侧。

映射没有源列时，以及其目标列缺少**日期列**、**值列**或某个**序列列**时，无法保存——*Source columns are required: use Populate to read them from the input table.*

### 数据筛选器

使用筛选器选项卡，在运行预测之前限制行、应用条件、汇总输入数据或对结果切片。

## 行为

步骤会创建或更新已配置的输出表，写入所选预测范围的预测行。配置**序列列**后，PlaidCloud 会分别预测每个序列，并在输出中包含序列的值。

## ARIMA 模型、拟合和诊断

**模型设置**部分包含以下字段：

* **模型**（`forecast_model`）——除上述模型（`automatic`、`auto_ets`、`auto_arima`、`seasonal_naive`、`naive`、`auto_theta`）外，**ARIMA**、**季节性 ARIMA (SARIMA)** 和**带回归变量的季节性 ARIMA (SARIMAX)**（`arima`、`sarima`、`sarimax`）会按您给出的阶数拟合：**ARIMA 阶数 (p, d, q)**（`order`）为 `[p, d, q]`，**季节阶数 (P, D, Q, m)**（`seasonal_order`）为 `[P, D, Q, s]`（`sarima`、`sarimax`），**回归变量列**（`exog_columns`）指定外生回归变量列（`sarimax`）。
* **众数**（`mode`）——`forecast`（默认）写入每个序列的预测。`fit` 使用 `arima`、`sarima` 或 `sarimax` 拟合一个序列，并将模型写为表。`apply` 写入由**模型表**（`model_frame`）指定的模型表的预测；对于 `sarimax` 模型，输入表包含未来的回归变量。
* **拟合值的对数**（`log_transform`）——对值的自然对数进行拟合。使用 `apply` 时，表示预测是否从对数尺度返回。
* **改为写入诊断信息**（`diagnostics`）——写入一张表而不是预测：`residuals` 或 `coefficients` 为 `model_frame` 中模型的残差或系数，`autocorrelation`（ACF 和 PACF）或 `residual_stats` 针对输入的值列，`ljung_box` 为模型残差每个滞后的 Q 统计量和 p 值，没有模型时则针对输入的值列。**最大滞后**（`max_lag`，默认 40）是 `autocorrelation` 和 `ljung_box` 的最大滞后，**动态预测（将预测值反馈回去）**（`dynamic`）使 `residuals` 使用动态样本内预测。
* **KNIME 时间序列节点**（`knime_config`）——运行 KNIME 时间序列准备节点而不是预测：`aggregate_granularity` 将值聚合到年、季度、月、周、日、小时、分钟或秒，`align_timestamps` 将其对齐到某个周期。

AI 助手或 REST API 还可以设置 `interval_levels`（预测区间水平）；`95` 是唯一的水平。

## 资源

预测处理在单独的作业中运行。只有当预测需要的 CPU 或内存超过默认请求时，才启用**高级资源管理**。提高资源请求可能会在调度容量期间延迟预测的启动。同时设置 `cpu`（1 到 7，默认 1）和 `memory`（8 到 56 GiB，默认 8）。
