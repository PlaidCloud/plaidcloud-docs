---
title: Delete Old Files (passo)
description: Elimine ficheiros de uma conta de documentos mais antigos ou mais recentes do que uma idade escolhida, com uma listagem de ensaio antes de remover o que quer que seja.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Descrição

Elimina ficheiros de uma conta de documentos com base na idade. Utilize-o para evitar que uma pasta de exportação ou de receção cresça sem limite — descarte as extrações de ontem ou limpe arquivos com mais de um ano.

## Configuração

### Ficheiros a eliminar

- **Caminho do ficheiro** — a conta de documentos e a pasta onde trabalhar.
- **Idade** — um número mais uma unidade: minutos, horas, dias, meses ou anos.
- **Antes ou depois** — elimina ficheiros modificados pela última vez **antes** da data-limite (o sentido habitual de limpeza) ou **depois** dela.
- **Recursivo** — desativado por predefinição. Ative-o para incluir as subpastas.
- **Tabela de resultados do teste** — a tabela onde o botão **Testar** do editor do passo escreve
  a pré-visualização dos ficheiros correspondentes.

<Aside type="caution" title="Pré-visualize com Testar, não executando o passo">
  A pré-visualização provém do botão **Testar** enquanto edita o passo.
  Executar o passo num fluxo de trabalho elimina sempre — não existe modo de ensaio
  e a tabela de resultados do teste não o desvia. A eliminação não é reversível
  e um caminho errado com **Recursivo** ativado alcança mais do que seria de esperar,
  por isso verifique a pré-visualização antes de o agendar.
</Aside>

## Relacionado

- [Passos de documentos](/pt-pt/reference/workflow-steps/document/)
- [Delete Document File (passo)](/pt-pt/reference/workflow-steps/document/delete-document-file/)
- [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/)
