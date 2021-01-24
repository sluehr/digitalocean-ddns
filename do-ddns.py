#!/usr/bin/env python3

import logging
import os
import requests

REQUIRED_ENV_VARIABLES = ['DO_API_TOKEN', 'DO_DOMAIN', 'DO_RECORD']

for var in REQUIRED_ENV_VARIABLES:
    if var not in os.environ:
        raise EnvironmentError(f"Environment variable {var} not set.")

api_token = os.environ['DO_API_TOKEN']
domain_name = os.environ['DO_DOMAIN']
record_name = os.environ['DO_RECORD']

headers = {"Authorization": f"Bearer {api_token}"}


def fetch_type_a_record():
    records_url = f"https://api.digitalocean.com/v2/domains/{domain_name}/records" \
                  f"?name={record_name}.{domain_name}&type=A"
    response = requests.get(records_url, headers=headers)
    response.raise_for_status()

    domain_records = response.json().get('domain_records', [])
    if not domain_records:
        raise ValueError(f"Didn't find record for {domain_name}")

    return domain_records[0]


def update(record):
    record_url = f"https://api.digitalocean.com/v2/domains/{domain_name}/records/{record['id']}"
    response = requests.put(record_url, headers=headers, data={"data": current_ip_address})
    response.raise_for_status()


current_ip_address = requests.get('http://ipinfo.io/ip').text
domain_record = fetch_type_a_record()

if domain_record['data'] == current_ip_address:
    logging.info(f"[NO CHANGE] Record for {record_name}.{domain_name} is up to date")
else:
    logging.info(f"[MODIFY] Updating {record_name}.{domain_name} -> {current_ip_address}")
    update(domain_record)
