from .llms import make_model
from .prompts import GOOD_PROMPT, BAD_PROMPT

import gantry.dataset as gdataset
from gantry.dataset_pytest_plugin.plugin import dataset_pytest_iter

# TODO: Change this to GOOD_PROMPT to make the test pass.
PROMPT = BAD_PROMPT

tag = "bug" if PROMPT == BAD_PROMPT else "fix"

gdataset._init()
dataset = gdataset.sync_dataset_data("evaluation_dataset.json")
eval_metrics = ["exact_match"]

model = make_model(PROMPT)


@dataset_pytest_iter(dataset, tag, eval_metrics)
def test_model(input, label, join_key, run):
    """
    A simple test to make sure the model is working as expected. The 
    test works as follows:

    1. Initialize the model with a prompt template.
    2. Load a dataset of test inputs from a json file. 
    3. Initialize a run with the dataset.
    4. Start the run. When we start the run, all OpenAI SDK calls
    will be tracked, and inputs & outputs will be logged locally.
    5. Iterate over the inputs and run the model on each input.
    6. Assert model predictions are as expected.
    """
    model_output = model(**input)

    # log run results
    run.log_output(model_output, join_key)
    run.log_metadata()

    # assert that the model output is as expected
    assert model_output.strip() == label
