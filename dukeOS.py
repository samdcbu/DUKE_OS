import time
import random
noreply = ''

#The DukeOS logo
print '  _____  _    _ _  ________    ____   _____ '
print ' |  __ \| |  | | |/ /  ____|  / __ \ / ____|'
print ' | |  | | |  | | \' /| |__    | |  | | (___  '
print ' | |  | | |  | |  < |  __|   | |  | |\___ \ '
print ' | |__| | |__| | . \| |____  | |__| |____) |'
print ' |_____/ \____/|_|\_\______|  \____/|_____/ '
print '                                            '
print '           Type help for help               '
#Big While loop
while 1 == 1:
	command = raw_input('>>>')
	command = command.lower()
	#DukeOS help menu
	if command == 'help':
		print "Welcome to the debut of DUKEOS, here are some helpful commands\n"
		print "start_download: will begin downloading fun files to your hard drive\n"
		print "Why?: brings up a detailed history of DUKEOS and an FAQ\n"
		print "Battle!: doesn't do much...\n"
		print "Ride on The Internet: On your mark, get set, we're riding on the internet\n"
		print "Click cookies: Brings you to cookie clicker \n"
		print "Adventure!: brings you to a non-generic and creative RPG"
	#RPG enter command
	elif command == "adventure!":
		print"Welcome to Enemies and player, the most generic RPG ever."
		print "Help for help"
		#Initial player stats
		playerhp = 20
		playermaxhp = 20

		playeratxpat = 0
		playerbaseat = 5
		playerwepat = 1
		playertotalat = playerbaseat+playeratxpat+playerwepat

		atcritchance = 5
		atcrit = 0

		playeratname = "The Fist of ... Hitting"

		playerbasedef = 5
		playerxpdef = 0
		playerwedef = 0
		playerdefname = "Birthday Suit"
		playerdeftotal = playerbasedef+playerxpdef+playerwedef

		magcritchance = 20
		playerbasemag = 3
		playermagwe= 1
		playerxpmag = 0
		playertotalmag = playerbasemag+playermagwe+playerxpmag

		playermagname = "Bad Magic Trick"

		playerxp = 0
		playerxpt = 10

		playergold = 0

		enemyat= 0
		enemydef = 0
		#Display stats function
		def callstats():
			print "Your total HP:",playerhp
			print "Your total Attack:",playertotalat
			print "Your total Defense:",playerdeftotal
			print "Your total Magic:",playertotalmag
			print "Xp till level up:",(playerxpt-playerxp)
			print "Your total Gold:",int(playergold)







		#Level one encounter

		def encounter():
			#Your stats
			global playerhp 
			global playermaxhp

			global playeratxpat
			global playeratname
			global playertotalat
			global playerbaseat

			global atcrit
			global atcritchance

			global playeratname

			global playerbasedef
			global playerxpdef
			global playerwedef
			global playerdeftotal

			global magcritchance 
			global playerbasemag
			global playermagwe
			global playerxpmag
			global playertotalmag

			global playermagname

			global playerxp
			global playerxpt 

			


			global playergold

			#Enemy stats
			enemyat = random.randrange(4,8)
			enemydef = random.randrange(4,8)
			enemyhp = random.randrange(5,15)
			enemylvl = (enemyhp+enemydef+enemyat)/3 
			#Fight calculation
			print "\n A level",enemylvl,"enemy appeared!\n"
			while playerhp>0 and enemyhp>0:

				atchoice = raw_input("Use magic or attack?\n").lower()

				while atchoice  != "magic" and atchoice != "attack":
					atchoice = raw_input("Invalid move: please select magic or attack.\n")
				print "\n\n"
				if atchoice == "attack":
					enemyhp = enemyhp - round(playertotalat*(playertotalat/float(enemydef)))
					print "\nYou hit for",round(playertotalat*(playertotalat/float(enemydef))),"HP with",playeratname
					print "Enemy HP left:",enemyhp,"\n"
				elif atchoice == "magic":
					atcrit = random.randrange(1,100)
					if magcritchance>=atcrit:
						print "\nCRITICAL HIT!"
						print "You hit for",round(playertotalmag*1.5),"HP with",playermagname
						enemyhp -= round(playertotalmag*1.5)
						print "Enemy HP left:",enemyhp,"\n"
					if magcritchance<= atcrit:
						enemyhp -= playertotalmag
						print "\nYou hit for",playertotalmag,"HP with",playermagname
						print "Enemy HP left:",enemyhp,"\n"
				if enemyhp<0:
					break
				playerhp -= round(enemyat*(enemyat/float(playerdeftotal)))
				print "You were hit for",round(enemyat*(enemyat/float(playerdeftotal))),"HP"
				print "You have",playerhp,"HP left"
			if playerhp>0:
				print "You won the encounter"
				xpgain = random.randrange(1,3)
				playerxp += xpgain
				print "You have",playerhp,"HP left"
				print "You gained",xpgain,"XP"
				goldgain = random.randrange(10,30)
				playergold += goldgain
				print "You gained",goldgain,"Gold"
			if playerhp <= 0:
				print "You lost"
				goldloss = round(playergold/4.0)
				print "And lost",goldloss,"gold"
				playergold -= goldloss
			#Health reset
			playerhp = playermaxhp
			#Leveling up system
			if playerxp > playerxpt:
				print "Level up!"
				pickstat = raw_input("Would you like to improve defense, attack or magic?").lower()
				while pickstat != "magic" and pickstat != "attack" and pickstat != "magic":
					pickstat = raw_input("Invalid please pick defense, attack or magic.")
				if pickstat == "magic":
					print "MAGIC UPGRADED!"
					playerxpmag += 1
					playertotalat = playerbaseat+playeratxpat+playerwepat

				playerxp -= playerxpt
				playerxpt = round(playerxpt*1.2)


		#Identical to the level one version but with harder enemies
		def encounter2():
			global playerhp 
			global playermaxhp

			global playeratxpat
			global playeratname
			global playertotalat
			global playerbaseat

			global atcrit
			global atcritchance

			global playeratname

			global playerbasedef
			global playerxpdef
			global playerwedef
			global playerdeftotal

			global magcritchance 
			global playerbasemag
			global playermagwe
			global playerxpmag
			global playertotalmag

			global playermagname

			global playerxp
			global playerxpt 

			


			global playergold


			enemyat = random.randrange(8,16)
			enemydef = random.randrange(8,16)
			enemyhp = random.randrange(10,30)
			enemylvl = (enemyhp+enemydef+enemyat)/3 

			print "\n A level",enemylvl,"enemy appeared!\n"
			while playerhp>0 and enemyhp>0:

				atchoice = raw_input("Use magic or attack?\n").lower()

				while atchoice  != "magic" and atchoice != "attack":
					atchoice = raw_input("Invalid move: please select magic or attack.\n")
				print "\n\n"
				if atchoice == "attack":
					enemyhp = enemyhp - round(playertotalat*(playertotalat/float(enemydef)))
					print "\nYou hit for",round(playertotalat*(playertotalat/float(enemydef))),"HP with",playeratname
					print "Enemy HP left:",enemyhp,"\n"
				elif atchoice == "magic":
					atcrit = random.randrange(1,100)
					if magcritchance>=atcrit:
						print "\nCRITICAL HIT!"
						print "You hit for",round(playertotalmag*1.5),"HP with",playermagname
						enemyhp -= round(playertotalmag*1.5)
						print "Enemy HP left:",enemyhp,"\n"
					if magcritchance<= atcrit:
						enemyhp -= playertotalmag
						print "\nYou hit for",playertotalmag,"HP with",playermagname
						print "Enemy HP left:",enemyhp,"\n"
				if enemyhp<0:
					break
				playerhp -= round(enemyat*(enemyat/float(playerdeftotal)))
				print "You were hit for",round(enemyat*(enemyat/float(playerdeftotal))),"HP"
				print "You have",playerhp,"HP left"
			if playerhp>0:
				print "You won the encounter"
				xpgain = random.randrange(3,6)
				playerxp += xpgain
				print "You have",playerhp,"HP left"
				print "You gained",xpgain,"XP"
				goldgain = random.randrange(20,60)
				playergold += goldgain
				print "You gained",goldgain,"Gold"
			if playerhp <= 0:
				print "You lost"
				goldloss = round(playergold/4.0)
				print "And lost",goldloss,"gold"
				playergold -= goldloss

			playerhp = playermaxhp
			if playerxp > playerxpt:
				print "Level up!"
				pickstat = raw_input("Would you like to improve defense, attack or magic?").lower()
				while pickstat != "magic" and pickstat != "attack" and pickstat != "magic":
					pickstat = raw_input("Invalid please pick defense, attack or magic.")
				if pickstat == "magic":
					print "MAGIC UPGRADED!"
					playerxpmag += 1
					playertotalat = playerbaseat+playeratxpat+playerwepat

				playerxp -= playerxpt
				playerxpt = round(playerxpt*1.2)

		#Like the level 1 one too
		def encounter3():
			global playerhp 
			global playermaxhp

			global playeratxpat
			global playeratname
			global playertotalat
			global playerbaseat

			global atcrit
			global atcritchance

			global playeratname

			global playerbasedef
			global playerxpdef
			global playerwedef
			global playerdeftotal

			global magcritchance 
			global playerbasemag
			global playermagwe
			global playerxpmag
			global playertotalmag

			global playermagname

			global playerxp
			global playerxpt 

			


			global playergold


			enemyat = random.randrange(16,32)
			enemydef = random.randrange(16,32)
			enemyhp = random.randrange(30,60)
			enemylvl = (enemyhp+enemydef+enemyat)/3 

			print "\n A level",enemylvl,"enemy appeared!\n"
			while playerhp>0 and enemyhp>0:

				atchoice = raw_input("Use magic or attack?\n").lower()

				while atchoice  != "magic" and atchoice != "attack":
					atchoice = raw_input("Invalid move: please select magic or attack.\n")
				print "\n\n"
				if atchoice == "attack":
					enemyhp = enemyhp - round(playertotalat*(playertotalat/float(enemydef)))
					print "\nYou hit for",round(playertotalat*(playertotalat/float(enemydef))),"HP with",playeratname
					print "Enemy HP left:",enemyhp,"\n"
				elif atchoice == "magic":
					atcrit = random.randrange(1,100)
					if magcritchance>=atcrit:
						print "\nCRITICAL HIT!"
						print "You hit for",round(playertotalmag*1.5),"HP with",playermagname
						enemyhp -= round(playertotalmag*1.5)
						print "Enemy HP left:",enemyhp,"\n"
					if magcritchance<= atcrit:
						enemyhp -= playertotalmag
						print "\nYou hit for",playertotalmag,"HP with",playermagname
						print "Enemy HP left:",enemyhp,"\n"
				if enemyhp<0:
					break
				playerhp -= round(enemyat*(enemyat/float(playerdeftotal)))
				print "You were hit for",round(enemyat*(enemyat/float(playerdeftotal))),"HP"
				print "You have",playerhp,"HP left"
			if playerhp>0:
				print "You won the encounter"
				xpgain = random.randrange(6,12)
				playerxp += xpgain
				print "You have",playerhp,"HP left"
				print "You gained",xpgain,"XP"
				goldgain = random.randrange(40,120)
				playergold += goldgain
				print "You gained",goldgain,"Gold"
			if playerhp <= 0:
				print "You lost"
				goldloss = round(playergold/4.0)
				print "And lost",goldloss,"gold"
				playergold -= goldloss

			playerhp = playermaxhp
			if playerxp > playerxpt:
				print "Level up!"
				pickstat = raw_input("Would you like to improve defense, attack or magic?").lower()
				while pickstat != "defense" and pickstat != "attack" and pickstat != "magic":
					pickstat = raw_input("Invalid please pick defense, attack or magic.")
				if pickstat == "magic":
					print "MAGIC UPGRADED!"
					playerxpmag += 1
					playertotalmag = playerbasemag+playerxpmag+playermagwe
				if pickstat == "attack":
					print "ATTACK UPGRADED!"
					playerxpat += 1
					playertotalat = playerbaseat+playeratxpat+playerwepat
				if pickstat == "defense":
					playerxpdef += 1
					playerdeftotal = playerbasedef+playerxpdef+playerwedef
				playerxp -= playerxpt
				playerxpt = round(playerxpt*1.2)

		#Help menu for the RPG
		def helpmenu():
			print "ADVENTURE: to go off and fight"
			print "Store: unknown"
			print "Stats: for stats"
			print "Get me outta this mess: ehhhhhh, don't do that one"


		#Function for buying an attack
		def buyattack(name,damage,cost):
			global playeratname
			global playerwepat
			global playergold

			playeratname = name
			playerwepat = damage
			playergold -= cost

			print "YOU RECIEVED:",name
		#Function for buying Magic
		def buymagic(name,damage,cost):
			global playermagname
			global playermagwe
			global playergold

			playermagname = name
			playermagwe = damage
			playergold -= cost
			print "YOU RECIEVED:",name
		#Function for buying clothes
		def buydefense(name,damage,cost):
			global playerdefname
			global playerwedef
			global playergold

			playerdefname = name
			playerwedef = damage
			playergold -= cost
			print "YOU RECIEVED:",name
		#Store Function
		def store():
			

			print "\nWelcome to the store, here's some stuff in chart form\n"
			print "Fighting Stuff that does damage but not in the way magic stuff does damage"


			#Makes nice charts and stuff
			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"
			print "|"+"Name                                         |Damage           |Cost         "+'|'
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Quality Stick: The best I've seen in awhile"+" "*2+"|"+"5"+" "*16+'|'+"100 GOLDS"+" "*4+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Sharper Metalic Slicy Stick: Swoard?"+" "*9+"|"+"15"+" "*15+'|'+""+"400 DUBLOONS"+' '*1+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Super rad weapon of... Hitting?: probably"+" "*4+"|"+"40"+" "*15+'|'+"2,000 MONIES"+" "*1+"|"
			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"

			print "\n\nMagic .... like old magic ... like the serious kind\n"


			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"
			print "|"+"Name                                         |Damage           |Cost         "+'|'
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Fire Spell: the weak kind, like a lighter"+" "*4+"|"+"3"+" "*16+'|'+"100 FRANKLINS"+" "*0+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Magic Slap: slaps with magic"+" "*17+"|"+"8"+" "*16+'|'+"400 WEALTH"+" "*3+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Real wizard stuff: for real"+" "*18+"|"+"23"+" "*15+'|'+""+"2,000 $$$$$"+" "*2+"|"
			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"


			print "\n\nClothing, the military grade stuff\n"
			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"
			print "|"+"Name                                         |Defense          |Cost         "+'|'
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Light T-Shirt: it's cold but not jacket cold"+" "*1+"|"+"10"+" "*15+'|'+"100 WHATSITZ"+" "*1+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Heavy Jacket: Mom says otherwise"+" "*13+"|"+"25"+" "*15+'|'+"400 BARRELS"+" "*2+"|"
			print "|"+"-"*45+"|"+"-"*17+'|'+"-"*13+"|"
			print "|"+"Parachute Pants: Now we're talking"+" "*11+"|"+"50"+" "*15+'|'+"2,000 CASHES"+" "*1+"|"
			print "|"+"-"*45+"*"+"-"*17+'*'+"-"*13+"|"
			#Raw input and figuring out if the player has enough money
			buything = raw_input("Buy something or get out.\n").lower()


			if buything == "quality stick" and playergold>= 100:
				buyattack('Quality Stick',5,100)
			elif buything == "quality stick" and playergold< 100:
				print "you need",(100-playergold),"more"
			elif buything == "sharper metalic slicy stick" and playergold>= 400:
				buyattack('Sharper Metalic Slicy Stick',15,400)
			elif buything == "sharper metalic slicy stick" and playergold< 400:
				print "you need",(400-playergold),"more"
			elif buything == "super rad weapon of... hitting?" and playergold>= 2000:
				buyattack('super rad weapon of... hitting?',40,2000)
			elif buything == "super rad weapon of... hitting?" and playergold< 2000:
				print "you need",(2000-playergold),"more"

			elif buything == "fire spell" and playergold>= 100:
				buymagic('Rusty Lighter',4,100)
			elif buything == "fire spell" and playergold< 100:
				print "you need",(100-playergold),"more"
			elif buymagic == "magic slap" and playergold>= 400:
				buyattack('magic slap',8,400)
			elif buything == "magic slap" and playergold< 400:
				print "you need",(400-playergold),"more"
			elif buything == "real wizard stuff" and playergold>= 2000:
				buymagic('real wizard stuff',23,2000)
			elif buything == "real wizard stuff" and playergold< 2000:
				print "you need",(2000-playergold),"more"

			elif buything == "light t-shirt" and playergold>= 100:
				buydefense('light t-shirt',10,100)
			elif buything == "light t-shirt" and playergold< 100:
				print "you need",(100-playergold),"more"
			elif buything == "heavy jacket" and playergold>= 400:
				buydefense('heavy jacket',25,400)
			elif buything == "heavy jacket" and playergold< 400:
				print "you need",(400-playergold),"more"
			elif buything == "parachute pants" and playergold>= 2000:
				buydefense('parachute pants',50,2000)
			elif buything == "parachute pants" and playergold< 2000:
				print "you need",(2000-playergold),"more"

			else:
				print "I don't understand what your saying, get out of my store!"
			#Updates stat totals
			playertotalat = playerbaseat+playeratxpat+playerwepat
			playerdeftotal = playerbasedef+playerxpdef+playerwedef
			playertotalmag = playerbasemag+playermagwe+playerxpmag




		#Directs to functions
		while 1==1:
			do = raw_input("What do?").lower()
			if do == "help":
				helpmenu()
			elif do == "adventure":
				whatlevel = raw_input("What level would you like. 1,2, or 3?")
				if whatlevel =="1":
					encounter()
				if whatlevel =="2":
					encounter2()
				if whatlevel =="3":
					encounter3()
			elif do == "store":
				store()
			elif do == "stats":
				callstats()
			elif do == "get me outta this mess":
				break



	#THE INTERNET OF DUKEOS
	elif command == "ride on the internet":
                print "Welcome to THE INTERNET. Current popular sites:"
                print "1. cats.com"
                #Pick site
                website = raw_input("What website would you like?\n").lower()
                url = 'cats.com'
                #Cats.com
                if website == "cats.com":
                    import random
                    print"\n"
                    cat=1
                    while 1==1:
                    	#Shifts pages and displays ASCII cats
                        how = raw_input('Type random, previous, next, first or last to navigate cat photos or back to \nleave\n').lower()
                        if how == 'previous':
                            if cat != 1:
                                cat -=1
                            else:
                                cat= 1
                        elif how == 'next':
                            if cat == 3:
                                cat =3 
                            else:
                                cat+= 1
                        elif how == "first":
                            cat = 1
                        elif how == "last":
                            cat = 3
                        elif how =="random":
                            cat = random.randint(1,3)
                        elif how =="back":
                            break
                        if cat == 1:
                            print "*"+"-"*77+"*"
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"*2+url+" "*(73-len(url))+"*\\"+'|'*2
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*19+'                    __     __,        '+" "*20+'|'
                            print "|"+" "*19+'                     \\,`~"~` /        '+" "*20+'|'
                            print "|"+" "*19+'      .-=-.           /    . .\\       '+" "*20+'|'
                            print "|"+" "*19+'     / .-. \\          {  =    Y}=     '+" "*20+'|'
                            print "|"+" "*19+'    (_/   \\ \\          \\      /       '+" "*20+'|'
                            print "|"+" "*19+'           \\ \\        _/`\'`\'`b        '+" "*20+'|'
                            print "|"+" "*19+'            \\ `.__.-\'`        \\-._    '+" "*20+'|'
                            print "|"+" "*19+'             |            \'.__ `\'-;_  '+" "*20+'|'
                            print "|"+" "*19+'             |            _.\' `\'-.__) '+" "*20+'|'
                            print "|"+" "*19+'              \\    ;_..--\'/     //  \\ '+" "*20+'|'
                            print "|"+" "*19+'              |   /  /   |     //    |'+" "*20+'|'
                            print "|"+" "*19+'        jgs   \\  \ \\__)   \\   //    / '+" "*20+'|'
                            print "|"+" "*19+'               \\__)        \'.//   .\'  '+" "*20+'|'
                            print "|"+" "*19+'                             `\'-\'`     '+" "*19+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*76+"1"+'|'
                            print "*"+"-"*77+"*"
                        if cat==2:
                            print "*"+"-"*77+"*"
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"*2+url+" "*(73-len(url))+"*\\"+'|'*2
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*27+'     /\\__/\\          '+" "*29+'|'
                            print "|"+" "*27+'    /`    \'\\         '+" "*29+'|'
                            print "|"+" "*27+'  === 0  0 ===       '+" "*29+'|'
                            print "|"+" "*27+'    \\  --  /         '+" "*29+'|'
                            print "|"+" "*27+'   /        \\        '+" "*29+'|'
                            print "|"+" "*27+'  /          \\       '+" "*29+'|'
                            print "|"+" "*27+' |            |      '+" "*29+'|'
                            print "|"+" "*27+'  \\  ||  ||  /       '+" "*29+'|'
                            print "|"+" "*27+'   \\_oo__oo_/#######o'+" "*29+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*76+"2"+'|'
                            print "*"+"-"*77+"*"
                        if cat==3:
                            print "*"+"-"*77+"*"
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"*2+url+" "*(73-len(url))+"*\\"+'|'*2
                            print "|"+"*"+"-"*75+"*"+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*26+'   /\\     /\\            '+" "*27+'|'
                            print "|"+" "*26+'  {  `---\'  }           '+" "*27+'|'
                            print "|"+" "*26+'  {  O   O  }           '+" "*27+'|'
                            print "|"+" "*26+'  ~~>  V  <~~           '+" "*27+'|'
                            print "|"+" "*26+'   \\  \\|/  /            '+" "*27+'|'
                            print "|"+" "*26+'    `-----\'__           '+" "*27+'|'
                            print "|"+" "*26+'    /     \\  `^\\_       '+" "*27+'|'
                            print "|"+" "*26+'   {       }\\ |\\_\\_   W '+" "*27+'|'
                            print "|"+" "*26+'   |  \\_/  |/ /  \\_\\_( )'+" "*27+'|'
                            print "|"+" "*26+'    \\__/  /(_E     \\__/ '+" "*27+'|'
                            print "|"+" "*26+'      (  /              '+" "*27+'|'
                            print "|"+" "*26+'       MM               '+" "*27+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*77+'|'
                            print "|"+" "*76+"3"+'|'
                            print "*"+"-"*77+"*"
    #The MAGIKARP battle
	elif command == "Battle" or command == "battle" or command == "battle!" or command == "Battle!":
		#Health sets
		dragonitehp = 100
		magikarphp = 500
		print '\nA wild magikarp has appeared! Go, dragonite!'
		while dragonitehp > 0 and magikarphp > 0:
			#Magikarps turn
		    magikarp_miss = random.randint(1, 100)
		    if magikarp_miss <= 2:
		        print 'Magikarp missed!'
		    else:
		        magikarp_attack = random.randint(40, 60)
		        print 'Magikarp used Splash! It did',magikarp_attack,'damage!'
		        dragonitehp -= magikarp_attack
		    if dragonitehp <=0:
		        break
		    print 'Dragonite has',dragonitehp,'hp left.'
		    #PLayer's turn
		    dragonite_attack = raw_input('Choose between Dragon Claw, Waterfall, Earthquake, and Hurricane.\n')
		    invalid = True
		    while invalid:
		        if dragonite_attack == 'Dragon Claw' or dragonite_attack == 'dragon claw' or dragonite_attack == 'Dragon claw' or dragonite_attack == 'dragon Claw':
		            invalid = False
		            miss = random.randint(1, 100)
		            if miss <= 20:
		                print 'Dragonite missed!'
		            else:
		                damage = random.randint(80, 100)
		                print '\nDragonite used Dragon Claw! It did',damage,'damage!'
		                magikarphp -= damage
		        elif dragonite_attack == 'Waterfall' or dragonite_attack == 'waterfall':
		            invalid = False
		            damage = random.randint(50, 80)
		            print '\nDragonite used Waterfall! It did',damage,'damage!'
		            magikarphp -= damage
		        elif dragonite_attack == 'Earthquake' or dragonite_attack == 'earthquake':
		            invalid = False
		            miss = random.randint(1, 100)
		            if miss <= 10:
		                print '\nDragonite missed!'
		            else:
		                damage = random.randint(70, 90)
		                print '\nDragonite used Earthquake! It did',damage,'damage!'
		                magikarphp -= damage
		        elif dragonite_attack == 'Hurricane' or dragonite_attack == 'hurricane':
		            invalid = False
		            miss = random.randint(1, 100)
		            if miss <= 50:
		                print '\nDragonite missed!'
		            else:
		                damage = random.randint(150, 300)
		                print '\nDragonite used Hurricane! It did',damage,'damage!'
		                magikarphp -= damage
		        else:
		            dragonite_attack = raw_input('Please enter "Dragon Claw", "Waterfall", "Earthquake", or "Hurricane" only.\n')
		    if magikarphp <= 0:
		        break
		    print 'Magikarp has',magikarphp,'hp left.'
		if dragonitehp <= 0:
		    print 'Dragonite fainted! You lost.'
		if magikarphp <=0:
		    print 'Magikarp fainted! You won!!!!!!!!!!!!'
	#The download command
	elif command == 'start_download':
		#Just no affect inputs and waits
		noreply == raw_input('Give DUKEOS access to the internet?\n>>>')
		noreply == raw_input('Thank you for access to the internet, allow DUKEOS to start_download\n>>>')
		print 'Download starting, please wait...'
		time.sleep(5)
		print "0%"
		time.sleep(1)
		print "1%"
		time.sleep(1)
		print '2%'
		time.sleep(1)
		print '4%'
		time.sleep(1)
		print '4%'
		time.sleep(1)
		print '4.5%'
		time.sleep(1)
		print '4.6%'
		time.sleep(1)
		print '4.7%'
		time.sleep(1)
		print '5%'
		time.sleep(1)
		print '7%'
		time.sleep(1)
		print 'NaN'
		time.sleep(1)
		print '20%'
		time.sleep(1)
		print '27%'
		time.sleep(1)
		print '39%'
		time.sleep(1)
		print '55%'
		time.sleep(1)
		print '78%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '1337%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '98%'
		time.sleep(1)
		print '99%'
		time.sleep(1)
		print '100%'
		time.sleep(1)
		print '101%'
		time.sleep(1)
		print '102%'
		time.sleep(1)
		print '104%'
		time.sleep(1)
		print '106%'
		noreply = raw_input('application MORERAM.exe has finished downloading, execute it?\n>>>')
		noreply = raw_input('Wait really? \n>>>')
		print 'Deleting from hard drive randomly to make space for more ram in computer'
		print 'randomly selecting file...'
		time.sleep(7)
		noreply = raw_input('file selected: wierd secrets, delete this file?\n>>>')
		print "uploading file to internet: wierd secrets"
		print '100%'
		time.sleep(2)
		print 'wow you\'re upload speed is so much quicker than you\'re download speed'
		time.sleep(1)
		noreply = raw_input('finish installing MORERAM.exe?\n>>>')
		print "installation begining"
		time.sleep(2)
		print 'computer evaluation begining to determine correct ram placement'
		time.sleep(4)
		print 'CPU: needs more ram' 
		time.sleep(4)
		print'RAM: needs more ram'
		time.sleep(4)
		print 'Graphics card can\'t run battlefield 4 at 10000 fps. Conclusion: More ram'
		time.sleep(4)
		print 'Monitor isn\'t CRT: More Ram installing to upgrade to CRT'
		time.sleep(4)
		print 'Evaluating atmosphere of room, not optimale, installing more ram'
		time.sleep(4)
		print 'Evaluation complete, downloading exactly \"more\" gigabytes of ram'
		time.sleep(4)
		print 'More RAM istalling...'
		time.sleep(8)
		print 'Congratulations, more RAM has been installed.'
	#cookie clicker
	elif command == "click cookies":
		#Default values set
		starttime = time.clock()
		play = True
		cookies = 0
		cursors = 0
		grandmas = 0
		farms = 0
		factories = 0
		mines = 0
		shipments = 0
		alchemy_labs = 0
		portals = 0
		time_machines = 0
		antimatter_condensers = 0
		prisms = 0

		clickcps = 1
		cursorcps = 0.1
		grandmacps = 0.5
		farmcps = 4
		factorycps = 10
		minecps = 40
		shipmentcps = 100
		alchemycps = 400
		portalcps = 6666
		timecps = 98765
		anticps = 999999
		prismcps = 10000000


		#Upgrade conditions and stuff
		Reinforced_Index_Finger = False
		Is_Reinforced_Index_Finger = 0
		Carpal_Tunnel = False
		Is_Carpal_Tunnel = 0
		ambidextrous = False
		Is_ambidextrous = 0
		forwards = False
		Is_forwards = 0
		#Cashin updates cookie amounts by time spent not cashing in
		def cashin(cursors,grandmas,farms,factories,mines,shipments,alchemy_labs,portals,time_machines,antimatter_condnsers,prisms):
		    endtime = time.clock()
		    global starttime
		    cookietime = endtime - starttime
		    global cookies
		    print "Cookies Earned:",(cursors*cursorcps*cookietime)+(grandmas*grandmacps*cookietime)+(farms*farmcps*cookietime)+(factories*factorycps*cookietime)+(mines*minecps*cookietime)+(shipments*shipmentcps*cookietime)+(alchemy_labs*alchemycps*cookietime)+(portals*portalcps*cookietime)+(time_machines*timecps*cookietime)+(antimatter_condensers*anticps*cookietime)+(prisms*prismcps*cookietime)
		    cookies += (cursors*cursorcps*cookietime)+(grandmas*grandmacps*cookietime)+(farms*farmcps*cookietime)+(factories*factorycps*cookietime)+(mines*minecps*cookietime)+(shipments*shipmentcps*cookietime)+(alchemy_labs*alchemycps*cookietime)+(portals*portalcps*cookietime)+(time_machines*timecps*cookietime)+(antimatter_condensers*anticps*cookietime)+(prisms*prismcps*cookietime)
		    starttime = time.clock()


		#The cookie clicker help menu
		def menu():
		    print "\n\nWelcome to cookie clicker. Here's a list of commands"
		    print "click: gives you",clickcps,"cookie"
		    print "cashin: updates cookies"
		    print "buy: brings you to the store"
		    print "evaluate: let's you see your total building numbers, costs for buildings and cps for buildings"
		    print "stop the madness: stops the game"
		    print "upgrade: a different store for upgrades"
		    print "help: bring up this menu"
		    print "save: save the game"
		    print "load: load the game"
		menu()
		#Actual playing stuff
		while play == True:
		    action = raw_input("\nWhat would you like to do?\n").lower()


		    #Saving stuff
		    if action == "save":
		    	#Basically opens a text file and writes the values in order
		        f= open('cookiesave.txt','w')
		        cashin(cursors,grandmas,farms,factories,mines,shipments,alchemy_labs,portals,time_machines,antimatter_condensers,prisms)
		        s = str(cookies)+("\n")
		        f.write(s)

		        s = str(cursors)+("\n")
		        f.write(s)

		        s = str(grandmas)+("\n")
		        f.write(s)

		        s = str(farms)+("\n")
		        f.write(s)
		        
		        s = str(factories)+("\n")
		        f. write(s)

		        s = str(mines)+("\n")
		        f.write(s)

		        s = str(shipments)+("\n")
		        f.write(s)

		        s = str(alchemy_labs)+("\n")
		        f.write(s)

		        s =str(portals)+("\n")
		        f.write(s)

		        s = str(time_machines)+("\n")
		        f.write(s)

		        s = str(antimatter_condensers)+("\n")
		        f.write(s)

		        s = str(prisms)+("\n")
		        f.write(s)

		        s = str(Is_Reinforced_Index_Finger)+("\n")
		        f.write(s)


		        s = str(Is_Carpal_Tunnel)+("\n")
		        f.write(s)

		        s= str(Is_ambidextrous)+("\n")
		        f.write(s)

		        s = str(Is_forwards)+("\n")
		        f.write(s)

		        f.close()
		        print "\nSAVED!"
		    #For loading saves
		    if action == "load":
		    	#Does the save thing in reverse and knows the order of lines and what number is assigned to what
		        f = open('cookiesave.txt','r')
		        a = f.readline()
		        a = a.rstrip('\n')
		        cookies = float(a)

		        a = f.readline()
		        a = a.rstrip('\n')
		        cursors = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        grandmas = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        farms = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        factories = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        mines = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        shipments = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        alchemy_labs = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        portals = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        antimatter_condensers = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        prisms = int (a)


		        a = f.readline()
		        a = a.rstrip('\n')
		        a = int(a)
		        if a == 1:
		            clickcps+=1
		            cursorcps+=0.1

		        a = f.readline()
		        a = a.rstrip('\n')
		        a = int(a)
		        if a == 1:
		            clickcps*=2
		            cursorcps*=2

		        a = f.readline()
		        a = a.rstrip('\n')
		        a = int(a)
		        if a == 1:
		            clickcps *=2
		            cursorcps *=2


		        a = f.readline()
		        a = a.rstrip('\n')
		        a = int(a)
		        if a == 1:
		            grandmacps += 0.3
		        print"LOADED!"

		    #cookie click action, gives you a cookie(or a couple more with upgrades)
		    if action == "click":
		        cookies += clickcps
		        print "Cookie Total:",cookies
		    #Let's you see current numbers of buildings 
		    if action == "evaluate":
		        print "\nCursors:",cursors
		        print "CPS per cursor:",cursorcps
		        print "Next cursor costs:",cursorcost,"cookies\n"
		        if cursors > 0:
		            print "Grandmas:",grandmas
		            print "Next grandma costs:",grandmacost,"cookies\n"
		            print "CPS per grandma:",grandmacps
		        if grandmas > 0:
		            print "Factories:",factories
		            print "CPS per factory:",factorycps
		            print "Next factory costs:",factorycost,"cookies\n"

		        if factories > 0:
		            print "Mines:",mines
		            print "CPS per mine",minecps
		            print "Next mine costs:",minecost,"cookies\n"
		        if mines >0:
		            print "Shipments:",shipments
		            print "CPS per shipment:",shipmentcps
		            print "Next shipment costs:",shipmentcost,"cookies\n"
		        if shipments>0:
		            print "Alchemy Labs:",alchemy_labs
		            print "CPS per alchemy lab:",alchemycps
		            print "Next Alchemy Lab costs:",alchemycost,"cookies\n"
		        if alchemy_labs>0:
		            print "Portals:",portals
		            print "CPS per portal:",portalcps
		            print "Next portal costs:",portalcost,"cookies\n"
		        if portals >0:
		            print "Antimatter Condensers:",antimatter_condensers
		            print "CPS per Antimatter Condenser",anticps
		            print "Next Antimatter Condenser:",anticost,"cookies\n"
		        if antimatter_condensers>0:
		            print "Prisms:",prisms
		            print "CPS per prism:",prismcps
		            print "Next Prism costs:",prismcost,"cookies\n"

		    #cost increasing
		    cursorcost= 15*(1.15**cursors)
		    grandmacost= 100*(1.15**grandmas)
		    farmcost = 500*(1.15**farms)
		    factorycost= 3000*(1.15**factories)
		    minecost = 10000*(1.15**mines)
		    shipmentcost = 40000*(1.15**shipments)
		    alchemycost = 200000*(1.15**alchemy_labs)
		    portalcost = 1666666*(1.15**portals)
		    timecost = 123456789*(1.15**time_machines)
		    anticost = 3999999999*(1.15**antimatter_condensers)
		    prismcost = 75000000000*(1.15**prisms)





		    #Calls the help menu
		    if action == "help":
		        menu()
		    #Gets you out of cookie clicker
		    if action == "stop the madness":
		        play = False
		    #uses the cashin function
		    if action == "cashin":
		        cashin(cursors,grandmas,farms,factories,mines,shipments,alchemy_labs,portals,time_machines,antimatter_condensers,prisms)
		        print "You have",cookies,"cookies"
		    #Secret Dev only stuff
		    #if action == "devclick":
		    #   cookies += 100000000000
		    #Does a store like thing
		    if action == "buy":
		    	#Auto cashin
		        cashin(cursors,grandmas,farms,factories,mines,shipments,alchemy_labs,portals,time_machines,antimatter_condensers,prisms)
		        #Store displaying unlocked buildings
		        print "\nYou have",cookies,"cookies\n"
		        print "Welcome to the store, here's a list of what you can buy, type exit to leave."
		        print "\nCursor: clicks a cookie every ten seconds,",cursorcost, "cookies"
		        if cursors > 0:
		            print"Grandma: A nice grandma to bake more cookies,",grandmacost,"cookies"
		            
		        if grandmas > 0:
		            print "Farm: Grows cookie plants from cookie seeds",farmcost,"cookies"
		        if farms > 0 :
		            print "Factory: Produces large quantities of cookies,",factorycost,"cookies"
		        if factories > 0:
		            print "Mine: Mines out cookie dough and chocolate chips,",minecost,"cookies"
		        if mines > 0:
		            print "Shipment: Brings fresh cookies from the cookie plantet,",shipmentcost,"cookies"
		        if shipments > 0:
		            print "Alchemy lab: Turns gold into cookies!",alchemycost,"cookies"
		        if alchemy_labs > 0:
		            print "Portal: Opens a door to the cookieverse,",portalcost,"cookies"
		        if portals > 0:
		            print "Time Machine: Brings cookies from the past, before they were even eaten,",timecost,"cookies"
		        if time_machines > 0:
		            print "Antimatter Condenser: Condenses the antimatter in the universe into cookies,",anticost,"cookies"
		        if antimatter_condensers >0 :
		            print "Prisms: Converts light itself into cookies,",prismcost,"cookies"
		        print "\n"




		        #The input
		        buyaction = raw_input("So what'll it be?\n")

		        if buyaction == "exit":
		            break
		        #Specific building unlocks and buying protocol
		        #CURSOR
		        if buyaction == "cursor" and cookies >= cursorcost:
		            cursors += 1
		            cookies -= cursorcost
		            print "Total cursors:",cursors
		            if cursors == 1:
		                print "Building: Grandma unlocked, 0.5CPS"
		                print "Upgrade: Reinforced Index Finger unlocked"
		                Reinforced_Index_Finger = True
		                print "Upgrade: Carpal Tunnel Prevention Cream unlocked"
		                Carpal_Tunnel = True
		            if cursors == 10:
		                print "Upgrade: Ambidextrous unlocked"
		        elif buyaction == "cursor" and cookies < cursorcost:
		            print "Sorry you need",str(cursorcost-cookies),"more"
		        #GRANDMA
		        if buyaction == "grandma" and cookies >= grandmacost and cursors > 0:
		            grandmas += 1
		            cookies -= grandmacost
		            print "Total grandmas:",grandmas
		            if grandmas == 1:
		                print "Farm unlocked, 4 CPS"
		                print "Forwards from grandma unlocked, 1000 cookies"
		                forwards = True
		        elif buyaction == "grandma" and cookies < grandmacost:
		            print "Sorry you need",str(grandmacost-cookies),"more"
		        #FARM
		        if buyaction == "farm" and cookies >= farmcost and grandmas > 0:
		            farms += 1
		            cookies -= farmcost
		            print "Total farms:",farms
		            if farms == 1:
		                print "Factory unlocked, 10 CPS"
		        elif buyaction == "farm" and cookies <farmcost :
		            print "Sorry you need",str(farmcost-cookies),"more"
		        #FACTORY
		        if buyaction == "factory" and cookies >= factorycost and farms > 0:
		            factories += 1
		            cookies -= factorycost
		            print "Total factories:",factories
		            if factories == 1:
		                print "Mine unlocked, 40 CPS"
		        elif buyaction == "factory" and cookies <factorycost :
		            print "Sorry you need",str(factorycost-cookies),"more"

		        #MINE
		        if buyaction == "mine" and cookies >= minecost and factories > 0:
		            mines += 1
		            cookies -= minecost
		            print "Total mines:",mines
		            if factories == 1:
		                print "Shipment unlocked, 100 CPS"
		        elif buyaction == "mine" and cookies <minecost :
		            print "Sorry you need",str(minecost-cookies),"more"
		        #SHIPMENT
		        if buyaction == "shipment" and cookies >= shipmentcost and mines > 0:
		            shipments += 1
		            cookies -= shipmentcost
		            print "Total shipments:",shipments
		            if factories == 1:
		                print "Alchemy Lab unlocked, 400 CPS"
		        elif buyaction == "shimpment" and cookies <shipmentcost :
		            print "Sorry you need",str(shipmentcost-cookies),"more"

		        #ALCHEMY LAB
		        if buyaction == "alchemy lab" and cookies >= alchemycost and shipments > 0:
		            alchemy_labs += 1
		            cookies -= alchemycost
		            print "Total alchemy labs:",alchemy_labs
		            if alchemy_labs == 1:
		                print "Portal unlocked, 6,666 CPS"
		        elif buyaction == "alchemy lab" and cookies <alchemycost :
		            print "Sorry you need",str(alchemycost-cookies),"more"
		        #PORTAL
		        if buyaction == "portal" and cookies >= portalcost and alchemy_labs > 0:
		            portals += 1
		            cookies -= portalcost
		            print "Total portals:",portals
		            if portals == 1:
		                print "Time Machine unlocked, 98,765 CPS"
		        elif buyaction == "portal" and cookies <portalcost :
		            print "Sorry you need",str(portalcost-cookies),"more"
		        #TIME MACHINE
		        if buyaction == "time machine" and cookies >= timecost and portals > 0:
		            time_machines += 1
		            cookies -= timecost
		            print "Total time machines:",time_machines
		            if time_machines == 1:
		                print "Antimatter Condenser unlocked, 999,999 CPS"
		        elif buyaction == "time machine" and cookies <timecost :
		            print "Sorry you need",str(timecost-cookies),"more"
		        #ANTIMATTER CONDENSER
		        if buyaction == "antimatter condenser" and cookies >= anticost and time_machines > 0:
		            antimatter_condensers += 1
		            cookies -= anticost
		            print "Total antimatter condensers:",antimatter_condensers
		            if antimatter_condensers == 1:
		                print "Prism unlocked, 10,000,000 CPS"
		        elif buyaction == "antimatter condneser" and cookies < anticost:
		            print "Sorry you need",str(anticost-cookies),"more"
		        #PRISM
		        if buyaction == "prism" and cookies >= prismcost and antimatter_condensers > 0:
		            prisms += 1
		            cookies -= prismcost
		            print "Total prisms:",prisms
		        elif buyaction == "prisms" and cookies < prismcost:
		            print "Sorry you need",str(prismcost-cookies),"more"
		        starttime = time.clock()

		    #Upgrade store
		    if action=="upgrade":
		        #Auto cashin
		        cashin(cursors,grandmas,farms,factories,mines,shipments,alchemy_labs,portals,time_machines,antimatter_condensers,prisms)
		        print "\nYou have",cookies,"cookeies\n"
		        print"Upgrades currently unlocked:\n"
		        #Displays currently unlocked upgrades
		        if Reinforced_Index_Finger == True:
		            print "Reinforced Index Finger: The mouse gains +1 cookie per click, cursors gain 0.1 CPS, 100 cookies"
		            print "\"prod prod\"\n"
		        if Carpal_Tunnel == True:
		            print "Carpal Tunnel Prevention Cream: The mouse and cursors are twice as efficent, 400 cookies"
		            print "\"it... it hurts to click...\"\n"
		        if ambidextrous == True:
		            print "Ambidextrous: The mouse and cursors are twice as efficient, 10,000 cookies"
		            print "\"Look ma, both hands!\"\n"
		        if forwards == True:
		            print "\"RE:RE:thought you'd get a kick out of this ;))\"\nre"


		        upgradebuy = (raw_input("So whatdya want?")).lower()
		        
		        #Upgrades use a true false method of determining ability to buy, then stores a one or a zero for the saving and loading function

		        #CURSOR
		        if upgradebuy =="reinforced index finger" and cookies>= 100 and Reinforced_Index_Finger == True:
		            
		            cookies -= 100
		            Reinforced_Index_Finger= False
		            Is_Reinforced_Index_Finger= 1
		            print "UPGRADED!"
		        else:
		            print "Need",(100-cookies),"cookeies"

		        if upgradebuy =="carpal tunnel prevention cream" and cookies>= 400 and Carpal_Tunnel == True:
		            clickcps*=2
		            cursorcps*=2
		            cookies -= 400
		            Carpal_Tunnel= False
		            Is_Carpal_Tunnel = 1
		            print "UPGRADED!"
		        else:
		            print "Need",(400-cookies),"cookeies"

		        if upgradebuy == "ambidextrous" and cookies>= 10000 and ambidextrous == True:
		            clickcps *=2
		            cursorcps *=2
		            cookies-= 10000
		            ambidextrous = False
		            Is_ambidextrous = 1
		            print "UPGRADED!"
		        else:
		            print "Need",(10000-cookies),"cookeies"

		        #GRANDMA
		        if upgradebuy =="forwards from grandma" and cookies>= 1000 and forwards== True:
		            grandmacps += 0.3
		            cookies -= 1000
		            print "UPGRADED!"
		            forwards = False
		            Is_forwards = 1
		        else:
		            print "Need",(1000-cookies),"cookeies"		







	#DukeOS explenation
	elif command == "Why?" or command == "why?" or command == "Why"or command == "Why":
		print 'DUKEOS is founded on the principals of providing a quality Operating System for all people, for only $999 a month.'
		print 'DUKEOS was created back in 7/2/14, when Duke Johnson decided he was fed up with the currenet Operating systems, windows, OSX, and linux.'
		print 'Decieding none of these were quality Duke decided it was time to serve the undereserved majority of people and provide the best Operating system possible.'
	#For when DukeOS doesn't get what your saying
	else:
		print 'processing'
		time.sleep(10)
		print('compiling result')
		time.sleep(10)
		print 'outputing result'
		time.sleep(10)
		print 'result = dirt'