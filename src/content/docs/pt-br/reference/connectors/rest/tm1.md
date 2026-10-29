---
title: Conector TM1
description: Conecte o PlaidCloud a um servidor IBM TM1 / Planning Analytics pela API REST, com autenticação Basic nativa ou por namespace CAM, diretamente da nuvem ou por meio de um agente PlaidLink local para um servidor que a nuvem não alcança.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Conecte o PlaidCloud a um servidor IBM **TM1 / Planning Analytics** por meio da API REST OData v4 publicada, sem ponte JVM nem driver PAOlap. Leia dados de cubo com [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/) ou uma hierarquia de dimensão do TM1 com [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/), ambos diretamente da nuvem. Para um servidor TM1 acessível apenas de dentro da sua rede, [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) envia a mesma leitura por um agente PlaidLink instalado.

O tipo de conexão aparece no seletor de conexões como **IBM Planning Analytics (TM1)**.

## Como a Autenticação Funciona

Há dois modos de autenticação, que correspondem aos esquemas de login REST do próprio TM1:

- **Native**: autenticação HTTP Basic com um nome de usuário e uma senha do TM1.
- **CAM**: logon único do IBM Cognos Access Manager, restrito a um namespace. A solicitação inclui um cabeçalho `Authorization: CAMNamespace` montado com o nome de usuário, a senha e o namespace em conjunto, diferente do Basic simples.

Ainda não há login por token de portador do PlanningAnalytics-as-a-Service (PAaaS); há somente os dois esquemas de login REST acima.

## Configuração

| Campo | Obrigatório | Descrição |
|---|---|---|
| Nome | Sim | Nome de exibição desta conexão. |
| Host | Sim | O host da API REST do TM1, por exemplo `https://tm1-prod.example.com:8010` ou uma URL do PAaaS. |
| Banco de dados padrão | Não | Preenchimento prévio para o campo Banco de dados de uma etapa TM1: Consultar cubo. Cada etapa pode substituí-lo. |
| Modo de autenticação | Sim | `Native` (usuário e senha do TM1) ou `CAM` (SSO do Cognos Access Manager). O padrão é Native. |
| Nome de usuário | Sim | A conta do TM1 usada na autenticação. |
| Senha | Sim | Armazenada com criptografia. |
| Namespace do CAM | Somente com CAM | O namespace do Cognos Access Manager em que a autenticação ocorre. Não é usado no modo Native. |
| Verificar certificado SSL | Não | Ativado por padrão. Desative somente para um certificado autoassinado conhecido em um servidor de teste. |
| Tempo limite (segundos) | Não | O padrão é 30. |

## Testando a Conexão

**Testar conexão** consulta o singleton `Configuration` do servidor (`GET {host}/api/v1/Configuration`), a chamada autenticada mais barata que o TM1 oferece e que não exige contexto de banco de dados nem de cubo. Um teste bem-sucedido informa o **`ProductVersion`** do servidor, confirmando que o host está acessível e que as credenciais autenticam.

## Somente Leitura

Este conector é somente leitura. Ele lê dados de cubo e hierarquias de dimensão do TM1; não grava, não lança nem executa processos TI de volta no TM1.

## O Que Você Pode Fazer com a Conexão

- **Ler dados de cubo por visão salva ou MDX.** A etapa [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/) executa uma visão de cubo nomeada ou uma consulta MDX bruta, aplica um recorte opcional de ponto de vista e grava o resultado em uma tabela.
- **Carregar uma hierarquia do TM1 como dimensão do PlaidCloud.** A etapa [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) lê os elementos, as relações entre pai e filho e os atributos de uma dimensão, e cria uma dimensão do PlaidCloud a partir deles.
- **Recortar por período para uma extração incremental.** O TM1 não tem controle de alterações integrado; por isso, um fluxo de trabalho que precisa apenas de dados novos restringe a consulta por período ou versão. Consulte a referência da etapa para ver o padrão.
- **Descobrir cubos, visões e dimensões em tempo real**, diretamente da nuvem. Os seletores Cubo, Visão e Dimensão do formulário da etapa consultam o servidor conectado diretamente, para que você escolha nomes reais em vez de digitá-los às cegas.
- **Ler um servidor TM1 que a nuvem não alcança, por meio de um agente local.** Consulte [Lendo o TM1 Atrás de um Firewall](#lendo-o-tm1-atrás-de-um-firewall) abaixo.

## Lendo o TM1 Atrás de um Firewall

Um servidor TM1 acessível apenas de dentro da sua rede, sem ponto de extremidade público, sem IP na lista de permissões e sem VPN para o PlaidCloud, é alcançado por meio de um **agente PlaidLink** instalado, em vez de diretamente da nuvem. A etapa de fluxo de trabalho [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) executa a mesma consulta de visão, MDX e ponto de vista que TM1: Consultar cubo, mas a envia ao agente, que acessa o TM1 na sua rede e devolve o resultado.

Este caminho exige:

- **Um agente PlaidLink instalado** em uma máquina com acesso de rede ao servidor TM1. Consulte [Instalar o PlaidLink](/pt-br/reference/cli/plaidlink/install/).
- **Uma versão desse agente que inclua o manipulador do TM1.** O PlaidCloud verifica os recursos anunciados por um agente antes de enviar uma consulta a ele; assim, uma versão mais antiga do agente não atende solicitações do TM1 até ser recompilada e reinstalada, pois o PlaidLink não se atualiza automaticamente. Consulte [Atualizar o PlaidLink](/pt-br/reference/cli/plaidlink/upgrade/).
- **Esta conexão TM1 compartilhada com esse agente**, além do acesso de membros ou grupos que ela já tem, a partir da lista `Actions > Agents` da conexão. Consulte [Modelo de segurança](/pt-br/guides/connections/create-connection/#modelo-de-segurança).

TM1: Consultar cubo (agente) não tem descoberta em tempo real, pois um agente só fica acessível durante uma execução, e não enquanto o formulário da etapa está aberto. Por isso, cubo, visão e MDX são digitados manualmente e validados quando a etapa é executada. TM1: Ler dimensão funciona somente diretamente da nuvem e ainda não tem caminho local.

## Limitações Conhecidas

| Limitação | O que significa |
|---|---|
| Somente leitura | Sem gravação de volta e sem execução de processos TI. |
| O alcance local é somente para consultas | O caminho do agente PlaidLink local cobre leituras de cubo (TM1: Consultar cubo (agente)). TM1: Ler dimensão ainda não tem caminho local e exige um caminho de rede que o PlaidCloud possa alcançar diretamente. |
| A leitura de dimensão admite uma única hierarquia e um único pai | Uma hierarquia do TM1 com um elemento sob mais de um pai não pode ser carregada como dimensão do PlaidCloud, e a magnitude do peso de uma consolidação (0,5; 2,0) não é representável, apenas o sinal. Consulte [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#o-que-esta-etapa-não-consegue-representar). |
| Sem autenticação por token de portador do PAaaS | Há suporte apenas para a autenticação Native (Basic) e CAM. |

## Relacionados

- [Conectar ao TM1 (guia)](/pt-br/guides/connections/tm1/): crie a conexão e monte uma consulta.
- [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/): leituras de cubo diretamente da nuvem.
- [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/): leituras de cubo por meio de um agente local.
- [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/): carregue uma hierarquia do TM1 como dimensão do PlaidCloud.
- [Criar e Gerenciar uma Conexão](/pt-br/guides/connections/create-connection/)
