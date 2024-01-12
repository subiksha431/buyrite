insert into buyrite.store_user (store_user_guid, store_id, email, role, title, working_hours, hourly_rate, weekly_payment
,hire_date,termination_date)
select '5d3a2714-9d27-4fca-a6bb-1333fe1e1abc', 1, 'abc@gmail.com', 'Temp', 'abc', CURRENT_TIME,
 22, 40, CURRENT_DATE, CURRENT_DATE;
