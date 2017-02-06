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

Consider a query as a function mapping zero or more relations to a new relation,
and use the notation `Q(R1, R2, ...)` as the output of the query.

This allows as the write the following type of programs:

```
let R0 = Q0(....)
let T1 = R0
while not empty T1:
    let T2 = Q1(T1, ...)
    let T1 = T1 UNION T2
```
