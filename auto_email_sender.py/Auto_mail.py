import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application im'

password_key = ''  #where you would enter your app passcode given by gmail
my_resume_file = "" # enter the directory to your file 


# SMTP Server and port no for Gmail.com
gmail_server = "smtp.gmail.com"
gmail_port = 587 

# Making the connection 
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()#TLS for creating a secure network 

# Logging into my email using the information provided/Encoding password to bytes
my_server.login(my_email, password_key) 
# Create email message
message = MIMEMultipart()
message["From"] = my_email
message["To"] = email_recepient  
message["Subject"] = "Test Email"

# Plain text and HTML version of the message 
text_content = "Hello, This is a test email being sent using a program I created. Attached is my resume as an example."


text_bytes = text_content.encode('utf-8')

message.attach(MIMEText(text_content, "plain"))

# Read the file from location and attach it to the email
with open( my_resume_file, 'rb') as f:
    resume_attachment = MIMEApplication(f.read(), name=os.path.basename(my_resume_file))
    resume_attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(my_resume_file)}"'
    message.attach(resume_attachment)

# Send email
my_server.sendmail(
    from_addr=my_email,
    to_addrs=email_recepient,
    msg=message.as_string()  # Use message.as_string() here
)

# Quit the server
my_server.quit()
