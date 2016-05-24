#### ESCAPE THE ROOM ####
## Now add in the read_notebook and display_health functionality

from sys import exit # import the exit function

### CURRENT TURN OPTIONS ###
cur_choose_door = False
cur_inspect = False
cur_fight = False
cur_read_notebook = False
cur_display_health = False
cur_quit_game = True

## ACTIONS GATE ## 
choose_door = True # this is pretty much always true, every room has a 'door'
inspect = True # always on, might not always return anything
fight = False # only becomes available when user has sword
read_notebook = True # always on, always have the option to read the notebook
display_health = True # always on, always have the option to see health
quit_game = True # action always available so you can leave the game at every step

actions = [ # available actions in the game
		   'choose door', 'inspect',
		   'fight', 'read notebook', 
		   'display health', 'quit game'
		  ]

## TOOLS GATE ## 
key = False
antidote = False
shield = False
sword = False
invisible_cloak = False

tools = ['key', 'antidote', 'shield', 'sword', 'invisible cloak'] # available tools in the game

## ATTRIBUTES ## 
health = 100
notebook = "\n---------------NOTEBOOK---------------\n"

############################################################
###### INSPECT ATTRIBUTES ##################################
############################################################




############################################################
###### ROOM ACTIONS ########################################
############################################################

### MAIN ROOM ACTIONS ###
main_rm_choose_door = True # can always choose a room to move through 
main_rm_inspect = True # in main room, you can inspect
main_rm_fight = False # you cant fight the main room, sadly
main_rm_read_notebook = True # you can always read your notebook
main_rm_display_health = True # you can always display your health
main_rm_quit_game = True # always can quit the game

### SNAKE PIT ROOM ACTIONS ###
snake_rm_choose_door = True
snake_rm_inspect = False
snake_rm_fight = False
snake_rm_read_notebook = True
snake_rm_display_health = True
snake_rm_quit_game = True

### CTHULHU ROOM ACTIONS ###
cthulhu_rm_choose_door = True
cthulhu_rm_inspect = False # false until you kill cthulhu
cthulhu_rm_fight = True 
cthulhu_rm_read_notebook = True
cthulhu_rm_display_health = True
cthulhu_rm_quit_game = True

### DRAGON ROOM ACTIONS ###
dragon_rm_choose_door = True
dragon_rm_inspect = True 
dragon_rm_fight = True
dragon_rm_read_notebook = True
dragon_rm_display_health = True
dragon_rm_quit_game = True

### PRISON CELL ACTIONS ###
prison_cell_choose_door = True
prison_cell_inspect = True
prison_cell_fight = False
prison_cell_read_notebook = True
prison_cell_display_health = True
prison_cell_quit_game = True

### MAIN TOWER ROOM ACTIONS ###
main_tower_choose_door = True
main_tower_inspect = True
main_tower_fight = False
main_tower_read_notebook = True
main_tower_display_health = True
main_tower_quit_game = True

### WEST TOWER ROOM ACTIONS
west_tower_choose_door = True
west_tower_inspect = True
west_tower_fight = False
west_tower_read_notebook = True
west_tower_display_health = True
west_tower_quit_game = True

### witch ROOM ACTION ###
witch_rm_choose_door = True
witch_rm_inspect = False # false until you kill cthulhu
witch_rm_fight = True
witch_rm_read_notebook = True
witch_rm_display_health = True
witch_rm_quit_game = True


## ROOM DOORS ##
north_door = True 
west_door = True
east_door = True
south_door = True
ladder = True

# doors names for printing/display
door_names = ['north door','east door',
              'west door','south door',
			  'ladder']


### INITIALIZE ###
def init_Act_Opts():
	choose_door = True
	inspect = True 
	fight = False
	read_notebook = True
	display_health = True
	quit_game = True 

def init_Tools():	
	key = False
	antidote = False
	shield = False
	sword = False
	invisible_cloak = False
	
def init_Attr():
	health = 10	
	notebook = "<<<NOTEBOOK>>>\n---------------\n"

##############################################################################
### DISPLAY ##################################################################
##############################################################################

