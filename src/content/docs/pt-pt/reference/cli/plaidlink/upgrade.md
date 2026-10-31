---
title: Atualizar
description: Atualize o seu agente PlaidLink para a versão mais recente para aceder a novas funcionalidades, correções de segurança e uma melhor compatibilidade com o sistema.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Pode ser necessária uma atualização manual do PlaidLink se o agente não tiver privilégios suficientes para se atualizar a si próprio quando são lançadas novas versões, ou se pretender um processo de atualização manual.

## Transferir o Agente

Consulte as versões disponíveis em [PlaidCloud.com](https://plaidcloud.com/) para o **PlaidLink**

## Parar o Agente Atual

Escreva **`Services`** na barra de pesquisa do Windows e abra o gestor de serviços. Na lista de serviços, localize **`PlaidCloud Agent`**.

Clique com o botão direito do rato no serviço **`PlaidCloud Agent`** e selecione *Stop*.  Quando o serviço parar com êxito, continue.

## Extrair o Agente

Navegue até à localização atual do agente instalado.

```bash
C:\Users\<Username here>\src\
```

Mude o nome da pasta da instalação atual para que deixe de ser referenciada.  Por exemplo, `Plaidlink_Old_12122022`

Extraia o ficheiro zip transferido para instalar o agente neste local. Em geral, este local será:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Iniciar o Agente

Regresse à janela *Services*.  Clique com o botão direito do rato no serviço **`PlaidCloud Agent`** e selecione *Start*.

Escreva **`Services`** na barra de pesquisa do Windows e abra o gestor de serviços. Na lista de serviços, localize **`PlaidCloud Agent`**.

Clique com o botão direito do rato no serviço e selecione **`Start`** para iniciar o agente.  Quando o agente passar ao estado **`Running`**, está novamente operacional na nova versão.
