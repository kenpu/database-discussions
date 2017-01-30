# Transactions

## ACID property

- Atomicity

    > Supported by SQLite

- Consistency

- Integrity

    > Supported by SQLite

- Durability

> Supporting all of them is impossibly costly.

It's up to the user to decide which one to give up.

## Transaction isolation level

- Full isolation = `SERIALIZABLE`

- No isolation = `READ UNCOMMITTED`


