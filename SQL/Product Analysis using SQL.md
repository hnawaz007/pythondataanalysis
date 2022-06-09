## Product Analysis using SQL

For database setup follow the stepts int following [video](https://www.youtube.com/watch?v=e5mvoKuV3xs&t)

## 1 - What is our Sales by Products?
Answer: Below query display Sales figures by Products.

SQL Query:
```sql 
Select
	p.EnglishProductName AS product_name,
	SUM(f.SalesAmount) AS sales_amount
from DimProduct p
inner join FactInternetSales f on p.ProductKey = f.ProductKey
Group By p.EnglishProductName
Order by SUM(f.SalesAmount) DESC
```

## 2 - What are our top 10 products by Sales?
Answer: Below query display Top 10 Products by Sales.

```sql
Select top 10 
	p.EnglishProductName AS product_name,
	SUM(f.SalesAmount) AS sales_amount
from DimProduct p
inner join FactInternetSales f on p.ProductKey = f.ProductKey
Group By p.EnglishProductName
Order by SUM(f.SalesAmount) DESC
```

## 3 - What are our top 10 products with lowest production cost?
Answer: Below query display Top 10 Products with lowest production cost.

```sql
--Products by Lowest Production Cost
Select top 10 
	p.EnglishProductName AS product_name,
	SUM(f.TotalProductCost) AS sales_amount
from DimProduct p
inner join FactInternetSales f on p.ProductKey = f.ProductKey
Group By p.EnglishProductName
Order by SUM(f.TotalProductCost) ASC
```

## 4 - How is our Prodcut categories are performing?
Answer: Below query showcases the categories performance.

```sql
Select 
	pc.EnglishProductCategoryName AS product_category,
        SUM(f.SalesAmount) AS total_sales
From DimProduct p
inner join DimProductSubcategory ps on p.ProductSubcategoryKey = ps.ProductSubcategoryKey
inner join DimProductCategory pc on ps.ProductCategoryKey = pc.ProductCategoryKey
inner join FactInternetSales f on f.ProductKey = p.ProductKey
Group by pc.EnglishProductCategoryName
Order by SUM(f.SalesAmount) DESC
```
