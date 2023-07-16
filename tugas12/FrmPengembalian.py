import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengembalian import *
class FrmPengembalian:
    
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
        Label(mainFrame, text='IDPENGEMBALIAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PENGEMBALIAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_MAHASISWA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtIdpengembalian = Entry(mainFrame) 
        self.txtIdpengembalian.grid(row=0, column=1, padx=5, pady=5)
        self.txtIdpengembalian.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTanggal_pengembalian = Entry(mainFrame) 
        self.txtTanggal_pengembalian.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtNama_mahasiswa = Entry(mainFrame) 
        self.txtNama_mahasiswa.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','Idpengembalian','tanggal_pengembalian','kodebuku','nama_mahasiswa')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="50")
        self.tree.heading('Idpengembalian', text='IDPENGEMBALIAN')
        self.tree.column('Idpengembalian', width="150")
        self.tree.heading('tanggal_pengembalian', text='TANGGAL_PENGEMBALIAN')
        self.tree.column('tanggal_pengembalian', width="200")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="100")
        self.tree.heading('nama_mahasiswa', text='NAMA_MAHASISWA')
        self.tree.column('nama_mahasiswa', width="200")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtIdpengembalian.delete(0,END)
        self.txtIdpengembalian.insert(END,"")
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,"")
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengembalian
        obj = Pengembalian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["Idpengembalian"],d["tanggal_pengembalian"],d["kodebuku"],d["nama_mahasiswa"]))
    def onCari(self, event=None):
        Idpengembalian = self.txtIdpengembalian.get()
        obj = Pengembalian()
        a = obj.get_by_Idpengembalian(Idpengembalian)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Idpengembalian = self.txtIdpengembalian.get()
        obj = Pengembalian()
        res = obj.get_by_Idpengembalian(Idpengembalian)
        self.txtIdpengembalian.delete(0,END)
        self.txtIdpengembalian.insert(END,obj.Idpengembalian)
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,obj.tanggal_pengembalian)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,obj.nama_mahasiswa)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Idpengembalian = self.txtIdpengembalian.get()
        tanggal_pengembalian = self.txtTanggal_pengembalian.get()
        kodebuku = self.txtKodebuku.get()
        nama_mahasiswa = self.txtNama_mahasiswa.get()
        # create new Object
        obj = Pengembalian()
        obj.Idpengembalian = Idpengembalian
        obj.tanggal_pengembalian = tanggal_pengembalian
        obj.kodebuku = kodebuku
        obj.nama_mahasiswa = nama_mahasiswa
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Idpengembalian(Idpengembalian)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Idpengembalian = self.txtIdpengembalian.get()
        obj = Pengembalian()
        obj.Idpengembalian = Idpengembalian
        if(self.ditemukan==True):
            res = obj.delete_by_Idpengembalian(Idpengembalian)
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
    aplikasi = FrmPengembalian(root2, "Aplikasi Data Pengembalian")
    root2.mainloop()