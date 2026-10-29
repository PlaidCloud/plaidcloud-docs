---
title: Etapas do Oracle EPM (HFM / FCCS)
description: "Etapas de fluxo de trabalho que obtêm por conta própria uma fatia de dados ad hoc do Oracle FCCS por meio da sua conexão HFM/FCCS: monte um ponto de vista, execute-o e grave o resultado como uma tabela."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

Etapas de fluxo de trabalho que leem do Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) por meio da sua [conexão HFM/FCCS](/pt-br/guides/connections/hfm-fccs/). Um usuário de finanças monta um ponto de vista no formulário da etapa, executa-o, e a grade retornada chega automaticamente como uma tabela de projeto, sem chamado para a equipe do HFM e sem exigir conhecimento de consolidação.

## Etapas

- [HFM/FCCS: Ler dados (ad hoc)](/pt-br/reference/workflow-steps/oracle-epm/hfm-fccs-read/): obtenha por conta própria uma fatia de dados com um seletor de ponto de vista; mantém em cache as extrações repetidas, está pronta para segurança em nível de linha e pode ser promovida a uma carga recorrente agendada.

## Relacionados

- [Extrair do HFM / FCCS (guia)](/pt-br/guides/connections/hfm-fccs/)
- [Conector HFM / FCCS](/pt-br/reference/connectors/rest/hfm-fccs/)
