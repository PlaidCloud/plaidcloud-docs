---
title: "TM1: Consultar cubo (agente)"
description: "Leia um corte de cubo de um servidor IBM TM1 / Planning Analytics local que a nuvem não consegue alcançar diretamente — a mesma consulta por vista/MDX/ponto de vista de TM1: Consultar cubo, enviada através de um agente PlaidLink instalado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Descrição

O equivalente local de [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/): a mesma leitura — uma **vista** guardada ou uma consulta **MDX** a um cubo do TM1, com um corte opcional por ponto de vista (POV), colocada numa tabela de projeto — enviada através de um [agente PlaidLink](/pt-pt/reference/cli/plaidlink/) instalado na sua rede em vez de chamada diretamente na nuvem. Utilize este passo, em vez de TM1: Consultar cubo, quando o servidor TM1 só é acessível a partir da sua própria rede.

Este passo aparece no menu de passos em **IBM TM1 / Planning Analytics**.

## O que difere de TM1: Consultar cubo

| | TM1: Consultar cubo | TM1: Consultar cubo (agente) |
|---|---|---|
| Transporte | Diretamente na nuvem através de REST | Enviado para um agente PlaidLink na sua rede |
| Campos de configuração | — | Idênticos, mais um **Agente** obrigatório |
| Descoberta de cubos/vistas | Em direto, a partir da base de dados ligada | Não disponível — escreva os nomes manualmente |
| Pré-visualização antes de guardar | Sim | Não disponível |

Tudo o resto — a ligação, a base de dados, a escolha entre vista/MDX, o corte por ponto de vista, Suprimir células com zero/vazias, Limite de linhas e o padrão de extração incremental por período — funciona exatamente como descrito na página [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/). Apenas as diferenças abaixo são específicas deste passo.

## Configuração

### Origem e destino

| Campo | Obrigatório | Notas |
|---|---|---|
| Agente | Sim | O agente PlaidLink para o qual enviar esta leitura. A sua compilação tem de incluir o manipulador de TM1 (consulte [Requisitos](#requisitos) abaixo). |
| Ligação TM1 | Sim | A [ligação TM1](/pt-pt/guides/connections/tm1/) através da qual ler. O seletor de ligações não é filtrado pelo agente selecionado — partilhe a ligação com o agente em separado (ver abaixo). |
| Ambiente | Sim | O ambiente da ligação. |
| Base de dados | Sim | A base de dados (instância) do TM1 a consultar. |
| Cubo | Sim | O cubo do TM1 a consultar. Escrito manualmente — neste passo não há descoberta em direto. |
| Tabela de destino | Sim | A tabela de projeto onde o conjunto de células devolvido é colocado. |

### Corte e opções

Os mesmos campos de [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/#corte) — Modo de origem (Por vista / Por MDX), Vista, MDX, Ponto de vista, Suprimir células com zero/vazias e Limite de linhas — todos de introdução escrita e não descobertos, e todos validados quando o passo é executado e não numa pré-visualização.

## Sem descoberta intermediada por agente

Os seletores de Cubo, Vista e Dimensão de TM1: Consultar cubo consultam o servidor ligado em direto enquanto edita o passo. Essa descoberta em direto não existe neste passo: um agente só é acessível durante uma execução, não enquanto um formulário está aberto no seu navegador. O cubo, a vista e o MDX são de introdução escrita, e um nome não reconhecido faz a execução falhar com um erro claro em vez de falhar silenciosamente. Pela mesma razão, não existe botão de **Pré-visualização** — uma pré-visualização teria de chegar ao TM1, o que só o agente consegue fazer.

## Requisitos

Ler um servidor TM1 local requer:

- **Um agente PlaidLink instalado** numa máquina com acesso de rede ao servidor TM1. Consulte [Instalar o PlaidLink](/pt-pt/reference/cli/plaidlink/install/).
- **Uma compilação desse agente que inclua o manipulador de TM1.** O PlaidCloud verifica as capacidades anunciadas pelo agente antes de enviar; um agente cuja compilação seja anterior a esta capacidade não pode atender o pedido. **O PlaidLink não se atualiza automaticamente** — um agente existente tem de ser recompilado/reinstalado manualmente para obter o suporte a TM1. Consulte [Atualizar o PlaidLink](/pt-pt/reference/cli/plaidlink/upgrade/).
- **A ligação TM1 partilhada com esse agente**, além de qualquer acesso de membro/grupo que já tenha — conceda-o a partir da lista `Actions > Agents` da ligação. Consulte [Modelo de segurança](/pt-pt/guides/connections/create-connection/#modelo-de-segurança).

## Relacionados

- [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — o equivalente direto na nuvem que este passo espelha.
- [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — carrega uma hierarquia do TM1 numa dimensão do PlaidCloud, diretamente na nuvem.
- [Ligar ao TM1 (guia)](/pt-pt/guides/connections/tm1/) — criar a ligação.
- [Conector TM1](/pt-pt/reference/connectors/rest/tm1/) — referência dos campos da ligação, incluindo o caminho do agente local.
- [PlaidLink](/pt-pt/reference/cli/plaidlink/) — instalar e atualizar agentes.
- [Passos do IBM TM1 / Planning Analytics](/pt-pt/reference/workflow-steps/ibm-planning-analytics/)
