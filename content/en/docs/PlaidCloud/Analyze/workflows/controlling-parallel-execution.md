---
title: Controlling Parallel Execution
slug: controlling-parallel-execution
weight: 13.0
description: How to control serial versus parallel execution of steps in a workflow
date: 2022-01-25T07:40:20
---


Workflows in PlaidCloud can be executed as a combination of serial steps and parallel operations. To set a group of steps to run in parallel, place the steps in a group within the workflow hierarchy. Right click on the group folder and select the **Execute in Parallel** option. This will allow all the steps in the group to trigger simultaneously and execute in parallel. Once all steps in the group complete, the next step or group in the workflow after the group will activate.

