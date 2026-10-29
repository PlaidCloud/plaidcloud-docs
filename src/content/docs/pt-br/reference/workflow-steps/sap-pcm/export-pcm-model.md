---
title: Calculate and Export PCM Model
description: Execute o cálculo de um modelo PCM e exporte o resultado para um banco de dados ou um arquivo delimitado, por meio de um agente PlaidLink.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Descrição

Calcula um modelo do SAP PCM e exporta o resultado em uma única etapa, por meio de um [agente PlaidLink](/pt-br/reference/workflow-steps/agent/) com acesso à instalação do PCM. Enquanto [Calculate PCM Model](/pt-br/reference/workflow-steps/sap-pcm/calculate-pcm-model/) apenas executa o cálculo, esta etapa também move a saída.

## Configuração

### Agente a usar

O agente PlaidLink que alcança a instalação do PCM.

### Informações do modelo

- **Nome do modelo** — o modelo PCM a calcular.
- **Export specification path** — a especificação de exportação do PCM que descreve o que exportar.

### Destino da saída de exportação

Escolha um destino de banco de dados, um destino de arquivo ou ambos.

**Para um banco de dados** — ativado por padrão; a exportação grava por meio do destino de banco de dados configurado na especificação.

**Para um arquivo** — desativado por padrão. Quando ativado:

- **Caminho do arquivo** — onde o agente grava o arquivo.
- **Alias** — o alias registrado na exportação. O padrão é `DEFAULT ALIAS`.
- **Precision** — casas decimais dos valores exportados. O padrão é 0.
- **Delimitador** — vírgula, tabulação, barra vertical, ponto e vírgula, espaço, `@`, `~` ou `:`. O padrão é tabulação.
- **Anexar** — desativado por padrão, de modo que cada execução substitui o arquivo. Ative para acumular as execuções.
- **Include rules** — desativado por padrão. Ative para exportar as regras do modelo junto com os valores.
- **Unicode** — desativado por padrão. Ative quando os dados exportados contiverem caracteres fora da codificação padrão.

## Relacionados

- [Etapas do SAP-PCM](/pt-br/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/pt-br/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/pt-br/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
