## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        first_trip = trip_reader.__next__()
        
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)
        
    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip
def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    
    # YOUR CODE HERE
    if city == 'Washington' :
        duration = int(datum['Duration (ms)'])/60000
    else :
        duration = int(datum['tripduration'])/60
    
    return duration


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001
def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    
    # YOUR CODE HERE
    if city == 'NYC' :
        starttime = datetime.strptime(datum['starttime'],"%m/%d/%Y %H:%M:%S")
        month = int(starttime.strftime("%m"))
        hour = int(starttime.strftime("%H"))
        day_of_week = starttime.strftime("%A")
    elif city == 'Washington' :
        starttime = datetime.strptime(datum['Start date'],"%m/%d/%Y %H:%M")
        month = int(starttime.strftime("%m"))
        hour = int(starttime.strftime("%H"))
        day_of_week = starttime.strftime("%A")
    elif city == 'Chicago' :
        starttime = datetime.strptime(datum['starttime'],"%m/%d/%Y %H:%M")
        month = int(starttime.strftime("%m"))
        hour = int(starttime.strftime("%H"))
        day_of_week = starttime.strftime("%A")      
    
    return (month, hour, day_of_week)


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

actual = {}

#for city in tests:
#	actual['month'] = time_of_trip(example_trips[city], city)[0]
#	print(actual['month']) 
#
 #    city_total[city] = number_of_trips(filenames['out_file'])[0]
  #   city_subscribers[city] = number_of_trips(filenames['out_file'])[1]

#
#for city in tests:
#    assert time_of_trip(example_trips[city], city) == tests[city]



def mnumber_of_trips(filename, month):
    """
    This function reads in a file with trip data and reports the duration of
    trips made by users.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        
        # initialize count variables
        sub_trips = 0
        cus_trips = 0
        tot_trips = 0
        
        # compute total duration of all trips for subscriber#
        # and customer                                      #
        for row in reader :
        	if row['month'] == str(month):
        		if row['user_type'] == 'Subscriber' :
        			sub_trips += 1
        		else :
        			cus_trips += 1
        
        # Calculate Total trip duration                     #

        tot_trips = sub_trips + cus_trips
        
        # return tallies as a tuple
        return(sub_trips, cus_trips, tot_trips)

print(mnumber_of_trips('./data/NYC-2016-Summary.csv', 1))


