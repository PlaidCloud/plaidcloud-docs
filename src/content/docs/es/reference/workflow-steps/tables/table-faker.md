---
title: Paso Table Faker
description: Genere datos de prueba sintéticos en un paso de flujo de trabajo de PlaidCloud con Faker para crear conjuntos de datos de ejemplo realistas para desarrollo.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## Descripción


Table Faker genera datos ficticios.



### Dirección




| Generador | Argumentos opcionales |
| Número de edificio |  |
| Ciudad |  |
| Sufijo de ciudad |  |
| País |  |
| Código de país | “representation”=”alpha-2” |
| Dirección completa |  |
| Latitud |  |
| Longitud |  |
| DPO militar |  |
| Código postal |  |
| Código postal más 4 |  |
| Estado |  |
| Abreviatura del estado |  |
| Dirección postal |  |
| Nombre de la calle |  |
| Sufijo de la calle |  |

### Automoción




| Generador | Argumentos opcionales |
| Matrícula |  |

### Código de barras




| Generador | Argumentos opcionales |
| EAN13 |  |
| EAN8 |  |

### Colores




| Generador | Argumentos opcionales |
| Nombre del color |  |
| Color hexadecimal |  |
| Color RGB |  |
| Color RGB CSS |  |
| Nombre de color seguro |  |
| Color hexadecimal seguro |  |

### Empresa




| Generador | Argumentos opcionales |
| Eslogan de la empresa |  |
| Nombre de la empresa |  |
| Sufijo de la empresa |  |

### Tarjeta de crédito




| Generador | Argumentos opcionales |
| Fecha de vencimiento | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Completa | “card_type”=null |
| Número | “card_type”=null |
| Proveedor | “card_type”=null |
| Código de seguridad | “card_type”=null |

### Moneda




| Generador | Argumentos opcionales |
| Código |  |

### Fecha y hora




| Generador | Argumentos opcionales |
| a. m./p. m. |  |
| Siglo |  |
| Fecha | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Fecha y hora | “tzinfo”:null“end_datetime”=null |
| Fecha y hora de este siglo | “before_now”=true“after_now”=false“tzinfo”=null |
| Fecha y hora de esta década | “before_now”=true“after_now”=false“tzinfo”=null |
| Fecha y hora de este mes | “before_now”=true“after_now”=false“tzinfo”=null |
| Fecha y hora de este año | “before_now”=true“after_now”=false“tzinfo”=null |
| Día del mes |  |
| Día de la semana |  |
| Fecha y hora ISO8601 | “tzinfo”=null“end_datetime”=null |
| Mes |  |
| Nombre del mes |  |
| Fecha pasada (últimos 30 días) | “start_date”=”-30d”“tzinfo”=null |
| Zona horaria |  |
| Hora Unix | “end_datetime”=null“start_datetime”=null |
| Año |  |

### Archivo




| Generador | Argumentos opcionales |
| Extensión de archivo | “category”=null |
| Nombre de archivo | “category”=null“extension”=null |
| Ruta del archivo | “depth”=”1”“category”=null“extension”=null |
| Tipo MIME | “category”=null |

### Internet




| Generador | Argumentos opcionales |
| Correo electrónico de empresa |  |
| Nombre de dominio |  |
| Palabra de dominio |  |
| Correo electrónico |  |
| Correo electrónico gratuito |  |
| Dominio de correo electrónico gratuito |  |
| URL de imagen | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| Dirección MAC |  |
| Correo electrónico seguro |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| Extensión de URL |  |
| Página de URL |  |
| Nombre de usuario |  |

### ISBN




| Generador | Argumentos opcionales |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Empleo




| Generador | Argumentos opcionales |
| Nombre del puesto |  |

### Lorem




| Generador | Argumentos opcionales |
| Párrafo | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Párrafos | “nb”=”3”“ext_word_list”=null |
| Oración | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Oraciones | “nb”=”3”“ext_word_list”=null |
| Texto | “max_nb_chars”=”200”“ext_word_list”=null |
| Palabra | “ext_word_list”=null |
| Palabras | “nb”=”3”“ext_word_list”=null |

### Varios




| Generador | Argumentos opcionales |
| Binario | “length”=”1048576” |
| Booleano | “chance_of_getting_true”=”50” |
| Booleano nulo |  |
| Configuración regional |  |
| Código de idioma |  |
| MD5 | “raw_output”=false |
| Contraseña | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| Cadena aleatoria |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Numérico




