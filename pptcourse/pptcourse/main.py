from pptcourse.dagster_pipeline import ppt_generation_pipeline

def run_pipeline():
    """
    Runs the pipeline manually (without Dagster UI).
    """
    ppt_generation_pipeline.execute_in_process()

if __name__ == "__main__":
    run_pipeline()