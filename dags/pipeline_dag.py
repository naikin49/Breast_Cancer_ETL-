from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.load_data import load_data
from etl.preprocess import preprocess_data
from etl.train_model import train_model
from etl.evaluate import evaluate_model
from etl.save_results import save_all

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    dag_id='medical_etl_pipeline',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
) as dag:

    def step_load():
        global df
        df = load_data("data.csv")

    def step_preprocess():
        global X, y
        X, y = preprocess_data(df)

    def step_train():
        global model
        model = train_model(X, y)

    def step_evaluate():
        global metrics
        metrics = evaluate_model(model, X, y)

    def step_save():
        save_all(model, metrics)

    t1 = PythonOperator(task_id="load", python_callable=step_load)
    t2 = PythonOperator(task_id="preprocess", python_callable=step_preprocess)
    t3 = PythonOperator(task_id="train", python_callable=step_train)
    t4 = PythonOperator(task_id="evaluate", python_callable=step_evaluate)
    t5 = PythonOperator(task_id="save", python_callable=step_save)

    t1 >> t2 >> t3 >> t4 >> t5
