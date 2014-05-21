#!/usr/bin/python
# -*- coding: utf-8 -*- 
import wx
import generaCPubCPriv

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textonombre = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textonombre.Wrap( -1 )
		bSizer3.Add( self.textonombre, 0, wx.ALL, 5 )
		
		self.nombretxt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer3.Add( self.nombretxt, 0, wx.ALL, 5 )
		
		bSizer2.Add( bSizer3, 0, wx.EXPAND|wx.TOP, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nombretxt1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Directorio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt1.Wrap( -1 )
		bSizer31.Add( self.nombretxt1, 0, wx.ALL, 5 )
		
		self.dirclaves = wx.DirPickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Selecciona una carpeta", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer31.Add( self.dirclaves, 0, wx.ALL, 5 )
		
		bSizer2.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		self.generarbtn = wx.Button( self.m_panel1, wx.ID_ANY, u"Generar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.generarbtn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Generar Claves", False )
		self.m_panel11 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textonombre1 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Fichero", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textonombre1.Wrap( -1 )
		bSizer32.Add( self.textonombre1, 0, wx.ALL, 5 )
		
		self.ficherofile = wx.FilePickerCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer32.Add( self.ficherofile, 0, wx.ALL, 5 )
		
		bSizer21.Add( bSizer32, 0, wx.EXPAND|wx.TOP, 5 )
		
		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nombretxt11 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Clave publica", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt11.Wrap( -1 )
		bSizer311.Add( self.nombretxt11, 0, wx.ALL, 5 )
		
		self.publicafile = wx.FilePickerCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer311.Add( self.publicafile, 0, wx.ALL, 5 )
		
		bSizer21.Add( bSizer311, 0, wx.EXPAND, 5 )
		
		bSizer3111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nombretxt111 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Clave privada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt111.Wrap( -1 )
		bSizer3111.Add( self.nombretxt111, 0, wx.ALL, 5 )
		
		self.privadafile = wx.FilePickerCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer3111.Add( self.privadafile, 0, wx.ALL, 5 )
		
		bSizer21.Add( bSizer3111, 1, wx.EXPAND, 5 )
		
		self.firmarbtn = wx.Button( self.m_panel11, wx.ID_ANY, u"Firmar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.firmarbtn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel11.SetSizer( bSizer21 )
		self.m_panel11.Layout()
		bSizer21.Fit( self.m_panel11 )
		self.m_notebook1.AddPage( self.m_panel11, u"Firmar", False )
		self.m_panel111 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer211 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textonombre11 = wx.StaticText( self.m_panel111, wx.ID_ANY, u"Fichero", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textonombre11.Wrap( -1 )
		bSizer321.Add( self.textonombre11, 0, wx.ALL, 5 )
		
		self.ficherofile1 = wx.FilePickerCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer321.Add( self.ficherofile1, 0, wx.ALL, 5 )
		
		bSizer211.Add( bSizer321, 0, wx.EXPAND|wx.TOP, 5 )
		
		bSizer3112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nombretxt112 = wx.StaticText( self.m_panel111, wx.ID_ANY, u"Firma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt112.Wrap( -1 )
		bSizer3112.Add( self.nombretxt112, 0, wx.ALL, 5 )
		
		self.firmafile = wx.FilePickerCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer3112.Add( self.firmafile, 0, wx.ALL, 5 )
		
		bSizer211.Add( bSizer3112, 0, wx.EXPAND, 5 )
		
		bSizer31111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nombretxt1111 = wx.StaticText( self.m_panel111, wx.ID_ANY, u"Clave publica", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nombretxt1111.Wrap( -1 )
		bSizer31111.Add( self.nombretxt1111, 0, wx.ALL, 5 )
		
		self.publicafile1 = wx.FilePickerCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer31111.Add( self.publicafile1, 0, wx.ALL, 5 )
		
		bSizer211.Add( bSizer31111, 1, wx.EXPAND, 5 )
		
		self.solfirma = wx.TextCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.solfirma.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer211.Add( self.solfirma, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.firmarbtn1 = wx.Button( self.m_panel111, wx.ID_ANY, u"Comprobar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.firmarbtn1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel111.SetSizer( bSizer211 )
		self.m_panel111.Layout()
		bSizer211.Fit( self.m_panel111 )
		self.m_notebook1.AddPage( self.m_panel111, u"Comprobar firma", True )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.generarbtn.Bind( wx.EVT_BUTTON, self.generar )
		self.firmarbtn.Bind( wx.EVT_BUTTON, self.firmar )
		self.firmarbtn1.Bind( wx.EVT_BUTTON, self.comprobarFirma )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def generar( self, event ):
		generaCPubCPriv.generarClave(self.nombretxt.GetValue(), self.dirclaves.GetPath())
	
	def firmar( self, event ):
		pass
	
	def comprobarFirma( self, event ):
		pass

class MyApp(wx.App):
	def OnInit(self):
		frame_1 = MyFrame1(None)
		self.SetTopWindow(frame_1)
		frame_1.Show()
		return 1

if __name__ == "__main__":
	app = MyApp(0)
	app.MainLoop()
