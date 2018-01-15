from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
import MySQLdb as db

try:
	conn = db.connect('data.cojvodnw3hk2.ap-south-1.rds.amazonaws.com','user','ibadkhan','cube_iot')
except:
	pass


		
class screen(GridLayout):
	def __init__(self, **kwargs):
		super(screen,self).__init__(**kwargs)
		self.cols = 3
		self.l1=Label(text="27c",font_size='60sp')
		self.l2=Label(text="70%",font_size='60sp')
		self.l3=Label(text="1003",font_size='60sp')
		self.add_widget(Image(source='temp.jpg'))
		self.add_widget(Image(source="humi.png"))
		self.add_widget(Image(source="press.png"))
                self.add_widget(self.l1)
                self.add_widget(self.l2)
                self.add_widget(self.l3)
		Clock.schedule_interval(self.my_callback,0.5)
		
	def my_callback(self,dt):
		try:
                
			c=conn.cursor()
	        	c.execute("select * from value1")
			rows = c.fetchall()
                	self.l1.text=str(rows[0][1])+"c"
			self.l2.text=str(rows[0][2])+"%"
                	self.l3.text=str(rows[0][3])+"Pa"
			conn.commit()
		except:
			self.l1.text=str("nan")
                        self.l2.text=str("nan")
                        self.l3.text=str("nan")

class mainapp(App):
	def build(self):
		return screen()
if __name__=="__main__":
	mainapp().run() 
