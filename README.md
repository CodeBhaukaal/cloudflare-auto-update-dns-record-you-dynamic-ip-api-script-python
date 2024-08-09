
Cloudflare DNS Auto Updater Your Dynamic IP 
=================================

This Python script automatically updates the DNS A record for a specific domain on Cloudflare with the current public IPv4 address of your machine. It is particularly useful for dynamically updating DNS records in scenarios where your IP address frequently changes, such as with residential ISPs.

Features
--------

*   **Dynamic IP Address Fetching**: The script fetches the current public IPv4 address.
*   **Cloudflare API Integration**: It uses Cloudflare's API to create or update the DNS A record for the specified domain.
*   **Automatic Execution**: The script runs in an infinite loop, checking and updating the IP address every 2 minutes.

Prerequisites
-------------

*   **Python 3.x**
*   **`requests` library**: You can install it using the following command:

    pip install requests

Setup Instructions
------------------

### 1\. Clone the Repository

First, clone the repository to your local machine and navigate to the directory:

    git clone <repository-url>
    cd <repository-directory>

### 2\. Install Required Python Packages

Install the necessary Python packages by running the following command:

    pip install requests

### 3\. Set Up Your Cloudflare API Token

You need to replace the placeholders for `API_TOKEN`, `ZONE_ID`, and `DOMAIN` in the script with your actual Cloudflare credentials. Open the script and update the following lines:

    API_TOKEN = "your_cloudflare_api_token"
    ZONE_ID = "your_cloudflare_zone_id"
    DOMAIN = "your_domain.com"

*   **API\_TOKEN**: This is your Cloudflare API token.
*   **ZONE\_ID**: The unique identifier of the Cloudflare zone associated with your domain.
*   **DOMAIN**: The domain name for which you want to update the DNS A record.

How to Run the Script
---------------------

### Run the Script Manually

To run the script once and update the DNS record, execute the following command:

    python your_script.py

### Run the Script in an Infinite Loop

If you want the script to continuously check and update the DNS A record every 2 minutes, run:

    python your_script.py

The script will continue running and update the DNS A record as necessary.

Customization
-------------

### Update Interval

You can customize how often the script checks and updates the IP address. By default, it runs every 2 minutes (120 seconds). To change this interval, modify the following line in the `main_loop()` function:

    time.sleep(120)  

#### Example: Change Interval to 5 Minutes

If you want the script to check and update the DNS A record every 5 minutes, change the interval as shown below:

    time.sleep(300)  

Troubleshooting
---------------

### Cloudflare API Errors

*   **Ensure Correct Permissions**: Make sure your API token has the appropriate permissions to edit DNS records.
*   **Check API Token Validity**: Verify that the API token is correct and hasn't expired.

### Invalid IP Address

*   **Network Connection**: Check your network connection to ensure that the IP fetching service is reachable.
*   **IP Fetching Service**: Verify that the service used to fetch the IP address is up and running.

License
-------

This script is licensed under the MIT License. You can use, modify, and distribute it as per the terms of the license. See the LICENSE file for more information.
