CREATE OR REPLACE VIEW retail.forecast_view as (
SELECT
 date(DATE_TRUNC(PARSE_DATETIME('%D %H:%M',datetime_id),DAY)) as date,
 product_id as product,
 sum(quantity) as history_value,
 NULL as forecast_value
from retail.fct_invoices
group by
 date,product
UNION ALL
SELECT date(DATE_TRUNC(forecast_timestamp,day)) as date,
 product,
 NULL as history_value,
 forecast_value
 FROM ML.FORECAST(MODEL retail.forcast_by_product, struct(30 AS horizon))
ORDER BY date
)
