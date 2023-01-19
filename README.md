# file_manage

## Problem
- Extract all names of `employees` file.
- For each name, get the amount time.
- Generate a csv file with the next headers:
```py
{
    'name_employee': <str>,
    'total_time': <int>,
    'payment': <float>,
}
```
> NOTE:
- `total_time` must be calculated in minutes
- `payment` is equal to `total_time * 2.4`