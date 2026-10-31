---
title: Apache Kafka
description: Configure una conexión de Apache Kafka en PlaidCloud para leer los mensajes de los temas en tablas y enviar las filas de una tabla como mensajes.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka** es una plataforma distribuida de transmisión de eventos. Use esta conexión con [Importar Kafka](/es/reference/workflow-steps/import/import-kafka/) para leer los mensajes de los temas en una tabla, y con [Exportar Kafka](/es/reference/workflow-steps/export/export-kafka/) para enviar cada fila de una tabla como un mensaje. Para crear una, elija **Apache Kafka** como tipo de conexión.

## Documentación del proveedor
[La documentación de Apache Kafka](https://kafka.apache.org/documentation/).

## Configuración

### Conexión de Kafka

| Campo | Obligatorio | Descripción |
|---|---|---|
| Brokers | Sí | Los brokers a los que conectarse, separados por comas, como `broker1:9092,broker2:9092`. |
| Protocolo de seguridad | No | `PLAINTEXT` (el valor predeterminado), `SSL`, `SASL_PLAINTEXT` o `SASL_SSL`. |
| Tiempo de espera de sesión (ms) | No | Cuánto tiempo esperan los brokers sin recibir noticias de PlaidCloud antes de excluirlo del grupo de consumidores. Al menos 1000. |

### Credenciales SASL

Se usan cuando el protocolo de seguridad es `SASL_PLAINTEXT` o `SASL_SSL`.

| Campo | Descripción |
|---|---|
| Mecanismo SASL | `PLAIN` (el valor predeterminado), `SCRAM-SHA-256`, `SCRAM-SHA-512` u `OAUTHBEARER`. Kerberos (`GSSAPI`) no está disponible. |
| Usuario | El usuario con el que conectarse, para `PLAIN` y `SCRAM`. |
| Contraseña | La contraseña del usuario (solo escritura), para `PLAIN` y `SCRAM`. |

### OAuth (OAUTHBEARER)

Se usa cuando el mecanismo SASL es `OAUTHBEARER`. PlaidCloud obtiene su token de su proveedor de identidad mediante la concesión de credenciales de cliente de OAuth, y obtiene uno nuevo cuando caduca.

| Campo | Descripción |
|---|---|
| URL del punto de conexión del token | El punto de conexión de tokens del proveedor de identidad. Debe ser una dirección `https` en la internet pública. |
| ID de cliente | El cliente con el que se solicita el token. Obligatorio. |
| Secreto de cliente | El secreto del cliente (solo escritura). Obligatorio. |
| Ámbito | El ámbito que se solicita, cuando su proveedor lo necesita. |
| Extensiones SASL | Pares `key=value` opcionales, separados por comas, que se envían con el token, como `logicalCluster` e `identityPoolId`, que solicita Confluent Cloud. |

### TLS

| Campo | Descripción |
|---|---|
| Certificado de CA (PEM) | La entidad de certificación que firmó los certificados de los brokers, cuando no es una pública. Déjelo en blanco al editar para conservar el certificado guardado. |
