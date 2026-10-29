---
title: Etapa de LLM
description: Execute um prompt em um LLM com acesso delimitado de leitura e/ou gravação aos dados do projeto, em que o modelo grava seus resultados diretamente por meio do servidor MCP.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Descrição

A **Etapa de LLM** envia um prompt a um modelo de linguagem de grande porte. Com uma conexão de LLM da Anthropic, o modelo recebe acesso delimitado às tabelas, dimensões e documentos do projeto que você vincular — **Leitura**, **Gravação** ou ambos por objeto — e grava seus resultados diretamente nas vinculações com Gravação habilitada. Uma vinculação de Gravação é a saída da etapa; não existe um formato de saída separado.

Para um passo a passo completo, consulte o [guia da Etapa de LLM](/pt-br/guides/workflows/llm-step/).

## Configuração

* **Conexão de LLM** *(obrigatório)* — uma conexão do tipo LLM (por exemplo, Anthropic). Seu **Acesso do agente** deve ser **Leitura e gravação** para qualquer vinculação de Gravação. **Completo** também permite gravações até ser removido em 15 de janeiro de 2027, e uma etapa que o usa registra um aviso no log quando é concluída. Em **Leitura e gravação**, uma etapa grava apenas em vinculações com Gravação marcada e não pode executar SQL que grave nem criar tabelas.
* **Modelo** *(opcional)* — assume o modelo padrão da conexão. Qualquer modelo Claude funciona com uma conexão da Anthropic, inclusive modelos mais antigos, como o Claude Sonnet 4.5.
* **Prompt** *(obrigatório)* — aceita referências `{{tables.NAME}}`, `{{dimensions.NAME}}` e `{{documents.NAME}}` a objetos vinculados.
* **Result schema** *(opcional para a Anthropic; obrigatório para outros provedores)* — um **Esquema JSON** (raiz `"type": "object"`) para um resumo estruturado capturado; com a Anthropic, deixe em branco quando o trabalho do modelo for suas gravações via MCP. Provedores que não são a Anthropic não têm acesso ao MCP, portanto um esquema é obrigatório.
* **Bindings** — Tabelas, Dimensões e Documentos que o modelo pode acessar, cada um escolhido com um seletor e com **Leitura** e/ou **Gravação** concedidas. Tabelas de gravação recebem linhas inseridas, dimensões de gravação recebem nós e documentos de gravação recebem arquivos enviados.
* **Limites** — Máximo de tokens de saída (1.024 a 128.000) e Credential TTL (60 a 3.600 segundos).

## Comportamento

* A chamada ao modelo é executada em seu próprio job. Uma credencial delimitada e de curta duração é gerada para a execução e revogada quando ela termina.
* O acesso é controlado por objeto e por caixa de seleção: o modelo lê apenas objetos vinculados com Leitura e grava apenas em objetos vinculados com Gravação — nunca em um objeto que você não vinculou. A gravação exige um objeto de destino existente; a etapa não cria um.
* Cada execução faz uma chamada faturável ao provedor e grava nos objetos que você vinculou.

## O que é verificado ao salvar

* **Result schema** — quando você informa um, ele deve ser um JSON válido, um objeto JSON e declarar `"type": "object"` na raiz. Caso contrário, o salvamento é recusado, por exemplo com *O esquema de resultado deve declarar "type": "object" na raiz.*
* **Bindings e a conexão** — somente uma conexão da Anthropic dá ao modelo acesso a vinculações. Salvar uma etapa com vinculações em uma conexão de outro provedor é recusado, com uma mensagem que nomeia o provedor e pede que você *Remova as vinculações ou escolha uma conexão da Anthropic.* Uma vinculação com **Gravação** marcada precisa de uma conexão cujo **Acesso do agente** permita gravações. Em uma conexão somente de Leitura, o salvamento é recusado com *A conexão de LLM selecionada tem Acesso do agente somente de Leitura, portanto uma vinculação com Gravação marcada não poderia gravar. Defina a conexão como 'Leitura e gravação' ou desmarque Gravação nas vinculações.* Uma etapa salva pela API sem conexão é verificada em relação à conexão de LLM padrão do espaço de trabalho, na qual ela também é executada: a que um administrador marcou como padrão ou, na falta dela, a atualizada mais recentemente. Sem uma conexão padrão marcada por um administrador, editar outra conexão de LLM faz dela a padrão e pode recusar o próximo salvamento da etapa.
