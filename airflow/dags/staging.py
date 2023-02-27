import dagfactory
from airflow import DAG

dag_factory = dagfactory.DagFactory("/opt/airflow/factory/config_file.yml")
dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())

