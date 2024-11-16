import csv
import json
import time
import requests


def simulate(file_path):
    health = True

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                response = requests.get('http://127.0.0.1:9292/health')
                response.raise_for_status()
                health_data = response.json()
                if health_data.get('status') != 'ok':
                    print("Server health check failed.")
                    health = False
                else:
                    print("Health Check Succeeded.")
                    health = True

            except requests.exceptions.RequestException as e:
                print(f"Server health check failed.")
                health = False

            time.sleep(4)

            if (health):
              json_data = json.dumps(row)
              data = json.loads(json_data)
              try:
                print(
                      f"New Call:\n"
                      f"  Incident #: {data['incident_number']}\n"
                      f"  Call Type: {data['call_type']}\n"
                      f"  Call Time: {data['call_time']}\n"
                )
                response = requests.post('http://127.0.0.1:9292/call_details', data=json_data, headers={'Content-Type': 'application/json'})
                response.raise_for_status()
              except requests.exceptions.RequestException as e:
                  print(f"Error posting data: {e}")
                  return

if __name__ == '__main__':
    simulate('police-incidents-2022.csv')
