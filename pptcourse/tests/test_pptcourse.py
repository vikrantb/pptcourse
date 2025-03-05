import pytest
from pptcourse.api_clients import call_deepseek
from pptcourse.ppt_generator import create_ppt
from pptcourse.dagster_pipeline import ppt_generation_pipeline

def test_api_response():
    response = call_deepseek("What is AI?")
    assert isinstance(response, str), "API did not return a string"

def test_ppt_generation():
    try:
        create_ppt("Test Slide", "This is a test slide.", "test.pptx")
        assert True  # If no error, the test passes
    except Exception as e:
        assert False, f"PowerPoint generation failed: {e}"

def test_pipeline_execution():
    try:
        ppt_generation_pipeline.execute_in_process()
        assert True
    except Exception as e:
        assert False, f"Dagster pipeline execution failed: {e}"