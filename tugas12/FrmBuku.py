import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='IDBUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDULBUKU:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtIdbuku = Entry(mainFrame) 
        self.txtIdbuku.grid(row=0, column=1, padx=5, pady=5)
        self.txtIdbuku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJudulbuku = Entry(mainFrame) 
        self.txtJudulbuku.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtTahun = Entry(mainFrame) 
        self.txtTahun.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','Idbuku','Judulbuku','Penulis','Tahun','Kodebuku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="50")
        self.tree.heading('Idbuku', text='IDBUKU')
        self.tree.column('Idbuku', width="100")
        self.tree.heading('Judulbuku', text='JUDULBUKU')
        self.tree.column('Judulbuku', width="300")
        self.tree.heading('Penulis', text='PENULIS')
        self.tree.column('Penulis', width="150")
        self.tree.heading('Tahun', text='TAHUN')
        self.tree.column('Tahun', width="150")
        self.tree.heading('Kodebuku', text='KODEBUKU')
        self.tree.column('Kodebuku', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtIdbuku.delete(0,END)
        self.txtIdbuku.insert(END,"")
        self.txtJudulbuku.delete(0,END)
        self.txtJudulbuku.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["Idbuku"],d["Judulbuku"],d["Penulis"],d["Tahun"],d["Kodebuku"]))
    def onCari(self, event=None):
        Idbuku = self.txtIdbuku.get()
        obj = Buku()
        a = obj.get_by_Idbuku(Idbuku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Idbuku = self.txtIdbuku.get()
        obj = Buku()
        res = obj.get_by_Idbuku(Idbuku)
        self.txtIdbuku.delete(0,END)
        self.txtIdbuku.insert(END,obj.Idbuku)
        self.txtJudulbuku.delete(0,END)
        self.txtJudulbuku.insert(END,obj.Judulbuku)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.Penulis)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,obj.Tahun)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.Kodebuku)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Idbuku = self.txtIdbuku.get()
        Judulbuku = self.txtJudulbuku.get()
        Penulis = self.txtPenulis.get()
        Tahun = self.txtTahun.get()
        Kodebuku = self.txtKodebuku.get()
        # create new Object
        obj = Buku()
        obj.Idbuku = Idbuku
        obj.Judulbuku = Judulbuku
        obj.Penulis = Penulis
        obj.Tahun = Tahun
        obj.Kodebuku = Kodebuku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Idbuku(Idbuku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Idbuku = self.txtIdbuku.get()
        obj = Buku()
        obj.Idbuku = Idbuku
        if(self.ditemukan==True):
            res = obj.delete_by_Idbuku(Idbuku)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()