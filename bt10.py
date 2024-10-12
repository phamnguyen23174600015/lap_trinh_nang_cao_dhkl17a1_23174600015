import json
#Đọc dữ liệu từ file JSON
def Data(employee_data):
    with open(employee_data, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
#Thống kê nhân viên theo đơn vị
def phan_tich(data):
    ten = data['company']
    dia_chi = data['address']
    
    tong_nv = 0
    for unit in data['units']:
        tong_nv += unit['employees']


    print(f"Tên công ty: {ten}\n Địa chỉ: {dia_chi}\n Tổng số nhân viên: {tong_nv}")
    print("----Thống kê nhân viên theo đơn vị----")
    for donvi in data['units']:
        ten_dv = donvi['name']
        nv = donvi['employees']
        ti_le = (nv / tong_nv) * 100
        print(f"Tên đơn vị: {ten_dv}\n Số nhân viên: {nv}\n Tỷ lệ: {ti_le:.2f}%")

data = Data('employee_data.json')
phan_tich(data)   