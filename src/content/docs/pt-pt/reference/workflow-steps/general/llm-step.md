---
title: Passo LLM
description: Execute um pedido num LLM com acesso de leitura e/ou escrita limitado aos dados do projeto, em que o modelo escreve os resultados diretamente através do servidor MCP.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Descrição

O **Passo LLM** envia um pedido a um modelo de linguagem de grande dimensão. Com uma ligação LLM da Anthropic, o modelo recebe acesso limitado às tabelas, dimensões e documentos do projeto que associar — **Leitura**, **Escrita** ou ambos por objeto — e escreve os resultados diretamente nas associações com escrita ativada. Uma associação de escrita é a saída do passo; não existe um formato de saída separado.

Para um guia completo, consulte o [guia do Passo LLM](/pt-pt/guides/workflows/llm-step/).

## Configuração

* **Ligação ao LLM** *(obrigatório)* — uma ligação do tipo LLM (por exemplo, Anthropic). O seu **Acesso do agente** tem de ser **Leitura e escrita** para qualquer associação de escrita. **Completo** também permite escritas até ser removido a 15 de janeiro de 2027, e um passo que o utilize regista um aviso quando termina. Com **Leitura e escrita**, um passo escreve apenas nas associações com Escrita selecionada e não pode executar SQL que escreva nem criar tabelas.
* **Modelo** *(opcional)* — por predefinição, o modelo predefinido da ligação. Qualquer modelo Claude funciona com uma ligação Anthropic, incluindo modelos mais antigos como o Claude Sonnet 4.5.
* **Pedido** *(obrigatório)* — suporta referências `{{tables.NAME}}`, `{{dimensions.NAME}}` e `{{documents.NAME}}` aos objetos associados.
* **Result schema** *(opcional para a Anthropic; obrigatório para outros fornecedores)* — um esquema JSON (raiz `"type": "object"`) para um resumo estruturado capturado; com a Anthropic, deixe em branco quando o trabalho do modelo são as suas escritas MCP. Os fornecedores que não são a Anthropic não têm acesso MCP, pelo que é obrigatório um esquema.
* **Bindings** — Tabelas, Dimensões e Documentos a que o modelo pode aceder, cada um escolhido com um seletor e com **Leitura** e/ou **Escrita** concedidas. As tabelas de escrita recebem linhas inseridas, as dimensões de escrita recebem nós e os documentos de escrita recebem ficheiros carregados.
* **Limites** — Máximo de tokens de saída (1024 a 128 000) e TTL da credencial (60 a 3600 segundos).

## Comportamento

* A chamada ao modelo é executada na sua própria tarefa. É criada uma credencial limitada e de curta duração para a execução, que é revogada quando esta termina.
* O acesso é controlado por objeto e por caixa de seleção: o modelo lê apenas objetos associados com Leitura e escreve apenas nos associados com Escrita — nunca num objeto que não tenha associado. A escrita requer um objeto de destino existente; o passo não cria nenhum.
* Cada execução faz uma chamada faturável ao fornecedor e escreve nos objetos que associou.

## O que é verificado ao guardar

* **Result schema** — quando fornece um, tem de ser JSON válido, um objeto JSON e declarar `"type": "object"` na raiz. Caso contrário, a gravação é recusada, por exemplo com *The result schema must declare "type": "object" at its root.*
* **Associações e a ligação** — só uma ligação Anthropic dá ao modelo acesso a associações. Guardar um passo com associações numa ligação de outro fornecedor é recusado, com uma mensagem que nomeia o fornecedor e pede *Remove the bindings or choose an Anthropic connection.* Uma associação com **Escrita** selecionada precisa de uma ligação cujo **Acesso do agente** permita escritas. Numa ligação só de leitura, a gravação é recusada com *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* Um passo guardado através da API sem ligação é verificado em relação à ligação LLM predefinida da área de trabalho, na qual também é executado: a que um administrador marcou como predefinida ou, na falta desta, a atualizada mais recentemente. Sem uma predefinição marcada por um administrador, editar outra ligação LLM torna essa a predefinida e pode recusar a gravação seguinte do passo.
