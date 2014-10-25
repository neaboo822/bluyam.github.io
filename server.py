import sendgrid
from flask import Flask
app = Flask(__name__)


sg = sendgrid.SendGridClient('neaboo822', 'cyneaboo822')


@app.route("/sg", methods=['POST'])
def send_email():
	message = sendgrid.Mail()
	message.add_to('receiver <ss1234534@gmail.com>')
	message.set_subject('Hello')
	message.set_html('Thisthisthis')
	message.set_text('BodyBodyBody')
	message.set_from('chihyen <ss1234534@hotmail.com>')
	status, msg = sg.send(message)
	return msg

if __name__ == "__main__":
    app.run()
