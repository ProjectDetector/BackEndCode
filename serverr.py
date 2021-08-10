# Mail Package
import smtplib
from email.message import EmailMessage

# google sheet package
from gsheets import Sheets

# Authorizing the api
sheets = Sheets.from_files('FD4GS.json', 'FD4GS_cache.json')


# Fetching information from owners database
# Vehicle Information
# Link: https://docs.google.com/spreadsheets/d/1URQBjLmkRkPxI1RGQFpp_ZxUa1xMcoMth3qmWH9DK2Y/edit#gid=972904917
vi1 = sheets.get('1URQBjLmkRkPxI1RGQFpp_ZxUa1xMcoMth3qmWH9DK2Y')

vi1_form1_ws = vi1.sheets[0]

entries1 = vi1_form1_ws.values()[1:]

entries1 = [(i[2], i[6], i[1]) for i in entries1]


# Fetching information from search database
# Search Database
# Link: https://docs.google.com/spreadsheets/d/1i2_N7yqcJQQ7cpBJqR8KnxpUOPh3TgNvY8oC1mCSv0U/edit#gid=2035337844
vi2 = sheets.get('1i2_N7yqcJQQ7cpBJqR8KnxpUOPh3TgNvY8oC1mCSv0U')

vi2_form1_ws = vi2.sheets[0]

entries2 = vi2_form1_ws.values()[1:]

entries2 = [(j[1], j[2]) for j in entries2]


# Fetching information from helper database
# Helper Database
# Link: https://docs.google.com/spreadsheets/d/1dYaQqMVPEbJuBwHC-nPbu-2NPIcaqwJf8-MqiZswmU4/edit#gid=176906407
vi3 = sheets.get('1dYaQqMVPEbJuBwHC-nPbu-2NPIcaqwJf8-MqiZswmU4')

vi3_form1_ws = vi3.sheets[0]

entries3 = vi3_form1_ws.values()[1:]

entries3 = [(k[2], k[3], k[1], k[4]) for k in entries3]

# print(entries3)


# Fetching common features between all three database
# a[0]is mail, a[1] is color, a[2] is name,  b[0] is a mail,b[1]is date, c[0] is location, c[1] is color, c[2] is image link


maaail = 1
for b in entries2:
    for a in entries1:
        if b[0] == a[0]:  # matching mail
            matchess = []
            linkk = []
            for c in entries3:

                if c[1].casefold() == a[1].casefold():  # matching color
                    # storing location in list
                    data_matched = [c[0]]
                    matchess.append(data_matched)
                    # storing image links in list
                    link_matched = [c[2]]
                    linkk.append(link_matched)
                    continue
                if c[1] == "null":
                    val = c[3].split(",")
                    for v in val:
                        vs = str(v)
                        if vs.casefold() == a[1].casefold():
                            data_matched = [c[0]]
                            matchess.append(data_matched)
                            # storing image links in list
                            link_matched = [c[2]]
                            linkk.append(link_matched)

            # print("Mail:", b[0], "Location:", matchess)

            # Making a mail template
            if len(matchess) == 0:
                continue
            f = open("textformat.txt", "w")
            sent = "Hello " + \
                str(a[2]) + "!" + " \n \n \n \t \tWe have collected certain  images based on your features and thier locations are: \n \n "
            for ii in range(0, len(matchess)):
                sent = sent + "\t\t\t" + str(ii+1) + ") " + str(
                    matchess[ii][0]) + " and the image link is " + str(linkk[ii][0]) + "\n \n"
                continue
            f.write(sent)
            f.close()

            # print(sent)
            fii = open("textformat.txt")
            final = fii.read()
            # print(final)

            # Sending Mail
            msg = EmailMessage()
            msg['Subject'] = "Vehicle Matching"
            msg['From'] = "Vehicle Detector Application"
            msg['to'] = b[0]

            location = "Your cars are found in " + str(matchess)
            msg.set_content(final)

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("vehicledetectorproject@gmail.com",
                         "kumarannaveenpradeish14")
            server.send_message(msg)
            server.quit()
            print("Mail" + str(maaail)+" Sent!")
            print("************************************")
            maaail = maaail + 1
            f.close()

print("All emails sent!!!")
