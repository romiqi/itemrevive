import tkinter as tk
import tkinter.font
from tkinter import * 

class InitializeMainPage:#页面初始化
	def __init__(self, lastWindow):
		lastWindow.destroy() 
		self.root = tk.Tk()  
		self.root.title('物品复活小程序')
		self.root.geometry('500x200')
		self.root.resizable(0, 0)	
  
		#添加功能按键和导航
		buttonAdd = Button(self.root, text = "添加物品", font = tkinter.font.Font(size = 16),
        command = lambda: AddItems(self.root), width = 10, height = 2, fg = 'white', bg = 'gray', activebackground = 'black', activeforeground = 'white')
		buttonAdd.place(x = 75, y = 0)
  
		buttonDelete = Button(self.root, text = "删除物品", font = tkinter.font.Font(size = 16), 
        command = lambda: DeleteItems(self.root), width = 10, height = 2, fg = 'white', bg = 'gray', activebackground = 'black', activeforeground = 'white')
		buttonDelete.place(x = 300, y = 0)
   
		buttonFind = Button(self.root, text = "查找物品", font = tkinter.font.Font(size = 16), 
        command = lambda: FindItems(self.root), width = 10, height = 2, fg = 'white', bg = 'gray', activebackground = 'black', activeforeground = 'white')
		buttonFind.place(x = 75, y = 75)
		
		buttonList = Button(self.root, text = "物品列表", font = tkinter.font.Font(size = 16), 
        command = lambda: ListItems(self.root), width = 10, height = 2, fg = 'white', bg = 'pink', activebackground = 'black', activeforeground = 'white')
		buttonList.place(x = 300, y = 75)
		
		buttonExit = Button(self.root, text = "退出", font = tkinter.font.Font(size = 16), 
        command = self.root.destroy, width = 20, height = 1, fg = 'white', bg = 'red', activebackground = 'black', activeforeground = 'white')
		buttonExit.place(x = 125, y = 150)
		
		self.root.mainloop()

items = []

class AddItems:#添加物品
	def __init__(self, lastWindow):
		lastWindow.destroy()
		self.root = tk.Tk() 
		self.root.title('添加物品')
		self.root.geometry('450x300')
		self.root.resizable(0, 0)	

		#输入框设置和按钮设置
		tk.Label(self.root, text = '物品名称: ').place(x = 80, y =  50)
		tk.Label(self.root, text = '物品描述: ').place(x = 80, y =  100)
		tk.Label(self.root, text = '联系人信息: ').place(x = 80, y =  150)

		self.itemName = tk.Entry(self.root)
		self.itemName.place(x = 160, y = 50)
  
		self.itemDescription = tk.Entry(self.root)
		self.itemDescription.place(x = 160, y = 100)
  
		self.contactsInfo = tk.Entry(self.root)
		self.contactsInfo.place(x = 160, y = 150)

		buttonReturn = Button(self.root, text = "确定", width = 8, font = tkinter.font.Font(size = 12), command = self.addItems)
		buttonReturn.place(x = 200, y = 200)
		buttonReturn = Button(self.root, text = "返回", width = 8, font = tkinter.font.Font(size = 12), command = self.returnToHomePage)
		buttonReturn.place(x = 200, y = 250)
		
		self.root.mainloop()

	def addItems(self):
		#键入物品信息
		itemInfo = {}
		itemInfo['itemName'] = self.itemName.get()
		itemInfo['itemDescription'] = self.itemDescription.get()
		itemInfo['contactsInfo'] = self.contactsInfo.get()
		items.append(itemInfo)
		#添加物品
		successInfo = tk.Tk()
		successInfo.geometry('150x100')
		tk.Label(successInfo, text = '添加成功 ').place(x = 50, y =  25)
  
		successInfo.mainloop()

	def returnToHomePage(self):
    		InitializeMainPage(self.root)


