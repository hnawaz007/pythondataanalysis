USE [AdventureWorksDW2019]
GO 
-----------------
SET IDENTITY_INSERT dbo.product ON
insert into dbo.product
 (	   [ProductID]
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
      ,[SellStartDate]
      ,[SellEndDate])
SELECT 
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
FROM [AdventureWorks2019].Production.product
where [ProductID] = 322

SET IDENTITY_INSERT dbo.product OFF

------
  update [AdventureWorksDW2019].dbo.product
  set Color = 'Black'
  where ProductID = 1

  select * from [AdventureWorksDW2019].dbo.product
  order by ModifiedDate DESC

