USE [AdventureWorksDW2019]
GO

/****** Object:  Trigger [dbo].[ModifiedDate]    Script Date: 4/24/2024 5:45:10 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[ModifiedDate]
    ON [dbo].[product]
    AFTER INSERT, UPDATE
AS
BEGIN
    UPDATE X 
    SET ModifiedDate = GETDATE()
    FROM dbo.product X
    JOIN inserted i ON X.ProductID = i.ProductID -- change to whatever key identifies 

END 
GO

ALTER TABLE [dbo].[product] ENABLE TRIGGER [ModifiedDate]
GO

