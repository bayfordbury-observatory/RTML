# RTML

A simple python script to generate RTML based on a template file and a list of targets.

Template for a single target plan, and two target plan (e.g. for observing a standard star) are included.

The input file should be a CSV file. The first four lines should contain
1. Observer name(s)
2. Project name
3. Project description
4. Telescope ID number (found on the telescope setup page)

Subsequent lines should list targets in the following format:

>target_name,right_ascension,declination,filter,exposure_time

Or for two targets:

>target_name1,right_ascension1,declination1,filter1,exposure_time1,target_name2,right_ascension2,declination2,filter2,exposure_time2

Coordinates must be in decimal degrees, and exposure time is in seconds. Filters must match those available on the selected telescope (see telescope setup page).

An example 'input.csv' is included.

Run the script with the input csv and output RTML as arguments, e.g.:

>python loopRTML input.csv out.rtml
