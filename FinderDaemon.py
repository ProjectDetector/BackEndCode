from gsheets import Sheets

sheets = Sheets.from_files('FD4GS.json','FD4GS_cache.json')

vi = sheets.get('1URQBjLmkRkPxI1RGQFpp_ZxUa1xMcoMth3qmWH9DK2Y') # Vehicle Information

vi_form1_ws = vi.sheets[0]

entries = vi_form1_ws.values()[1:]

entries = [(i[2],i[6]) for i in entries]

print(entries)
