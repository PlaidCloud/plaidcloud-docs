---
title: Encrypt File and Decrypt File (passo)
description: Encripte ou desencripte um ficheiro de documentos completo com AES ou Blowfish, ou adicione ou remova a palavra-passe de um livro Excel, num passo de fluxo de trabalho PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Descrição

**Documento: encriptar ficheiro** encripta um ficheiro de uma conta de documentos e escreve o resultado noutro ficheiro. **Documento: desencriptar ficheiro** faz o inverso. Ambos os passos têm as mesmas definições. Utilize-os para receber ficheiros encriptados de um parceiro, desencriptá-los antes de uma importação os ler e encriptar uma exportação antes de seguir para outro sistema.

## Ficheiros

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Ficheiro de origem | Sim | O ficheiro a encriptar ou desencriptar. |
| Ficheiro de destino | Sim | O ficheiro a escrever. Tem de ser diferente do ficheiro de origem, para que uma nova execução nunca atue sobre o seu próprio resultado. |
| Eliminar o ficheiro de origem depois de escrever o ficheiro de destino | Não | Remove o ficheiro de origem depois de o ficheiro de destino ser escrito em segurança. |

Um ficheiro de origem que não existe não é um erro: o passo termina com um aviso que indica o caminho e não escreve nada, e o fluxo de trabalho continua. Um ficheiro de origem vazio escreve um ficheiro de destino vazio com um aviso, exceto que encriptar um ficheiro vazio com AES ou Blowfish escreve um verdadeiro ficheiro encriptado. Não é possível utilizar uma conta de documentos Smartsheet, porque não é possível voltar a ler ficheiros a partir dela.

## Parâmetros

| Definição | O que faz |
| --- | --- |
| Algoritmo | No grupo Cifra: **AES-128 (chave de 16 bytes)**, **AES-192 (chave de 24 bytes)**, **AES-256 (chave de 32 bytes)**, **Blowfish (chave de 4 a 56 bytes)** ou **Palavra-passe do livro do Excel**. |
| Modo | **CBC** (o predefinido), **ECB** ou **GCM**. O Blowfish aceita apenas CBC ou ECB. |
| Variável da chave | A variável de fluxo de trabalho ou de projeto que contém a chave de encriptação, como `{aes_key}`. Obrigatória para AES e Blowfish. |
| Codificação da chave e do IV | A forma como a chave e o IV são escritos: **Texto (UTF-8)**, **Hexadecimal** ou **Base64**. |
| IV fixo | O vetor de inicialização. Se o deixar em branco, a encriptação inicia o ficheiro com um IV aleatório, que a desencriptação volta a ler a partir do início do ficheiro. A encriptação GCM utiliza sempre um IV aleatório, pelo que deve deixá-lo em branco para GCM. |
| Variável da palavra-passe do livro | A variável de fluxo de trabalho ou de projeto que contém a palavra-passe a definir num livro Excel, ou a remover dele, como `{xlsx_password}`. Obrigatória para **Palavra-passe do livro do Excel**. |

CBC e ECB preenchem com PKCS7, e o GCM acrescenta uma etiqueta de autenticação de 16 bytes depois dos dados encriptados. Um ficheiro GCM pode ter até 256 MB. Uma chave ou um IV incorretos interrompem o passo com um erro e não deixam nenhum ficheiro parcial.

## As chaves residem em variáveis

**Variável da chave** e **Variável da palavra-passe do livro** aceitam apenas uma referência a uma variável, como `{aes_key}`, nunca a própria chave ou palavra-passe: guardar um passo com qualquer outra coisa nestes campos é recusado. Coloque o segredo numa [variável de fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/) ou numa variável de projeto, para que seja definido num único local e nunca apareça no passo, nas suas versões, nas suas cópias nem no que um assistente de IA lê. O passo lê o valor da variável quando é executado. **IV fixo** é um campo de palavra-passe, pelo que o seu valor fica oculto no formulário.

Os passos que continham uma chave ou palavra-passe escrita antes desta regra tiveram-na movida automaticamente para uma nova variável de projeto, visível apenas para Arquitetos, e passaram a referenciar essa variável.

## Relacionado

- [Passos de documentos](/pt-pt/reference/workflow-steps/document/)
- [Gerir variáveis de fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
