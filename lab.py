from xhtml2pdf import pisa
from datetime import datetime

lst = []
source_html = []

def outInfor(dic): #Xuất dữ liệu
    print('========== User Ifor ==========')

    print('ID : ', str(dic['id'])+ '\n' + 
          'Name : ', dic['name'] + '\n'+
          'Birthday : ',  str(dic['birthday']) + '\n'
          'Phone_value : ', str(dic['phone_value']) + '\n'
          'Email_value : ', str(dic['email_value']))
    print('===============================')


def validate():
        import datetime

        try:
            birthday = input('enter : \n'+
                             'ex: YYYY-MM-DD  : ')
            datetime.date.fromisoformat(birthday)
        except :
            return validate()
        return birthday

def inputUserKB(): #Nhập thông tin

    user = {}
    user['id'] = trEx_int('id')
    user['name'] = input('Enter your name : ')
    user['birthday']= validate()
    user['phone_value'] = input('Enter your phone : ')
    user['email_value'] = input('Enter your email \n'+
                            'ex: abcdef@gmail.com : '  )
    return user


def trEx_int(msg):  #Xử lý ngoại lệ
    try:
        num = int(input(f'Enter your {msg} : '))
        return num
    except:
        return trEx_int(msg)


def showInfor(user_lst): #In tất cả các dữ liệu 
    for user in user_lst:
        outInfor(user)
    print(lst)


