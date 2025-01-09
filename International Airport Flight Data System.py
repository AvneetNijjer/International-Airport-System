# Import the turtle Module
import turtle


# Define the passenger_data function
def passenger_data():
    """
    
    Returns
    -------
    list_passengers : 2D List
        This is a 2D list of all the passengers with each passenger's data
        being formatted as followed:
        
        [Passenger's name, First letter of last name, Gate, Seating class, 
        Destination, Arrival status, Baggage weight, Layover status (if 
        applicable)].
    
    Purpose:
    -------
    This function is meant to open the passenger_data.txt file and extract
    each line from within that file creating each line as it's own seperate
    1D list within a 2D lisbob.

    """
    #Import and Open the File
    file_name = "passenger_data_v1.txt" # You can change the file name to
                                        # whatever file needed to open
    file = open(file_name, "r")
    
    # Create an empty list that will be filled with the array of 1D lists
    list_passengers = []
    
    # Read the file line by line, creating each line into a designated 1D list
    for line in file:
        # Remove the \n at the end of each line
        line = line.strip()
        # Split the list according to ,s
        line = line.split(',')
        # Convert every non-string entry into it's data type
        line[6] = float(line[6])
        # Check if the layover status is applicable, if not remove the 7th
        # entry from that 1D list
        if line[7] == "":
            line.pop(7)
        # Append the 1D list into the bigger 2D list
        list_passengers.append(line)
        
    # Return the 2D list
    return list_passengers


# Define the fleet_data function
def fleet_data():
    """

    Returns
    -------
    list_fleet : 2D list
        This is a 2D list of all the planes with each plane's data
        being formatted as followed:
        
        [Plane model, Number of business seats, Number of economy seats, 
        Total number of seats, Gate, Destination, Arrival status, 
        Maximum baggage weight allowed per passenger]
    
    Purpose:
    -------
    This function is meant to open the fleet_data.txt file and extract
    each line from within that file creating each line as it's own seperate
    1D list within a 2D lisbob.

    """
    #Import and Open the File
    file_name = "fleet_data.txt" # You can change the file name to
                                 # whatever file needed to open
    file = open(file_name, "r")
    
    # Create an empty list that will be filled with the array of 1D lists
    list_fleet = []
    
    # Read the file line by line, creating each line into a designated 1D list
    for line in file:
        # Remove the \n at the end of each line
        line = line.strip()
        # Split the list according to ,s
        line = line.split(',')
        # Convert every non-string entry into it's data type
        line[1] = int(line[1])
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[7] = int(line[7])
        # Append the 1D list into the bigger 2D list
        list_fleet.append(line)
    
    # Return the 2D list
    return list_fleet

# Owen Maclennan Function
def daily_data(passenger: list, fleet: list):
    master_data = []
    
    #Add each gate and economy/business seat to 1-D list
    for person in passenger:
        master_data.append(person[3]+person[2])
        
    daily_data = []
    
    #For every plane in fleet list
    for plane in fleet:
        storing_list = []
        
        #Add the gate to the list
        storing_list.append(plane[4])
        
        #Count how many business passengers in current plane
        storing_list.append(master_data.count("B"+plane[4]))
        
        #Count how many economy passengers in current plane
        storing_list.append(master_data.count("E"+plane[4]))
        
        #Append data for current plane to 2-D list
        daily_data.append(storing_list)
        
    return daily_data


