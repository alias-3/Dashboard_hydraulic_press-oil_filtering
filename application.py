from flask import Flask,render_template
import serial
ser = serial.Serial('/dev/ttyACM0',9600)

POWER_ON='A'
LID_OPEN='B'
LID_CLOSE='C'
MOTOR_OFF='D'
MOTOR_FWD='E'
MOTOR_REV='F'
TRANS_OFF='G'
TRANS_HIGH='H'
TRANS_LOW='I'
MIN_FLOAT_HIGH='J'
MIN_FLOAT_LOW='K'
MAX_FLOAT_HIGH='L'
MAX_FLOAT_LOW='M'

POWER_OFF='Z'

'''
P ERROR MSG 50 OR/AND 48 LOW
S
'''

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("dashboard.html")


@app.route("/power_on",methods=['POST'])
def power_on():
	return "True";

@app.route("/power_off",methods=['POST'])
def power_off():
	ser.write(POWER_OFF.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='Z'):
		return "POWER OFF: SUCCESS"
	return "POWER OFF: FAILED, please check again"

@app.route("/motor_off",methods=['POST'])
def motor_off():
	ser.write(MOTOR_OFF.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='D'):
		return "MOTOR OFF: SUCCESS"
	return "MOTOR OFF: FAILED, please check again"

@app.route("/trans_off",methods=['POST'])
def trans_off():
	ser.write(TRANS_OFF.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='G'):
		return "TRANSFORMER OFF: SUCCESS"
	return "TRANSFORMER OFF: FAILED, please check again"

@app.route("/motor_fwd",methods=['POST'])
def motor_fwd():
	ser.write(MOTOR_FWD.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='E'):
		return "SWITCH MOTOR ON (FORWARD) : SUCCESS"
	elif(resp=='B'):
		return "PLEASE CLOSE LID and try again"
	return "SWITCH MOTOR ON (FORWARD): FAILED, please check again"

@app.route("/motor_rev",methods=['POST'])
def motor_rev():
	ser.write(MOTOR_REV.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='F'):
		return "SWITCH MOTOR ON (REVERSE) : SUCCESS"
	elif(resp=='B'):
		return "PLEASE CLOSE LID and try again"
	return "SWITCH MOTOR ON (REVERSE): FAILED, please check again"

@app.route("/trans_high",methods=['POST'])
def trans_high():
	ser.write(TRANS_HIGH.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='H'):
		return "SWITCH TRANSFORMER ON (HIGH) : SUCCESS"
	return "SWITCH TRANSFORMER ON (HIGH): FAILED, please check again"

@app.route("/trans_low",methods=['POST'])
def trans_low():
	ser.write(TRANS_LOW.encode())
	response = ser.read()
	resp = response.decode()
	if(resp=='I'):
		return "SWITCH TRANSFORMER ON (LOW) : SUCCESS"
	return "SWITCH TRANSFORMER ON (LOW): FAILED, please check again"

def monitor():
	resp = ser.read()
	resp.decode()
	return resp


if __name__ == "__main__":
	app.run(debug=True)
