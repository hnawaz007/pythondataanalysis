USE [AdventureWorksDW2019]
GO 

SELECT top 10
	   [ProductID]
      ,[Name]
      ,[ProductNumber]
      ,[FinishedGoodsFlag]
      ,[Color]
      ,[SafetyStockLevel]
      ,[ReorderPoint]
      ,[StandardCost]
      ,[ListPrice]
      ,[Size]
      ,[DaysToManufacture]
      ,[ProductSubcategoryID]
      ,dateadd(year,9,[SellStartDate]) AS [SellStartDate]
      ,dateadd(year,9,[SellEndDate]) AS [SellEndDate]
      ,dateadd(year,9,[ModifiedDate]) as ModifiedDate
into [AdventureWorksDW2019].dbo.product
  FROM [AdventureWorks2019].[Production].[Product]
  order by ProductID ASC


select * 
from [AdventureWorksDW2019].dbo.product

