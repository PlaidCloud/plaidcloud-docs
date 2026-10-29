---
title: Cambiar el idioma
description: Muestre PlaidCloud en English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 o 简体中文, y haga que su elección le acompañe en otros dispositivos.
sidebar:
  label: Cambiar el idioma
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/change-your-language.md
---

La interfaz de PlaidCloud está disponible en once idiomas:

| Idioma | Entrada del menú |
|---|---|
| Inglés (EE. UU.) | English (US) |
| Inglés (Reino Unido) | English (UK) |
| Alemán | Deutsch |
| Español | Español |
| Francés | Français |
| Portugués (Portugal) | Português (Portugal) |
| Portugués (Brasil) | Português (Brasil) |
| Polaco | Polski |
| Japonés | 日本語 |
| Coreano | 한국어 |
| Chino (simplificado) | 简体中文 |

Todos comienzan en inglés (EE. UU.). Nada cambia hasta que elija un idioma.

## Cambiar el idioma

1. En el encabezado superior, haga clic en el botón **Idioma**, junto al botón **Apariencia**. Su menú enumera cada idioma con su propio nombre, de modo que puede encontrar el suyo sea cual sea el idioma que se esté mostrando.
2. Elija un idioma.
3. Un mensaje confirma que PlaidCloud se volverá a cargar en ese idioma. Los cambios sin guardar se pierden, así que guarde primero su trabajo. Haga clic en **Recargar** para continuar o cancele para quedarse como está.

PlaidCloud guarda su elección en su perfil y se vuelve a cargar en el nuevo idioma. Para volver atrás, elija **English (US)** del mismo modo.

## Dónde se aplica su elección

- **Otros dispositivos y navegadores.** Su elección le acompaña. Si inicia sesión en el mismo espacio de trabajo desde otro dispositivo o navegador, se aplica desde la siguiente carga de página.
- **Por espacio de trabajo.** La elección pertenece a su perfil en un espacio de trabajo. Si usa varios espacios de trabajo, configure el idioma en cada uno.

## Números y fechas

Los números y las fechas se muestran en el formato del idioma que elija. En alemán, por ejemplo, mil doscientos treinta y cuatro y medio se muestra como `1.234,5`. En polaco, 1234567.89 se muestra como `1 234 567,89` y el 12 de octubre de 2026 como `12.10.2026`. El japonés y el chino muestran esa fecha como `2026/10/12`, y el coreano como `26. 10. 12.`. English (UK) usa la ortografía y los formatos británicos.

Solo cambia la visualización. Los valores que guarda, exporta o envía a integraciones conservan su formato habitual.

## Escribir en japonés, coreano y chino

Los métodos de entrada de japonés, coreano y chino funcionan en los campos numéricos y en otros campos que limitan lo que se puede escribir. Los dígitos de ancho completo se convierten a medida que escribe, de modo que `１２３` se convierte en `123`.

## Qué más sigue su idioma

El texto que PlaidCloud le envía desde el servidor también sigue su idioma, en todos los idiomas que ofrece PlaidCloud:

- **Correos electrónicos.** Los correos del sistema, como invitaciones, restablecimientos de contraseña, avisos de flujos de trabajo y migraciones, y los correos de registro, facturación y soporte.
- **Pantallas de inicio de sesión.** Las pantallas de inicio de sesión, de establecimiento de contraseña y de cierre de sesión, y los correos que Keycloak envía desde ellas.
- **Mensajes de error.** Los mensajes que PlaidCloud muestra cuando falla una solicitud, en la interfaz, a través de la API REST y a través de JSON-RPC.
- **PDF de documentación del proyecto.** El PDF que PlaidCloud genera para documentar un proyecto.

## Cómo elige PlaidCloud el idioma

| Dónde | Idioma que se usa |
|---|---|
| Dentro de PlaidCloud | El idioma que eligió con el botón **Idioma**. Su página de inicio de sesión y los correos siguen la misma elección. |
| Inicio de sesión y otras pantallas antes de iniciar sesión | El idioma de su navegador. |
| Registro | El idioma de su navegador. PlaidCloud lo almacena en su organización, y los correos de facturación y de cuenta dirigidos a la organización lo usan. |

Si su navegador o perfil usa un idioma que PlaidCloud no ofrece, el texto aparece en inglés (EE. UU.). Los navegadores configurados en chino tradicional (zh-TW o zh-HK) recurren al inglés (EE. UU.) para el texto del servidor.

## Qué permanece en inglés

- Los mensajes y registros de ejecución de flujos de trabajo y pasos, y el flujo de actividad. Muchas personas los leen, y mantenerlos en un solo idioma los hace fáciles de buscar y coherentes.
- El texto del asistente de IA y de las herramientas MCP.
- Los correos que escribe usted mismo, incluidas las plantillas de correo y los correos enviados por los pasos de informes.
- La documentación de OpenAPI.
- El texto de error de los motores de SQL y de expresiones.
- Las pantallas de registro.
- El contenido que usted crea, como los nombres de proyectos, tablas y pasos.