def disp_Cur_Opts():
	"""this function will display the available actions that 
	the user has based on their current decision in the house."""
	# define action list
	cur_action_options = [cur_choose_door, cur_inspect,cur_fight,
						  cur_read_notebook, cur_display_health, 
						  cur_quit_game]
	i = 0 # index used in display

	print "\n-------Available Moves--------\n"

	for action in cur_action_options:
		if action == True:
			print "%s is AVAILABLE" % actions[i] #print the el that is true
		# else:
		# 	print "%s is NOT FOUND" % actions[i] # print the el that is false
		i += 1

def disp_Tools():
	"""this function will display the available tools that 
	the user has based on current decision in the house."""	
	
	tools = [key, antidote, shield, sword, invisible_cloak] #define the tools list
	i = 0 #index for display
	
	print "These are your available tools"
	for tool in tools:
		if tool == True:
			print "%s is AVAILABLE" % tools[i] # print out the tool
		# else:
		# 	print "%s is NOT FOUND" % tools[i] # print out the tool
		i += 1	

def disp_Avail_Doors(control):
	""" this function displays the available doors that the user
	can pick from based on current location in the house - determined by 
	control """
	# we know that each room has a different set of available doors, we need
	# to determine how those are displayed and then a valid choice selected

	doors = [north_door, east_door, west_door, south_door, ladder]
	i = 0 # index for display

	print "\n-----------Doors available-----------\n"
	for door in doors:
		if door == True:
			print "%s is AVAILABLE" % door_names[i] # print out door namae
		# else:
		# 	print "%s is NOT AVAILALBE" % door_names[i] # print out door name
		i += 1

def read_Notebook():
	print notebook

def disp_Health():
	print "\n>>> HEALTH: %d" % health

def healthy_To_Continue():
	if health <= 0:
		print "\nYou ran out of health!"	
		dead()
	else:
		disp_Health()


##############################################################################
### UPDATE CURRENT OPTIONS AND ROOMS #########################################
##############################################################################

def update_Cur_Opts(control):
	""" 
	This function updates the current user action options based on
	control (i.e. what entity the user is facing - monster, room, etc)
	"""
	
	## need to know what room/monster/entity we are facing
	## and what tools we have to dictate the available options
	global cur_choose_door 
	global cur_inspect
	global cur_fight
	global cur_read_notebook
	global cur_display_health
	global cur_quit_game

	# if we're in the main room, let's determine what you can do with the room
	if control == 'main room':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN - 
		# # we know this is updating correctly
		# disp_Cur_Opts() # CLEAN - we know this is updating correctly
		# # updating current options based on decision point
		cur_choose_door = (choose_door and main_rm_choose_door)
		cur_inspect = (inspect and main_rm_inspect)
		cur_fight = (fight and main_rm_fight)
		cur_read_notebook = (read_notebook and main_rm_read_notebook)
		cur_display_health = (display_health and main_rm_display_health)
		cur_quit_game = (quit_game and main_rm_quit_game)

		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts() # CLEAN

	elif control == 'snake pit':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# # updating current options based on decision point
		cur_choose_door = (choose_door and snake_rm_choose_door)
		cur_inspect = (inspect and snake_rm_inspect)
		cur_fight = (fight and snake_rm_fight)
		cur_read_notebook = (read_notebook and snake_rm_read_notebook)
		cur_display_health = (display_health and snake_rm_display_health)
		cur_quit_game = (quit_game and snake_rm_quit_game) 

		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	elif control == 'cthulhu room':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# # updating current options based on decision point
		cur_choose_door = (choose_door and cthulhu_rm_choose_door)
		cur_inspect = (inspect and cthulhu_rm_inspect)
		cur_fight = (fight and cthulhu_rm_fight)
		cur_read_notebook = (read_notebook and cthulhu_rm_read_notebook)
		cur_display_health = (display_health and cthulhu_rm_display_health)
		cur_quit_game = (quit_game and cthulhu_rm_quit_game) 

		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	elif control == 'dragon room':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# # updating current options based on decision point
		cur_choose_door = (choose_door and dragon_rm_choose_door)
		cur_inspect = (inspect and dragon_rm_inspect)
		cur_fight = (fight and dragon_rm_fight)
		cur_read_notebook = (read_notebook and dragon_rm_read_notebook)
		cur_display_health = (display_health and dragon_rm_display_health)
		cur_quit_game = (quit_game and dragon_rm_quit_game) 
		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	elif control == 'prison cell':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# # updating current options based on decision point
		cur_choose_door = (choose_door and prison_cell_choose_door)
		cur_inspect = (inspect and prison_cell_inspect)
		cur_fight = (fight and prison_cell_fight)
		cur_read_notebook = (read_notebook and prison_cell_read_notebook)
		cur_display_health = (display_health and prison_cell_display_health)
		cur_quit_game = (quit_game and prison_cell_quit_game)
		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	elif control == 'main tower':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# updating current options based on decision point
		cur_choose_door = (choose_door and main_tower_choose_door)
		cur_inspect = (inspect and main_tower_inspect)
		cur_fight = (fight and main_tower_fight)
		cur_read_notebook = (read_notebook and main_tower_read_notebook)
		cur_display_health = (display_health and main_tower_display_health)
		cur_quit_game = (quit_game and main_tower_quit_game)		
		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()		

	elif control == 'west tower':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# updating current options based on decision point
		cur_choose_door = (choose_door and west_tower_choose_door)
		cur_inspect = (inspect and west_tower_inspect)
		cur_fight = (fight and west_tower_fight)
		cur_read_notebook = (read_notebook and west_tower_read_notebook)
		cur_display_health = (display_health and west_tower_display_health)
		cur_quit_game = (quit_game and west_tower_quit_game) 		
		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	elif control == 'witch room':
		# print "\nBEFORE update_Cur_Opts() RUNS for %s" % control# CLEAN -
		# disp_Cur_Opts() 
		# updating current options based on decision point
		cur_choose_door = (choose_door and witch_rm_choose_door)
		cur_inspect = (inspect and witch_rm_inspect)
		cur_fight = (fight and witch_rm_fight)
		cur_read_notebook = (read_notebook and witch_rm_read_notebook)
		cur_display_health = (display_health and witch_rm_display_health)
		cur_quit_game = (quit_game and witch_rm_quit_game)		
		# print "\nAFTER update_Cur_Opts() for %s" % control # CLEAN
		disp_Cur_Opts()

	else: 
		print "\nDEBUG IN update_Cur_Opts() - probably haven't accounted\
		       for this %s control statement" % control # CLEAN


