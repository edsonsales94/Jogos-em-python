import pendulum


dt_toronto = pendulum.from_format(transaction_date[:-6], 'YYYY-MM-DD')
dt_vancouver = pendulum.datetime(2012, 1, 1, tz='America/Vancouver')

print(dt_toronto)