---
title: 'Aggregate Functions'
---

Aggregate functions are essential tools in SQL that allow you to perform calculations on a set of values and return a single result.

These functions help you extract and summarize data from databases to gain valuable insights. 

| Function Name                                                    | What It Does                                                                 | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Checks if any row meets the specified condition                              | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Estimates the number of distinct values with HyperLogLog                     | 
| [ARG_MAX](aggregate-arg-max)                                     | Finds the arg value for the maximum val value                                | 
| [ARG_MIN](aggregate-arg-min)                                     | Finds the arg value for the minimum val value                                | 
| [AVG_IF](aggregate-avg-if)                                       | Calculates the average for rows meeting a condition                          | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Converts all the values of a column to an Array                              |
| [AVG](aggregate-avg)                                             | Calculates the average value of a specific column                            | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Counts the number of distinct values in a column                             | 
| [COUNT_IF](aggregate-count-if)                                   | Counts rows meeting a specified condition                                    | 
| [COUNT](aggregate-count)                                         | Counts the number of rows that meet certain criteria                         | 
| [COVAR_POP](aggregate-covar-pop)                                 | Returns the population covariance of a set of number pairs                   | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Returns the sample covariance of a set of number pairs                       | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Returns an array with elements calculates the moving average of input values |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Returns an array with elements calculates the moving sum of input values     |
| [KURTOSIS](aggregate-kurtosis)                                   | Calculates the excess kurtosis of a set of values                            | 
| [MAX_IF](aggregate-max-if)                                       | Finds the maximum value for rows meeting a condition                         | 
| [MAX](aggregate-max)                                             | Finds the largest value in a specific column                                 | 
| [MEDIAN](aggregate-median)                                       | Calculates the median value of a specific column                             | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Calculates the median value of a specific column using t-digest algorithm    | 
| [MIN_IF](aggregate-min-if)                                       | Finds the minimum value for rows meeting a condition                         | 
| [MIN](aggregate-min)                                             | Finds the smallest value in a specific column                                | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Calculates the interpolated quantile for a specific column                   |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Calculates the quantile for a specific column                                | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Calculates the quantile using t-digest algorithm                             |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Calculates the quantile with weighted using t-digest algorithm               |
| [RETENTION](aggregate-retention)                                 | Calculates retention for a set of events                                     | 
| [SKEWNESS](aggregate-skewness)                                   | Calculates the skewness of a set of values                                   | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Calculates the population standard deviation of a column                     | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Calculates the sample standard deviation of a column                         | 
| [STRING_AGG](aggregate-string-agg)                               | Converts all the non-NULL values to String, separated by the delimiter       |
| [SUM_IF](aggregate-sum-if)                                       | Adds up the values meeting a condition of a specific column                  | 
| [SUM](aggregate-sum)                                             | Adds up the values of a specific column                                      | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analyzes user behavior in a time-ordered sequence of events                  | 