def update_Avail_Rooms(control):
	"""
	This function updates the available room booleans based on what room
	the user is in. There is no need to account for being sent an
	arbitrary decision node because that will be accounted for further up
	the stack
	"""

	global north_door
	global west_door
	global east_door
	global south_door
	global ladder

	# we make a branch for each room
	if control == 'main room':
		north_door = True
		west_door = True
		east_door = True
		south_door = True
		ladder = False
	elif control == 'snake pit':
		north_door = False
		west_door = False
		east_door = False
		south_door = True
		ladder = True
	elif control == 'cthulhu room':
		north_door = False
		west_door = False
		east_door = True
		south_door = False
		ladder = False
	elif control == 'dragon room':
		north_door = True
		west_door = False
		east_door = False
		south_door = False
		ladder = False
	elif control == 'prison cell':
		north_door = False
		west_door = True
		east_door = False
		south_door = False
		ladder = False
	elif control == 'main tower':
		north_door = False
		west_door = True
		east_door = True
		south_door = False
		ladder = True
	elif control == 'west tower':
		north_door = False
		west_door = False
		east_door = True
		south_door = False
		ladder = False
	elif control == 'witch room':
		north_door = False
		west_door = True
		east_door = False
		south_door = False
		ladder = False
	else:
		print "\n%s NOT HANDLED IN update_Avail_Rooms()" % control# update needed here

def update_Health(next_room):
	global health
	# assumes next_room is valid, based on door_Decision
	if next_room == 'snake pit':
		if antidote:
			print "\nThe antidote you found is making you impervious to the venom"
		else:
			print "\nThe snakes are bitting you!\nYou lost 2 health points\n"
			health = health - 2
			healthy_To_Continue()

	elif next_room == 'dragon room':
		if invisible_cloak:
			print "\nThe dragon can't see you! This cloak must disguise you from sight"
		else:		
			print "\nThe dragon can see you and scorched you!\nYou lost 4 health points\n"
			health = health - 4
			healthy_To_Continue()

	elif next_room == 'cthulhu room':
		if invisible_cloak and sword and shield and antidote:
			print "\nYou're impervious to Cthulhu's attacks!"
		else:
			print "\nCthulhu chomped your arm!\nYou lost 3 health points\n"
			health = health - 3
			healthy_To_Continue()
	elif next_room == 'prison cell':
		print "\nWhew, no monsters attack you."
	else:
		None


