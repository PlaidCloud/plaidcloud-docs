---
title: Funções de agregação (Lakehouse v1)
description: "Funções de agregação SQL do Lakehouse v1: resumem linhas — SUM, AVG, MIN, MAX, COUNT e agregações estatísticas."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

As funções de agregação são ferramentas essenciais em SQL que permitem efetuar cálculos sobre um conjunto de valores e devolver um único resultado.

Estas funções ajudam a extrair e a resumir dados de bases de dados para obter informações valiosas. 

| Nome da função                                                   | O que faz                                                                    | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Verifica se alguma linha cumpre a condição especificada                      | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Estima o número de valores distintos com HyperLogLog                         | 
| [ARG_MAX](aggregate-arg-max)                                     | Encontra o valor de arg correspondente ao valor máximo de val                | 
| [ARG_MIN](aggregate-arg-min)                                     | Encontra o valor de arg correspondente ao valor mínimo de val                | 
| [AVG_IF](aggregate-avg-if)                                       | Calcula a média das linhas que cumprem uma condição                          | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Converte todos os valores de uma coluna numa matriz                          |
| [AVG](aggregate-avg)                                             | Calcula o valor médio de uma coluna específica                               | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Conta o número de valores distintos numa coluna                              | 
| [COUNT_IF](aggregate-count-if)                                   | Conta as linhas que cumprem uma condição especificada                        | 
| [COUNT](aggregate-count)                                         | Conta o número de linhas que cumprem determinados critérios                  | 
| [COVAR_POP](aggregate-covar-pop)                                 | Devolve a covariância da população de um conjunto de pares de números        | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Devolve a covariância da amostra de um conjunto de pares de números          | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Devolve uma matriz com os elementos que calculam a média móvel dos valores de entrada |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Devolve uma matriz com os elementos que calculam a soma móvel dos valores de entrada |
| [HISTOGRAM](aggregate-histogram)                                | Gera um histograma da distribuição dos dados com intervalos de igual altura  | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | Converte valores numa matriz JSON, ignorando os NULL                         | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | Converte pares chave-valor num objeto JSON                                   | 
| [KURTOSIS](aggregate-kurtosis)                                   | Calcula a curtose em excesso de um conjunto de valores                       | 
| [MAX_IF](aggregate-max-if)                                       | Encontra o valor máximo das linhas que cumprem uma condição                  | 
| [MAX](aggregate-max)                                             | Encontra o maior valor de uma coluna específica                              | 
| [MEDIAN](aggregate-median)                                       | Calcula a mediana de uma coluna específica                                   | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Calcula a mediana de uma coluna específica com o algoritmo t-digest          | 
| [MIN_IF](aggregate-min-if)                                       | Encontra o valor mínimo das linhas que cumprem uma condição                  | 
| [MIN](aggregate-min)                                             | Encontra o menor valor de uma coluna específica                              | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Calcula o quantil interpolado de uma coluna específica                       |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Calcula o quantil de uma coluna específica                                   | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Calcula o quantil com o algoritmo t-digest                                   |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Calcula o quantil ponderado com o algoritmo t-digest                         |
| [RETENTION](aggregate-retention)                                 | Calcula a retenção para um conjunto de eventos                               | 
| [SKEWNESS](aggregate-skewness)                                   | Calcula a assimetria de um conjunto de valores                               | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Calcula o desvio padrão da população de uma coluna                           | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Calcula o desvio padrão da amostra de uma coluna                             | 
| [STRING_AGG](aggregate-string-agg)                               | Converte todos os valores não NULL em String, separados pelo delimitador     |
| [SUM_IF](aggregate-sum-if)                                       | Soma os valores de uma coluna específica que cumprem uma condição            | 
| [SUM](aggregate-sum)                                             | Soma os valores de uma coluna específica                                     | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analisa o comportamento dos utilizadores numa sequência de eventos ordenada no tempo |
