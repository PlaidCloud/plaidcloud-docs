---
title: SAP S/4HANA Connector
description: SAP S/4HANA connects to PlaidCloud through the shared SAP ECC / S/4HANA RFC connection — see the combined connector reference for its configuration fields.
sidebar:
  order: 1
---

S/4HANA does not have a connector of its own. It shares one connection type with SAP ECC, because PlaidCloud reaches both through the same Remote Function Call interface. In the **Connections** screen, choose **New → SAP ECC / S/4HANA Instance**.

**[SAP ECC and S/4HANA Connector →](/reference/connectors/erp/sap-ecc/)** — every configuration field, for both generations.

## Upstream Documentation

See the [SAP S/4HANA documentation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE).

## Related

- [SAP workflow steps](/reference/workflow-steps/sap/) — the steps that run against this connection.
- [SAP Analytics Cloud (SAC)](/reference/connectors/erp/sap-sac/), [SAP PaPM](/reference/connectors/erp/sap-papm/), and [SAP PCM](/reference/connectors/erp/sap-pcm/) are separate connectors with their own configuration.