| Generador | Argumentos opcionales |
| Serial grande (autoincremental) |  |
| Número flotante aleatorio |  |
| Número flotante aleatorio en un rango |  |
| Entero aleatorio |  |
| Entero aleatorio en un rango |  |
| Numérico aleatorio |  |
| Porcentaje aleatorio (0 – 1) |  |
| Porcentaje aleatorio (0 – 100) |  |
| Serial (autoincremental) |  |

### Persona




| Generador | Argumentos opcionales |
| Nombre |  |
| Nombre (femenino) |  |
| Nombre (masculino) |  |
| Nombre completo |  |
| Nombre completo (femenino) |  |
| Nombre completo (masculino) |  |
| Apellido |  |
| Apellido (femenino) |  |
| Apellido (masculino) |  |
| Prefijo |  |
| Prefijo (femenino) |  |
| Prefijo (masculino) |  |
| Sufijo |  |
| Sufijo (femenino) |  |
| Sufijo (masculino) |  |

### Teléfono




| Generador | Argumentos opcionales |
| Número de teléfono |  |
| RDSI |  |

### Impuestos




| Generador | Argumentos opcionales |
| EIN |  |
| SSN completo |  |
| ITIN |  |

### Agente de usuario




| Generador | Argumentos opcionales |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| Agente de usuario completo |  |
| Internet Explorer |  |
| Token de plataforma Linux |  |
| Procesador Linux |  |
| Token de plataforma Mac |  |
| Procesador Mac |  |
| Opera |  |
| Safari |  |
| Token de plataforma Windows |  |

### Generadores especiales


Aunque estos dos generadores no tienen argumentos, las opciones que ofrecen funcionan de forma similar a los argumentos.



**Generador de patrones**:




| Número | Formato | Salida | Descripción |
| 3.1415926 | \{:.2f} | 3.14 | 2 decimales |
| 3.1415926 | \{:+.2f} | +3.14 | 2 decimales con signo |
| -1 | \{:+.2f} | -1.00 | 2 decimales con signo |
| 2.71828 | \{:.0f} | 3 | Sin decimales |
| 5 | \{:0>2d} | 05 | Rellenar el número con ceros (relleno a la izquierda, ancho 2) |
| 5 | \{:x&lt;4d} | 5xxx | Rellenar el número con x (relleno a la derecha, ancho 4) |
| 10 | \{:x&lt;4d} | 10xx | Rellenar el número con x (relleno a la derecha, ancho 4) |
| 1000000 | \{:,} | 1,000,000 | Formato de número con coma como separador |
| 0.25 | \{:.2%} | 25.00% | Formato de porcentaje |
| 1000000000 | \{:.2e} | 1.00e+09 | Notación exponencial |
| 13 | \{:10d} | 13 | Alineado a la derecha (predeterminado, ancho 10) |
| 13 | \{:&lt;10d} | 13 | Alineado a la izquierda (ancho 10) |
| 13 | \{:^10d} | 13 | Alineado al centro (ancho 10) |

**Elección aleatoria**:


Para indicar las opciones de elección aleatoria, basta con poner cada opción entre comillas y separarlas con comas. Una cadena de opciones de elección aleatoria tendría este aspecto: “x”,”y”,”z”



Aquí, la columna “Key Word Args/Pattern/Choices” de la fila “pattern” contiene una oración con varias referencias. La primera ecuación de referencia ( \{percentage0-100:.2f}% ) apunta a la fila “percentage0-100”, que generará una ecuación aleatoria. Por lo tanto, el porcentaje aleatorio producido por la fila “percentage0-100” se insertará automáticamente en la oración. La ecuación de referencia \{first_name} apunta a la fila titulada “first_name”, que generará un nombre aleatorio, y ese nombre se insertará automáticamente en la oración. La última ecuación de referencia ( \{randomn_choice} ) funciona igual que las otras dos.



Con esto, cuando se ejecute el generador de patrones, obtendrá los siguientes resultados.


## Recuento de filas desde una tabla

Para tomar el número de filas de los datos, establezca **Tabla con el recuento** (`rows_source`) y **Columna con el recuento** (`rows_column`). El paso lee el número de la primera fila de la tabla, en esa columna, cuando se ejecuta, en lugar del recuento de filas que haya establecido. Un valor ausente, o menor que 1, no genera ninguna fila.

## Qué se comprueba al guardar

Cada fila de **Columnas de datos ficticios y tipos de datos** se convierte en una columna de la tabla generada, por lo que cada una necesita un nombre propio. Se rechaza el guardado con *Every fake data column needs a name.* cuando un nombre está en blanco, y con *Fake data column name 'city' is used more than once; each needs its own.* cuando dos comparten el mismo.
