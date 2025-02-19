# -*- coding: utf-8 -*-
"""Test_file

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SbSjwQFEFtcAVQaVVkPSQdt7PDDjBF38
"""

import json
import csv
from deliverable2 import *



# Instantiate the URLValidator class
validator = URLValidator()

# Define test cases with user prompts and URLs
test_cases = [
    {
        "user_prompt": "Are eggs good for heart health?",
        "url": "https://www.heart.org/en/news/2021/02/08/are-eggs-good-or-bad-for-my-heart"
    },
    {
        "user_prompt": "What are the symptoms of the flu?",
        "url": "https://www.cdc.gov/flu/symptoms/symptoms.htm"
    },
    {
        "user_prompt": "What are the latest advancements in AI for medical diagnosis?",
        "url": "https://www.nature.com/articles/s41591-021-01529-3"
    }
]

# Open a CSV file to store results
csv_filename = "url_validation_results.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["User Prompt", "URL", "Domain Trust", "Content Relevance", "Bias Score", "Final Score", "Stars"])

    # Process each test case
    for test in test_cases:
        user_prompt = test["user_prompt"]
        url_to_check = test["url"]

        # Run the validation
        result = validator.rate_url_validity(user_prompt, url_to_check)

        # Print the results in JSON format
        print(f"Results for: {user_prompt}")
        print(json.dumps(result, indent=2))
        print("\n" + "="*80 + "\n")

        # Write results to CSV
        writer.writerow([
            user_prompt,
            url_to_check,
            result["raw_score"]["Domain Trust"],
            result["raw_score"]["Content Relevance"],
            result["raw_score"]["Bias Score"],
            result["raw_score"]["Final Validity Score"],
            result["stars"]["icon"]
        ])

print(f"Results saved to {csv_filename}")
