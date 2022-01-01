""" SudokuGUI.py
"""

import wx
from wx import xrc
import wx.grid

class SudokuApp( wx.App ):
	size = 9
	def OnInit( self ):
		self.res = xrc.XmlResource( "SudokuGUI.xrc" )
		self.init_frame()
		return True
	def init_frame( self ):
		self.frame = self.res.LoadFrame( None, "SG_Frame" )
		self.grid = xrc.XRCCTRL( self.frame, "s_grid" )
		self.init_grid()

		#self.panel = xrc.XRCCTRL( self.frame, "EvEInfo_Panel" )
		wx.EVT_MENU( self, wx.ID_EXIT, self.onQuit )
		self.frame.Show()
	def init_grid( self ):
		# Grid
		self.grid.CreateGrid( self.size, self.size )
		self.grid.EnableEditing( True )
		self.grid.EnableGridLines( True )
		#self.grid.EnagleDragGridSize( False )
		self.grid.SetMargins( 0, 0 )
		
		# Columns
		for c in range( self.size ):
			self.grid.SetColSize( c, 20 )
		self.grid.EnableDragColMove( False )
		self.grid.EnableDragColSize( False )
		self.grid.SetColLabelSize( 30 )
		#self.grid.SetColLabelAlignment( wxALIGN_CENTRE, wxALIGH_CENTRE )
		
		# Rows
		#self.grid.EnagleDragRowSize( True )
		#self.grid.SetRowLabelSize( 80 )
		#self.grid.SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGH_CENTRE )
		
		# Colors
		for y in range(self.size):
			for x in range(self.size):
		#		print x,y
		#		self.grid.setCellBackgroundColor( "#888888", x, y )
				pass
				
		
		
	def onQuit( self, evt ):
		self.frame.Close()
	
	