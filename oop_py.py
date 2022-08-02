
class Nguoi:
    def __init__(self, name, address, sex):
        self.name = name
        self.address = address
        self.sex = sex
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getSex(self):
        return self.sex
    
class SinhVien(Nguoi):
    global lop, nganh
    
    def setLop(self, val):
        self.lop = val
    def getLop(self, val):
        return self.lop
    
    def setNganh(self, val):
        return self.nganh
    def getNganh(self, val):
        self.nganh = val
        
    def tinhDiemThuong(self):
        if self.nganh == "cntt":
            return 1
        else:
            if self.nganh == "kinhte":
                return 1.5
            else:
                return 0
            
class GiangVien(Nguoi):
    global trinhdo
    
    def luongcb(self):
        return 150000
    
    def setTrinhDo(self, val):
        self.trinhdo = val
    def getTrinhDo(self):
        return self.trinhdo
    
    def tinhLuong(self):
        if self.trinhdo == "cunhan":
            return float(self.luongcb()) * 2.34
        if self.trinhdo == "thacsi":
            return float(self.luongcb()) * 3.67
        if self.trinhdo == "tiensi":
            return float(self.luongcb()) * 5.66
        

myIn4 = GiangVien("Mang Bảo", "Cam Ranh", "Nam")
myIn4.setTrinhDo("cunhan")
print(myIn4.tinhLuong())