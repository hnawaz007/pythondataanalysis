use AdventureWorksDW2019
Go
--insert
INSERT [dbo].[customers] ( [customername], [customertype], [entrydate], [created_at], [modified_at]) 
VALUES ( N'Pam Halpert', N'Individual', getdate(), getdate(), getdate()),
       ( N'Stanely Hudson', N'Individual', getdate(), getdate(), getdate())

--update
update dbo.customers
set [customertype] = 'Corporate'
where customerId = 3