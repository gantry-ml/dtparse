from .llms import make_model
from .prompts import GOOD_PROMPT, BAD_PROMPT

import gantry.dataset as gdataset
from gantry.llm import EvaluationRun

# TODO: Change this to GOOD_PROMPT to see the test pass.
PROMPT = BAD_PROMPT

tag = "bug" if PROMPT == BAD_PROMPT else "fix"


def test_model():
    """
    A simple test to make sure the model is working as expected. The 
    test works as follows:
    
    1. Initialize the model with a prompt template.
    2. Load a dataset of test inputs from a json file. 
    3. Initialize a run with the dataset.
    4. Start the run. When we start the run, all OpenAI SDK calls
    will be tracked, and inputs & outputs will be logged locally.
    5. Iterate over the inputs and run the model on each input.
    6. Assert that the run metrics are as expected.
    """
    model = make_model(PROMPT)
    dataset = gdataset.sync_dataset_data(
        "eval_set.json",
    )
    run = EvaluationRun(dataset)
    with run.start(tag=tag):
        for input in run.inputs:
            model(**input)

    assert run.metrics["exact_match"] == 1.0
