---
title: ODBC
description: Configure uma conexão ODBC no PlaidCloud por meio de um DSN do sistema ou de um driver ODBC na máquina de um agente PlaidLink, no Windows ou no Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC (Open Database Connectivity)** acessa um banco de dados por meio da configuração ODBC da máquina em que um [agente PlaidLink](/pt-br/reference/cli/plaidlink/) é executado. Use-o para um banco de dados que não tenha um conector dedicado do PlaidCloud, a partir de etapas de agente como [Agent Remote Export of SQL Result](/pt-br/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Para criar uma, escolha **ODBC** como o tipo de conexão.

:::note
Uma conexão ODBC exige o PlaidLink 1.2.31 ou posterior no agente. Consulte [Atualização](/pt-br/reference/cli/plaidlink/upgrade/).
:::

Uma conexão ODBC funciona de duas maneiras:

- **Por um DSN.** Deixe **Driver ODBC** em branco e informe uma origem de dados (DSN) configurada na máquina do agente. O DSN guarda o driver, o servidor, o banco de dados e quaisquer outras configurações do driver, e os **Atributos de conexão** podem substituí-los. Isso funciona com qualquer driver ODBC.
- **Por um driver.** Escolha ou digite um **Driver ODBC** instalado na máquina do agente e informe o servidor e o banco de dados. O PlaidCloud passa ao driver uma configuração `Server` e uma `Database`, seguidas de quaisquer **Atributos de conexão**. Isso funciona com os drivers do SQL Server da Microsoft. Para qualquer outro driver, inclusive os outros que a lista sugere, use um DSN.

## Documentação do Fornecedor
Cada driver ODBC de banco de dados tem suas próprias configurações. Consulte a documentação do fornecedor do driver para saber as palavras-chave que ele aceita, tanto ao criar um DSN quanto ao escrever atributos de conexão.

## Criar o DSN na Máquina do Agente

Configure o DSN na máquina em que o agente é executado, como um DSN do sistema, para que o agente o encontre independentemente da conta com a qual é executado.

### No Windows

1. Abra **ODBC Data Sources (64-bit)**.
2. Na guia **System DSN**, adicione uma origem de dados que use o driver ODBC do banco de dados e informe o servidor, o banco de dados e quaisquer outras configurações que o driver solicitar.
3. Anote o **Nome da origem de dados**. Você o informa na conexão.

:::caution
O DSN deve ser um **System DSN** de 64 bits. No Windows, o agente é executado como um serviço, que não enxerga um User DSN nem um DSN criado no administrador ODBC de 32 bits. A etapa então falha com `ODBC data source '<name>' is not defined on the agent machine`.
:::

### No Linux

No Linux, o agente acessa o ODBC por meio do unixODBC.

1. Instale o unixODBC e o driver ODBC do banco de dados.
2. Verifique se o driver está registrado em `odbcinst.ini`, com o nome entre colchetes. A maioria dos pacotes de driver se registra sozinha ao ser instalada, e `odbcinst -q -d` lista os drivers registrados.
3. Adicione a origem de dados ao `odbc.ini` do sistema, como uma seção com o nome do DSN. Defina `Driver` com o nome do driver registrado e adicione o servidor, o banco de dados e quaisquer outras configurações que o driver solicitar:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Anote o nome da seção, `Sales` neste exemplo. Você o informa na conexão.

`odbcinst -j` mostra onde estão o `odbcinst.ini` e o `odbc.ini` do sistema, geralmente em `/etc`. Um DSN no `~/.odbc.ini` de um usuário só é encontrado quando o agente é executado com esse usuário.

### Em um Contêiner

A imagem de contêiner do PlaidLink inclui o unixODBC, mas nenhum driver ODBC. Para usar o ODBC a partir de um agente executado no Docker ou no Kubernetes, crie uma imagem a partir dela que instale o driver e adicione à imagem o `odbc.ini` do sistema com o DSN, ou monte-o no contêiner. A imagem é executada com o usuário `plaid`, então mude para `root` para instalar o driver e volte para `plaid` depois.

## Configuração

### Conexão de banco de dados

| Campo | Obrigatório | Descrição |
|---|---|---|
| Driver ODBC | Não | Deixe em branco para se conectar por um DSN. Caso contrário, o nome de um driver ODBC instalado na máquina do agente, exatamente como essa máquina o registra: no Windows, como o **ODBC Data Sources (64-bit)** o lista na guia **Drivers**, e no Linux, como o nome da seção em `odbcinst.ini`. A lista oferece drivers comuns, e você pode digitar qualquer outro. Aqui só funcionam os drivers do SQL Server da Microsoft. Para qualquer outro driver, inclusive os outros que a lista oferece, deixe em branco e use um DSN. O nome de um driver não pode conter chaves nem ponto e vírgula. |
| Nome da origem de dados (DSN) ou servidor | Sim | Sem um driver, o nome do System DSN na máquina do agente. Com um driver, o nome do host do servidor de banco de dados, ou `host,port` para o SQL Server em uma porta não padrão. |
| Banco de dados | Com um driver | O banco de dados a abrir. Ele não está disponível sem um driver, porque o DSN define o seu próprio, e salvar recusa um banco de dados sem um driver. |
| Atributos de conexão | Não | Outras configurações do driver, como pares `KEY=value` separados por `;`. Consulte [Atributos de conexão](#atributos-de-conexão). |

A conexão não tem campo de porta. Para o SQL Server em uma porta não padrão, adicione-a ao servidor como `host,port`, porque os drivers do SQL Server da Microsoft não têm palavra-chave de porta. Com um DSN, defina a porta no DSN ou substitua-a com um atributo como `PORT=5433`, para um driver que aceite um.

### Atributos de conexão

Os **Atributos de conexão** passam configurações ODBC ao driver em qualquer um dos modos, escritas como o ODBC as escreve:

- Com um driver, eles são adicionados depois das configurações da própria conexão. Use-os para tudo o mais que o driver precisar, como `ApplicationIntent=ReadOnly` para se conectar a uma réplica somente leitura.
- Com um DSN, eles substituem as configurações do próprio DSN, como `PORT=5433`, ou `DBQ=MYLIB` para a biblioteca padrão do IBM i.

Separe os pares com `;`, como em `Encrypt=yes;ApplicationIntent=ReadOnly`. Coloque entre chaves um valor que contenha `;`, como em `KEY={first;second}`, e dentro das chaves escreva `}` como `}}`. As palavras-chave chegam ao driver em maiúsculas; as palavras-chave do ODBC não diferenciam maiúsculas de minúsculas.

Salvar recusa:

- texto que não seja composto de pares `KEY=value`, inclusive uma chave que nunca é fechada e uma palavra-chave sem valor;
- uma palavra-chave informada mais de uma vez, em qualquer combinação de maiúsculas e minúsculas;
- uma palavra-chave que a conexão define a partir de seus próprios campos: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` e `PASSWORD`;
- `FILEDSN` e `SAVEFILE`, que fariam o agente ler as configurações da conexão de um arquivo em sua máquina, ou gravá-las em um.

As listas de conexões mascaram os atributos, porque um driver pode aceitar ali uma palavra-chave de credencial própria; o formulário da própria conexão os mostra. Limpe o campo para removê-los. Informe o usuário e a senha em **Credenciais de autenticação**.

:::note
O **ODBC Driver 18 for SQL Server** criptografa a conexão e verifica o certificado do servidor por padrão. Para um servidor com certificado autoassinado, adicione `TrustServerCertificate=yes` aos atributos.
:::

### Credenciais de autenticação

| Campo | Descrição |
|---|---|
| Usuário | O usuário com o qual se conectar. Por um DSN, deixe em branco para entrar como o DSN está configurado ou, no SQL Server, adicione `TRUSTED_CONNECTION=Yes` aos atributos para entrar com a própria conta do agente. Com um driver do SQL Server e sem usuário, a conexão entra com a própria conta do agente: a conta do Windows ou, no Linux, o tíquete Kerberos. |
| Usar autenticação de logon único (sem senha, usuário opcional) | Conecta sem uma senha armazenada. |
| Senha | A senha do usuário (somente gravação). Deixe em branco ao editar para manter a senha salva. |

### Configuração de SSL e Configuração de SSH

Estas guias não se aplicam a uma conexão ODBC. Defina a criptografia e outras opções do driver no DSN ou nos atributos de conexão.

## Conexões Salvas por uma Versão Anterior

As versões anteriores deste formulário exigiam um **Banco de dados** e um driver escolhido de uma lista fixa, e preenchiam uma **Porta**, mas nunca repassavam o driver, de modo que essas conexões não conseguiam se conectar. Abra a conexão e faça uma das opções:

- **Conectar por um DSN:** limpe **Driver ODBC**, informe o DSN e salve. Ao salvar, o Banco de dados antigo é limpo.
- **Conectar por um driver do SQL Server:** verifique se **Driver ODBC** corresponde a um driver do SQL Server instalado na máquina do agente. Muitos nomes da lista antiga não eram os nomes com que os drivers se registram.

Uma conexão que mantém um driver da lista antiga abre como uma conexão por driver. Ela falha ao se conectar até que o driver seja um driver do SQL Server instalado na máquina do agente; para qualquer outro banco de dados, conecte-se por um DSN.

Salvar também limpa a Porta antiga. Uma conexão que sempre teve apenas um DSN, sem Banco de dados, abre com **Driver ODBC** em branco.