##############################################################################
#### UPDATE GAME STATE AND DECISION NODES ####################################
##############################################################################

def update_Game_State(control):
	valid_requested_move = False # control gate for while block
	
	print "\n>>>>>>>>>>>> CURRENT MOVE <<<<<<<<<<<<\n\n"\
	      "You're in the %s" % control
	update_Cur_Opts(control) # update our current user action options

	while not valid_requested_move:
		# requested_move will be the action that the user requests to take next
		# will perform sanity checks at each level but will eventually pass
		# that request up to control which will dictate the next move
		requested_move = raw_input("\nWhat would you like to do?\n>> ")
		valid_requested_move = check_Valid_Move(requested_move)

		# now we need to update the state of the game based on choice
		if valid_requested_move and (requested_move == 'choose door'):
			outcome = door_Decision(control)
			return outcome
		elif valid_requested_move and (requested_move == 'inspect'):
			inspect_Object(control)
			return control 
		elif valid_requested_move and (requested_move == 'fight'):
			fight_Monster(control) # fight the monster in the room that you're in
			return control
		elif valid_requested_move and (requested_move == 'read notebook'):
			read_Notebook()
			return control
		elif valid_requested_move and (requested_move == 'display health'):
			disp_Health()
			return control
		elif valid_requested_move and (requested_move == 'quit game'):
			print "\nYou give up and sit in a corner, then..."
			dead()
		else:
			print "\nDEBUG >> bottom of update_Game_State - control: %s and"\
			      " requested move %s" % (control, requested_move)


##############################################################################
#### DOOR DECISION NODES #####################################################
##############################################################################

def door_Decision(control):
	"""
	This node will hold the decision making for choosing a door
	This needs to return the room that the player will
	move into
	"""
	valid_door_choice = False 

	update_Avail_Rooms(control)

	while not valid_door_choice: # while invalid_door selection still true
		disp_Avail_Doors(control)
		door_choice = raw_input("\nWhich door will you take?\n>> ")
		valid_door_choice = check_Valid_Door_Selection(door_choice)
	
		if valid_door_choice: # these are valid
			print going_through_doorway
			next_room = determine_Next_Room(control, door_choice)
			update_Health(next_room) # this node will update the health of the user
			# each time they move into certain rooms.
			return next_room
		else:
			print "\nPlease choose again"

def determine_Next_Room(control, door_choice):
	"""
	Takes 2 inputs, first input is which room
	This function assumes that it only called when control is a valid room 
	and door_choice is appropriate for that room
	"""

	if control == 'main room':
		if door_choice == 'north door':
			return 'snake pit'
		elif door_choice == 'west door':
			return 'cthulhu room'
		elif door_choice == 'east door':
			return 'prison cell'
		elif door_choice == 'south door':
			return 'dragon room'
		else:
			print "DEBUG >> BOTTOM OF 'main room' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'snake pit':
		if door_choice == 'south door':
			return 'main room'
		elif door_choice == 'ladder':
			return 'main tower'
		else:
			print "DEBUG >> BOTTOM of 'snake pit' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'cthulhu room':
		if door_choice == 'east door':
			return 'main room'
		else: 
			print "DEBUG >> BOTTOM of 'cthulhu room' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'dragon room':
		if door_choice == 'north door':
			return 'main room'
		else:
			print "DEBUG >> BOTTOM OF 'dragon room' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'prison cell':
		if door_choice == 'west door':
			return 'main room'
		else:
			print "DEBUG >> BOTTOM OF 'prison cell' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'main tower':
		if door_choice == 'west door':
			return 'west tower'
		elif door_choice == 'east door':
			return 'witch room'
		elif door_choice == 'ladder':
			return 'snake pit'
		else:
			print "DEBUG >> BOTTOM OF 'prison cell' determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice)
			return 'INVALID'
	elif control == 'west tower':
		if door_choice == 'east door':
			return 'main tower'
		else:
			print "DEBUG >> BOTTOM OF west tower determine_Next_Room() "\
			      "branch for %s and %s" % (control, door_choice) 		
	elif control == 'witch room':
		if door_choice == 'west door':
			return 'main tower'
		else:
			print "DEBUG >> BOTTOM OF witch room determine_Next_Room() "\
				  "branch for %s and %s" % (control, door_choice) 		
	else:
		print "DEBUG >> BOTTOM OF outer stack determine_Next_Room() "\
		      "branch for %s and %s" % (control, door_choice)
		return 'INVALID'
	
