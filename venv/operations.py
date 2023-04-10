input_data = 86467
days = input_data//(60*60*24)
hours = (input_data - days*60*60*24)//(60*60)
minutes = (input_data - days*60*60*24 - hours*60*60)//60
seconds = (input_data - days*60*60*24 - hours*60*60 - minutes*60)
print(days, hours, minutes, seconds)
