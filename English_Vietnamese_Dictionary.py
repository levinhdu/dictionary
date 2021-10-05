my_dict = {"Hello": "Xin chào","name":"Tên","age":"Tuổi","egg":"trứng","meat":"thịt","one":'số một',"two":'số hai',"three":"số ba"}

def show_header():
    print('''
        Nhập 1 để nhập từ tiếng anh.
        Nhập 2 để thoát chương trình.
    ''')

def search(my_dict):
    C = False
    vocabulary = input("Nhập từ tiếng anh cần tra sang tiếng việt: ")
    for eng, vn in my_dict.items():
        if vocabulary == eng:
            print(f'Từ {vocabulary} có nghĩa tiếng việt là {vn}')
            C= True
            break
    if C == False:
        print(f'Từ {vocabulary} không có trong từ điển.')

def get_choice():
    return input("Lựa chọn của bạn: ")

while True:
    show_header()
    choice = get_choice()
    if choice == '1':
        search(my_dict)
    elif choice == '2':
        break

