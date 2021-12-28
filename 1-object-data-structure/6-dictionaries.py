dict = {'key1':'value1',
				'key2':'value2'}

dict['key1'] # returns 'value1'

prices = {'apple':37.50,
					'orange':50,
					'milk':29.99}

d = {'k1':123,
		 'k2':[0,1,2],
		 'k3':{'insideKey':100}}

d['k2'][0] #returns 0

d['k3']['insideKey'] #returns 100

d['k4'] = 300 #adds key-value pair to dict

d['k1'] = 124 #changes value

d.keys() #returns keys

d.values() #returns valyes

d.items() #returns key value as a tuple in a list
