import openai
from typing import Optional, List, Union, Dict
from string import Formatter
from datetime import datetime, date
from dataclasses import dataclass, asdict
import gantry

PROMPT = """
You are a calendar. Users will submit you a request in natural language. You will return a date and time in the format "YYYY-MM-DD HH:MM:SS" that corresponds to the date and time the user would like to see.

If the request does not specify a year, assume that the year is the current year.
If the request does not specify a month, assume that the month is the current month.
If the request does not specify a day, assume that the day is the current day.
If the request does not specify a time, assume that the time is 12:00:00.

Begin.

request: "tomorrow at 3pm"
current date: 2020-01-01
current time: 12:00:00
response: 2020-01-02 15:00:00

request: "last saturday"
current date: 2023-02-19
current time: 15:54:30
response: 2023-02-12 12:00:00

request: "next year"
current date: 2023-02-19
current time: 15:54:30
response: 2024-01-01 12:00:00

request: "one year from today"
current date: 2023-02-19
current time: 15:54:30
response: 2024-02-19 12:00:00

request: "april 11 at 8pm"
current date: 2023-02-19
current time: 15:54:30
response: 2023-04-11 20:00:00

request: "last march 1st"
current date: 2023-01-11
current time: 02:23:11
response: 2022-03-01 12:00:00

request: "{request}"
current date: {date}
current time: {time}
response:"""

@dataclass
class OpenAI:
    model: str = "davinci"
    # suffix: Optional[str] = None
    max_tokens: int = 16
    temperature: float = 1.0
    top_p: float = 1.0
    n: int = 1
    stream: bool = False
    # logprobs: Optional[int] = None
    echo: bool = False
    # stop: Optional[Union[str, List[str]]] = None
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    best_of: int = 1
    # logit_bias: Optional[Dict[str, float]] = None
    # user: Optional[str] = None

    def complete(self, prompt: str, **kwargs) -> openai.Completion:
        return openai.Completion.create(prompt=prompt, **asdict(self), **kwargs)

class GantryCallback:
    def __init__(self, app_name: str):
        self.app_name = app_name
        gantry.init()
    
    def __call__(self, prompt: str, args: tuple, kwargs: dict, completion: openai.Completion, llm, model_id):
        inputs = kwargs
        for i, arg in enumerate(args):
            inputs[f"_arg{i}"] = arg
        outputs = {"completion": completion.choices[0].text}
        tags = {
            "prompt": prompt, 
            "openai_id": completion["id"],
            "openai_usage_prompt_tokens": completion["usage"].get("prompt_tokens"),
            "openai_usage_completion_tokens": completion["usage"].get("completion_tokens"),
            "openai_usage_total_tokens": completion["usage"].get("total_tokens"),
            "model_id": model_id,
            **asdict(llm)
        }
        # Get around tags needing to be strings
        tags = {k: str(v) for k, v in tags.items()}
        gantry.log_record(
            self.app_name,
            inputs=inputs,
            outputs=outputs,
            tags=tags,
        )

def model(prompt, llm=OpenAI(temperature=0), callbacks=[GantryCallback("dtparse")]):
    def func(*args, **kwargs):
        inputs = prompt.format(*args, **kwargs)
        completion = llm.complete(inputs, stop="\n")
        model_metadata = asdict(llm)
        model_metadata.update({"prompt": prompt})
        model_id=hash(frozenset(model_metadata.items()))
        for callback in callbacks:
            callback(prompt=prompt, args=args, kwargs=kwargs, completion=completion, llm=llm, model_id=model_id)
        return completion.choices[0].text
    return func

m = model(PROMPT)

dtparse = lambda req: m(date=str(date.today()), time=datetime.now().strftime("%H:%M:%S"), request=req)

def main():
    for req in ["tomorrow at 3pm", "next saturday", "the day after tomorrow", "monday morning", "the second sunday of next month"]:
        print(f"{req} -> {dtparse(req)}")

if __name__ == '__main__':
    main()
