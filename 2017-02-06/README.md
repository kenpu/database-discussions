Features of POSTGRES
====================

## Set operations

- UNION
- UNION ALL
- INTERSECT
- INTERSECT ALL
- EXCEPT
- EXCEPT ALL

## Constants

- Scalar values

- Table values with:
    
```
values (<tuple>), ... AS R(c1,c2...)    
```

when used as a relation (say in a SELECT query), it must be assigned schema
information (namely, the attribute names)

> *Note*:
>
> Use single quote for strings in Postgresql

## Recursive queries

> *Note*: this is support in SQLite3 since version 3.8.

### Common table expression


```
WITH R(...) AS (
    SELECT
), R(...) AS (
    SELECT
)
QUERY
```

### Iteration with `RECURSIVE`

    WITH R(c1,c2,c3) AS (
        SELECT-QUERY without using R, call this Q0
        UNION
        SELECT-QUERY with using R, call this Q1
    )

This corresponds to the following pseudo code.

    var R0 Relation(c1,c2,c3) = empty
    var R1 Relation(c1,c2,c3) = empty
    var R2 Relation(c1,c2,c3)

    R0 = Q0()
    R1 = R0
    while R1 != empty:
        R2 = Q1(R1)
        R0 = R0 UNION R2
        R1 = R2

## A more intuitive interpretation

R[0] = Q0()
R[1] = Q1(R[0])
R[2] = Q1(R[1])
R[3] = Q1(R[2])
...
R[i] = Q1(R[i-1])

Stops when R[n] = empty.

RESULT of the recursive SQL = UNION(R[0], R[1], ...)
