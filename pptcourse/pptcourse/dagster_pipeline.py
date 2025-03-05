from dagster import job, op
from pptcourse.api_clients import call_deepseek
from pptcourse.ppt_generator import create_ppt

@op
def fetch_content():
    """
    Fetches content using the DeepSeek API.
    """
    prompt = "Generate a summary about Artificial Intelligence in simple terms."
    return call_deepseek(prompt)

@op
def generate_ppt(content: str):
    """
    Generates a PowerPoint with fetched content.
    """
    create_ppt("AI Summary", content, "ai_summary.pptx")

@job
def ppt_generation_pipeline():
    """
    Dagster job that runs the pipeline.
    """
    content = fetch_content()
    generate_ppt(content)