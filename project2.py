from login import User
from etf_index import ETFIndex
import MySQLdb
import MySQLdb.cursors
import json
#import matplotlib.pyplot as plt


def run(do_debug=False):
	"""
	Main function to run the program.
	"""
	# Create the user object which has all of the credentials
	user = User()

	db = MySQLdb.connect(
		host="134.74.126.107",
		user=user.username,
		passwd=user.password,
		db="F16336team7",
		cursorclass=MySQLdb.cursors.DictCursor
	)

	cursor = db.cursor()
	# Create the object which computes the ETFIndex object
	etf_name = "etf1"
	etf_object = ETFIndex(cursor,etf_name)
	etf_object.debug = do_debug

	# etf_object.trading_symbols
	trading_symbols = etf_object.get_trading_symbols()
	# etf_object.compute_etf_index(etf_object.initial_date, debug_list=True)
	etf_object.compute_monthly_etf(2, 2005)
	# etf_object.compute_yearly_etf()
	#etf_object.compute_time_span_etf(2005, 2006)

	sql_statement = "DELETE FROM ETF_RECORDS;"
	cursor.execute(sql_statement)
	db.commit()

	for item in etf_object.date_and_index:
		sql = "INSERT INTO ETF_RECORDS(TRADE_DATE,TRADING_SYMBOL,ULYING_INDEX) values(%s,%s,%s)"
		cursor.execute(sql,item)
		db.commit()	
		#sql = "INSERT INTO ETF_RECORDS(TRADING_SYMBOL) values(%s)"
	 	#cursor.execute(sql,name)
                #db.commit() 
		
	#print(dates)

if __name__ == "__main__":
	run(True)