def overweight(passenger: list, fleet: list):
    """

    Parameters
    ----------
    passenger : 2D list
        A 2D list (expected to be coming from the passenger_data() fun).
    fleet : 2D list
        A 2D list (expected to be coming from the fleet_data() fun).

    Returns
    -------
    plane_overweight : 2D list
        A list of planes and how many passengers are overweight within that
        specific plane.
    passenger_overweight : 2D list
        A list of passengers, their names, their gate, 
        and by how much that specific passenger is overweight by.
        
    Purpose
    -------
    This will output two different lists one consisting of all the planes
    and how many overweight baggages it contains, while the other addresses
    every passenger in every plane, their names, their gates,
    and by how much they are overweight by.
    

    """
    # Create 2 empty lists to act as the final products
    plane_overweight = [] # A empty 2D list for the planes
    passenger_overweight = [] # A empty 2D list for the passengers
    
    # Iterate through the length of the list coming from fleet
    for i in range(len(fleet)):
        # Create a temporary list for the current plane
        current_plane = []
        # Keep track of how many baggages are overweight within that plane
        overweight = 0
        # Append the model of the plane into the temporary list
        current_plane.append(fleet[i][0])
        
        # Iterate through the length of the list coming from fleet
        for j in range(len(passenger)):
            # Create a temporary list for the current passenger
            current_passenger = []
            # The following if-statement checks which passenger is within the
            # current plane by comparing the following variables: Gate, 
            # Arrival status, Destination
            if((fleet[i][4] == passenger[j][2]) and (fleet[i][5] == passenger[j][4]) and (fleet[i][6] == passenger[j][5])):
                # The following if-statement checks if the passenger is
                # overweight
                if(passenger[j][6] > fleet[i][7]):
                    # Append the following variables into the current
                    # passenger list: Passenger name, last name, gate, 
                    # how much it is overweight by
                    current_passenger.append(passenger[j][0])
                    current_passenger.append(passenger[j][1])
                    current_passenger.append(passenger[j][2])
                    current_passenger.append(passenger[j][6] - fleet[i][7])
                    # Adds one to the current plane overweight count
                    overweight += 1
                    # Appends current passenger list into passenger_overweight
                    passenger_overweight.append(current_passenger)
                    
        # Appends how many passangers are overweight into plane_overweight
        current_plane.append(overweight)
        # Appends current plane list into plane_overweight
        plane_overweight.append(current_plane)
        
    # Return the 2 final lists for planes and passengers
    return plane_overweight, passenger_overweight


def layover(passenger: list, fleet: list):
    """

    Parameters
    ----------
    passenger : 2D list
        A 2D list (expected to be coming from the passenger_data() fun).
    fleet : 2D list
        A 2D list (expected to be coming from the fleet_data() fun).

    Returns
    -------
    plane_layover : 2D list
        A list of planes and how many passengers are lay over within that
        specific plane.
    passenger_layover : 2D list
        A list of passengers, their names, and their gate.

    Purpose
    -------
    This will output two different lists one consisting of all the planes
    and how many layover people it contains, while the other addresses
    every passenger in every plane, their names, and their gate.

    """
    # Create 2 empty lists to act as the final products
    plane_layover = [] # A empty 2D list for the planes
    passenger_layover = [] # A empty 2D list for the passengers
    
    # Iterate through the length of the list coming from fleet
    for i in range(len(fleet)):
        # Create a temporary list for the current plane
        current_plane = []
        # Keep track of how many people are lay over within that plane
        total_layovers = 0
        # Append the model of the plane into the temporary list
        current_plane.append(fleet[i][0])
        
        # Iterate through the length of the list coming from fleet
        for j in range(len(passenger)):
            # Create a temporary list for the current passenger
            current_passenger = []
            # The following if-statement checks which passenger is within the
            # current plane by comparing the following variables: Gate, 
            # Arrival status, Destination
            if((fleet[i][4] == passenger[j][2]) and (fleet[i][5] == passenger[j][4]) and (fleet[i][6] == passenger[j][5])):
                # Tries the command 'passenger[j][7]'
                
                try:
                    passenger[j][7]
                    
                # If performing that command gives an IndexError
                except IndexError:
                    # Keep total layovers the same
                    total_layovers = total_layovers
                    
                # However if the command returns a value and not an error
                else:
                    # Append the following variables into the current
                    # passenger list: Passenger name, last name, gate
                    current_passenger.append(passenger[j][0])
                    current_passenger.append(passenger[j][1])
                    current_passenger.append(passenger[j][2])
                    # Adds one to the current plane layover count
                    total_layovers += 1
                    # Appends current passenger list into passenger_layover
                    passenger_layover.append(current_passenger)
                
                    
        # Appends how many passangers are lay over into plane_layover
        current_plane.append(total_layovers)
        # Appends current plane list into plane_layover
        plane_layover.append(current_plane)
        
    # Return the 2 final lists for planes and passengers
    return plane_layover, passenger_layover


