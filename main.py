# Define an empty dictionary to store complaints
complaints = {}

# Function to submit a complaint
def submit_complaint():
    name = input("Enter your name: ")
    category = input("Enter the category of complaint: ")
    description = input("Enter the description of the complaint: ")

    complaint_id = len(complaints) + 1
    complaint = {
        'name': name,
        'category': category,
        'description': description
    }

    complaints[complaint_id] = complaint
    print("Complaint submitted successfully!\n")

# Function to view all complaints
def view_complaints():
    if not complaints:
        print("No complaints found.\n")
    else:
        print("All Complaints:")
        for complaint_id, complaint in complaints.items():
            print(f"Complaint ID: {complaint_id}")
            print(f"Name: {complaint['name']}")
            print(f"Category: {complaint['category']}")
            print(f"Description: {complaint['description']}")
            print()

# Function to search for a complaint by ID
def search_complaint():
    if not complaints:
        print("No complaints found.\n")
        return

    complaint_id = int(input("Enter the Complaint ID: "))
    complaint = complaints.get(complaint_id)
    if complaint:
        print("Complaint Details:")
        print(f"Name: {complaint['name']}")
        print(f"Category: {complaint['category']}")
        print(f"Description: {complaint['description']}\n")
    else:
        print("Complaint not found.\n")

# Main function to run the complaint management system
def main():
    while True:
        print("Complaint Management System")
        print("1. Submit a Complaint")
        print("2. View All Complaints")
        print("3. Search for a Complaint")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a valid choice (1/2/3/4).\n")
            continue

        if choice == 1:
            submit_complaint()
        elif choice == 2:
            view_complaints()
        elif choice == 3:
            search_complaint()
        elif choice == 4:
            print("Exiting the Complaint Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
