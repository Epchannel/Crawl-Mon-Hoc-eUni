# Thay Line 10 & 20
import requests

url = "https://edusoft-api.humg.edu.vn/api/sch/w-locdssinhvientheotohoc"

headers = {
    "User-Agent": "Dart/2.18 (dart:io)",
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip",
    "Authorization": "XXX",
    "Host": "edusoft-api.humg.edu.vn"
}

cookies = {
    "ASP.NET_SessionId": "5nvai1iuk201lvdbto5fttu1"
}

data = {
    "filter": {
        "id_to_hoc": "XXX"
    },
    "additional": {
        "paging": {
            "limit": 1000,
            "page": 1
        },
        "ordering": [
            {
                "name": "ten",
                "order_type": "1"
            }
        ]
    }
}

response = requests.post(url, headers=headers, cookies=cookies, json=data)

if response.status_code == 200:
    json_data = response.json()

    ds_sinh_vien = json_data['data']['ds_sinh_vien']

    for sinh_vien in ds_sinh_vien:
        print("Mã sinh viên:", sinh_vien['ma_sinh_vien'])
        print("Họ và tên:", sinh_vien['ho_lot'], sinh_vien['ten'])
        print("Ngày sinh:", sinh_vien['ngay_sinh'])
        print("Lớp:", sinh_vien['ma_lop'], sinh_vien['ten_lop'])

        # Kiểm tra xem trường "dien_thoai" có tồn tại hay không trước khi hiển thị
        if 'dien_thoai' in sinh_vien:
            print("Điện thoại:", sinh_vien['dien_thoai'])
        else:
            print("Không có thông tin điện thoại")
            
        print("Email:", sinh_vien['e_mail'])
        print("==============================")
else:
    print("Failed to fetch data from the API.")
    print("Error:", response.text)  # In ra thông điệp lỗi chi tiết từ phản hồi
