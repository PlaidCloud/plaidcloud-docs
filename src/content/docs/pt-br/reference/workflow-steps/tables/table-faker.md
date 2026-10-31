---
title: Table Faker (etapa)
description: Gere dados de teste sintéticos em uma etapa de fluxo de trabalho do PlaidCloud usando o Faker para criar conjuntos de dados de exemplo realistas para desenvolvimento.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## Descrição


O Table Faker gera dados falsos.



### Endereço




| Gerador | Argumentos opcionais |
| Número do edifício |  |
| Cidade |  |
| Sufixo de cidade |  |
| País |  |
| Código do país | “representation”=”alpha-2” |
| Endereço completo |  |
| Latitude |  |
| Longitude |  |
| DPO militar |  |
| Código postal |  |
| Código postal mais 4 |  |
| Estado |  |
| Sigla do estado |  |
| Logradouro |  |
| Nome da rua |  |
| Sufixo de rua |  |

### Automotivo




| Gerador | Argumentos opcionais |
| Placa de veículo |  |

### Código de barras




| Gerador | Argumentos opcionais |
| EAN13 |  |
| EAN8 |  |

### Cores




| Gerador | Argumentos opcionais |
| Nome da cor |  |
| Cor hexadecimal |  |
| Cor RGB |  |
| Cor RGB CSS |  |
| Nome de cor segura |  |
| Cor hexadecimal segura |  |

### Empresa




| Gerador | Argumentos opcionais |
| Slogan da empresa |  |
| Nome da empresa |  |
| Sufixo da empresa |  |

### Cartão de crédito




| Gerador | Argumentos opcionais |
| Data de validade | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Completo | “card_type”=null |
| Número | “card_type”=null |
| Bandeira | “card_type”=null |
| Código de segurança | “card_type”=null |

### Moeda




| Gerador | Argumentos opcionais |
| Código |  |

### Data e hora




| Gerador | Argumentos opcionais |
| AM/PM |  |
| Século |  |
| Data | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Data e hora | “tzinfo”:null“end_datetime”=null |
| Data e hora neste século | “before_now”=true“after_now”=false“tzinfo”=null |
| Data e hora nesta década | “before_now”=true“after_now”=false“tzinfo”=null |
| Data e hora neste mês | “before_now”=true“after_now”=false“tzinfo”=null |
| Data e hora neste ano | “before_now”=true“after_now”=false“tzinfo”=null |
| Dia do mês |  |
| Dia da semana |  |
| Data e hora ISO8601 | “tzinfo”=null“end_datetime”=null |
| Mês |  |
| Nome do mês |  |
| Data passada (últimos 30 dias) | “start_date”=”-30d”“tzinfo”=null |
| Fuso horário |  |
| Hora Unix | “end_datetime”=null“start_datetime”=null |
| Ano |  |

### Arquivo




| Gerador | Argumentos opcionais |
| Extensão de arquivo | “category”=null |
| Nome do arquivo | “category”=null“extension”=null |
| Caminho do arquivo | “depth”=”1”“category”=null“extension”=null |
| Tipo MIME | “category”=null |

### Internet




| Gerador | Argumentos opcionais |
| E-mail corporativo |  |
| Nome de domínio |  |
| Palavra de domínio |  |
| E-mail |  |
| E-mail gratuito |  |
| Domínio de e-mail gratuito |  |
| URL de imagem | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| Endereço MAC |  |
| E-mail seguro |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| Extensão de URL |  |
| Página de URL |  |
| Nome de usuário |  |

### ISBN




| Gerador | Argumentos opcionais |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Profissão




| Gerador | Argumentos opcionais |
| Nome do cargo |  |

### Lorem




| Gerador | Argumentos opcionais |
| Parágrafo | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Parágrafos | “nb”=”3”“ext_word_list”=null |
| Frase | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Frases | “nb”=”3”“ext_word_list”=null |
| Texto | “max_nb_chars”=”200”“ext_word_list”=null |
| Palavra | “ext_word_list”=null |
| Palavras | “nb”=”3”“ext_word_list”=null |

### Diversos




| Gerador | Argumentos opcionais |
| Binário | “length”=”1048576” |
| Booleano | “chance_of_getting_true”=”50” |
| Booleano nulo |  |
| Localidade |  |
| Código de idioma |  |
| MD5 | “raw_output”=false |
| Senha | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| String aleatória |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Numérico




