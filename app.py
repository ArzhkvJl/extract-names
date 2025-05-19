import json
from dotenv import load_dotenv
from agent import companies, create_agent

load_dotenv()

while True:
    print("Read the input file and choose the number of text. Type this number. To exit conversation print 'e'.")
    request = input()
    try:
        num = int(request)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        break
    if request == 'e':
        break
    company_names = companies(request)
    if not company_names:
        print("No companies found in the input text.")
        continue
    print()
    print(f"Found {len(company_names)} potential companies: {company_names}")
    agent = create_agent()
    results = []
    output = True
    for company in company_names:
        try:
            company_info = agent.invoke(
                {"messages": [{"role": "user", "content": f"About the {company}"}]}
            )
            results.append(company_info["structured_response"].model_dump())
        except Exception as e:
            print(f"Error initializing Groq and Tavily. Add a valid API key.")
            output = False
            break

    if output:
        with open('output.json', 'w') as outfile:
            json.dump(results, outfile, ensure_ascii=False)
            print(f"Analysis completed. Results saved to {outfile.name}")
    else:
        break

