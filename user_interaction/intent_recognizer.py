import pandas as pd

def process_query(query, df, summary):
    # Convert query to lowercase for easier matching
    query = query.lower()
    query_words = query.split()

    # Find columns that match exactly with words in the query
    column = [col for col in df.columns if col.lower() in query_words]
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    response = ""

    # Define simple rule-based responses for various tasks
    if len(column) >= 1:
        for col in column:
            if col in numerical_columns:
                if "outliers" in query or "anomalies" in query or "outliers" in query:
                    response += f"The number of outliers in {col} are: {summary['Statistics'][col]['outliers']}"
                    response += f" And their percentage is: {summary['Statistics'][col]['outliers_percentage']}"
                    return response                
                elif "missing" in query or " null" in query:
                    response += f"The number of missing values in {col} are: {summary['Statistics'][col]['missing_values']}"
                    response += f" And their percentage is: {summary['Statistics'][col]['missing_values_percentage']}"
                    return response
                elif "distinct" in query or "unique" in query:
                    response += f"The number of unique values in {col} are: {summary['Statistics'][col]['distinct_values']}"
                    response += f" And their percentage is: {summary['Statistics'][col]['distinct_values_percentage']}"
                    return response
                elif 'summary' in query or "summarize" in query:
                    response += f"The 5 number summary of the {col} is: \n{pd.DataFrame(summary['Description'][col])} "    
                    return response
            else:
                response += "As this is just a prototype, please see the report for in-depth analysis :)"
                return response
    else:
        if 'summary' in query or 'summarize' in query:
            response += f"The summary of the dataset:\n"
            response += f"{pd.DataFrame(summary['Statistics']['overall'])}"
            return response
        else:
            response += "Try searching for summary, else see the report for in-depth analysis :)"
            return response

