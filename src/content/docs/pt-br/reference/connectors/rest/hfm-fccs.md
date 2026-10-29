---
title: Conector HFM / FCCS
description: Configure uma conexão com o Oracle FCCS (Financial Consolidation and Close, EPM Cloud) no PlaidCloud para obter, por conta própria, um recorte ad hoc de dados com um seletor de ponto de vista, com cache opcional e uma carga recorrente agendada.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Conecte o PlaidCloud ao **FCCS** da Oracle (Financial Consolidation and Close, parte do Oracle EPM Cloud) para que um usuário de finanças obtenha um recorte de dados por conta própria, sem abrir um chamado para a equipe do HFM. A etapa [HFM/FCCS: Ler dados (ad hoc)](/pt-br/reference/workflow-steps/oracle-epm/hfm-fccs-read/) parece uma consulta ao vivo, mas, por baixo dos panos, é uma sequência assíncrona de solicitar, consultar e buscar na API de jobs de exportação de dados do FCCS.

O tipo de conexão aparece no seletor de conexões como **REST - HFM/FCCS**.

:::note[Delimite a dimensão de entidade]
Mantenha todo ponto de vista delimitado: uma extração sem escopo pode bloquear o aplicativo FCCS por muito tempo enquanto o job de exportação é executado.
:::

## Documentação da API

O conector usa a [API REST](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) do Oracle EPM Cloud: os endpoints de metadados do aplicativo (para descobrir dimensões e membros) e os endpoints de jobs de exportação de dados (para solicitar, consultar e buscar uma grade).

## Como funciona a autenticação

A conexão usa **autenticação HTTP Basic com uma conta de serviço** em um pod clássico do EPM Cloud; não há fluxo OAuth nem de token (pods OCI / Gen 2 com token de portador estão fora do escopo). Quando um **Domínio de identidade** está definido, o PlaidCloud compõe o login como `identitydomain.username` (o domínio, um ponto e depois o nome de usuário); se você deixar o Domínio de identidade em branco, ou se o seu nome de usuário já contiver um ponto, o nome de usuário é enviado como está. Aponte a conexão para uma conta de serviço de integração dedicada, com acesso de leitura aos aplicativos e aos recortes de ponto de vista que seus usuários vão extrair por conta própria.

## Configuração

| Campo | Obrigatório | Descrição |
|---|---|---|
| Nome | Sim | Nome de exibição desta conexão. |
| URL do EPM Cloud | Sim | A URL do pod/serviço do seu EPM Cloud, por exemplo `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Domínio de identidade | Não | O domínio de identidade do seu EPM Cloud. Quando definido, o PlaidCloud o adiciona como prefixo ao nome de usuário, no formato `identitydomain.username`, no login. |
| Nome de usuário | Sim | O nome de usuário da conta de serviço de integração. |
| Senha | Sim | A senha da conta de serviço. Armazenada de forma criptografada. |
| Aplicativo padrão | Não | Um aplicativo FCCS padrão para preencher previamente o seletor de ponto de vista da etapa. Cada etapa pode substituí-lo. |

## O que você pode fazer com a conexão

- **Obter um recorte ad hoc por conta própria.** Monte um ponto de vista (POV), com Aplicativo mais as dimensões do FCCS, no formulário da etapa, clique em Executar, e uma tabela de resultado é criada automaticamente. Consulte [HFM/FCCS: Ler dados (ad hoc)](/pt-br/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Dispensar o chamado.** O recorte é executado com a conta de serviço da conexão, então um usuário de finanças extrai os dados sozinho, sem esperar por um administrador do HFM.
- **Armazenar em cache extrações repetidas.** O mesmo POV e a mesma data de referência, solicitados novamente, retornam instantaneamente a cópia já carregada, em vez de consultar o FCCS outra vez.
- **Controlar quem vê quais entidades.** A tabela carregada está **pronta para segurança em nível de linha**: um administrador pode declarar Acesso a linhas na coluna `Entity` para que os usuários só vejam as entidades às quais têm direito. Isso é governado sob controle do administrador, não é automático; consulte a referência da etapa.
- **Agendar uma carga recorrente.** Ative **Vincular destino** para promover um recorte ad hoc a uma tabela persistente que cresce de forma aditiva e faz mesclagem em vez de sobrescrever, de modo que a mesma etapa, colocada em um fluxo de trabalho agendado, se torna uma carga recorrente noturna.

## Descoberta de metadados

Em pods FCCS compatíveis, o formulário da etapa descobre ao vivo a lista de membros de cada dimensão a partir dos metadados do aplicativo, assim que você escolhe uma conexão e um aplicativo, de modo que o seletor de POV oferece membros reais para escolha (ele refaz a descoberta sempre que um dos dois muda). Em pods mais antigos que não expõem o endpoint de metadados, a descoberta não retorna nada e o seletor recorre à entrada manual: você digita os nomes dos membros à mão, e um ponto de vista salvo sempre é recuperado corretamente. A extração funciona da mesma forma nos dois casos.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Somente leitura | O conector extrai dados do FCCS. Ele não grava dados de consolidação, não executa consolidações nem lança de volta. |
| Delimite a dimensão de entidade | Uma extração sem escopo (sem seleção de `Entity`) pode bloquear o aplicativo FCCS por muito tempo enquanto o job de exportação é executado. Mantenha a seleção de entidades delimitada. |
| Membros manuais em pods mais antigos | Quando um pod não expõe o endpoint de metadados, as listas de membros não são preenchidas automaticamente; digite os nomes dos membros à mão. |
| A segurança em nível de linha é governada pelo administrador, não é automática | A tabela carregada pode ser governada com Acesso a linhas, mas um administrador precisa publicar, declarar a coluna `Entity`, aprovar a primeira gravação governada e reconciliar. Até que faça isso, a tabela não é filtrada. |

## Relacionados

- [Extrair do HFM / FCCS (guia)](/pt-br/guides/connections/hfm-fccs/) — crie a conexão, monte um POV, execute-o, use cache, governe e agende.
- [HFM/FCCS: Ler dados (ad hoc)](/pt-br/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — a referência de campos da etapa.
- [Gerenciar grupos de segurança e atribuições](/pt-br/administration/access/managing-security-groups-and-assignments/) — como o Acesso a linhas governa a tabela carregada.
- [Criar e gerenciar uma conexão](/pt-br/guides/connections/create-connection/)
