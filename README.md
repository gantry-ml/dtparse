## DTParse

DTParse is an application that takes in natural language queries like "noon last Sunday" along with the current date and time and returns a corresponding timestamp. For example, if the current date is March 21st and time is 1:17 PM, and the query is "noon last Sunday", the application will return "2023-03-19 12:00:00". The application uses GPT-3 and the OpenAI SDK under the hood.

The application can handle a wide range of natural language queries, including relative times (e.g., "2 hours from now"), absolute times (e.g., "January 1, 2023 at 3:30pm"), and complex queries that combine multiple time references (e.g., "2 days after next Tuesday at 9am").

