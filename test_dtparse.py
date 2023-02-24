

eval_data = [
	{	
        "request": "today",
        "date": "2010-07-13",
        "time": "16:30:10",
        "label": "2010-07-13 00:00:00"
    },
	{
        "request": "tomorrow",
        "date": "2011-01-20",
        "time": "08:01:50",
        "label": "2004-03-21 00:00:00"
    },
	{
        "request": "yesterday",
        "date": "2012-04-11",
        "time": "23:53:17",
        "label": "2017-11-10 00:00:00"
    },
	{
        "request": "in a couple of days",
        "date": "2013-02-02",
        "time": "12:05:03",
        "label": "2022-02-04 00:00:00"
    },
	{
        "request": "a couple of days from now",
        "date": "2014-08-18",
        "time": "02:15:15",
        "label": "2014-08-20 02:15:15"
    },
	{
        "request": "a couple of days from today",
        "date": "2015-05-22",
        "time": "12:37:00",
        "label": "2015-05-24 00:00:00"
    },
	{
        "request": "in a day",
        "date": "2016-03-13",
        "time": "14:21:41",
        "label": "2016-03-14 00:00:00"
    },
	{
        "request": "3 days ago",
        "date": "2017-06-25",
        "time": "12:00:00",
        "label": "2017-06-22 00:00:00"
    },
	{
        "request": "3 days from now",
        "date": "2018-09-19",
        "time": "09:47:14",
        "label": "2018-09-22 09:47:14"
    },
	{
        "request": "a day ago",
        "date": "2019-02-01",
        "time": "13:30:00",
        "label": "2019-01-31 00:00:00"
    },
	{
        "request": "now",
        "date": "2020-01-11",
        "time": "17:29:21",
        "label": "2020-01-11 17:29:21"
    },
	{
        "request": "10 minutes ago",
        "date": "2021-07-01",
        "time": "00:05:00",
        "label": "2021-06-30 23:55:00"
    },
	{
        "request": "10 minutes from now",
        "date": "2022-04-23",
        "time": "13:30:13",
        "label": "2022-04-23 13:40:13"
    },
	{
        "request": "in 10 minutes",
        "date": "2023-01-16",
        "time": "15:57:03",
        "label": "2023-01-16 16:07:03"
    },
	{
        "request": "in a minute",
        "date": "2024-12-31",
        "time": "23:59:30",
        "label": "2025-01-01 00:00:30"
    },
	{
        "request": "in a couple of minutes",
        "date": "2025-08-24",
        "time": "12:00:00",
        "label": "2025-08-24 12:02:00"
    },
	{
        "request": "20 seconds ago",
        "date": "2023-02-23",
        "time": "22:05:31",
        "label": "2023-02-23 22:05:11"
    },
	{
        "request": "in 30 seconds",
        "date": "2021-05-02",
        "time": "04:00:00",
        "label": "2020-01-01 12:00:00"
    },
	{
        "request": "20 seconds before noon",
        "date": "2019-11-11",
        "time": "22:40:13",
        "label": "2019-11-11 11:59:40"
    },
	{
        "request": "20 seconds before noon tomorrow",
        "date": "2017-10-01",
        "time": "14:19:49",
        "label": "2017-10-02 11:59:40"
    },
	{
        "request": "noon",
        "date": "2015-01-30",
        "time": "00:59:50",
        "label": "2015-01-30 12:00:00"
    },
	{
        "request": "midnight",
        "date": "2013-02-20",
        "time": "01:58:40",
        "label": "2013-02-21 00:00:00"
    },
	{
        "request": "noon tomorrow",
        "date": "2011-03-29",
        "time": "02:57:30",
        "label": "2011-03-30 12:00:00"
    },
	{
        "request": "6am tomorrow",
        "date": "2013-04-28",
        "time": "03:56:20",
        "label": "2013-04-29 06:00:00"
    },
	{
        "request": "0800 yesterday",
        "date": "2015-05-27",
        "time": "04:55:10",
        "label": "2015-05-26 08:00:00"
    },
	{
        "request": "12:15 AM today",
        "date": "2017-06-26",
        "time": "05:54:00",
        "label": "2017-06-26 00:15:00"
    },
	{
        "request": "3pm 2 days from today",
        "date": "2019-07-25",
        "time": "06:53:55",
        "label": "2019-07-07 15:00:00"
    },
	{
        "request": "a week from today",
        "date": "2021-08-24",
        "time": "07:52:45",
        "label": "2021-08-31 00:00:00"
    },
	{
        "request": "a week from now",
        "date": "2023-09-23",
        "time": "08:41:35",
        "label": "2023-09-30 08:41:35"
    },
	{
        "request": "3 weeks ago",
        "date": "2022-10-22",
        "time": "09:50:25",
        "label": "2022-10-01 00:00:00"
    },
	{
        "request": "noon next Sunday",
        "date": "2023-02-23",
        "time": "10:49:15",
        "label": "2023-03-05 12:00:00"
    },
	{
        "request": "noon Sunday",
        "date": "2023-02-23",
        "time": "11:48:05",
        "label": "2023-02-30 12:00:00"
    },
	{
        "request": "noon last Sunday",
        "date": "2023-02-23",
        "time": "12:47:57",
        "label": "2023-02-19 12:00:00"
    },
]

import pytest
from .llms import make_model
from .prompts import PROMPT

model = make_model(PROMPT)

@pytest.mark.parametrize("example", eval_data)
def test_model(example):
    result = model(**example)
    assert result == example["label"]
