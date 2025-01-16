-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hospital_management;

-- Use the database
USE hospital_management;

-- Patients Table
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    contact_number VARCHAR(15),
    address TEXT
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(100),
    contact_number VARCHAR(15),
    email VARCHAR(100)
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATETIME,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Bills Table
CREATE TABLE IF NOT EXISTS Bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    amount DECIMAL(10, 2),
    date DATETIME,
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
