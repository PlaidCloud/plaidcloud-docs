---
title: "TM1: Consultar cubo (agente)"
description: "Leia um recorte de cubo de um servidor IBM TM1 / Planning Analytics local que a nuvem não consegue alcançar diretamente — a mesma consulta por visão/MDX/ponto de vista de TM1: Consultar cubo, despachada por um agente PlaidLink instalado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Descrição

O equivalente local de [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/): a mesma leitura — uma **visão** salva ou uma consulta **MDX** em um cubo do TM1, com um recorte opcional por ponto de vista (POV), gravada como uma tabela de projeto — despachada por um [agente PlaidLink](/pt-br/reference/cli/plaidlink/) instalado na sua rede, em vez de chamada diretamente da nuvem. Use esta etapa, em vez de TM1: Consultar cubo, quando o servidor TM1 só é acessível de dentro da sua própria rede.

Esta etapa aparece no menu de etapas em **IBM TM1 / Planning Analytics**.

## Diferenças em relação a TM1: Consultar cubo

| | TM1: Consultar cubo | TM1: Consultar cubo (agente) |
|---|---|---|
| Transporte | Direto da nuvem por REST | Despachado para um agente PlaidLink na sua rede |
| Campos de configuração | — | Idênticos, mais um **Agente** obrigatório |
| Descoberta de cubo / visão | Ao vivo, a partir do banco de dados conectado | Não disponível — digite os nomes manualmente |
| Pré-visualização antes de salvar | Sim | Não disponível |

Todo o resto — a conexão, o banco de dados, a escolha de visão/MDX, o recorte por ponto de vista, Suprimir células zeradas/vazias, Limite de linhas e o padrão de extração incremental por período — funciona exatamente como descrito na página [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/). Somente as diferenças abaixo são específicas desta etapa.

## Configuração

### Origem e destino

| Campo | Obrigatório | Observações |
|---|---|---|
| Agente | Sim | O agente PlaidLink para o qual despachar esta leitura. Seu build deve incluir o handler do TM1 (consulte [Requisitos](#requisitos) abaixo). |
| Conexão TM1 | Sim | A [conexão TM1](/pt-br/guides/connections/tm1/) pela qual ler. O seletor de conexões não é filtrado pelo agente selecionado — compartilhe a conexão com o agente separadamente (veja abaixo). |
| Ambiente | Sim | O ambiente da conexão. |
| Banco de dados | Sim | O banco de dados (instância) do TM1 a consultar. |
| Cubo | Sim | O cubo do TM1 a consultar. Digitado manualmente — não há descoberta ao vivo nesta etapa. |
| Tabela de destino | Sim | A tabela de projeto em que o cellset retornado é gravado. |

### Recorte e opções

Os mesmos campos de [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/#recorte) — Modo de origem (Por visão / Por MDX), Visão, MDX, Ponto de vista, Suprimir células zeradas/vazias e Limite de linhas — todos com entrada digitada em vez de descobertos e todos validados quando a etapa é executada, e não em uma pré-visualização.

## Sem descoberta mediada por agente

Os seletores de Cubo, Visão e Dimensão de TM1: Consultar cubo consultam o servidor conectado ao vivo enquanto você edita a etapa. Essa descoberta ao vivo não existe nesta etapa: um agente só é acessível durante uma execução, e não enquanto um formulário está aberto no seu navegador. Cubo, visão e MDX são de entrada digitada, e um nome não reconhecido faz a execução falhar com um erro claro, em vez de falhar silenciosamente. Pelo mesmo motivo, não há botão de **Pré-visualização** — uma pré-visualização precisaria alcançar o TM1, o que só o agente pode fazer.

## Requisitos

Ler um servidor TM1 local exige:

- **Um agente PlaidLink instalado** em uma máquina com acesso de rede ao servidor TM1. Consulte [Instalar o PlaidLink](/pt-br/reference/cli/plaidlink/install/).
- **Um build desse agente que inclua o handler do TM1.** O PlaidCloud verifica as capacidades anunciadas pelo agente antes de despachar; um agente cujo build é anterior a esta capacidade não pode atender à solicitação. **O PlaidLink não se atualiza automaticamente** — um agente existente deve ser recompilado/reinstalado manualmente para obter o suporte ao TM1. Consulte [Atualizar o PlaidLink](/pt-br/reference/cli/plaidlink/upgrade/).
- **A conexão TM1 compartilhada com esse agente**, além de qualquer acesso de membro/grupo que ela já tenha — conceda-o na lista `Actions > Agents` da conexão. Consulte [Modelo de segurança](/pt-br/guides/connections/create-connection/#modelo-de-segurança).

## Relacionados

- [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — o equivalente direto da nuvem que esta etapa espelha.
- [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — carrega uma hierarquia do TM1 em uma dimensão do PlaidCloud, direto da nuvem.
- [Conectar ao TM1 (guia)](/pt-br/guides/connections/tm1/) — crie a conexão.
- [Conector TM1](/pt-br/reference/connectors/rest/tm1/) — referência dos campos da conexão, incluindo o caminho do agente local.
- [PlaidLink](/pt-br/reference/cli/plaidlink/) — instalação e atualização de agentes.
- [Etapas do IBM TM1 / Planning Analytics](/pt-br/reference/workflow-steps/ibm-planning-analytics/)
