# Q1: What is the start date and end date of the dataset?
```sql
SELECT MIN(trip_pickup_date_time), MAX(trip_pickup_date_time), FROM "trips"
```

# Q2: What proportion of trips are paid with credit card? (1 point)
```sql
with trips_cards as 
  (SELECT
  COUNT(*) as total_cards
  FROM "trips"
  WHERE payment_type = 'Credit'),
trips_all as (
  SELECT COUNT(*) as total_trips
  FROM "trips"
  )
SELECT total_cards/total_trips
FROM trips_cards, trips_all
```

# Q3: What is the total amount of money generated in tips? (1 point)

```sql
SELECT SUM(tip_amt)
FROM "trips"
```