##############################################################################
#### FIGHT DECISION NODES ####################################################
##############################################################################

def fight_Monster(control):
	"""
	Fight decision determined by the room that the user is in, as that will
	dictate who they are facing.
	"""
	global dragon_rm_fight
	global witch_rm_fight
	global cthulhu_rm_fight

	global witch_rm_inspect
	global cthulhu_rm_inspect

	
	if control == 'dragon room':
		if invisible_cloak:
			print "\nYou slayed the dragon, nice work!"
		
			dragon_rm_fight = False
		else:
			print "\nYou slayed the dragon!"
			print "...but he saw you attack and killed you as you threw"\
			      " your sword at him"
			dead()


	elif control == 'cthulhu room':
		if invisible_cloak and sword and shield and antidote:
			print "\nYou attack Cthulhu and chop his head off!"
			print "\nHis body rolls off the perch and falls down the stairs"
			
			cthulhu_rm_fight = False
			cthulhu_rm_inspect = True
	
		else:
			print "\nYou don't have the tools to take on Cthulhu!"
			print "\nHe rises from the chair and destroys you."
			dead()
	elif control == 'witch room':
		print "\nYou attack the witch with ferocity!"
		print "\nThe witch is dead!"

		witch_rm_fight = False
		witch_rm_inspect = True

	else:
		print "\nDEBUG >> UNHANDLED CONTROL IN fight_Monster(%s)" % control

##############################################################################
#### INSPECT DECISION NODE  ##################################################
##############################################################################

def inspect_Object(control):
	"""
	This function will perform the inspection of objects within a room and update 
	the various driver variables accordingly.

	This never changes control, i.e. the location of the user.
	"""
	global main_rm_inspect
	global cthulhu_rm_inspect
	global dragon_rm_inspect
	global prison_cell_inspect
	global snake_rm_inspect
	global main_tower_inspect
	global west_tower_inspect
	global witch_rm_inspect

	global shield
	global sword
	global invisible_cloak
	global key
	global antidote

	global fight

	
	if control == 'main room' and main_rm_inspect:
		# object to inspect is the chest
		print "\nThere seems to be a chest over here..."\
		      "you open it up to find instructions\n"
		update_Notebook('chest')
		read_Notebook()
		main_rm_inspect = False # set this to false because we've inspected the main room

	elif control == 'dragon room' and dragon_rm_inspect:
		print "\nThere is something shiny in the corner, it's a shield!"
		update_Notebook('shield')
		read_Notebook()
		shield = True
		dragon_rm_inspect = False

	elif control == 'prison cell' and prison_cell_inspect:
		print "\nThere is skull in the middle of the floor"\
		      " you look inside and find a key"
		update_Notebook('skull')
		read_Notebook()
		prison_cell_inspect = False
		antidote = True

	elif control == 'main tower' and main_tower_inspect:
		print "\nThere is a box in the corner..."
		if sword:
			print "\nYou smash open the container with the sword"
			print "\nYou find a **KEY** and some instructions"
			update_Notebook('box')
			read_Notebook()
			main_tower_inspect = False
			key = True
		else:
			print "\nThe box looks too strong, if only you had a weapon"\
			      " to break it open"
	elif control == 'cthulhu room' and cthulhu_rm_inspect:
		print "\nThere is a trap door under the body!"
		if key:
			print "\nThe key you found fits perfectly into the lock"
			escaped()
		else:
			print "\nThere is a sturdy looking lock here"

	elif control == 'west tower' and west_tower_inspect:
		print "\nThere is sword here! Hope you know how to use it!"
		
		update_Notebook('sword')
		read_Notebook()
		west_tower_inspect = False
		sword = True
		fight = True

	elif control == 'witch room' and witch_rm_inspect:
		print "\nYou inspect the dead witch...\n"\
		      "Looks like there is some sort of cloak here, you put it on"
		
		update_Notebook('invisible cloak')
		read_Notebook()
		witch_rm_inspect = False
		invisible_cloak = True
	else:
		print "\n UNHANDLED control in inspect_Object()"

