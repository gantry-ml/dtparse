from .llms import make_model
from .prompts import GOOD_PROMPT, BAD_PROMPT

import gantry.dataset as gdataset
from gantry.llm import EvaluationRun


def test_model():
    model = make_model(BAD_PROMPT)
    dataset = gdataset.sync_dataset_data(
        "eval_set.json",
    )
    run = EvaluationRun(dataset)
    with run.start(tag="stable"):
        for input in run.inputs:
            model(**input)

    assert run.metrics["exact_match"] == 1.0
