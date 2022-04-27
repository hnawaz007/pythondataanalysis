--On average, how many orders do we receive per day? Plus, what's our average sales per day?
with avg_sales_per_day as (
	select OrderDate, 
		   count(distinct SalesOrderNumber) as order_count,
			sum(SalesAmount) as Sales
    from  [dbo].[FactInternetSales]
    group by OrderDate
)

select 
   avg(Sales) as avg_sales_day,
   avg(order_count) avg_order_count
from avg_sales_per_day
