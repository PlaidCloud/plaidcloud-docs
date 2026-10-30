---
title: Encrypt File and Decrypt File
description: Criptografe ou descriptografe um arquivo de documento inteiro com AES ou Blowfish, ou adicione ou remova a senha de uma pasta de trabalho do Excel, em uma etapa de fluxo de trabalho do PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Descrição

**Documento: criptografar arquivo** criptografa um arquivo de uma conta de documentos e grava o resultado em outro arquivo. **Documento: descriptografar arquivo** faz o inverso. As duas etapas usam as mesmas configurações. Use-as para receber arquivos criptografados de um parceiro, descriptografá-los antes que uma importação os leia e criptografar uma exportação antes que ela siga para outro sistema.

## Arquivos

| Configuração | Obrigatória | O que faz |
| --- | --- | --- |
| Arquivo de origem | Sim | O arquivo a criptografar ou descriptografar. |
| Arquivo de destino | Sim | O arquivo a gravar. Deve ser diferente do arquivo de origem, para que uma nova execução nunca atue sobre a própria saída. |
| Excluir o arquivo de origem depois que o arquivo de destino for gravado | Não | Remove o arquivo de origem depois que o arquivo de destino for gravado com segurança. |

Um arquivo de origem que não existe não é um erro: a etapa termina com um aviso que informa o caminho e não grava nada, e o fluxo de trabalho continua. Um arquivo de origem vazio grava um arquivo de destino vazio com um aviso, exceto que criptografar um arquivo vazio com AES ou Blowfish grava um arquivo criptografado de verdade. Uma conta de documentos do Smartsheet não pode ser usada, porque não é possível ler os arquivos de volta dela.

## Parâmetros

| Configuração | O que faz |
| --- | --- |
| Algoritmo | No grupo Cifra: **AES-128 (chave de 16 bytes)**, **AES-192 (chave de 24 bytes)**, **AES-256 (chave de 32 bytes)**, **Blowfish (chave de 4 a 56 bytes)** ou **Senha da pasta de trabalho do Excel**. |
| Modo | **CBC** (o padrão), **ECB** ou **GCM**. O Blowfish aceita apenas CBC ou ECB. |
| Variável da chave | A variável de fluxo de trabalho ou de projeto que contém a chave de criptografia, como `{aes_key}`. Obrigatória para AES e Blowfish. |
| Codificação da chave e do IV | Como a chave e o IV são escritos: **Texto (UTF-8)**, **Hexadecimal** ou **Base64**. |
| IV fixo | O vetor de inicialização. Deixe em branco e a criptografia inicia o arquivo com um IV aleatório, que a descriptografia lê de volta no início do arquivo. A criptografia GCM sempre usa um IV aleatório, portanto deixe em branco para GCM. |
| Variável de senha da pasta de trabalho | A variável de fluxo de trabalho ou de projeto que contém a senha a definir em uma pasta de trabalho do Excel, ou a remover dela, como `{xlsx_password}`. Obrigatória para **Senha da pasta de trabalho do Excel**. |

CBC e ECB preenchem com PKCS7, e GCM adiciona uma tag de autenticação de 16 bytes depois dos dados criptografados. Um arquivo GCM pode ter até 256 MB. Uma chave ou um IV incorreto interrompe a etapa com um erro e não deixa nenhum arquivo parcial.

## As chaves ficam em variáveis

**Variável da chave** e **Variável de senha da pasta de trabalho** aceitam somente uma referência a variável, como `{aes_key}`, nunca a chave ou a senha em si: salvar uma etapa com qualquer outra coisa nesses campos é recusado. Coloque o segredo em uma [variável de fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/) ou em uma variável de projeto, para que seja definido em um só lugar e nunca apareça na etapa, em suas versões, em suas cópias ou no que um assistente de IA lê de volta. A etapa lê o valor da variável quando é executada. **IV fixo** é um campo de senha, portanto seu valor fica oculto no formulário.

As etapas que guardavam uma chave ou uma senha digitada antes desta regra tiveram esse valor movido automaticamente para uma nova variável de projeto, visível somente para Arquitetos, e agora referenciam essa variável.

## Relacionados

- [Etapas de documento](/pt-br/reference/workflow-steps/document/)
- [Gerenciar variáveis de fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
