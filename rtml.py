from urllib.request import urlopen
import json

#start of RTML
start = '<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n<RTML version=\"2.3\">\n  <Contact>\n    <User/>\n    <Email/>\n    <Organization>University of Hertfordshire</Organization>\n  </Contact>\n'

#open templates
file = open("plan_template_one_target.rtml", "r")

template1 = file.read()

file.close()

#open templates
file = open("plan_template_two_targets.rtml", "r")

template2 = file.read()

file.close()

#file to output created RTML
output = open("out.rtml", "w", newline='\r\n')

#output start of RTML
out = output.write(start)

#read input csv
file1 = open('input.csv', 'r')
Lines = file1.readlines()

#count number of lines
i=0

# Strips the newline character
for line in Lines:

	print(line.strip())

	if i==0:
		observer = line.strip()
	elif i==1:
		project = line.strip()
	elif i==2:
		description = line.strip()
	elif i==3:
		telescope = line.strip()
	else:

		column = line.split(",")

		if len(column)==10:
			plan = template2
		else:
			plan = template1

		plan = plan.replace("$OBSERVER", observer)
		plan = plan.replace("$PROJECT", project)
		plan = plan.replace("$DESCRIPTION", description)
		plan = plan.replace("$TELESCOPE", telescope)
		
		target1 = column[0].strip()
		ra1 = column[1].strip()
		dec1 = column[2].strip()
		filter1 = column[3].strip()
		exp1 = column[4].strip()

		plan = plan.replace("$TARGET1", target1)
		plan = plan.replace("$RA1", ra1)
		plan = plan.replace("$DEC1", dec1)
		plan = plan.replace("$FILTER1", filter1)
		plan = plan.replace("$EXP1", exp1)
		
		if len(column)==10:
			#two targets	
			
			target2 = column[5].strip()
			ra2 = column[6].strip()
			dec2 = column[7].strip()
			filter2 = column[8].strip()
			exp2 = column[9].strip()

			plan = plan.replace("$TARGET2", target2)
			plan = plan.replace("$RA2", ra2)
			plan = plan.replace("$DEC2", dec2)
			plan = plan.replace("$FILTER2", filter2)
			plan = plan.replace("$EXP2", exp2)

		#write the plan RTML to file
		out = output.write(plan)
	
	i=i+1

#output end
out = output.write("</RTML>")

output.close()

print("Done")