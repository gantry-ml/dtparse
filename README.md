## DTParse

DTParse is an application that takes in natural language queries like "noon last Sunday" along with the current date and time and returns a corresponding timestamp. For example, if the current date is March 21st and time is 1:17 PM, and the query is "noon last Sunday", the application will return "2023-03-19 12:00:00". The application uses GPT-3 and the OpenAI SDK under the hood.

The application can handle a wide range of natural language queries, including relative times (e.g., "2 hours from now"), absolute times (e.g., "January 1, 2023 at 3:30pm"), and complex queries that combine multiple time references (e.g., "2 days after next Tuesday at 9am").

## Demo
### Step 1: Install the experimental version of the SDK

```
pip install -U --pre gantry
```

### Step 2: Set up environment variables

To run this, we need to set the OpenAI API key as an environment variable:
```
export OPENAI_API_KEY="..."
```

### Step 3: Run the test

To run the test, just run `pytest test_dtparse.py`.

We can see that the test is failing and the model outputs do
not match the labels.. To fix this, maybe we should
try GOOD_PROMPT instead. Change the prompt to GOOD_PROMPT and
rerun the test. It should pass!

### Step 4: View the runs in a jupyter notebook

Run `jupyter notebook` to start the Jupyter server, and open up
the demo notebook to explore the test run.
