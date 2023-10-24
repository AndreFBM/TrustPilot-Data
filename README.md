# Trustpilot Data Extraction to SQL Server
This script fetches TrustScore data from the Trustpilot API for a predefined list of market IDs. Once extracted, the data is stored in a SQL Server table.

### Prerequisites
- Python 3
- Required Python Libraries:
  - requests
  - pandas
  - sqlalchemy
  - pyodbc

You can install the required libraries using pip:

**pip install requests pandas sqlalchemy pyodbc**

### Configuration

**API Details:**

Update **YOUR_API_KEY_HERE** in the **HEADERS** variable with your Trustpilot API key.

**HEADERS = {"apikey": "YOUR_API_KEY_HERE"}**

**Market IDs:**

The list named **markets** contains the IDs of the markets you want to fetch information for. Modify it as needed.

**Database Connection Details:**

Replace placeholders in the **CONNECTION_STRING** with your actual database connection details.

CONNECTION_STRING = (
    "DRIVER={YOUR_DRIVER_HERE};"
    "SERVER=YOUR_SERVER_HERE;"
    "DATABASE=YOUR_DATABASE_NAME_HERE;"
    "UID=YOUR_USERNAME_HERE;"
    "PWD=YOUR_PASSWORD_HERE;"
)

**Table Name:**

Specify the SQL Server table name where the data will be inserted.

**table_name = "YOUR_TABLE_NAME_HERE"**

**Usage**

Ensure you have configured the script as described in the Configuration section.

**python your_script_name.py**

On successful execution, the script will fetch the data from the Trustpilot API and insert it into the specified SQL Server table. A success message will be printed indicating the completion of the operation.
