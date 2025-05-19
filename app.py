import json
from dotenv import load_dotenv
from agent import companies, create_agent

load_dotenv()

while True:
    print("Read the input file and choose the number of text. Type this number. To exit conversation print 'e'.")
    request = input()
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
    for company in company_names:
        company_info = agent.invoke(
            {"messages": [{"role": "user", "content": f"About the {company}"}]}
        )
        results.append(company_info["structured_response"].model_dump())
    with open('output.json', 'w') as outfile:
        json.dump(results, outfile, ensure_ascii=False)
        print(f"Analysis completed. Results saved to {outfile.name}")