def update_Notebook(entity):
	global notebook

	if entity == 'chest':
		notebook += "\nWithout a weapon, you'll never escape alive!!!\n"
	elif entity == 'skull':
		notebook += "\nYou must disguise yourself to get past the dragon...\n"
	elif entity == 'sword':
		notebook += "\nBe careful who you fight...\n"
	elif entity == 'box':
		notebook += "\nAlways inspect dead opponents, they might "\
		            "hold something you need to escape\n"
	elif entity == 'shield':
		notebook += "\nThe escape is hidden"
	elif entity == 'invisible cloak':
		notebook += "\nYou must find the key to escape!"
	else:
		print "\nINSIDE add_Instructions() - unhandled entity %s" % entity

##############################################################################
#### VALIDITY CHECKS #########################################################
##############################################################################

def check_Valid_Move(requested_move):
	# need this to determine if input was part of the valid curr action opts
	if requested_move == 'choose door' and cur_choose_door:
		return True
	elif requested_move == 'inspect' and cur_inspect:
		return True
	elif requested_move == 'fight' and cur_fight:
		return True
	elif requested_move == 'read notebook' and cur_read_notebook:
		return True
	elif requested_move == 'display health' and cur_display_health:
		return True
	elif requested_move == 'quit game' and cur_quit_game:
		return True
	else:
		print "\nERROR: Please choose valid move"	# CLEAR

def check_Valid_Door_Selection(door_choice):
	"""
	This function determines if the input for door choice is valid based
	on location of the user
	"""
	if door_choice == 'north door' and north_door:
		return True
	elif door_choice == 'west door' and west_door:
		return True
	elif door_choice == 'east door' and east_door:
		return True
	elif door_choice == 'south door' and south_door:
		return True
	elif door_choice == 'ladder' and ladder:
		return True
	else:
		print "INVALID"
		return False

##############################################################################
### CONTROL OF GAME ##########################################################
##############################################################################

# define a die function to quit
def dead():
	print "You're dead"
	exit(0)

# define an escaped function
def escaped():
	print "You escaped!"
	exit(0)

#define a start function - need to build out
def start():
	"""start is the decision making hub - this is where things happen
	and control of the flow is dictated"""

	# control - this is the element that is used to update current game state
	# 

	# initialize
	init_Attr()
	init_Tools()
	init_Act_Opts()

	control = 'main room' # this is going to control the flow of the game
	
	# main room
	# chest
	# dragon room
	while control != None:
		if control == 'main room': # check to see if in main room
			control = update_Game_State(control) # pass information into main room
		# elif control == some_door or other action
			# execute that action and return the information necessary to update game state
		elif control == 'snake pit': # we're in the snape pit, pass control
				# update player stats - i.e. subtract health
			control = update_Game_State(control) # pass control back 
		elif control == 'cthulhu room': # we're in the snape pit, pass control
			# into update_Game_State
			control = update_Game_State(control) # pass control back 
				
		elif control == 'dragon room':
			control = update_Game_State(control)

		elif control == 'prison cell':
			control = update_Game_State(control)
		
		elif control == 'main tower':
			control = update_Game_State(control)

		elif control == 'west tower':
			control = update_Game_State(control)

		elif control == 'witch room':
			control = update_Game_State(control)

		else:
			print "DEBUG >> %r - START()" % control
			dead()

##############################################################################
### GRAPHICS #################################################################
##############################################################################

going_through_doorway = """
        0   /
-----  -|- /-----
       / \           
"""

key = """

  
"""

inspect = """     
   ***
  *****
   ***
  / /
 / /
/ /

^that's a magnifying glass

"""
##############################################################################



##
# DEBUG helpers
##

def debugGetTools():
	global invisible_cloak
	global key
	global antidote
	global shield 
	global sword

	key = True
	antidote = True
	shield = True
	sword = True
	invisible_cloak = True


