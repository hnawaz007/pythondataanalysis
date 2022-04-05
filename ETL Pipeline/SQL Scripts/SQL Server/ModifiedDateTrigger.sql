use AdventureWorksDW2019
Go
 CREATE TRIGGER dbo.updateDate
ON [dbo].[customers]
AFTER  UPDATE 
AS UPDATE [dbo].[customers] SET Modified_at = CURRENT_TIMESTAMP
      FROM [dbo].[customers] t
	    INNER JOIN inserted i
		  ON t.customerId = i.customerId
GO