def oversold(passenger: list, fleet: list, daily_data: list):
    """

    Parameters
    ----------
    passenger : 2D list
        A 2D list (expected to be coming from the passenger_data() fun).
    fleet : 2D list
        A 2D list (expected to be coming from the fleet_data() fun).

    Returns
    -------
    fleet_business : 2D list
        List of the plane and how many business seats are oversold.
    fleet_economy : 2D list
        List of the plane and how many economy seats are oversold.
        
    Purpose
    -------
    This will output two different lists one consisting of all the planes
    and how many more business seats were sold than the amount they contain, 
    while the other consists of all the planes and how many more economy 
    seats were sold than the amount they contain.
    
    """
    # Create 2 empty lists to act as the final products
    fleet_business = [] # A empty 2D list for the business seats
    fleet_economy = [] # A empty 2D list for the economy seats
   
    for plane in range(len(fleet)):
         # Create 2 empty lists to act as the current plane
        current_plane_business = [] # A empty 2D list for the business seats
        current_plane_economy = [] # A empty 2D list for the economy seats
      
        # Append the model of the plane into both temporary lists
        current_plane_economy.append(fleet[plane][0])
        current_plane_business.append(fleet[plane][0])
        for data in range(len(daily_data)):
            
            #If the gates match
            if fleet[plane][4]==daily_data[data][0]:
                
                #Number of busines/economy seat for current plane
                business=daily_data[data][1]
                economy=daily_data[data][2]
                
                # If the number of total business seats in the current plane is MORE
                # than the total business seats sold, simply append zero, HOWEVER,
                # if it is LESS then append 'sold - total'
                if (business - fleet[plane][1]) < 0:
                    current_plane_business.append(0)
                else:
                    current_plane_business.append(business - fleet[plane][1])
                # If the number of total economy seats in the current plane is MORE
                # than the total economy seats sold, simply append zero, HOWEVER,
                # if it is LESS then append 'sold - total'
                if (economy - fleet[plane][2] < 0):
                    current_plane_economy.append(0)
                else:
                    current_plane_economy.append(economy - fleet[plane][2])
                
                # Append the current plane's business and economy temporary lists
                # into the final lists
                fleet_business.append(current_plane_business)
                fleet_economy.append(current_plane_economy)
    # Return the 2 final lists for business and economy
    return fleet_business, fleet_economy


# Done as group even though not required with only 4 team members
def time_delay(passenger: list, fleet: list):
    """

    Parameters
    ----------
    passenger : 2D list
        A 2D list (expected to be coming from the passenger_data() fun).
    fleet : 2D list
        A 2D list (expected to be coming from the fleet_data() fun).

    Returns
    -------
    delay : 2D list
        A list of all the planes, and how many passengers have both the late
        and layover status to their name.

    Purpose
    -------
    This will output one list that contains a list for every plane, and how 
    many passangers within that plane have both the late and layover status.

    """
    # Create a list that will contain every plane
    delay = []
    # Iterate through the length of the list coming from fleet
    for i in range(len(fleet)):
        # Create a temporary list for the current plane
        delay_single = []
        # Keep track of how many people are lay over and late within the plane
        timedelay = 0
        # Append the model of the plane into the temporary list
        delay_single.append(fleet[i][0])
        # Iterate through the length of the list coming from fleet
        for j in range(len(passenger)):
            # The following if-statement checks which passenger is within the
            # current plane by comparing the following variables: Gate, 
            # Arrival status, Destination
            if((fleet[i][4] == passenger[j][2]) and (fleet[i][5] == passenger[j][4]) and (fleet[i][6] == passenger[j][5])):
                # Tries the command 'passenger[j][7]'
                try:
                    passenger[j][7]
                # If performing that command gives an IndexError
                except IndexError:
                    # Keep the total late/layovers the same
                    timedelay = timedelay
                # However if the command returns a value and not an error
                else:
                    # Check if that layover passenger is also late
                    if passenger[j][5] == 'Late':
                        # Add 1 to the total layover/late passengers
                        timedelay += 1
                        
        # Appends how many passangers are layover/late into delay_single
        delay_single.append(timedelay)
        # Appends current plane list into delay
        delay.append(delay_single)
        
    # Return the final list for all planes
    return delay


