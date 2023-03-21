import requests
import mysql.connector
import yaml

# Load configuration from YAML file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Extract configuration values
MOLLIE_API_KEY = config['mollie_api_key']
MYSQL_HOST = config['mysql_host']
MYSQL_USER = config['mysql_user']
MYSQL_PASSWORD = config['mysql_password']
MYSQL_DATABASE = config['mysql_database']
limit = 250  # Maximum number of customers to retrieve per request
# Define Mollie API endpoint and initial parameters
MOLLIE_API_ENDPOINT = 'https://api.mollie.com/v2/customers'
params = {'limit': limit}  # Maximum number of customers to retrieve per request

# Connect to MySQL database
cnx = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

# Retrieve all customers from Mollie's API
while True:
    response = requests.get(MOLLIE_API_ENDPOINT, headers={'Authorization': f'Bearer {MOLLIE_API_KEY}'}, params=params)

    if response.status_code != 200:
        raise Exception('Failed to retrieve customers from Mollie API')

    mollie_customers = response.json()['_embedded']['customers']

    for mollie_customer in mollie_customers:
        # Compare Mollie customer to users in MySQL database
        with cnx.cursor() as cursor:
            cursor.execute('SELECT customer_id FROM users WHERE customer_id = %s', (mollie_customer['id'],))
            db_user = cursor.fetchone()

            if db_user is None:
                # If Mollie customer not found in MySQL database, print customer details
                print(
                    f"New user '{mollie_customer['name']}' with email {mollie_customer['email']} and edit URL {mollie_customer['_links']['dashboard']['href']}")

                # Insert Mollie customer into MySQL database
                # cursor.execute('INSERT INTO users (customer_id, name, email) VALUES (%s, %s, %s)',
                #                (mollie_customer['id'], mollie_customer['name'], mollie_customer['email']))
                # cnx.commit()

    # Check if there are more customers to retrieve
    if 'next' in response.json()['_links']:
        next_url = response.json()['_links']['next']['href']
        params = {'from': response.json()['_embedded']['customers'][-1]['id'],
                  'limit': limit}  # Set 'from' parameter to the ID of the last customer retrieved
    else:
        break

cnx.close()
