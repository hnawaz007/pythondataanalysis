create table if not exists stg_denormalized_products as (
    SELECT 
      ps."EnglishProductSubcategoryName" AS ProductSubcategoryName
      ,pc."EnglishProductCategoryName" AS ProductCategoryName
      ,p."ProductKey"
      ,p."EnglishProductName" AS Product_Name
      ,p."ProductLine"
      ,p."FinishedGoodsFlag"
      ,p."Color"
      ,p."SafetyStockLevel"
      ,p."ReorderPoint"
      ,p."StandardCost"
      ,p."ListPrice"
      ,p."Size"
      ,p."SizeUnitMeasureCode"
      ,p."WeightUnitMeasureCode"
      ,p."Weight"
      ,p."DaysToManufacture"
      ,p."Class"
      ,p."Style"
      ,p."ModelName"
      ,p."StartDate"
      ,p."EndDate"
      ,p."Status"
  FROM public.stg_products p
  left join public.stg_productsubcategory ps on p."ProductSubcategoryKey" = ps."ProductSubcategoryKey"
  left join public.stg_productcategory pc on ps."ProductCategoryKey" = pc."ProductCategoryKey"
) 