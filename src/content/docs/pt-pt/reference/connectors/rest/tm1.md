---
title: Conector TM1
description: Ligue o PlaidCloud a um servidor IBM TM1 / Planning Analytics através da sua API REST — autenticação Basic nativa ou autenticação por espaço de nomes CAM — diretamente a partir da cloud ou através de um agente PlaidLink local para um servidor que a cloud não consegue alcançar diretamente.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Ligue o PlaidCloud a um servidor IBM **TM1 / Planning Analytics** através da sua API REST OData v4 publicada — sem ponte JVM, sem controlador PAOlap. Leia dados de cubos com [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) ou uma hierarquia de dimensão do TM1 com [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/), ambos diretamente a partir da cloud; para um servidor TM1 acessível apenas a partir da sua própria rede, [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) envia a mesma leitura através de um agente PlaidLink instalado.

O tipo de ligação aparece no seletor de ligações como **IBM Planning Analytics (TM1)**.

## Como Funciona a Autenticação

Dois modos de autenticação, correspondentes aos esquemas de início de sessão REST do próprio TM1:

- **Native** — autenticação HTTP Basic com um nome de utilizador e palavra-passe do TM1.
- **CAM** — início de sessão único (SSO) do IBM Cognos Access Manager, com âmbito num espaço de nomes. O pedido transporta um cabeçalho `Authorization: CAMNamespace` construído a partir do nome de utilizador, da palavra-passe e do espaço de nomes em conjunto, distinto do Basic simples.

Ainda não existe início de sessão com token de portador do PlanningAnalytics-as-a-Service (PAaaS) — apenas os dois esquemas de início de sessão REST acima.

## Configuração

| Campo | Obrigatório | Descrição |
|---|---|---|
| Nome | Sim | Nome de apresentação desta ligação. |
| Anfitrião | Sim | O anfitrião da API REST do TM1, por exemplo `https://tm1-prod.example.com:8010` ou um URL PAaaS. |
| Base de dados predefinida | Não | Um pré-preenchimento de conveniência para o campo Base de dados de um passo TM1: Consultar cubo. Cada passo pode substituí-lo. |
| Modo de autenticação | Sim | `Native` (utilizador/palavra-passe do TM1) ou `CAM` (SSO do Cognos Access Manager). Por predefinição, Native. |
| Nome de utilizador | Sim | A conta TM1 com a qual autenticar. |
| Palavra-passe | Sim | Guardada de forma encriptada. |
| Espaço de nomes CAM | Apenas com CAM | O espaço de nomes do Cognos Access Manager contra o qual autenticar. Não utilizado no modo Native. |
| Verificar certificado SSL | Não | Ativado por predefinição. Desative apenas para um certificado autoassinado conhecido num servidor de teste. |
| Tempo limite (segundos) | Não | Por predefinição, 30. |

## Testar a Ligação

**Testar ligação** sonda o singleton `Configuration` do servidor (`GET {host}/api/v1/Configuration`) — a chamada autenticada mais económica que o TM1 expõe, e que não precisa de contexto de base de dados nem de cubo. Um teste bem-sucedido indica a **`ProductVersion`** do servidor, confirmando que o anfitrião é alcançável e que as credenciais autenticam.

## Só de Leitura

Este conector é só de leitura. Lê dados de cubos e hierarquias de dimensões a partir do TM1; não escreve, não lança nem executa processos TI de volta no TM1.

## O que Pode Fazer com a Ligação

- **Ler dados de cubos por vista guardada ou MDX.** O passo [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) executa uma vista de cubo com nome ou uma consulta MDX em bruto, aplica uma fatia de ponto de vista opcional e coloca o resultado numa tabela.
- **Carregar uma hierarquia do TM1 como dimensão do PlaidCloud.** O passo [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) lê os elementos, as arestas pai/filho e os atributos de uma dimensão e constrói a partir deles uma dimensão do PlaidCloud.
- **Dividir por período para uma extração incremental.** O TM1 não tem controlo de alterações incorporado, pelo que um fluxo de trabalho que só precisa de dados novos restringe a consulta por período ou versão — consulte a referência do passo para ver o padrão.
- **Descobrir cubos, vistas e dimensões em direto**, diretamente a partir da cloud. Os seletores de Cubo, Vista e Dimensão do formulário do passo consultam diretamente o servidor ligado, pelo que escolhe nomes reais em vez de os escrever às cegas.
- **Ler um servidor TM1 que a cloud não consegue alcançar, através de um agente local.** Consulte [Ler o TM1 atrás de uma firewall](#ler-o-tm1-atrás-de-uma-firewall) mais abaixo.

## Ler o TM1 atrás de uma Firewall

Um servidor TM1 acessível apenas a partir da sua própria rede — sem ponto de acesso público, sem IP na lista de permissões, sem VPN para o PlaidCloud — é alcançado através de um **agente PlaidLink** instalado, em vez de diretamente a partir da cloud. O passo de fluxo de trabalho [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) executa a mesma consulta de vista/MDX/ponto de vista que TM1: Consultar cubo, mas envia-a para o agente, que acede ao TM1 na sua rede e devolve o resultado.

Este caminho requer:

- **Um agente PlaidLink instalado** numa máquina com acesso de rede ao servidor TM1. Consulte [Instalar o PlaidLink](/pt-pt/reference/cli/plaidlink/install/).
- **Uma compilação desse agente que inclua o gestor de TM1.** O PlaidCloud verifica as capacidades anunciadas por um agente antes de lhe enviar uma consulta, pelo que uma compilação de agente mais antiga não consegue servir pedidos TM1 até ser recompilada e reinstalada — o PlaidLink não se atualiza automaticamente. Consulte [Atualizar o PlaidLink](/pt-pt/reference/cli/plaidlink/upgrade/).
- **Esta ligação TM1 partilhada com esse agente**, além de qualquer acesso de membro/grupo que já tenha, a partir da lista `Actions > Agents` da ligação. Consulte [Modelo de segurança](/pt-pt/guides/connections/create-connection/#modelo-de-segurança).

TM1: Consultar cubo (agente) não tem descoberta em direto — um agente só é acessível durante uma execução, não enquanto o formulário do passo está aberto —, pelo que o cubo, a vista e o MDX são escritos manualmente e validados quando o passo é executado. TM1: Ler dimensão funciona apenas diretamente a partir da cloud; ainda não tem caminho local.

## Limitações Conhecidas

| Limitação | O que significa |
|---|---|
| Só de leitura | Sem escrita de retorno, sem execução de processos TI. |
| O alcance local limita-se a consultas | O caminho do agente PlaidLink local abrange leituras de cubos (TM1: Consultar cubo (agente)). TM1: Ler dimensão ainda não tem caminho local — precisa de um caminho de rede que o PlaidCloud consiga alcançar diretamente. |
| A leitura de dimensões é de hierarquia única e pai único | Uma hierarquia do TM1 com um elemento sob mais do que um pai não pode ser carregada como dimensão do PlaidCloud, e a magnitude do peso de uma consolidação (0.5, 2.0) não é representável — apenas o seu sinal. Consulte [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#o-que-este-passo-não-consegue-representar). |
| Sem autenticação por portador PAaaS | Apenas são suportadas a autenticação Native (Basic) e CAM. |

## Relacionado

- [Ligar ao TM1 (guia)](/pt-pt/guides/connections/tm1/) — criar a ligação e construir uma consulta.
- [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — leituras de cubos, diretamente a partir da cloud.
- [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — leituras de cubos através de um agente local.
- [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — carregar uma hierarquia do TM1 como dimensão do PlaidCloud.
- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/)
