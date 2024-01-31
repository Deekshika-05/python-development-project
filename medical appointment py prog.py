import json

appointments = {}

def schedule_appointment(date, time, patient_name):
    key = f"{date} {time}"
    if key not in appointments:
        appointments[key] = {"patient_name": patient_name, "status": "Scheduled"}
        return "Appointment scheduled successfully"
    else:
        return "Appointment slot is not available"

def get_appointments():
    return json.dumps(appointments, indent=2)

if __name__ == '__main__':
    while True:
        print("\n1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            date = input("Date (DD-MM-YYYY): ")
            time = input("Time: ")
            patient_name = input("Patient Name: ")
            result = schedule_appointment(date, time, patient_name)
            print(result)
        elif choice == '2':
            appointments_str = get_appointments()
            print(appointments_str)
        elif choice == '3':
            break
        else:
            print("Please try again!!!")
