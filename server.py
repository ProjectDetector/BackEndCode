#Mail Package
import smtplib
from email.message import EmailMessage

#google sheet package
from gsheets import Sheets

#Authorizing the api
sheets = Sheets.from_files('FD4GS.json','FD4GS_cache.json')



#Fetching information from owners database
vi1 = sheets.get('1URQBjLmkRkPxI1RGQFpp_ZxUa1xMcoMth3qmWH9DK2Y') # Vehicle Information

vi1_form1_ws = vi1.sheets[0]

entries1 = vi1_form1_ws.values()[1:]

entries1 = [(i[2],i[6]) for i in entries1]



#Fetching information from search database
vi2 = sheets.get('1i2_N7yqcJQQ7cpBJqR8KnxpUOPh3TgNvY8oC1mCSv0U') # Search Database

vi2_form1_ws = vi2.sheets[0]

entries2 = vi2_form1_ws.values()[1:]

entries2 = [(j[1],j[2]) for j in entries2]



#Fetching information from helper database
vi3 = sheets.get('1dYaQqMVPEbJuBwHC-nPbu-2NPIcaqwJf8-MqiZswmU4') # Helper Database

vi3_form1_ws = vi3.sheets[0]

entries3 = vi3_form1_ws.values()[1:]

entries3 = [(k[2],k[3]) for k in entries3]


# Fetching common features between these two database
#a[0]is mail, a[1] is color, b[0] is a mail,b[1]is date, c[0] is location, c[1] is color


maaail = 1
for b in entries2:
    for a in entries1:
        if b[0] == a[0]:
            matchess = [] 
            for c in entries3:
                if c[1].casefold() == a[1].casefold(): 
                    data_matched = [c[0]]
                    matchess.append(data_matched)
                    continue
            #print("Mail:", b[0], "Location:", matchess)

            msg = EmailMessage()
            msg['Subject'] = " We have found few vehicles matches with your feature"
            msg['From'] = "Vehicle Detector Application"
            msg['to'] = b[0]

            location = "Your cars are found in " + str(matchess)
            msg.set_content(location)

            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.login("vehicledetectorproject@gmail.com","<Our Password>")
            server.send_message(msg)
            server.quit()
            print("Mail"+ str(maaail)+" Sent!")
            print("************************************")
            maaail = maaail + 1

print("All emails sent!!!")


                    
                    
