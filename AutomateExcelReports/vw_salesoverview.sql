USE [AdventureWorks2012]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE view [Sales].[vw_salesoverview]
AS
 
SELECT 
	pc.Name as productcategory,
	s.Name productsubcategory,
	pr.[Name] as product,
	st.Name as saleterritory,
	[CountryRegion].Name as Country, 
	[Address].City,
	stat.Name Sate,
	ct.FirstName + SPACE(1) + ct.LastName AS Customer, 
	P.FirstName + SPACE(1) + P.LastName AS Employee, 
	COUNT(DET.SalesOrderID) AS OrderCount,
	OrderDate,
	pr.StandardCost,
	DET.UnitPrice,
	DET.UnitPriceDiscount,
	SUM(DET.UnitPrice * DET.OrderQty) * DET.UnitPriceDiscount as  Discount,
	ph.ListPrice,
	SUM(pr.StandardCost * DET.OrderQty) as SaleswithStandard,
	SUM(DET.LineTotal) - SUM(pr.StandardCost * DET.OrderQty) AS  NetSales, 
	SUM(DET.OrderQty) OrderQuantity,
	SUM(DET.LineTotal) AS Sales
FROM [Sales].[SalesPerson] SP 
	INNER JOIN [Sales].[SalesOrderHeader] SOH ON SP.[BusinessEntityID] = SOH.[SalesPersonID]
	INNER JOIN Sales.SalesOrderDetail DET ON SOH.SalesOrderID = DET.SalesOrderID
	INNER JOIN [Person].[Person] P ON P.[BusinessEntityID] = SP.[BusinessEntityID]
	Left join [Production].[Product] pr on DET.ProductID = pr.ProductID and OrderDate between pr.SellStartDate and ISNULL(pr.SellEndDate, '9999-12-31')
	left join  [Production].[ProductSubcategory] s on pr.ProductSubcategoryID = s.ProductSubcategoryID
	left join  [Production].[ProductCategory] pc on s.ProductCategoryID = pc.ProductCategoryID
	left Join Sales.Customer c on SOH.CustomerID = c.CustomerID
	left join Sales.SalesTerritory st on SOH.TerritoryID = st.TerritoryID
	INNER JOIN [Person].[Person] ct ON c.PersonID = ct.BusinessEntityID
	left join [Person].[Address] on [Address].[AddressID] = SOH.BillToAddressID
	left join Person.StateProvince stat on stat.StateProvinceID = Address.StateProvinceID
	left join [Person].[CountryRegion] on [CountryRegion].[CountryRegionCode] = st.CountryRegionCode
	left join [Production].[ProductCostHistory] ch on ch.ProductID = DET.ProductID and OrderDate between ch.StartDate and ch.EndDate
	left join [Production].[ProductListPriceHistory] ph on ph.ProductID = DET.ProductID and OrderDate between ph.StartDate and ISNULL(ph.EndDate, '9999-12-31')

GROUP BY 
	P.FirstName + SPACE(1) + P.LastName, 
	SOH.SalesPersonID, 
	OrderDate,
	pr.[Name] ,
	pc.Name ,
	s.Name ,
	st.Name ,
	ct.FirstName + SPACE(1) + ct.LastName ,
	[Address].City,
	stat.Name,
	[CountryRegion].Name,
	pr.ListPrice,
	pr.StandardCost,
	DET.UnitPrice,
	DET.UnitPriceDiscount,
	ph.ListPrice

GO


