"""
context.py must contain the following variables:
CUSTOMER_CODE='123456'
USER='user name'
PASS='password'
"""
from tests.context import CUSTOMER_CODE, USER, PASS
import petl

from erply_api import Erply, ErplyAuth

auth = ErplyAuth(CUSTOMER_CODE, USER, PASS)
erply = Erply(auth)
conf = erply.fetch_config()
assert 'csv_field_separator' in conf

csv = erply.getAmountsOnOrder(warehouseID=2, responseType='CSV')
tbl = petl.fromcsv(csv.url)
assert len(tbl.header())==2

csv = erply.getProductStockCSV(warehouseID=2, responseType='CSV')
tbl = petl.fromcsv(csv.url)
assert len(tbl.header())==2

csv = erply.getSalesReport(getCOGS=1, warehouseID=2, dateStart='2020-01-01', dateEnd='2020-08-01', recordsOnPage=3500, reportType='SALES_BY_INVOICE_ROWS')
tbl = petl.fromcsv(csv.url, delimiter=conf['csv_field_separator'])
assert tbl.header()[0]=='LINE_NUMBER'