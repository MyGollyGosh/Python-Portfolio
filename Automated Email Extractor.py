from datetime import datetime
import imaplib
import email
import os
import re
from openpyxl import Workbook

#Email config. Change these to your specific details as a string
IMAP_SERVER = ''
EMAIL = ''
PASSWORD = ''
SEARCH_SUBJECT = '' #Title of email that will be searched for

#Excel config
EXCEL_FILE = 'TIME BACK OWED.xlsx'
CUSTOM_PATH = r'C:\Users\refur\Documents' #File path excel document will be save to
EXCEL_FILE = os.path.join(CUSTOM_PATH, 'TIME BACK OWED.xlsx')

def format_search_date(date):
    return date.strftime('%d-%b-%Y')

#IMAP setup
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox') #Change this to search specific folder 

def pull_emails_to_excel():
    #Set start and end date to 1st of previous month with handler for January
    today = datetime.today()
    if today.month == 1:
        start_date = datetime(today.year - 1, 12, 1)
    else: 
        start_date = datetime(today.year, today.month - 1, 1)
    end_date = datetime(today.year, today.month + 1, 1)

    #Search for all email within specified time and with subject
    search_query = f'(SINCE "{format_search_date(start_date)}" BEFORE "{format_search_date(end_date)}" SUBJECT "{SEARCH_SUBJECT}")'
    result, data = mail.search(None, search_query)
    email_ids = data[0].split()

    #Handler conditional for if no emails were found.
    if email_ids:
        wb = Workbook()
        ws = wb.active
        ws.append(['From', 'Subject', 'CONVO-ID', 'CN', 'OVERTIME', 'Date Sent'])

        #Get content for each email
        for email_id in email_ids:
            result, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            sender = msg['From']
            subject = msg['Subject']
            date_sent = msg['Date']

            #This is for handling multipart emails and checks for data that isn't simple text. As only simple text is needed for this ignores any images or links ect.
            def extract_text_from_part(part):
                if part.is_multipart():
                    for subpart in part.get_payload():
                        extracted_text = extract_text_from_part(subpart)
                        if extracted_text:
                            return extracted_text
                elif part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
                    return part.get_payload(decode=True).decode(part.get_content_charset())
                return None

            body = extract_text_from_part(msg)

            #Regex to search for and pull the required information out of email.
            convo_id = re.search(r'CONVO-ID: (\w+)', body)
            cn = re.search(r'CN: (\w+)', body)
            overtime = re.search(r'OVERTIME: (\w+)', body)

            #Set values to add to excel document or add message to hep trouble shooting.
            convo_id = convo_id.group(1) if convo_id else 'Error or no data in email'
            cn = cn.group(1) if cn else 'Error or no data in email'
            overtime = overtime.group(1) if overtime else 'Error or no data in email'

            ws.append([sender, subject, convo_id, cn, overtime, date_sent])

        wb.save(EXCEL_FILE)
        print("Emails extracted and saved to Excel successfully!")
    else:
        print("No emails found with the specified subject in the previous month.")


    mail.logout()

pull_emails_to_excel()