| Gerador | Argumentos opcionais |
| Serial grande (autoincremento) |  |
| Float aleatório |  |
| Float aleatório em um intervalo |  |
| Inteiro aleatório |  |
| Inteiro aleatório em um intervalo |  |
| Numérico aleatório |  |
| Porcentagem aleatória (0 – 1) |  |
| Porcentagem aleatória (0 – 100) |  |
| Serial (autoincremento) |  |

### Pessoa




| Gerador | Argumentos opcionais |
| Nome |  |
| Nome feminino |  |
| Nome masculino |  |
| Nome completo |  |
| Nome completo feminino |  |
| Nome completo masculino |  |
| Sobrenome |  |
| Sobrenome feminino |  |
| Sobrenome masculino |  |
| Prefixo |  |
| Prefixo feminino |  |
| Prefixo masculino |  |
| Sufixo |  |
| Sufixo feminino |  |
| Sufixo masculino |  |

### Telefone




| Gerador | Argumentos opcionais |
| Número de telefone |  |
| ISDN |  |

### Impostos




| Gerador | Argumentos opcionais |
| EIN |  |
| SSN completo |  |
| ITIN |  |

### User Agent




| Gerador | Argumentos opcionais |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| User Agent completo |  |
| Internet Explorer |  |
| Token de plataforma Linux |  |
| Processador Linux |  |
| Token de plataforma Mac |  |
| Processador Mac |  |
| Opera |  |
| Safari |  |
| Token de plataforma Windows |  |

### Geradores especiais


Embora esses dois geradores não tenham argumentos, as opções que oferecem funcionam de forma semelhante a argumentos.



**Gerador de padrão**:




| Número | Formato | Saída | Descrição |
| 3.1415926 | \{:.2f} | 3.14 | 2 casas decimais |
| 3.1415926 | \{:+.2f} | +3.14 | 2 casas decimais com sinal |
| -1 | \{:+.2f} | -1.00 | 2 casas decimais com sinal |
| 2.71828 | \{:.0f} | 3 | Sem casas decimais |
| 5 | \{:0>2d} | 05 | Preenche o número com zeros (preenchimento à esquerda, largura 2) |
| 5 | \{:x&lt;4d} | 5xxx | Preenche o número com x (preenchimento à direita, largura 4) |
| 10 | \{:x&lt;4d} | 10xx | Preenche o número com x (preenchimento à direita, largura 4) |
| 1000000 | \{:,} | 1,000,000 | Formato numérico com vírgula como separador |
| 0.25 | \{:.2%} | 25.00% | Formata como porcentagem |
| 1000000000 | \{:.2e} | 1.00e+09 | Notação exponencial |
| 13 | \{:10d} | 13 | Alinhado à direita (padrão, largura 10) |
| 13 | \{:&lt;10d} | 13 | Alinhado à esquerda (largura 10) |
| 13 | \{:^10d} | 13 | Centralizado (largura 10) |

**Escolha aleatória**:


Para fornecer as opções da escolha aleatória, basta colocar as opções entre aspas e separar cada uma com uma vírgula. Assim, uma string de opções de escolha aleatória ficaria assim: “x”,”y”,”z”



Aqui, a coluna “Key Word Args/Pattern/Choices” da linha “pattern” contém uma frase com várias referências. A primeira equação de referência ( \{percentage0-100:.2f}% ) aponta para a linha “percentage0-100”, que gera uma equação aleatória. Assim, a porcentagem aleatória produzida pela linha “percentage0-100” é inserida automaticamente na frase. A equação de referência \{first_name} aponta para a linha chamada “first_name”, que gera um nome aleatoriamente, e esse nome é inserido automaticamente na frase. A última equação de referência ( \{randomn_choice} ) funciona da mesma forma que as outras duas.



Com isso, quando o gerador de padrão é executado, você recebe os seguintes resultados.


## Contagem de linhas de uma tabela

Para obter o número de linhas a partir de dados, defina **Tabela com a contagem** (`rows_source`) e **Coluna com a contagem** (`rows_column`). A etapa lê o número da primeira linha da tabela, nessa coluna, quando é executada, no lugar da contagem de linhas que você definiu. Um valor ausente, ou menor que 1, não gera nenhuma linha.

## O que é verificado ao salvar

Cada linha de **Colunas de dados falsos e tipos de dados** se torna uma coluna da tabela gerada, portanto cada uma precisa de um nome próprio. O salvamento é recusado com *Every fake data column needs a name.* quando um nome está em branco, e com *Fake data column name 'city' is used more than once; each needs its own.* quando dois compartilham o mesmo nome.
