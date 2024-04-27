 SELECT top 10
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
  into dbo.customer
FROM [AdventureWorksDW2019].[dbo].[DimCustomer]
order by [CustomerKey] ASC