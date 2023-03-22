
training_data = [
    {
        "request": "tomorrow at 3pm",
        "current date": "2020-01-01",
        "current time": "12:00:00",
        "label": "2020-01-02 15:00:00",
    },
    {
        "request": "last saturday",
        "current date": "2017-02-19",
        "current time": "15:54:30",
        "label": "2023-02-12 12:00:00",
    },
    {
        "request": "next year",
        "current date": "2023-02-19",
        "current time": "15:54:30",
        "label": "2024-01-01 12:00:00",
    },
    {
        "request": "one year from today",
        "current date": "2023-02-19",
        "current time": "15:54:30",
        "label": "2024-02-19 12:00:00",
    },
    {
        "request": "april 11 at 8pm",
        "current date": "2023-02-19",
        "current time": "15:54:30",
        "label": "2023-04-11 20:00:00",
    },
    {
        "request": "last march 1st",
        "current date": "2023-01-11",
        "current time": "02:23:11",
        "label": "2022-03-01 12:00:00",
    }
]

BAD_PROMPT = """
You are a calendar. Users will submit you a request in natural language. You will return a date and time in the format "YYYY-MM-DD HH:MM:SS" that corresponds to the date and time the user would like to see.

If the request does not specify a year, assume that the year is the current year.
If the request does not specify a month, assume that the month is the current month.
If the request does not specify a day, assume that the day is the current day.
If the request does not specify a time, assume that the time is 00:00:00.

Begin.

"""

context = "\n".join([
    f"request: {d['request']}\ncurrent date: {d['current date']}\ncurrent time: {d['current time']}\nresponse: {d['label']}\n" 
    for d in training_data])

answer_format = """
request: "{request}"
current date: {date}
current time: {time}
response:"""

BAD_PROMPT += context
BAD_PROMPT += answer_format

GOOD_PROMPT = """
You are a calendar. Users will submit you a request in natural language. 
You will return a date and time in the format "YYYY-MM-DD HH:MM:SS" that corresponds to the date and time the user would like to see.

Here are examples of a submission:


request: "noon Sunday",
current date: 2023-02-23,
current time: 15:54:30,
response: 2023-02-26 12:00:00

request: "noon Sunday",
current date: 2023-03-16,
current time: 15:54:30,
response: 2023-03-19 12:00:00

request: "noon last Sunday",
current date: 2023-02-23,
current time: 15:54:30,
response: 2023-02-19 12:00:00

"""


GOOD_PROMPT += """

Begin.
"""

GOOD_PROMPT += answer_format