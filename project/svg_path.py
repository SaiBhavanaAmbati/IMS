#construct series given the data
def construct_series(list_dates) :
	series_dates = [0,0,0,0,0,0,0,0,0,0,0,0]
	for row in range(len(list_dates)) :
		date_str = str(list_dates[row][0])
		month = date_str.split("-")[1]
		#print(int(month))
		series_dates[int(month)-1] = series_dates[int(month)-1] + 1
	print("series",series_dates)
	return series_dates
# constructs an svg given the series of bins
def construct_path(series_dates) :
	svg = "M0,50 "
	scale_x = 240/12 
	scale_y = 50/max(series_dates)
	#print(max(series_dates))
	for month  in range(12) :
		y = scale_y * series_dates[month]
		#print(y)
		x = scale_x * month
		svg = svg + "L" + str(x) + "," + str(50-y) + " "
	svg = svg + "L200,50 Z"
	return svg

# accepts list of dates to convert to svg		
def construct_svg_path(data):
	dates = [("2018-01-01",0), ("2018-01-06",0), ("2018-01-08",0), ("2018-02-01",0), ("2018-02-02",0), ("2018-02-09",0), ("2018-02-04",0), ("2018-03-09",0), ("2018-03-01",0), ("2018-04-01",0), ("2018-04-05",0),("2018-04-09",0) ,("2018-04-04",0), ("2018-05-01",0), ("2018-06-01",0), ("2018-06-01",0), ("2018-08-01",0)]

	svg_paths = []
	for i in range(4) :
		if len(data[i]) != 0:
			svg_path = construct_path(construct_series(data[i]))
		else  : 
			svg_path = ""
		svg_paths.append(svg_path)
		print(svg_path)
	return svg_paths
"""
dates = [("2018-01-01",0), ("2018-01-06",0), ("2018-01-08",0), ("2018-02-01",0), ("2018-02-02",0), ("2018-02-09",0), ("2018-02-04",0), ("2018-03-09",0), ("2018-03-01",0), ("2018-04-01",0), ("2018-04-05",0),("2018-04-09",0) ,("2018-04-04",0), ("2018-05-01",0), ("2018-06-01",0), ("2018-06-01",0), ("2018-08-01",0)]

print(construct_svg_path([dates,dates,dates,dates])[0])
"""
