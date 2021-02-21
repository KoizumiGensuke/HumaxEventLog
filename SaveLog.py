#
# Store HG100R-02JG event log to csv file
# 2021/2/21 koizumi
#
import csv
import datetime
import humax # https://github.com/radomirbosak/humax
import os
import locale # to avoid strftime locale error

h = humax.Humax('http://192.168.0.1')
h.login('id', 'password')
log = h.post(humax.Device.getDBInfo, token=h.token, return_raw=True, CM_SNMP_Event_Log='')
entries = log['result']['CM_SNMP_Event_Log']['snmp_event_log']
folder = os.path.dirname(os.path.abspath(__file__))
locale.setlocale(locale.LC_CTYPE, 'Japanese_Japan.932') # to avoid strftime locale error
csvfilename = datetime.datetime.strftime(datetime.datetime.now(), folder + '/Humax%Y%m%d%H%M%S.csv')

with open(csvfilename, 'w') as fout:
    writer = csv.DictWriter(fout, fieldnames = list(entries[0].keys()))
    writer.writeheader()
    for entry in entries:
        entry['time'] = entry['time'][:-1] # omit tailing newline
        writer.writerow(entry)
