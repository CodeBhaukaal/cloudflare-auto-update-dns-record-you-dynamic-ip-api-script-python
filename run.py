import time
import requests
import re

# Your Cloudflare credentials
API_TOKEN = "your_cloudflare_api_token"
ZONE_ID = "your_cloudflare_zone_id"
DOMAIN = "your_domain.com"

# Get the current IPv4 address
def get_current_ip():
    try:
        response = requests.get("https://ipv4.icanhazip.com")
        response.raise_for_status()
        ip_address = response.text.strip()
        print(f"Current IP Address: {ip_address}")  # Debugging line
        return ip_address
    except requests.RequestException as e:
        print(f"Error getting current IP address: {e}")
        return None

# Validate the IP address
def is_valid_ipv4(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

# Get the Record ID for the A record
def get_record_id():
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records?type=A&name={DOMAIN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        records = response.json().get("result", [])
        if records:
            return records[0]["id"]
        else:
            print(f"No A record found for {DOMAIN}")
            return None
    except requests.RequestException as e:
        print(f"Error getting record ID: {e}")
        return None

# Create a new A record with the current IP
def create_a_record(current_ip):
    if not is_valid_ipv4(current_ip):
        print("Invalid IPv4 address.")
        return
    
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": DOMAIN,
        "content": current_ip,
        "ttl": 120,
        "proxied": False
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        if result.get("success"):
            print(f"A record created successfully with IP {current_ip}")
        else:
            print(f"Failed to create A record: {result}")
    except requests.RequestException as e:
        print(f"Error creating A record: {e}")
        if response is not None:
            print(f"Response content: {response.text}")

# Update the existing A record with the current IP
def update_a_record(current_ip, record_id):
    if not is_valid_ipv4(current_ip):
        print("Invalid IPv4 address.")
        return
    
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": DOMAIN,
        "content": current_ip,
        "ttl": 120,
        "proxied": False
    }

    try:
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        if result.get("success"):
            print(f"A record updated successfully to {current_ip}")
        else:
            print(f"Failed to update A record: {result}")
    except requests.RequestException as e:
        print(f"Error updating A record: {e}")

def main():
    current_ip = get_current_ip()
    if current_ip:
        record_id = get_record_id()
        if record_id:
            update_a_record(current_ip, record_id)
        else:
            create_a_record(current_ip)

# Main loop to run the script every 2 minutes
def main_loop():
    while True:
        main()  # Run the main function
        time.sleep(120)  # Sleep for 2 minutes (120 seconds)

if __name__ == "__main__":
    main_loop()