def ExportPDF(user_lst):
    for i in user_lst:
        html = f"""
            <img src="https://scontent-hkg4-1.xx.fbcdn.net/v/t1.30497-1/143086968_2856368904622192_1959732218791162458_n.png?_nc_cat=1&cb=99be929b-59f725be&ccb=1-7&_nc_sid=7206a8&_nc_ohc=DH2e7R2-NdgAX8QfZX-&_nc_ht=scontent-hkg4-1.xx&oh=00_AfC15rMxMACqzfDATkLyr4TN-IugZ-q5srOeXqV547CMfw&oe=64D1E6F8" >
                <h1>ID  : {i['id']}  </h1>
                <h1>Name : {i['name']}   </h1>
                <h1>Birthday : {i['birthday']}   </h1>
                <h1>Phone : {i['phone_value']}  </h1>
                <h1>Email : {i['email_value']}  </h1>
            <hr>
        """
        source_html.append(html)

    user_html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>TEST</title>
        </head>
        <body>
            {''.join(source_html)}
        </body>
    </html>
    """
    output_filename = "infor.pdf"

    
    def convert_to_pdf(sourcePDF,outputPDF):


        result_file = open(outputPDF,'w+b')
        pisa_status = pisa.CreatePDF(sourcePDF,dest=result_file)

        result_file.close()
        return pisa_status.error

    if __name__ == '__main__':
        pisa.showLogging()
        convert_to_pdf(user_html,output_filename)


def sortedUser(): # Sắp xếp id

    global lst
    swapped = False
    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user1 = lst[j]
            user2 = lst[j+1]
            if user1['id'] > user2['id']:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
                return  



def sortedName(): #Sắp xếp tên


    global lst
    swapped = False
    for i in range(len(lst)-1): 

        for j in range(0,len(lst)-1-i): 
            user1 = lst[j]
            user2 = lst[j+1]
            if user1['name'] > user2['name']:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
                return  



def sortedDate():

    global lst
    swapped = False

    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user_date_1 = datetime.strptime(lst[j]['birthday'],'%Y-%m-%d').date()
            user_date_2 = datetime.strptime(lst[j+1]['birthday'],'%Y-%m-%d').date()
            if user_date_1.day > user_date_2.day:
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
            return
        


        
def sortedMonth():

    global lst
    swapped = False
    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user_month_1 = datetime.strptime(lst[j]['birthday'],'%Y-%m-%d').date()
            user_month_2 = datetime.strptime(lst[j+1]['birthday'],'%Y-%m-%d').date()
            if user_month_1.month > user_month_2.month:
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
            return 



def sortedYear():

    global lst
    swapped = False
    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user_year_1 = datetime.strptime(lst[j]['birthday'],'%Y-%m-%d').date()
            user_year_2 = datetime.strptime(lst[j+1]['birthday'],'%Y-%m-%d').date()
            if user_year_1.year > user_year_2.year:
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
            return 

def removeInfor(user_lst): # Xóa dữ liệu
    del_user = int(input('Enter id : '))
    for i in range(len(user_lst)):
        if user_lst[i]['id'] == del_user:
            del user_lst[i]
            break


def exportCSV(lst):
    with open('information.csv','w') as fileOut:
        fileOut.write('ID,')
        fileOut.write('Name,')
        fileOut.write('Birthday,')
        fileOut.write('Phone,')
        fileOut.write('Email \n',)
        for i in lst:
            fileOut.write(str(i['id'])+',')
            fileOut.write(str(i['name'])+',')
            fileOut.write(str(i['birthday'])+',')
            fileOut.write(str(i['phone_value'])+',')
            fileOut.write(str(i['email_value'])+'\n')



def inputUser(id,name,birthday,phone_value,email_value): #Nhập thông tin

    user = {}
    user['id'] = int(id)
    user['name'] = name
    user['birthday']= birthday
    user['phone_value'] = phone_value
    user['email_value'] = email_value

    return user



def inputfromCSV():
    
    with open(input('Nhap file : '),'r') as f:
        read_line = f.readlines()


    for i in range(1,len(read_line)):
        data = ''.join(read_line[i].split('\n')).split(',')
        user = inputUser(data[0],data[1],data[2],data[3],data[4])
        lst.append(user)



while True:
    print('==================================')
    lua_chon = int(input('Select number \n'+
                            '1-Input data \n'+
                            '2-Delete data \n' +
                            '3-Sort information \n'+
                            '4-Show all information\n' +
                            '5-Export to PDF\n' + 
                            '6-Export to CSV\n' + 
                            '7-Input from CSV\n' +
                            '8-Quit    \n'+
                            '================================== \n'+
                            'Enter your answer : '))
    print('==================================')

    if lua_chon == 1:
        user = inputUserKB()
        lst.append(user)

    elif lua_chon == 2:
        if len(lst) == 0:
            print('No Data Found!')
        else:
            removeInfor(lst)
            print('Success')

    elif lua_chon == 3:
        if len(lst) == 0:
            print('No Data Found!')
        else:
            while True:
                choices = int(input('Select number \n'+
                                    '1-Sort id \n'+
                                    '2-Sort name \n'+
                                    '3-Sort birth \n'+
                                    '4-Quit\n'+
                                    'Enter your answer : '))
                
                if choices == 1:
                    asc_des = int(input('Select number \n'+
                                    '1-Ascending \n'+
                                    '2-Descending\n'+
                                    'Enter your answer : '))
                    if asc_des == 1:
                        sortedUser()
                        print('Success')

                    elif asc_des == 2:
                        sortedUser()
                        lst.reverse()
                        print('Success')

                elif choices == 2:
                    asc_des = int(input('Select number \n'+
                                    '1-Ascending \n'+
                                    '2-Descending\n'+
                                    'Enter your answer : '))
                    if asc_des == 1:
                        sortedName()
                        print('Success')

                    elif asc_des == 2:
                        sortedName()
                        lst.reverse()
                        print('Success')

                elif choices == 3:
                    asc_des = int(input('Select number \n'+
                                    '1-Ascending \n'+
                                    '2-Descending\n'+
                                    'Enter your answer : '))
                    
                    if asc_des == 1:
                        sortedDate()
                        sortedMonth()
                        sortedYear()
                        print('Success')

                    elif asc_des == 2:
                        sortedDate()
                        sortedMonth()
                        sortedYear()                    
                        lst.reverse()
                        print('Success')

                elif choices == 4:
                    break
            
    elif lua_chon == 4:
        showInfor(lst)

    elif lua_chon == 5: 
        ExportPDF(lst)
        print('Success')
    
    elif lua_chon == 6:
        exportCSV(lst)
        print('Success')

    elif lua_chon == 7:
        inputfromCSV()
        print('Success')

    elif lua_chon == 8:
        break