CREATE DATABASE hospital_portal;
USE hospital_portal;

CREATE TABLE patients (
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
	patient_name VARCHAR(45) NOT NULL,
	age INT NOT NULL,
	admission_date DATE,
	discharge_date DATE

);

CREATE TABLE appoinments (
	appointment_id INT AUTO_INCREMENT PRIMARY KEY,
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	appointment_date DATE NOT NULL,
	appointment_time DECIMAL NOT NULL,
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)

);

INSERT INTO patients (patient_name, age, admission_date, discharge_date)
VALUES
	('Maria Jozef', 67, '2023-10-01', '2023-10-07'),
	('John Doe', 45, '2023-09-15', '2023-09-22'),
	('Alice Smith', 30, '2023-11-05', '2023-11-12')
DELIMITER //

CREATE PROCEDURE ScheduleAppoinment(
	IN patientID INT,
    IN doctorID INT,
    IN appDate DATE,
    IN appTime DECIMAL


)

BEGIN 
	INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
	VALUES (patient_id, doctor_id, appDate, appTime);
END//
DELIMITER ;
DELIMITER //

CREATE PROCEDURE DischargePatient(
IN patientID INT


)

BEGIN 
	UPDATE patients SET discharge_date = CURRENT_DATE() WHERE patient_id = patientID;
    
END//
DELIMITER //

CREATE TABLE doctors(

	doctor_id INT AUTO_INCREMENT PRIMARY KEY,
	doctor_name VARCHAR(45) NOT NULL,
	specialization VARCHAR(45) NOT NULL

);
INSERT INTO doctors (doctor_name, specialty) VALUES

	('Dr. Smith', 'Cardiology'),
	('Dr. Johnson', 'Orthopedics'),
	('Dr. Brown', 'Pediatrics')
CREATE VIEW doctor_appoinment_patient AS
SELECT
	a.appoinment_id,
    p.patient_id,
    p.patient_name,
    p.age,
    p.admission_date,
    p.discharge_date,
    d.doctor_id,
    a.appoinment_date,
    a.appoinment_time
FROM appoinments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

call scheduleappoinment(1,3,"2023-11-05" , "12.00");

select * from appoinments



    
    
    