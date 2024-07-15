import pandas as pd
import requests
from time import sleep
from random import randint

def get_ean_status(ean):
    url = f"https://www.emag.hu/search/{ean}?ref=effective_search"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        if "0 találat a következő kifejezésre" in response.text:
            print ("no result")
            return 0
        else:
            print ("result found")
            return 1
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    excel_file = 'ean_codes.xlsx'
    df = pd.read_excel(excel_file)
    
    # Ensure there's a fourth column to store the results
    if df.shape[1] < 4:
        df.insert(3, 'Result', '')

    # Iterate through the EAN codes and check their status
    for index, row in df.iterrows():
        ean = row[0]
        status = get_ean_status(ean)
        df.at[index, 'Result'] = status
        
        # Random sleep to avoid getting blocked
        sleep(randint(1, 5))  # Sleep between 1 to 5 seconds

    # Save the updated DataFrame back to the Excel file
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    main()