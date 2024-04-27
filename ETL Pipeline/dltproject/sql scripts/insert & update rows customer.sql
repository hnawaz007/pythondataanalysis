USE [AdventureWorksDW2019]
GO 
-----------------
SET IDENTITY_INSERT dbo.customer ON
insert into dbo.customer (
       [CustomerKey]
      ,[CustomerAlternateKey]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[EmailAddress]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[Phone]
      ,[DateFirstPurchase]
      ,[CommuteDistance]
)
SELECT top 11
       [CustomerKey]
      ,[CustomerAlternateKey]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[EmailAddress]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[Phone]
      ,[DateFirstPurchase]
      ,[CommuteDistance]
--into dbo.customer
  FROM [AdventureWorksDW2019].[dbo].[DimCustomer]
   where CustomerKey = 11010
order by [CustomerKey] ASC

SET IDENTITY_INSERT dbo.customer OFF

------------------
/****** Script for SelectTopNRows command from SSMS  ******/


  update dbo.customer
  set MiddleName = 'Von'
  where CustomerKey = 11002