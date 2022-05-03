
class sinhvien:
    def __init__(self,malop,masv,hoten,ngaysinh,dtb):
        self.__infor = {
            'malop':malop,
            'masv': masv,
            'hoten':hoten,
            'ngaysinh':ngaysinh,
            'dtb': dtb
            }
    def get_malop(self):
        return self.__infor['malop']
    def get_masv(self):
        return self.__infor['masv']
    def get_hoten(self):
        return self.__infor['hoten']
    def get_ngaysinh(self):
        return self.__infor['ngaysinh']
    def get_dtb(self):
        return self.__infor['dtb']

lst_sv = []



    
