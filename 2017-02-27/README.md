Advanced SELECT SQL queries
==========================

We will analyse the mycampus database and Starbucks store location database

Here are the schema of the databases

- _mycampus_

    CREATE TABLE schedule (
                semester    VARCHAR(10),
                title       VARCHAR(100),
                crn         VARCHAR(30),
                code        VARCHAR(30),
                levels      VARCHAR(100),
                credits     FLOAT,
                campus      VARCHAR(50),
                section     INTEGER,
                capacity    INTEGER,
                actual      INTEGER,
                type        VARCHAR(30),
                starthour   INTEGER,
                startmin    INTEGER,
                endhour     INTEGER,
                endmin      INTEGER,
                weekday     VARCHAR(10),
                room        VARCHAR(50),
                datestart   VARCHAR(50),
                dateend     VARCHAR(50),
                schtype     VARCHAR(30),
                instructor  VARCHAR(100),
                prereq      VARCHAR(100),
                coreq       VARCHAR(100))

- _starbucks_

    CREATE TABLE stores (
        Brand text,
        Store_Number text,
        Store_Name text,
        Ownership_Type text,
        Street_Address text,
        City text,
        State_Province text,
        Country text,
        Postcode text,
        Phone_Number text,
        Timezone text,
        Longitude float,
        Latitude float);

    CREATE TABLE countries (
        ID text,
        Common_Name text,
        Formal_Name text,
        Type text,
        Subtype text,
        Sovereignty text,
        Capital text,
        Currency_Code text,
        Currentcy_Name text,
        Tel_Code text,
        Letter_Code text,
        Letter_Code3 text,
        Number text,
        Internet_Code text);

## Aggregation

- Tabulating the number of lectures / tutorials / labs
  over the different days of the week

- Use common table expressions to define _temporary_ views for modular
  query construction.

- Use outer join types to ensure that no tuples are lost during join.

- Use CASE WHEN to convert NULL values to 0.  Must use ISNULL to check of
  a value is NULL due to the 3-value logic of SQL.

## Subqueries

- Instructors who teach at least one large (> 100)course every semester since 2015.

- Instructors who only teach BUSI courses.

## Indexes

- For previous query, nested subquery solution requires (n^2) table scan if no indexes are created.

- With `CREATE INDEX .... ON schedule(instructor, actual)`, one can improve the query performance
  to (nlogn).

Next Week
=========================

- Working on starbucks database

    - What is the most isolated starbucks in Toronto?
    - What is the most isolated starbucks in the world?

- ...
