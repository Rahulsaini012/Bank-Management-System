# Bank Management System - Python Project

## 📜 Description
Welcome to the **Bank Management System**! This Python-based command-line application simulates a simple banking system. It allows users to create accounts, deposit and withdraw money, and view account details. The system is designed with **Object-Oriented Programming (OOP)** principles to provide an intuitive user experience with error handling for common banking operations.

## 🚀 Features
- **Create Account**: Users can create a new account by entering an account number, holder’s name, and an initial deposit amount.
- **Deposit Money**: Allows users to deposit funds into their account.
- **Withdraw Money**: Enables users to withdraw money from their account, ensuring there are sufficient funds.
- **View Account Details**: Displays the account number, holder’s name, and the current balance.
- **Exit**: Allows users to exit the system gracefully.

## 🛠️ Technologies Used
- **Python**: The core programming language used to build the system.
- **Object-Oriented Programming (OOP)**: Classes and objects to manage accounts and their operations.
- **Command-Line Interface (CLI)**: Text-based interaction with the system.

## 💾 Installation & Setup

### Prerequisites:
- Python 3.x or later is required to run this project.

### Steps to Run:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
Navigate into the project directory:

bash
Copy code
cd bank-management-system
Run the Python script:

bash
Copy code
python bank_management_system.py
You can now interact with the Bank Management System directly from your terminal!
🧳 Usage
Once the program is running, you’ll see a menu with options to:

Create Account: Enter a unique account number, account holder's name, and an initial deposit to create a new account.
Deposit Money: Deposit funds into an existing account by entering the account number and deposit amount.
Withdraw Money: Withdraw funds from your account, as long as there is sufficient balance.
View Account Details: View the account number, account holder's name, and current balance.
Exit: Exit the system with a message.
Sample Interaction:
markdown
Copy code
Welcome to the Bank Management System!

Options:
1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Account Details
5. Exit

Enter your choice (1-5): 1

Enter Account Number: 12345
Enter Account Holder's Name: John Doe
Enter Initial Deposit Amount: 500

Account Created Successfully for John Doe!

Options:
1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Account Details
5. Exit

Enter your choice (1-5): 2

Enter Account Number: 12345
Enter Amount to Deposit: 200

Deposit Successful! New Balance: $700.00

Options:
1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Account Details
5. Exit

Enter your choice (1-5): 4

Account Details:
Account Number: 12345
Account Holder: John Doe
Current Balance: $700.00

Options:
1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Account Details
5. Exit

Enter your choice (1-5): 5

Thank you for using the Bank Management System. Goodbye!
🖥️ Code Overview
BankAccount Class
Attributes: Account number, holder's name, and current balance.
Methods:
deposit(): Adds a specified amount to the account balance.
withdraw(): Deducts a specified amount from the balance, ensuring sufficient funds.
view_account_details(): Displays the account's details such as number, holder’s name, and balance.
Bank Management System
The system offers a simple menu-driven interface with options for the user to interact with the bank's services. It allows:

Creating a new account.
Depositing and withdrawing funds.
Viewing account details.
Exiting the system.
🔄 Contributing
We welcome contributions! If you have suggestions for improvements or bug fixes, feel free to fork the project and submit a pull request.

You can help improve this project by:

Adding new features such as transaction history or loan management.
Improving user interface and error handling.
Refactoring code for better efficiency.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For inquiries or issues, contact me:

Email: your.email@example.com
GitHub: Your GitHub Profile











