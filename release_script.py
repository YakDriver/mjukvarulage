import sys
import os
import requests

def run_query(query, headers): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def main(*args):
    print("MJUKVARULAGE ----")
    print("Release/Version:", os.environ["VERSION"])

    headers = {"Authorization": os.environ["API_KEY"]}

    # The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
    query = """
    {
    viewer {
        login
    }
    rateLimit {
        limit
        cost
        remaining
        resetAt
    }
    }
    """

    result = run_query(query, headers) # Execute the query
    remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
    print("Remaining rate limit - {}".format(remaining_rate_limit))

    print("Data:",result["data"])

    return 0

if __name__ == "__main__":
    # execute only if run as a script
    sys.exit(main(*sys.argv[1:]))