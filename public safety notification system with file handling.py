import os

class NotificationSystem:
    def __init__(self):
        self.notification_records = {}
        self.subscriber_lists = {}
        self.records_file = "notification_records.txt"

    def load_notification_records(self):
        if os.path.exists(self.records_file):
            with open(self.records_file, 'r') as file:
                for line in file:
                    notification_id, message = line.strip().split(':')
                    self.notification_records[notification_id] = message

    def save_notification_records(self):
        with open(self.records_file, 'w') as file:
            for notification_id, message in self.notification_records.items():
                file.write(f"{notification_id}:{message}\n")

    def create_notification_record(self, notification_id, message):
        self.notification_records[notification_id] = message
        print(f"Notification record {notification_id} created.")
        self.save_notification_records()

    def read_notification_record(self, notification_id):
        if notification_id in self.notification_records:
            return self.notification_records[notification_id]
        else:
            return "Notification record not found."

    def update_notification_record(self, notification_id, new_message):
        if notification_id in self.notification_records:
            self.notification_records[notification_id] = new_message
            print(f"Notification record {notification_id} updated.")
            self.save_notification_records()
        else:
            print("Notification record not found.")

    def delete_notification_record(self, notification_id):
        if notification_id in self.notification_records:
            del self.notification_records[notification_id]
            print(f"Notification record {notification_id} deleted.")
            self.save_notification_records()
        else:
            print("Notification record not found.")

    def send_public_alerts(self, alert_id):
        # Simulated function to send alerts to subscribers
        print(f"Sending public alert with ID {alert_id} to subscribers.")

    def manage_subscriber_list(self, list_id):
        # Simulated function to manage subscriber lists
        print(f"Managing subscriber list with ID {list_id}.")

# Main function to test the NotificationSystem class
def main():
    notification_system = NotificationSystem()
    notification_system.load_notification_records()

    while True:
        print("Notification System Menu")
        print("1. Create Notification Record")
        print("2. Read Notification Record")
        print("3. Update Notification Record")
        print("4. Delete Notification Record")
        print("5. Send Public Alerts")
        print("6. Manage Subscriber List")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            notification_id = input("Enter notification ID: ")
            message = input("Enter notification message: ")
            notification_system.create_notification_record(notification_id, message)
        elif choice == 2:
            notification_id = input("Enter notification ID: ")
            print(notification_system.read_notification_record(notification_id))
        elif choice == 3:
            notification_id = input("Enter notification ID: ")
            new_message = input("Enter new notification message: ")
            notification_system.update_notification_record(notification_id, new_message)
        elif choice == 4:
            notification_id = input("Enter notification ID: ")
            notification_system.delete_notification_record(notification_id)
        elif choice == 5:
            alert_id = input("Enter alert ID: ")
            notification_system.send_public_alerts(alert_id)
        elif choice == 6:
            list_id = input("Enter list ID: ")
            notification_system.manage_subscriber_list(list_id)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
