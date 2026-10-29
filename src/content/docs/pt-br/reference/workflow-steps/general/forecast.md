---
title: Previsão
description: Gere previsões de séries temporais a partir de uma tabela de projeto e grave os valores previstos em uma tabela de saída.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Descrição

A etapa **Previsão** lê uma série temporal de uma tabela de entrada, ajusta um modelo de previsão e grava os valores futuros previstos em uma tabela de saída. Use-a quando você tiver valores históricos por data e quiser que o fluxo de trabalho produza uma previsão repetível.

## Configuração

### Parâmetros de previsão

* **Tabela de entrada** *(obrigatório)* — a tabela que contém a série temporal histórica.
* **Tabela de saída** *(obrigatório)* — a tabela em que as linhas de previsão são gravadas.
* **Coluna de data** *(obrigatório)* — a coluna de destino mapeada que contém a data ou o carimbo de data/hora de cada observação. O padrão é `ds`.
* **Coluna de valor** *(obrigatório)* — a coluna de destino mapeada que contém o valor numérico a prever.
* **Colunas de série** *(opcional)* — colunas de destino mapeadas que identificam séries separadas na mesma tabela, como cliente, produto, região ou conta.
* **Frequência** — `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` ou `Quarterly`. Use uma frequência explícita quando as datas de entrada forem esparsas ou irregulares.
* **Horizonte** — número de períodos futuros a prever. O padrão é 12.
* **Modelo** — `Automatic` por padrão. Você também pode selecionar `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` ou `AutoTheta`.

### Seleção de dados da tabela

Use a guia de seleção de dados da tabela para moldar a tabela de entrada antes da previsão. As colunas de destino mapeadas devem incluir a **Coluna de data**, a **Coluna de valor** e quaisquer **Colunas de série**.

Use **Inspecionar origem** para preencher o mapeamento a partir da tabela de entrada selecionada. Você pode preencher os dois lados do mapeamento, somente o lado da origem ou somente o lado do destino antes de ajustar as colunas.

O salvamento é recusado enquanto o mapeamento não tiver colunas de origem — *As colunas de origem são obrigatórias: use Populate para lê-las da tabela de entrada.* — e enquanto suas colunas de destino omitirem a **Coluna de data**, a **Coluna de valor** ou uma **Coluna de série**.

### Filtros de dados

Use a guia de filtros para limitar linhas, aplicar condições, agregar os dados de entrada ou fatiar o resultado antes de a previsão ser executada.

## Comportamento

A etapa cria ou atualiza a tabela de saída configurada com as linhas de previsão para o horizonte selecionado. Quando você configura **Colunas de série**, o PlaidCloud prevê cada série separadamente e inclui os valores da série na saída.

## Modelos ARIMA, ajuste e diagnósticos

A seção **Configurações do modelo** tem estes campos:

* **Modelo** (`forecast_model`) — além dos modelos acima (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`), **ARIMA**, **ARIMA sazonal (SARIMA)** e **ARIMA sazonal com regressores (SARIMAX)** (`arima`, `sarima`, `sarimax`) ajustam a ordem que você informar, usando **Ordem ARIMA (p, d, q)** (`order`) é `[p, d, q]`, **Ordem sazonal (P, D, Q, m)** (`seasonal_order`) é `[P, D, Q, s]` (`sarima`, `sarimax`), e **Colunas de regressores** (`exog_columns`) nomeia as colunas de regressores exógenos (`sarimax`).
* **Modo** (`mode`) — `forecast` (padrão) grava a previsão de cada série. `fit` ajusta uma série com `arima`, `sarima` ou `sarimax` e grava o modelo como uma tabela. `apply` grava as previsões da tabela de modelo indicada em **Tabela de modelo** (`model_frame`); para um modelo `sarimax`, a tabela de entrada contém os regressores futuros.
* **Ajustar o logaritmo dos valores** (`log_transform`) — ajusta sobre o logaritmo natural dos valores. Com `apply`, define se as previsões são retornadas da escala logarítmica.
* **Gravar diagnósticos em vez disso** (`diagnostics`) — grava uma tabela em vez de uma previsão: `residuals` ou `coefficients` do modelo em `model_frame`, `autocorrelation` (ACF e PACF) ou `residual_stats` da coluna de valor de entrada, ou `ljung_box`, a estatística Q e o valor p de cada defasagem dos resíduos do modelo, ou então da coluna de valor de entrada. **Defasagem máxima** (`max_lag`, padrão 40) é a maior defasagem para `autocorrelation` e `ljung_box`, e **Prever dinamicamente (realimentar as previsões)** (`dynamic`) faz `residuals` usar a previsão dinâmica na amostra.
* **Nó de séries temporais do KNIME** (`knime_config`) — executa um nó de preparação de séries temporais do KNIME em vez de uma previsão: `aggregate_granularity` agrega os valores por ano, trimestre, mês, semana, dia, hora, minuto ou segundo, e `align_timestamps` os alinha a um período.

Um assistente de IA ou a API REST também pode definir `interval_levels`, os níveis do intervalo de previsão; `95` é o único nível.

## Recursos

O processamento da previsão é executado em um job separado. Ative o **Gerenciamento avançado de recursos** somente quando a previsão precisar de mais CPU ou memória do que a solicitação padrão. Aumentar as solicitações de recursos pode atrasar o início da Previsão enquanto a capacidade é agendada. Defina `cpu` (1 a 7, padrão 1) e `memory` (8 a 56 GiB, padrão 8) junto com ele.