class DeleteItems:#删除物品
	def __init__(self, lastWindow):
		lastWindow.destroy() 
		self.root = tk.Tk() 
		self.root.title('删除物品')
		self.root.geometry('450x300')

		#输入框设置和按钮设置
		tk.Label(self.root, text = '物品名称: ').place(x = 80, y =  50)
		tk.Label(self.root, text = '物品描述: ').place(x = 80, y =  100)
		tk.Label(self.root, text = '联系人信息: ').place(x = 80, y =  150)
		
		self.itemName = tk.Entry(self.root)
		self.itemName.place(x = 160, y = 50)

		self.itemDescription = tk.Entry(self.root)
		self.itemDescription.place(x = 160, y = 100)
  
		self.contactsInfo = tk.Entry(self.root)
		self.contactsInfo.place(x = 160, y = 150)

		buttonReturn = Button(self.root, text = "确定", width = 8, font = tkinter.font.Font(size = 12), command = self.deleteItems)
		buttonReturn.place(x = 200, y = 200)
		buttonReturn = Button(self.root, text = "返回", width = 8, font = tkinter.font.Font(size = 12), command = self.returnToHomePage)
		buttonReturn.place(x = 200, y = 250)
		
		self.root.mainloop()


	def deleteItems(self):
     
		findItemFlag = 0
		#键入物品信息
		itemName = self.itemName.get()
		itemDescription = self.itemDescription.get()
		contactsInfo = self.contactsInfo.get()
		#查找物品并删除，若未查找到输出提示
		for item in items:
			if item.get('itemName') == itemName and item.get('itemDescription') == itemDescription and item.get('contactsInfo') == contactsInfo:
				items.remove(item)
				findItemFlag = 1
		if findItemFlag:	
			successInfo = tk.Tk()
			successInfo.geometry('100x50')
			tk.Label(successInfo, text = '物品删除成功 ').place(x = 30, y =  20)
			successInfo.mainloop()
		if not findItemFlag:
			successInfo = tk.Tk()
			successInfo.geometry('100x50')
			tk.Label(successInfo, text = '未找到此物品').place(x = 30, y =  20)
			successInfo.mainloop()
  	
	def returnToHomePage(self):
    		InitializeMainPage(self.root)


class ListItems:#显示物品信息
	def __init__(self, lastWindow):
		lastWindow.destroy()
		self.root = tk.Tk()  
		self.root.title('物品列表')
		self.root.geometry('450x300')

		tkScroll = tk.Scrollbar(self.root)
		tkScroll.pack(side = tk.RIGHT,fill = tk.Y)
		#输出所有物品信息
		printMessage = tk.Text(self.root,width = 100,height = 20)
		for item in items:
			printMessage.insert('insert',"物品名称：{}\t物品描述：{}\t联系人信息：{}\n".format(item.get('itemName'),item.get('itemDescription'),item.get('contactsInfo')))
		
		printMessage.pack()

		printMessage.config(yscrollcommand = tkScroll.set) 
		tkScroll.config(command = printMessage.yview) 
					
		buttonReturn = Button(self.root, text = "返回", width = 8, font = tkinter.font.Font(size = 12), command = self.returnToHomePage)
		buttonReturn.place(x = 200, y = 270)
		
		self.root.mainloop()

	def returnToHomePage(self):
		InitializeMainPage(self.root)


class FindItems:#查找物品
	def __init__(self, lastWindow):
		lastWindow.destroy() 
		self.root = tk.Tk()  
		self.root.title('查找物品')
		self.root.geometry('450x300')
		
		#输入框设置和按钮设置
		tk.Label(self.root, text = '物品名称: ').place(x = 80, y =  50)
		tk.Label(self.root, text = '物品描述: ').place(x = 80, y =  100)
		tk.Label(self.root, text = '联系人信息: ').place(x = 80, y =  150)
  
		self.itemName = tk.Entry(self.root)
		self.itemName.place(x = 160, y = 50)

		self.itemDescription = tk.Entry(self.root)
		self.itemDescription.place(x = 160, y = 100)
  
		self.contactsInfo = tk.Entry(self.root)
		self.contactsInfo.place(x = 160, y = 150)

		buttonReturn = Button(self.root, text = "确定", width = 8, font = tkinter.font.Font(size = 12), command = self.findItems)
		buttonReturn.place(x = 200, y = 200)
		buttonReturn = Button(self.root, text = "返回", width = 8, font = tkinter.font.Font(size = 12), command = self.returnToHomePage)
		buttonReturn.place(x = 200, y = 250)
		
		self.root.mainloop()

	def findItems(self):
     
		findItemFlag = 0
  
		tkScroll = tk.Scrollbar(self.root)
		tkScroll.pack(side = tk.RIGHT,fill = tk.Y)
		#键入物品信息
		itemName = self.itemName.get()
		itemDescription = self.itemDescription.get()
		contactsInfo = self.contactsInfo.get()
		#查找物品 若未找到输出提示信息
		printMessage = tk.Text(self.root, width = 100, height = 20)
		for item in items:
			if item.get('itemName') == itemName and item.get('itemDescription') == itemDescription and item.get('contactsInfo') == contactsInfo:
				findItemFlag = 1
				printMessage.insert('insert',"物品名称：{}\t物品描述：{}\t联系人信息：{}\n".format(item.get('itemName'),item.get('itemDescription'),item.get('contactsInfo')))
		if not findItemFlag:
			printMessage.insert('insert','未找到该物品')
		printMessage.pack()

		printMessage.config(yscrollcommand = tkScroll.set) 
		tkScroll.config(command = printMessage.yview) 
							
		self.root.mainloop()
  
	def returnToHomePage(self):
		InitializeMainPage(self.root)


if __name__=='__main__':
	window = tk.Tk()
	InitializeMainPage(window)