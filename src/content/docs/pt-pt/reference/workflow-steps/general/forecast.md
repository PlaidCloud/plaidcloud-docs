---
title: Forecast
description: Gere previsões de séries temporais a partir de uma tabela de projeto e escreva os valores previstos numa tabela de saída.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Descrição

O passo **Forecast** lê uma série temporal de uma tabela de entrada, ajusta um modelo de previsão e escreve os valores futuros previstos numa tabela de saída. Utilize-o quando tem valores históricos por data e pretende que o fluxo de trabalho produza uma previsão repetível.

## Configuração

### Parâmetros de previsão

* **Tabela de entrada** *(obrigatório)* — a tabela que contém a série temporal histórica.
* **Tabela de saída** *(obrigatório)* — a tabela onde as linhas de previsão são escritas.
* **Coluna de data** *(obrigatório)* — a coluna de destino mapeada que contém a data ou o carimbo de data/hora de cada observação. A predefinição é `ds`.
* **Coluna de valor** *(obrigatório)* — a coluna de destino mapeada que contém o valor numérico a prever.
* **Colunas de séries** *(opcional)* — colunas de destino mapeadas que identificam séries separadas dentro da mesma tabela, como cliente, produto, região ou conta.
* **Frequência** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` ou `Quarterly`. Utilize uma frequência explícita quando as datas de entrada são esparsas ou irregulares.
* **Horizonte** — número de períodos futuros a prever. A predefinição é 12.
* **Modelo** — `Automatic` por predefinição. Também pode selecionar `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` ou `AutoTheta`.

### Seleção de dados da tabela

Utilize o separador de seleção de dados da tabela para moldar a tabela de entrada antes da previsão. As colunas de destino mapeadas têm de incluir a **Coluna de data**, a **Coluna de valor** e quaisquer **Colunas de séries**.

Utilize **Inspecionar origem** para preencher o mapeamento a partir da tabela de entrada selecionada. Pode preencher os dois lados do mapeamento, apenas o lado da origem ou apenas o lado do destino antes de ajustar as colunas.

A gravação é recusada enquanto o mapeamento não tiver colunas de origem — *Source columns are required: use Populate to read them from the input table.* — e enquanto as suas colunas de destino não incluírem a **Coluna de data**, a **Coluna de valor** ou uma **Coluna de séries**.

### Filtros de dados

Utilize o separador de filtros para limitar linhas, aplicar condições, agregar os dados de entrada ou fatiar o resultado antes de a previsão ser executada.

## Comportamento

O passo cria ou atualiza a tabela de saída configurada com linhas de previsão para o horizonte selecionado. Quando configura **Colunas de séries**, o PlaidCloud prevê cada série em separado e inclui os valores da série na saída.

## Modelos ARIMA, ajuste e diagnósticos

A secção **Configurações do modelo** tem estes campos:

* **Modelo** (`forecast_model`) — além dos modelos acima (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`), **ARIMA**, **ARIMA sazonal (SARIMA)** e **ARIMA sazonal com regressores (SARIMAX)** (`arima`, `sarima`, `sarimax`) ajustam a ordem indicada, utilizando **Ordem ARIMA (p, d, q)** (`order`), que é `[p, d, q]`, **Ordem sazonal (P, D, Q, m)** (`seasonal_order`), que é `[P, D, Q, s]` (`sarima`, `sarimax`), e **Colunas de regressores** (`exog_columns`), que indica as colunas de regressores exógenos (`sarimax`).
* **Modo** (`mode`) — `forecast` (predefinição) escreve a previsão de cada série. `fit` ajusta uma série com `arima`, `sarima` ou `sarimax` e escreve o modelo como tabela. `apply` escreve as previsões da tabela de modelo indicada em **Tabela de modelo** (`model_frame`); para um modelo `sarimax`, a tabela de entrada contém os regressores futuros.
* **Ajustar o logaritmo dos valores** (`log_transform`) — ajusta sobre o logaritmo natural dos valores. Com `apply`, indica se as previsões são devolvidas a partir da escala logarítmica.
* **Escrever diagnósticos em vez disso** (`diagnostics`) — escreve uma tabela em vez de uma previsão: `residuals` ou `coefficients` do modelo em `model_frame`, `autocorrelation` (ACF e PACF) ou `residual_stats` da coluna de valor de entrada, ou `ljung_box`, a estatística Q e o valor p de cada desfasamento dos resíduos do modelo, ou, na falta deste, da coluna de valor de entrada. **Defasagem máxima** (`max_lag`, predefinição 40) é o maior desfasamento para `autocorrelation` e `ljung_box`, e **Prever dinamicamente (realimentar as previsões)** (`dynamic`) faz com que `residuals` utilize a previsão dinâmica dentro da amostra.
* **Nó de séries temporais do KNIME** (`knime_config`) — executa um nó de preparação de séries temporais do KNIME em vez de uma previsão: `aggregate_granularity` agrega os valores por ano, trimestre, mês, semana, dia, hora, minuto ou segundo, e `align_timestamps` alinha-os a um período.

Um assistente de IA ou a API REST também pode definir `interval_levels`, os níveis do intervalo de previsão; `95` é o único nível.

## Recursos

O processamento da previsão é executado numa tarefa separada. Ative a **Gestão avançada de recursos** apenas quando a previsão precisar de mais CPU ou memória do que o pedido predefinido. O aumento dos pedidos de recursos pode atrasar o arranque da previsão enquanto a capacidade é agendada. Defina `cpu` (1 a 7, predefinição 1) e `memory` (8 a 56 GiB, predefinição 8) com ela.
