import requests
import schedule
import time
from tabulate import tabulate


subdomains = ['subdomain1.example.com', 'subdomain2.example.com', 'subdomain3.example.com']

def check_status():
    status_table = []

    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}", timeout=5)
            if response.status_code == 200:
                status = 'Up'
            else:
                status = 'Down'
        except requests.ConnectionError:
            status = 'Down'
        
        status_table.append([subdomain, status])
    
    print(tabulate(status_table, headers=['Subdomain', 'Status']))

schedule.every(1).minutes.do(check_status)

while True:
    schedule.run_pending()
    time.sleep(1)
