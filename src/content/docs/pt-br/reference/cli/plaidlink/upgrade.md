---
title: Atualizar
description: Atualize seu agente PlaidLink para a versão mais recente para acessar novos recursos, correções de segurança e melhor compatibilidade com o sistema.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Pode ser necessário atualizar o PlaidLink manualmente se o agente não tiver privilégios suficientes para se atualizar sozinho quando novas versões forem lançadas, ou se você preferir um processo de atualização manual.

## Baixar o Agente

Consulte as versões disponíveis em [PlaidCloud.com](https://plaidcloud.com/) para o **PlaidLink**.

## Parar o Agente Atual

Digite **`Services`** na barra de pesquisa do Windows e abra o gerenciador de serviços. Na lista de serviços, localize **`PlaidCloud Agent`**.

Clique com o botão direito do mouse no serviço **`PlaidCloud Agent`** e selecione *Stop*. Quando o serviço for interrompido com sucesso, continue.

## Extrair o Agente

Navegue até o local atual do agente instalado.

```bash
C:\Users\<Username here>\src\
```

Renomeie a pasta da instalação atual para que ela deixe de ser referenciada. Por exemplo, `Plaidlink_Old_12122022`.

Extraia o arquivo zip baixado para instalá-lo neste local. Em geral, esse local será:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Iniciar o Agente

Volte à janela *Services*. Clique com o botão direito do mouse no serviço **`PlaidCloud Agent`** e selecione *Start*.

Digite **`Services`** na barra de pesquisa do Windows e abra o gerenciador de serviços. Na lista de serviços, localize **`PlaidCloud Agent`**.

Clique com o botão direito do mouse no serviço e selecione **`Start`** para iniciar o agente. Quando o agente aparecer no estado **`Running`**, ele estará operacional novamente na nova versão.
