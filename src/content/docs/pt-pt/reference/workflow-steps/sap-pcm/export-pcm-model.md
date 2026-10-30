---
title: Calculate and Export PCM Model
description: Execute um cálculo de modelo PCM e exporte o resultado para uma base de dados ou para um ficheiro delimitado, através de um agente PlaidLink.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Descrição

Calcula um modelo SAP PCM e exporta o resultado num único passo, através de um [agente PlaidLink](/pt-pt/reference/workflow-steps/agent/) com acesso à instalação PCM. Enquanto [Calculate PCM Model](/pt-pt/reference/workflow-steps/sap-pcm/calculate-pcm-model/) apenas executa o cálculo, este passo também move o resultado.

## Configuração

### Agente a utilizar

O agente PlaidLink que acede à instalação PCM.

### Informações do modelo

- **Nome do modelo** — o modelo PCM a calcular.
- **Export specification path** — a especificação de exportação do PCM que descreve o que exportar.

### Destino de saída da exportação

Escolha um destino de base de dados, um destino de ficheiro, ou ambos.

**Para uma base de dados** — ativado por predefinição; a exportação grava através do destino de base de dados configurado na especificação.

**Para um ficheiro** — desativado por predefinição. Quando ativado:

- **Caminho do ficheiro** — onde o agente grava o ficheiro.
- **Alias** — o alias registado na exportação. Por predefinição, `DEFAULT ALIAS`.
- **Precision** — casas decimais dos valores exportados. Por predefinição, 0.
- **Delimitador** — vírgula, tabulação, barra vertical, ponto e vírgula, espaço, `@`, `~` ou `:`. Por predefinição, tabulação.
- **Acrescentar** — desativado por predefinição, pelo que cada execução substitui o ficheiro. Ative-o para acumular execuções.
- **Include rules** — desativado por predefinição. Ative-o para exportar as regras do modelo juntamente com os valores.
- **Unicode** — desativado por predefinição. Ative-o quando os dados exportados contêm carateres fora da codificação predefinida.

## Ver também

- [SAP-PCM steps](/pt-pt/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/pt-pt/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/pt-pt/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
