# EAN Checker for EMAG Hungary
This Python script checks EAN numbers from an Excel file to determine if they exist on the retailer EMAG Hungary's website. The script includes a delay between requests to avoid overwhelming the server and reduce the risk of getting your IP blocked.

# How It Works
1. Install Python libraries "pandas" and "requests".
2. Reading EANs from Excel: You will need an Excel file (properly named) with not more than 3 columns. The script reads a list of EAN codes from the first column of an Excel file using the pandas library.
3. Web Crawling: For each EAN, the script constructs a search URL for the EMAG Hungary website and sends an HTTP request to retrieve the search results page.
4. Check for Results: The script examines the page to see if it contains the phrase "0 találat a következő kifejezésre" (indicating no results).
5. Store Results: The script writes a "0" in the fourth column of the Excel file if no results are found for the EAN, and a "1" if results are found.
6. Respect for Robots.txt: Before running the script, the robots.txt file of emag.hu was checked to ensure the type of web crawling performed is allowed. Please do the same with any other website you plan to crawl.
