# bankfund_mngmnt
1. Reserve_bank (Base Class)
	•	Holds the overall reserve balance of the bank.
	•	Tracks the total number of accounts across all levels.

2. Tamil_nadu (Intermediate Class)
	•	Inherits from Reserve_bank.
	•	Represents a state-level banking system, maintaining state-level balance and account count.

3. SBI (Final Class)
	•	Inherits from Tamil_nadu.
	•	Represents an individual bank branch that handles customer accounts.
	•	Maintains user account details and balance information.

🔹 Account Opening – Users can create an account with a name and email.
🔹 Deposit Money – Users can deposit funds into their accounts.
🔹 Withdraw Money – Users can withdraw money, ensuring sufficient balance.
🔹 Close Account – Users can close their accounts permanently.
🔹 Check Account Details – Users can view their account details, including balance.
🔹 View All Accounts – Admin can view all active account holders.
🔹 File Storage – The system saves account and balance details in text files for data persistence.
🔹 Load Previous Data – On startup, the program reads from the saved files to restore accounts.
