from system.core.controller import *
import random

class GameBoard(Controller):		
	def __init__(self, action):
		super(GameBoard, self).__init__(action)
		
		self.load_model('WelcomeModel')
		self.db = self._app.db
		
		
	def index(self):
		message = ""
		session['turn'] = 0
		session['location'] = ""
		session['gold'] = 0
		if session['turn'] == 0:
			message = " " + "You are now in the scerene Dojo, surrounded by clarity." + "  "
		return self.load_view('index.html',message = message, turn = session['turn'],gold = session['gold'])
	
	def adventuring(self):
		session['location'] = request.form['building']
		if session['location'] == 'farm':
			return redirect('/GameBoard/addTurn')
			
		if session['location'] == 'cave':
			return redirect('/GameBoard/addTurn')
			
		if session['location'] == 'house':
			return redirect('/GameBoard/addTurn')
			
		if session['location'] == 'casino':
			return redirect('/GameBoard/addTurn')
			
	def addTurn(self):
		session['turn'] = session['turn'] + 1
		return redirect('/GameBoard/getMoney')
		
	def getMoney(self):
		if session['location'] == 'farm':
			addGold = random.randint(10,20)
			session['gold'] = session['gold'] + addGold
			message = " " + "Ninja is now on the {0}. Farm work earned Ninja {1} gold!".format(session['location'],addGold)			
			
		if session['location'] == 'cave':
			addGold = random.randint(5,10)
			session['gold'] = session['gold'] + addGold
			message = " " + "Ninja is now in a {0}!  Spelunking has found Ninja {1} gold!".format(session['location'],addGold)
			
		if session['location'] == 'house':
			addGold= random.randint(2,5)
			session['gold'] = session['gold'] + addGold
			message = " " + "Ninja sneaks into a {0}... lifts {1} gold...  someone coming...!".format(session['location'],addGold)
			
		if session['location'] == 'casino':
			if session['gold'] <= 0:
				message = " " + "Ninja cannot gamble with no gold! Ninja goes to rehab...".format(session['location'])
				return self.load_view('index.html',message = message,turn = session['turn'],gold = session['gold'])
			elif session['gold'] > 0:
				addGold= random.randint(-50,50)
				if addGold < 0:
					session['gold'] = session['gold'] + addGold
					if session['gold'] <=0:
						session['gold'] = 0
					message = "" + "Ninja trips to {0}, and  loses {1} gold!! Poor Ninja =(".format(session['location'],addGold)
					return self.load_view('index.html', message = message, turn = session['turn'], gold = session['gold'])
				session['gold'] = session['gold'] + addGold
				if session['gold'] < 0:
					session['gold'] = 0		
					message = "" + "Ninja trips to {0}, and  loses {1} gold!! Poor Ninja =(".format(session['location'],addGold)
					return self.load_view('index.html', message = message, turn = session['turn'], gold = session['gold'])
				else:
					message = "" + "Ninja trips to {0}! Wins {1} gold!! Lucky Ninja!!".format(session['location'],addGold)
			
		return self.load_view('index.html', message = message, turn = session['turn'], gold = session['gold'])
		
	def reset(self):
		message = "reset!"
		session['turn'] = 0
		session['location'] = " "
		return redirect('/')