---
linktitle: Date and Time
title: Date and Time
description: Basic date functions like current-date, now, and timeofday
weight: 12.0
---

Dates and times can cause some additional mental gymnastics at times due to timezones, offsets, varying days and weeks within months, and more.  While we can't solve the problem of how we measure and track time, there are a few ways to extract and manipulate date and time related data.

## Extracting the week from a date

This will extract the week in the `MON-DD` format:

```python
func.to_char(
    func.date_trunc('week', ((table.Date) - 6)),
    'MON-DD'
)
```

The example above assumes you have a date field in your data called `Date`.  In this example, we are subtracting six days from that date but that may not be necessary in your specific use case.  It is shown here to help if you do need to add or subtract days.

This uses the [to_char](https://www.postgresql.org/docs/13/functions-formatting.html) and the [date_trunc](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC) methods.

