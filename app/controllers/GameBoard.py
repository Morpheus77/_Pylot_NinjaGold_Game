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
			message = " " + "You are now in the {0}".format(session['location'])
			session['gold'] = random.randint(1,10)
			
		if session['location'] == 'cave':
			message = " " + "You are now in the {0}".format(session['location'])
			
		if session['location'] == 'house':
			message = " " + "You are now in the {0}".format(session['location'])
			
		if session['location'] == 'casino':
			message = " " + "You are now in the {0}".format(session['location'])
			
		return self.load_view('index.html', message = message, turn = session['turn'], gold = session['gold'])
		
	def reset(self):
		message = "reset!"
		session['turn'] = 0
		session['location'] = " "
		return redirect('/')