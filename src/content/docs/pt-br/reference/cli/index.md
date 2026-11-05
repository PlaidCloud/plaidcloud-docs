---
title: Ferramentas de CLI
description: Referência das ferramentas de linha de comando do PlaidCloud — o agente PlaidLink, o suplemento PlaidXL para Excel e a CLI do Jupyter para integração com notebooks.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

O PlaidCloud oferece três ferramentas de linha de comando e locais para trabalhar com espaços de trabalho fora da interface web:

## PlaidLink

O [PlaidLink](/pt-br/reference/cli/plaidlink/) é um agente que roda dentro da sua rede para conectar fluxos de trabalho do PlaidCloud a recursos protegidos por firewall — bancos de dados, compartilhamentos de arquivos e outros sistemas que o PlaidCloud não consegue acessar diretamente. Ele é instalado como um serviço do Windows, um daemon Unix/Linux/Mac, um contêiner ou um pod do Kubernetes.

- [Instalar](/pt-br/reference/cli/plaidlink/install/)
- [Configurar](/pt-br/reference/cli/plaidlink/configure/)
- [Agentes](/pt-br/reference/cli/plaidlink/agents/)
- [Atualizar versão](/pt-br/reference/cli/plaidlink/upgrade/)

## PlaidXL

O [PlaidXL](/pt-br/reference/cli/plaidxl/) é o suplemento do PlaidCloud para o Microsoft Excel. Ele recupera tabelas e dimensões de projeto para as planilhas, atualiza-as sob demanda, adiciona fórmulas `PLAIDXL` que calculam valores consolidados e métricas governadas a partir dos dados do PlaidCloud e grava de volta os valores planejados.

- [Instalar](/pt-br/reference/cli/plaidxl/install/)
- [Entrar](/pt-br/reference/cli/plaidxl/connect/)
- [Trabalhar com tabelas e dimensões](/pt-br/reference/cli/plaidxl/retrieve/)
- [Funções personalizadas](/pt-br/reference/cli/plaidxl/functions/)
- [Criar um relatório](/pt-br/reference/cli/plaidxl/build-a-report/)
- [Detalhar, escolher membros e explicar números](/pt-br/reference/cli/plaidxl/drill/)
- [Digitar valores no PlaidCloud](/pt-br/reference/cli/plaidxl/write-values/)
- [Perguntar ao Weave no Excel](/pt-br/reference/cli/plaidxl/weave/)
- [A faixa de opções do PlaidCloud](/pt-br/reference/cli/plaidxl/ribbon/)
- [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/)

## CLI do Jupyter

A [CLI do Jupyter](/pt-br/reference/cli/jupyter/) permite que cientistas de dados trabalhem com dados de projeto do PlaidCloud a partir de notebooks Jupyter, usando uma CLI com reconhecimento do PlaidCloud e auxiliares em Python.

- [Linha de comando](/pt-br/reference/cli/jupyter/command-line/)
- [Notebook Jupyter](/pt-br/reference/cli/jupyter/jupyter-notebook/)
- [Configuração do OAuth](/pt-br/reference/cli/jupyter/oauth-setup/)
