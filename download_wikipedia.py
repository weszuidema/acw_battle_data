# Imports packages I need for script

import requests
import json
import os

# Creates list of all battles we need to find data for.
# I'd like to read this directly from the .csv, but this is how I got it to work for now.

battles = ["Battle_of_Day's_Gap", "Battle_of_Athens_(1864)", "Battle_of_Mobile_Bay", "Battle_of_Decatur", "Battle_of_Spanish_Fort", "Battle_of_Fort_Blakely", "Battle_of_Selma", "Battle_of_Pea_Ridge", "Battle_of_Saint_Charles", "Battle_of_Cotton_Plant", "Battle_of_Cane_Hill", "Battle_of_Prairie_Grove", "Battle_of_Fort_Hindman", "Battle_of_Chalk_Bluff", "Battle_of_Helena", "Battle_of_Devil's_Backbone", "Battle_of_Bayou_Fourche", "Battle_of_Pine_Bluff", "Battle_of_Elkin's_Ferry", "Battle_of_Prairie_D'Ane", "Battle_of_Poison_Spring", "Battle_of_Marks'_Mills", "Battle_of_Jenkins'_Ferry", "Battle_of_Old_River_Lake", "Sand_Creek_massacre", "Battle_of_Fort_Stevens", "Battle_of_Santa_Rosa_Island", "Battle_of_Tampa", "Battle_of_Saint_John's_Bluff", "Battle_of_Fort_Brooke", "Battle_of_Olustee", "Battle_of_Natural_Bridge", "Battle_of_Fort_Pulaski", "Battle_of_Fort_McAllister_I", "Battle_of_Davis's_Cross_Roads", "Battle_of_Chickamauga", "Battle_of_Ringgold_Gap", "First_Battle_of_Dalton", "Battle_of_Rocky_Face_Ridge", "Battle_of_Resaca", "Battle_of_Adairsville", "Battle_of_New_Hope_Church", "Battle_of_Dallas", "Battle_of_Pickett's_Mill", "Battle_of_Marietta", "Battle_of_Kolb's_Farm", "Battle_of_Kennesaw_Mountain", "Battle_of_Peachtree_Creek", "Battle_of_Atlanta", "Battle_of_Ezra_Church", "Battle_of_Utoy_Creek", "Second_Battle_of_Dalton", "Battle_of_Lovejoy's_Station", "Battle_of_Jonesborough", "Battle_of_Allatoona", "Battle_of_Griswoldville", 
"Battle_of_Buck_Head_Creek", "Battle_of_Waynesboro_(Georgia)", "Second_Battle_of_Fort_McAllister", "Bear_River_Massacre", "Battle_of_Corydon", "Lawrence_Massacre", "Battle_of_Fort_Blair", "Battle_of_Mine_Creek", "Battle_of_Marais_des_Cygnes", "Battle_of_Barbourville", "Battle_of_Camp_Wildcat", "Battle_of_Ivy_Mountain", "Battle_of_Rowlett's_Station", "Battle_of_Middle_Creek", "Battle_of_Mill_Springs", "Battle_of_Richmond", "Battle_of_Munfordville", "Battle_of_Perryville", "Battle_of_Paducah", "Battle_of_Cynthiana", "Battle_of_Forts_Jackson_and_St._Philip", "Capture_of_New_Orleans", "Battle_of_Baton_Rouge_(1862)", "First_Battle_of_Donaldsonville", "Battle_of_Georgia_Landing", "Battle_of_Fort_Bisland", "Battle_of_Irish_Bend", "Battle_of_Vermillion_Bayou", "Battle_of_Plains_Store", "Siege_of_Port_Hudson", "Battle_of_Milliken's_Bend", "Battle_of_LaFourche_Crossing", "Second_Battle_of_Donaldsonville", "Battle_of_Goodrich's_Landing", "Battle_of_Kock's_Plantation", "Battle_of_Stirling's_Plantation", "Battle_of_Fort_De_Russy", "Battle_of_Mansfield", "Battle_of_Pleasant_Hill", "Battle_of_Blair's_Landing", "Battle_of_Monett's_Ferry", "Battle_of_Mansura", "Battle_of_Yellow_Bayou", "Battle_of_Hancock", "Battle_of_South_Mountain", "Battle_of_Antietam", "Battle_of_Williamsport", "Battle_of_Boonsboro", "Battle_of_Monocacy", "Battle_of_Folck's_Mill", "Battle_of_Fort_Ridgely", "Battle_of_Wood_Lake", "Battle_of_Boonville", "Battle_of_Carthage_(1861)", "Battle_of_Liberty", "Battle_of_Wilson's_Creek", "Battle_of_Dry_Wood_Creek", "First_Battle_of_Lexington", "Battle_of_Fredericktown", "First_Battle_of_Springfield", "Battle_of_Belmont", "Battle_of_Mount_Zion_Church", "Battle_of_Roan's_Tan_Yard", "Battle_of_Island_Number_Ten", "Battle_of_Kirksville", "First_Battle_of_Independence", "Battle_of_Lone_Jack", "First_Battle_of_Newtonia", "Battle_of_Clark's_Mill", "Second_Battle_of_Springfield", "Battle_of_Hartville", "Battle_of_Cape_Girardeau", "Battle_of_Fort_Davidson", "Battle_of_Glasgow", "Second_Battle_of_Lexington", "Battle_of_Little_Blue_River", 
"Second_Battle_of_Independence", "Battle_of_Byram's_Ford", "Battle_of_Westport", "Battle_of_Marmiton_River", "Second_Battle_of_Newtonia", "Battle_of_Iuka", "Second_Battle_of_Corinth", "Battle_of_Chickasaw_Bayou", "Battle_of_Grand_Gulf", "Battle_of_Snyder's_Bluff", "Battle_of_Port_Gibson", "Battle_of_Raymond", "Battle_of_Jackson,_Mississippi", "Battle_of_Champion_Hill", "Battle_of_Big_Black_River_Bridge", "Siege_of_Vicksburg", "Battle_of_Meridian", "Battle_of_Okolona", "Battle_of_Brice's_Crossroads", "Battle_of_Tupelo", "Siege_of_Corinth", "Battle_of_Hatteras_Inlet_Batteries", "Battle_of_Roanoke_Island", "Battle_of_New_Bern", "Battle_of_Fort_Macon", "Battle_of_South_Mills", "Battle_of_Tranter's_Creek", "Battle_of_Kinston", "Battle_of_White_Hall", "Battle_of_Goldsboro_Bridge", "Battle_of_Fort_Anderson", "Battle_of_Washington", "Battle_of_Plymouth_(1864)", "Battle_of_Albemarle_Sound", "First_Battle_of_Fort_Fisher", "Second_Battle_of_Fort_Fisher", "Battle_of_Wilmington", "Battle_of_Wyse_Fork", "Battle_of_Monroe's_Crossroads", "Battle_of_Averasborough", "Battle_of_Bentonville", "Battle_of_Big_Mound", "Battle_of_Dead_Buffalo_Lake", "Battle_of_Stony_Lake", "Battle_of_Whitestone_Hill", "Battle_of_Killdeer_Mountain", "Battle_of_Valverde", "Battle_of_Glorieta_Pass", "Battle_of_Buffington_Island", "Battle_of_Salineville", "Battle_of_Round_Mountain", "Battle_of_Chusto-Talasah", "Battle_of_Chustenahlah", "Battle_of_Old_Fort_Wayne", "Battle_of_Middle_Boggy_Depot", "Battle_of_Cabin_Creek", "Battle_of_Honey_Springs", "Battle_of_Hanover", "Battle_of_Gettysburg", "Battle_of_Fort_Sumter", "Battle_of_James_Island", "Battle_of_Simmon's_Bluff", "First_Battle_of_Charleston_Harbor", "First_Battle_of_Fort_Wagner", "Battle_of_Grimball's_Landing", "Second_Battle_of_Fort_Wagner", "Second_Battle_of_Charleston_Harbor", "Second_Battle_of_Fort_Sumter", "Battle_of_Honey_Hill", "Battle_of_Rivers'_Bridge", "Battle_of_Fort_Henry", "Battle_of_Fort_Donelson", "Battle_of_Shiloh", "Battle_of_Memphis", "First_Battle_of_Chattanooga", "First_Battle_of_Murfreesboro", "Battle_of_Hatchie's_Bridge", "Battle_of_Hartsville", "Battle_of_Jackson,_Tennessee", "Battle_of_Stones_River", "Battle_of_Parker's_Cross_Roads", 
"Battle_of_Dover_(1863)", "Battle_of_Thompson's_Station", "Battle_of_Vaught's_Hill", "Battle_of_Brentwood", "Battle_of_Franklin_(1863)", "Battle_of_Hoover's_Gap", "Second_Battle_of_Chattanooga", "Battle_of_Blountville", "Battle_of_Blue_Springs", "Battle_of_Wauhatchie", "Battle_of_Collierville", "Battle_of_Campbell's_Station", "Chattanooga_Campaign", "Battle_of_Lookout_Mountain", "Battle_of_Missionary_Ridge", "Battle_of_Fort_Sanders", "Battle_of_Bean's_Station", "Battle_of_Mossy_Creek", "Battle_of_Dandridge", "Battle_of_Fair_Garden", "Battle_of_Fort_Pillow", "Second_Battle_of_Memphis", "Battle_of_Johnsonville", "Battle_of_Bull's_Gap", "Battle_of_Columbia", "Battle_of_Spring_Hill", "Battle_of_Franklin_(1864)", "Third_Battle_of_Murfreesboro", "Battle_of_Nashville", "First_Battle_of_Sabine_Pass", "Battle_of_Galveston_Harbor_(1862)", "Battle_of_Galveston", "Battle_of_Palmito_Ranch", "Second_Battle_of_Sabine_Pass", "Battle_of_Sewell's_Point", "Battle_of_Aquia_Creek", "Battle_of_Big_Bethel", "Battle_of_Blackburn's_Ford", "First_Battle_of_Bull_Run", "Battle_of_Ball's_Bluff", "Battle_of_Dranesville", "Battle_of_Hampton_Roads", "Siege_of_Yorktown_(1862)", "Battle_of_Williamsburg", "Battle_of_Eltham's_Landing", "Battle_of_Drewry's_Bluff", "Battle_of_Hanover_Court_House", "Battle_of_Seven_Pines", "Battle_of_Oak_Grove", "Battle_of_Beaver_Dam_Creek", "Battle_of_Gaines's_Mill", "Battle_of_Garnett's_&_Golding's_Farm", "Battle_of_Savage's_Station", "Battle_of_White_Oak_Swamp", "Battle_of_Glendale", "Battle_of_White_Oak_Swamp", "Battle_of_Glendale", "Battle_of_Malvern_Hill", "Battle_of_Cedar_Mountain", "First_Battle_of_Rappahannock_Station", "Manassas_Station_Operations_(Stonewall_Jackson)", "Battle_of_Thoroughfare_Gap", "Second_Battle_of_Bull_Run", "Battle_of_Chantilly", "Battle_of_Fredericksburg", "Battle_of_Kelly's_Ford", "Battle_of_Suffolk_(Norfleet_House)", "Battle_of_Suffolk_(Hill's_Point)", "Battle_of_Chancellorsville", "Battle_of_Salem_Church", "Second_Battle_of_Fredericksburg", "Battle_of_Brandy_Station", "Battle_of_Aldie", "Battle_of_Middleburg", "Battle_of_Upperville", "First_Battle_of_Auburn", "Battle_of_Bristoe_Station", "Second_Battle_of_Auburn", "Battle_of_Buckland_Mills", "Second_Battle_of_Rappahannock_Station", 
"Battle_of_Mine_Run", "Battle_of_Morton's_Ford", "Battle_of_the_Wilderness", "Battle_of_Port_Walthall_Junction", "Battle_of_Spotsylvania_Court_House", "Battle_of_Cloyd's_Mountain", "Battle_of_Swift_Creek", "Battle_of_Chester_Station", "Battle_of_Yellow_Tavern", "Battle_of_Proctor's_Creek", "Battle_of_Ware_Bottom_Church", "Battle_of_North_Anna", "Battle_of_Wilson's_Wharf", "Battle_of_Totopotomoy_Creek", "Battle_of_Haw's_Shop", "Battle_of_Old_Church", "Battle_of_Cold_Harbor", "Second_Battle_of_Petersburg", "Battle_of_Lynchburg", "Battle_of_Jerusalem_Plank_Road", "Battle_of_Saint_Mary's_Church", "Battle_of_Sappony_Church", "First_Battle_of_Ream's_Station", "First_Battle_of_Deep_Bottom", "Battle_of_the_Crater", "Second_Battle_of_Deep_Bottom", "Battle_of_Globe_Tavern", "Second_Battle_of_Ream's_Station", "Battle_of_Peebles'_Farm", "Battle_of_Chaffin's_Farm", "Battle_of_Saltville_I", "Battle_of_Darbytown_and_New_Market", "Battle_of_Darbytown_Road", "Battle_of_Boydton_Plank_Road", "Battle_of_Fair_Oaks_&_Darbytown_Road", "Battle_of_Marion", "Battle_of_Saltville_II", "Battle_of_Hatcher's_Run", "Battle_of_Fort_Stedman", "Battle_of_Lewis's_Farm", "Battle_of_Dinwiddie_Court_House", "Battle_of_White_Oak_Road", "Battle_of_Five_Forks", "Third_Battle_of_Petersburg", "Battle_of_Sutherland's_Station", "Battle_of_Amelia_Springs", "Battle_of_Rice's_Station", 
"Battle_of_Sayler's_Creek", "Battle_of_Cumberland_Church", "Battle_of_High_Bridge", "Battle_of_Appomattox_Station", "Battle_of_Appomattox_Court_House", "First_Battle_of_Petersburg", "Battle_of_Trevilian_Station", "Battle_of_Cockpit_Point", "First_Battle_of_Kernstown", "Battle_of_McDowell", "Battle_of_Front_Royal", "First_Battle_of_Winchester", "Battle_of_Cross_Keys", "Battle_of_Port_Republic", "Second_Battle_of_Winchester", "Battle_of_Manassas_Gap", "Battle_of_Cove_Mountain", "Battle_of_New_Market", "Battle_of_Piedmont", "Battle_of_Staunton_River_Bridge", "Battle_of_Cool_Spring", "Battle_of_Rutherford's_Farm", "Second_Battle_of_Kernstown", "Battle_of_Guard_Hill", "Battle_of_Berryville", "Battle_of_Opequon", "Battle_of_Fisher's_Hill", "Battle_of_Tom's_Brook", "Battle_of_Cedar_Creek", "Battle_of_Waynesboro", "Battle_of_Namozine_Church", "Battle_of_Walkerton", "Battle_of_Philippi_(West_Virginia)", "Battle_of_Hoke's_Run", "Battle_of_Rich_Mountain", "Battle_of_Kessler's_Cross_Lanes", "Battle_of_Cheat_Mountain", "Battle_of_Carnifex_Ferry", "Battle_of_Greenbrier_River", "Battle_of_Camp_Allegheny", "Battle_of_Princeton_Court_House", "Battle_of_Harpers_Ferry", "Battle_of_Droop_Mountain", "Battle_of_Moorefield", "Battle_of_Summit_Point", "Battle_of_Smithfield_Crossing", "Battle_of_Shepherdstown"]

# Makes get request to Wikipedia, pulls data out in .jason format, and writes it to its own file in the wikidata directory
# Still need to figure out how to put this directly into the repository, rather that Python's default working directory

# Put your own directory path and API identifier below
save_path = "E:/gitrepos/acw_battle_data/wikidata/"
user = {'user-agent': 'wzuidema@uw.edu'}

# Iterates through list, getting data and writing each to its own .json file
for x in battles:
	url = "https://en.wikipedia.org/w/api.php?action=query&titles=" + x + "&prop=revisions&rvprop=content&format=json"
	wiki = requests.get(url, headers=user)
	out = wiki.json()
	out_string = json.dumps(out)
	with open('%s%s.json' % (save_path, x), 'a+') as textfile:
		textfile.write(out_string)
