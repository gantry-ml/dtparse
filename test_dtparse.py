from .llms import make_model
from .prompts import GOOD_PROMPT, BAD_PROMPT

import gantry.dataset as gdataset
from gantry.dataset_pytest_plugin.plugin import dataset_pytest_iter

# TODO: Change this to GOOD_PROMPT to make the test pass.
PROMPT = BAD_PROMPT

tag = "bug" if PROMPT == BAD_PROMPT else "fix"

# Initialize the dataset of test inputs 
# from a json file. The test will iterate
# over the dataset and run the model on each input.
gdataset._init()
dataset = gdataset.sync_dataset_data("evaluation_dataset.json")
# Specify the metrics we want to track
eval_metrics = ["exact_match"]

model = make_model(PROMPT)


@dataset_pytest_iter(dataset, tag, eval_metrics)
def test_model(input, label, join_key, run):
    """
    A simple test to make sure the model is working as expected. The 
    test will iterate over a dataset of inputs and labels, and assert
    that the model output is as expected. In addition, all OpenAI SDK
    calls that happen in application code will be tracked, and the test
    run information will be logged locally. 
    """
    model_output = model(**input)

    # log run results
    run.log_output(model_output, join_key)
    run.log_metadata()

    # assert that the model output is as expected
    assert model_output.strip() == label
