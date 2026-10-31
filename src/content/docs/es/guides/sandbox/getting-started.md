---
title: Introducción al Custom App Sandbox
description: Comience a crear e implementar aplicaciones personalizadas en el entorno PlaidCloud Sandbox con los pasos de preparación y configuración.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## Qué es el Sandbox
PlaidCloud Sandbox permite implementar sus propias aplicaciones personalizadas con acceso local nativo a los datos y a las operaciones de PlaidCloud.  El entorno Sandbox ofrece un entorno de cómputo completo para crear aplicaciones personalizadas que amplíen su uso de PlaidCloud.

Todas las aplicaciones personalizadas se ejecutan mediante procesos de implementación de Kubernetes, por lo que es necesario tener conocimientos básicos de los objetos de Kubernetes.  Hay disponible un [ejemplo de Hello World](https://github.com/PlaidCloud/custom-app-template) que muestra cómo implementar una aplicación sencilla.

## Recursos disponibles
Las aplicaciones de Sandbox tienen un límite flexible de recursos, con la expectativa de que el uso de recursos no se abuse.  Podemos admitir grandes cantidades de cómputo si es necesario, pero hablemos antes de intentar implementar.  Póngase en contacto con nosotros si espera necesitar recursos significativos.

Las aplicaciones que se ejecutan en el Sandbox tendrán acceso directo al Lakehouse y a tantas bases de datos Postgres como desee.  Las bases de datos Postgres están diseñadas para manejar datos de tamaño moderado, por lo que son perfectas para almacenar configuraciones y otros metadatos.  Para el almacenamiento principal de datos, use el Lakehouse, ya que permite almacenar grandes cantidades de datos y mantener el rendimiento.

Todas las API de PlaidCloud también están disponibles directamente desde el Sandbox sin usar una URL pública, lo que ayuda a la velocidad de transferencia de datos.

## Requisitos de la imagen

Cualquier imagen que admita una implementación de Kubernetes basada en Docker es adecuada para una aplicación personalizada.  Actualmente solo se admiten imágenes basadas en *nix.  Si necesita ejecutar una imagen basada en Windows, póngase en contacto con nosotros.

## Integración con su canalización de CI/CD

La implementación de Kubernetes de la aplicación de Sandbox utiliza procesos de GitOps.  Esto le permite implementar su propio proceso de CI/CD para las compilaciones de imágenes y las implementaciones.  El repositorio git de su aplicación personalizada se supervisa constantemente en busca de cambios, de modo que, a medida que se hacen actualizaciones, su sandbox se actualizará.
