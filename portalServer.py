from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi


class HospitalPortalHandler(BaseHTTPRequestHandler):

    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        try:
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_name = form.getvalue("patient_name")
                patient_id = form.getvalue("patient_id")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")

                self.database.addPatient(
                    patient_name, patient_id, age, admission_date, discharge_date)

                print("Patient added:", patient_name,
                      age, admission_date, discharge_date)

                self.wfile.write(
                    b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been added</h3>")
                self.wfile.write(
                    b"<div><a href='/addPatient'>Add Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = form.getvalue("patient_id")
                doctor_id = form.getvalue("doctor_id")
                appointment_date = form.getvalue("appointment_date")
                appointment_time = float(form.getvalue("appointment_time"))

                self.database.scheduleAppointment(
                    patient_id, doctor_id, appointment_date, appointment_time)

                print("Appointment scheduled for Patient ID:",
                      patient_id, "with Doctor ID:", doctor_id)

                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                <a href='/viewAppointments'>View Appointments</a>|\
                                <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Appointment scheduled</h2>")
                self.wfile.write(
                    b"<div><a href='/scheduleAppointment'>Schedule Another Appointment</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/viewAppointments':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Display appointments on the web page
                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>View Appointments</h2>")

                self.wfile.write(b"</center></body></html>")

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                patient_id = int(self.path.split('/')[-1])

                self.database.dischargePatient(patient_id)

                print("Patient ID:", patient_id, "discharged.")

                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Patient discharged</h2>")
                self.wfile.write(
                    b"<div><a href='/dischargePatient'>Discharge Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return

    def do_GET(self):
        try:
            if self.path == '/':
                data = []
                records = self.database.getAllPatients()
                print(records)
                data = records
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>All Patients</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Add New Patient</h2>")

                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="patient_name">Patient Name:</label>\
                      <input type="text" id="patient_name" name="patient_name"/><br><br>\
                      <label for="patient_age">Age:</label>\
                      <input type="number" id="patient_age" name="patient_age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date"id="admission_date" name="admission_date"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                <a href='/viewAppointments'>View Appointments</a>|\
                                <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Schedule Appointment</h2>")

                self.wfile.write(
                    b"<form id='scheduleForm' action='/scheduleAppointment' method='post'>")
                self.wfile.write(b"<label for='patient_id'>Patient ID:</label>\
                    <input type='text' id='patient_id' name='patient_id' required><br><br>\
                    <label for='doctor_id'>Doctor ID:</label>\
                    <input type='text' id='doctor_id' name='doctor_id' required><br><br>\
                    <label for='appointment_date'>Appointment Date:</label>\
                    <input type='date' id='appointment_date' name='appointment_date' required><br><br>\
                    <label for='appointment_time'>Appointment Time:</label>\
                    <input type='text' id='appointment_time' name='appointment_time' required><br><br>\
                    <input type='submit' value='Submit'>\
                    </form>")

                self.wfile.write(b"<script>")
                self.wfile.write(
                    b"document.getElementById('scheduleForm').addEventListener('submit', function(event) {")
                self.wfile.write(b"event.preventDefault();")
                self.wfile.write(
                    b"alert('Appointment scheduled successfully!');")
                self.wfile.write(
                    b"document.getElementById('scheduleForm').reset();")
                self.wfile.write(b"});")
                self.wfile.write(b"</script>")

                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/viewAppointments':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                appointments = self.database.viewAppointments()

                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                <a href='/viewAppointments'>View Appointments</a>|\
                                <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>View Appointments</h2>")

                self.wfile.write(b"<table border=2>")
                self.wfile.write(b"<tr><th> Appointment ID </th>\
                                <th> Patient ID </th>\
                                <th> Doctor ID </th>\
                                <th> Appointment Date </th>\
                                <th> Appointment Time </th></tr>")
                for row in appointments:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                <a href='/viewAppointments'>View Appointments</a>|\
                                <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Discharge Patient</h2>")

                self.wfile.write(
                    b"<form id='dischargeForm' action='/dischargePatient' method='post'>")
                self.wfile.write(b"<label for='patient_id'>Patient ID:</label>\
                    <input type='text' id='patient_id' name='patient_id' required><br><br>\
                    <input type='submit' value='Submit'>\
                    </form>")

                self.wfile.write(b"<script>")
                self.wfile.write(
                    b"document.getElementById('dischargeForm').addEventListener('submit', function(event) {")
                self.wfile.write(b"event.preventDefault();")
                # You can customize this message
                self.wfile.write(b"alert('Patient discharged successfully!');")
                # Clear the form fields
                self.wfile.write(
                    b"document.getElementById('dischargeForm').reset();")
                self.wfile.write(b"});")
                self.wfile.write(b"</script>")

                self.wfile.write(b"</center></body></html>")
                return

        except:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run(server_class=HTTPServer, handler_class=HospitalPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()
