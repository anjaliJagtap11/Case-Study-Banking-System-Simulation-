Case Study: Banking System Simulation 

 

Objective 

 

To design a Python-based banking system that: 

1. Reads customer data from a file. 

2. Simulates operations using OOP concepts. 

3. Implements conditional and looping statements for decision-making. 

4. Utilizes lists for storing transaction details. 

5. Handles errors using exceptions. 

6. Demonstrates multitasking using threading for concurrent tasks. 

 

Scenario 

 

You are tasked with developing a banking application prototype. The system will: 

1. Read customer details from a file. 

2. Allow users to perform operations like deposit, withdrawal, and view transaction history. 

3. Ensure robust error handling. 

4. Simulate account balance checks and updates using threading. 

 

Data.csv 

CustomerID, Name, AccountBalance 

101, John Doe, 5000 

102, Jane Smith, 3000 

103, Alice Johnson, 7000 

 

 

Key Additions 

1. Account Types: 

• account_type is passed when creating a customer. 

• Savings accounts allow interest application. 

2. Interest Calculation: 

• The apply_interest method calculates and adds interest for savings accounts. 

• Periodically applied via a separate thread. 

3. Real-Time Updates: 

• periodic_interest_application function runs as a daemon thread, applying interest at regular intervals (e.g., 10 seconds). 

4. Thread-Safety: 

• Used threading.Lock to ensure safe updates to shared data like account balances. 
