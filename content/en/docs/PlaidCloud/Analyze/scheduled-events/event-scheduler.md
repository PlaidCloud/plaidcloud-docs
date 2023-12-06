---
title: Event Scheduler
slug: event-scheduler
description: Create and organize a scheduled recurring event
date: 2022-01-25T07:39:49
---


## Description


Scheduling specific workflows can be a useful organization tool, so PlaidCloud provides the ability to do just that. Using event scheduler, you can schedule a workflow to run by month, day, hour, minute, or even on a financial workday schedule. If using the financial workday schedule approach, PlaidCloud also allows configuration of holiday schedules using various holiday calendars.



The Events Table will indicate whether the event is scheduled by month, day, hour and minute, or workday under the event description column.



**To view events:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”

This will open the **Events Table** showing all the current events configured for the workspace.

{{< note >}}
If the event is active, the “Active” icon will be displayed. 
{{< /note >}}


## Creating an Event


**To create an event:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”
4. Click “Add Scheduled Event”
5. Complete the required fields
6. Click “create”

**Limit Running**: this section allows you to schedule an event to run for a specific time period and a specific number of times.



Otherwise, you can set the workflow to run using the **classic schedule** approach.



**To use the classic schedule approach:**


1. Click the “Event Schedule” tab of the Event table
2. Under the “Schedule type” select “Use Classic Schedule”
3. Select the specific months, hours, minutes, and days you want the workflow to run

**To set the workflow to run using the workday schedule approach:**


1. Click the “Event Schedule” tab of the Event table
2. Under the “Schedule type” select “Use Workday Schedule”
3. Choose the workday you would like the workflow to run on

{{< note >}}
By default, the timezone for events is set to UTC but can be adjusted using the “Timezone” field.
{{< /note >}}


## Editing an Event


**To edit an event:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”
4. Click the edit icon
5. Adjust desired fields
6. Click “Update”

## Deleting an Event


**To delete an event:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”
4. Click the delete icon
5. Click delete again

## Pausing an Event


**To temporarily pause an event:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”
4. Click the edit icon
5. Uncheck the “Active” checkbox
6. Click “Update”

Saving the event after unchecking the active box means the event will no longer run on the specified schedule until it’s reactivated.



## Running Events on Demand


**To run an event immediately:**


1. Open Analyze
2. Select “Tools”
3. Click “Event Scheduler”
4. Select the desired event or events
5. Click “Run Selected Events”