# Define the graphical_teamID function
def graphical_teamID(oversold: list, overweight: list, layover: list, time_delay: list):
    """

    Parameters
    ----------
    oversold : 2D list
        A 2D list (expected to be coming from the oversold() fun).
    overweight : 2D list
        A 2D list (expected to be coming from the overweight() fun).
    layover : 2D list
        A 2D list (expected to be coming from the layover() fun).
    time_delay : 2D list
        A 2D list (expected to be coming from the time_delay() fun).

    Returns
    -------
    Nothing.
    
    Purpose
    -------
    This function takes in all the other functions we have created and
    displays all the information of each plane in the graphical interface
    within it's own table automatically formatted in 5 different columns, 
    and 4 rows.

    """
    # Create a 2D list that will store each information for each plane pre-
    # organized for us in it's own 1D list
    lists_2D = []
    # Iterate through the length oversold's business seats 2D list considering 
    # no matter what it will contain every single plane
    for i in range(len(oversold[0])):
        # Create a single list for each current plane
        lists_1D = []
        # Append the model, and etc into the 1D list
        lists_1D.append(oversold[0][i][0])
        lists_1D.append(f"Oversold Business Seats: {oversold[0][i][1]}")
        lists_1D.append(f"Oversold Economy Seats: {oversold[1][i][1]}")
        lists_1D.append(f"Overweight Bags: {overweight[0][i][1]}")
        lists_1D.append(f"Layover Passengers: {layover[0][i][1]}")
        lists_1D.append(f"Late Layover Passengers: {time_delay[i][1]}")
        # Append that 1D list into the list created for EVERY plane
        lists_2D.append(lists_1D)
    
    # -----------
    # Beyond this point is where the turtle code begins!
    # -----------
    
    # Turtle output
    # Constants (you can change these)
    SCREEN_WIDTH = 1250 # Width of the screen
    SCREEN_HEIGHT = 900 # Height of the screen
    WINDOW_TITLE = "Graphical Interface" # Title of the screen
    
    # Set up the screen object
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT) # Setting the screen up
    screen = turtle.Screen() # Putting the screen object into a variable
    screen.title(WINDOW_TITLE) # Adding the title to our screen object
    
    # Create the turtle object
    bob = turtle.Turtle() # Creating the turtle object and name him bob!
    bob.hideturtle() # Hiding the turtle so that the shape doesnt show
    screen.tracer(0) # Making the tracer speed to zero (it still makes but
                     # it doesn't show to the user until we update it)
    
    # The actual outputing
    current_plane_index = [-600,420] # This keeps track of the index of each
                                     # row's general height and total width
                                     
    # Iterate through the 2D list of all the planes
    for plane in lists_2D:
        # This variable keeps track of the CURRENT plane table's position
        index_of_item = [current_plane_index[0]+100,current_plane_index[1]]
        bob.setheading(0) # Make the turtle face East
        bob.up() # Raise the pen
        # Move the turtle to the starting position but slightly lower
        bob.goto(current_plane_index[0],current_plane_index[1]-50)
        bob.down() # Lower the pen
        bob.fillcolor('blue') # Set the fill color to blue
        bob.begin_fill() # Begin the fill (aka starting)
        
        # Create a rectange of width 200 and height 20
        for i in range(2):
            bob.forward(200)
            bob.left(90)
            bob.forward(20)
            bob.left(90)
            
        bob.end_fill() # Finish the fill (aka fill the object we just drew)
        bob.setheading(0) # Make the turtle face East
        bob.up() # Raise the pen
        # Move the turtle to the starting position for where to print the
        # model of the plane within that rectangle we just drew
        bob.goto(index_of_item[0],index_of_item[1]-47) 
        # Write the plane's model with a font size of 10
        bob.write(plane[0], align = 'center', font = ('Arial', 10, "normal"))
        index_of_item[1] -= 50 # Subtract 50 in the y-axis for the table
                               # near the bottom of the square
        # Iterate through the length of a single plane list
        for item in range(1,len(plane)):
            # Move the turtle 
            bob.setheading(0) # Make the turtle face East
            # Each time the next entry of the table is printed 
            # for the current plane lower the y-axis by 20 for the next entry
            bob.goto(index_of_item[0],index_of_item[1]-20)
            # Write the plane's current item with a font size of 10
            bob.write(plane[item], align = 'center', font = ('Arial', 10, "normal"))
            index_of_item[1] -= 15 # Subtract 15 in the y-axis for the table
                                   # near the bottom of the last item printed

        # Add 210 for the total x-axis of all the axises so that we can start
        # printing the table for the next plane
        current_plane_index[0] += 210
        # If the next table for the next plane goes beyond the screen
        if current_plane_index[0]+200 > 600:
            # Take it to the next row which is 150 below the last row's
            # starting position (within the y-axis) and set the x-axis back to 
            # the original
            current_plane_index[0] = -600
            current_plane_index[1] -= 150
        # However if the final row of the table is printed and the next row
        # goes beyond the screen then end the graphic interface printing
        # process (because there won't be anymore space)
        if current_plane_index[1]-200 < -420:
            break
    
    screen.update()
    screen.exitonclick() 
    turtle.done()


# -----------
# Testing beyond this point
# -----------

# Create an oversold, overweight, layover, daily_data and time delay variables
daily_data=(daily_data(passenger_data(),fleet_data()))
oversold = oversold(passenger_data(), fleet_data(),daily_data)
overweight = overweight(passenger_data(), fleet_data())
layover = layover(passenger_data(), fleet_data())
time_delay = time_delay(passenger_data(), fleet_data())
# Call the graphical_teamID function with all the objects we just made
graphical_teamID(oversold, overweight, layover, time_delay)
