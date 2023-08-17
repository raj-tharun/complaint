# Complaint Management System

This is a simple script for managing complaints. It allows users to submit, view, and search for complaints.

## How to Use

1. Run the script by executing it.
2. Choose from the following options:
    - **1. Submit a Complaint**: Enter your name, category of complaint, and description to submit a complaint.
    - **2. View All Complaints**: Display all submitted complaints.
    - **3. Search for a Complaint**: Search for a complaint using its ID.
    - **4. Exit**: Quit the Complaint Management System.

## Functions

### `submit_complaint()`

This function lets you submit a complaint. It prompts you to enter your name, category of complaint, and description. The complaint is then assigned a unique ID and stored in the system.

### `view_complaints()`

Displays all submitted complaints. If no complaints are found, it will indicate that there are no complaints available.

### `search_complaint()`

Allows you to search for a complaint by its unique ID. If the complaint exists, its details (name, category, and description) will be displayed. Otherwise, it will indicate that the complaint was not found.

### `main()`

The main function runs the Complaint Management System. It displays a menu of options and prompts you to choose an action. Based on your choice, it calls the corresponding functions.

## How to Run

1. Copy the script into a Python file (e.g., `complaint_management.py`).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script using the `cd` command.
4. Run the script by entering `python complaint_management.py`.

## Note

This script is meant for educational purposes and demonstrates a basic complaint management system. It does not include advanced error handling or persistent storage for complaints.
