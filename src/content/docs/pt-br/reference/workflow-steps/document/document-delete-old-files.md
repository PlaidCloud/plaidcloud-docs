---
title: Delete Old Files
description: Exclua arquivos de uma conta de documentos mais antigos ou mais recentes que uma idade escolhida, com uma listagem de teste antes de qualquer remoção.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Descrição

Exclui arquivos de uma conta de documentos com base na idade. Use-a para impedir que uma pasta de exportação ou de recebimento cresça sem limite: descarte os extratos de ontem ou limpe arquivos com mais de um ano.

## Configuração

### Arquivos a excluir

- **Caminho do arquivo** — a conta de documentos e a pasta em que trabalhar.
- **Idade** — um número mais uma unidade: minutos, horas, dias, meses ou anos.
- **Antes ou depois** — exclui os arquivos modificados pela última vez **antes** da data de corte (a direção usual de limpeza) ou **depois** dela.
- **Recursivo** — desativado por padrão. Ative para incluir as subpastas.
- **Tabela de resultados do teste** — a tabela em que o botão **Testar** do editor da etapa grava
  a pré-visualização dos arquivos correspondentes.

<Aside type="caution" title="Visualize com Testar, não executando a etapa">
  A pré-visualização vem do botão **Testar** enquanto você edita a etapa.
  Executar a etapa em um fluxo de trabalho sempre exclui: não existe modo de simulação,
  e a tabela de resultados do teste não desvia a exclusão. A exclusão não é reversível, e
  um caminho errado com **Recursivo** ativado alcança mais arquivos do que você espera, portanto confira a
  pré-visualização antes de agendar a etapa.
</Aside>

## Relacionados

- [Etapas de documento](/pt-br/reference/workflow-steps/document/)
- [Delete Document File](/pt-br/reference/workflow-steps/document/delete-document-file/)
- [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/)
