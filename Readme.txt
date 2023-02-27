Solution contains following directory:
|-airflow
  - dags (dag folder)
  - factory (path to dag factory yml)
  - scripts (path to python scripts for the assignment)
  - docker-compose.yaml (configuration for docker compose)
  - .env (environment variable for Airflow)
|-msql
  - data (directory to store json file from the api)
  
commands to run code
1. run `docker compose up` to deploy Airflow and Mysql server
2. update ip address for mysql server in airflow/factory/config_file.yml
3. Run the RTL DAG
4. check data in mysql `select * from unwrapper`

Considerations:
1. Since data granularity is daily (1 record per day), I am overwriting the files/tables daily
2. use of python operator for Airflow using python callables files in scripts folder
3. Mysql password not saved in Airflow secrets
4. Airflow schedule is daily to get exchange rate everyday
5. use of JSON_EXTRACT of mysql to read data using schema for example `select JSON_EXTRACT(data_col, '$.structure.dimensions.observation[0].values[*].name') from ingeston;`
6. three tasks for 
	1. ecb_api (to get json data from GET request)
	2. ingestion (to load json into ingestion table using json column)
	3. unwrapper (unwrap data from ingestion table using input schema and load into unwrapper table)
7. mysql server configs added to docker-compose.yaml provided by Apache Airflow
8. schema for final table (unwrapper) is [('value_recorded', 'float'), ('date_modify', 'string'), ('hash_id', 'string')]
	value_recorded - exchange rate value
	date_modify - date of the recorded value
9. update host address of mysql in dag factory


