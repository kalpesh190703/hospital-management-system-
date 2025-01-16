import mysql.connector
from datetime import datetime

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hospital_management"
)

mycursor = mydb.cursor()

# Function to add a patient
def add_patient(first_name, last_name, age, gender, contact, address):
    sql = "INSERT INTO Patients (first_name, last_name, age, gender, contact_number, address) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, age, gender, contact, address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Patient {first_name} {last_name} added successfully!")

# Function to add a doctor
def add_doctor(first_name, last_name, specialization, contact, email):
    sql = "INSERT INTO Doctors (first_name, last_name, specialization, contact_number, email) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name, last_name, specialization, contact, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Doctor {first_name} {last_name} added successfully!")

# Function to add an appointment
def add_appointment(patient_id, doctor_id, appointment_date, reason):
    sql = "INSERT INTO Appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)"
    val = (patient_id, doctor_id, appointment_date, reason)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Appointment added successfully!")

# Function to generate a bill
def generate_bill(patient_id, amount, status):
    sql = "INSERT INTO Bills (patient_id, amount, date, status) VALUES (%s, %s, %s, %s)"
    val = (patient_id, amount, datetime.now(), status)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Bill generated successfully!")

# Main function to test the system
def main():
    # Test Data
    add_patient("John", "Doe", 29, "Male", "1234567890", "123 Street Name")
    add_doctor("Dr. Smith", "Jones", "Cardiology", "0987654321", "dr.smith@example.com")
    add_appointment(1, 1, "2025-01-16 10:00:00", "General Checkup")
    generate_bill(1, 500, "Paid")

if __name__ == "__main__":
    main()
