## README for Python code

This Python code retrieves customers from Mollie's API and compares them to the customers in a MySQL database. If a customer exists in Mollie's API but not in the MySQL database, it prints the customer details and inserts the customer into the MySQL database.

### Requirements
This code requires the following Python packages:

requests
mysql-connector-python
pyyaml
Make sure these packages are installed before running the code.

### Configuration
The configuration values for the Mollie API key, MySQL database host, user, password, and database name are stored in a YAML file called config.yaml. Modify the values in this file to match your own configuration before running the code.

### Execution
To run the code, simply execute the Python script. The code will retrieve all customers from Mollie's API and compare them to the customers in the MySQL database. If a customer is not found in the MySQL database, the code will print the customer details and insert the customer into the MySQL database.

### Output
The output of the code will be a list of new customers (i.e., customers found in Mollie's API but not in the MySQL database). The output will be printed to the console.

Note that the code is currently set up to only print the new customer details to the console. If you want to insert the new customers into the MySQL database, uncomment the appropriate lines of code.
