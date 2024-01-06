CREATE OR REPLACE MODEL
 retail.forcast_by_product
OPTIONS(
 MODEL_TYPE='ARIMA',
 TIME_SERIES_TIMESTAMP_COL='inv_date',
 TIME_SERIES_DATA_COL='total_amount',
 TIME_SERIES_ID_COL='product',
 HOLIDAY_REGION='GLOBAL'
)
AS
SELECT
 DATE_TRUNC(PARSE_DATETIME('%D %H:%M',datetime_id),DAY) as inv_date,
 product_id as product,
 sum(quantity) as total_amount
from retail.fct_invoices
group by
 inv_date,product
having
 inv_date between DATE('2010-12-01') and DATE('2011-08-31')