import threading
import value
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
class PomeloFlask():
	def __init__(self): #Maze setup ayarlama
		self.maze1Section1 = ["forward 1", "right 1", "left 1"]
		self.mazeCount = 1
		self.mazeSectionCount = 1
		app.run(host='0.0.0.0', port=80, debug=True)
	def SectionCheck(self, q2, q3):
		SectionVal = q2.get()
		ButtonVal = q3.get()
		solved = False
		videoname = "0.0"
		MazeData = {'vid': videoname,
					'pressCount': ButtonVal
					'solved': solved
					}
		if self.mazeCount == 1:
			if self.mazeSectionCount == 1:
				if SectionVal == self.maze1Section1:
					videoname = str(mazeCount) + "." + str(mazeSectionCount)
					self.mazeSectionCount += 1 # eger sonuncuysa self.mazeCount += 1 /n self.mazeSectionCount = 1					return "Correct, with this many button pressess " + str(ButtonVal)
					solved = True
					MazeData.update({'vid': videoname,
									'solved': solved})
					return render_template("index.html", **MazeData)
				else:
					return render_template("index.html", **MazeData)

	def Loop(self, q2, q3):
		while True:
			self.SectionCheck(q2, q3)