from xhtml2pdf import pisa
from datetime import datetime
import os

lst = []
source_html = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
            birthday = input('Enter your birthday \n'+
                             'ex: YYYY-MM-DD  : ')
            datetime.date.fromisoformat(birthday)
        except :
            print('Incorect input!')
            return validate()
        return birthday


def tryceptID():

    user_id_trycep = trEx_int('id')
    for i in lst:
        if i['id'] == user_id_trycep:
            print('ID have been used!') 
            return tryceptID()
    else:
        return user_id_trycep

def inputUserKB(): #Nhập thông tin
    user = {}
    user['id'] = tryceptID()
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
        print('Incorect input!')
        return trEx_int(msg)


def showInfor(user_lst): #In tất cả các dữ liệu 
    for user in user_lst:
        outInfor(user)


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
    try:
        with open(input('Nhap file : '),'r') as f:
            read_line = f.readlines()

        for i in range(1,len(read_line)):
            data = ''.join(read_line[i].split('\n')).split(',')
            user = inputUser(data[0],data[1],data[2],data[3],data[4])
            lst.append(user)
    except FileNotFoundError as er:
        print(er)
        return inputfromCSV()

def updateUser():
    try:
        user_id = int(input('Enter your ID : '))
        for i in lst:
            if i['id'] == user_id:
                print('Success')
                while True:
                    print('==================================')
                    choice_update = int(input('1-Name\n'+
                                                '2-Birthday\n'+
                                                '3-Phone\n'+
                                                '4-Email\n'+
                                                '5-Quit\n'+
                                                '==================================\n'+
                                                'Enter your answer : '))
                    
                    if choice_update == 1:
                        cls()
                        i['name'] = input('Enter your name : ')

                    elif choice_update == 2:
                        cls()
                        i['birthday'] = validate()

                    elif choice_update == 3:
                        cls()
                        i['phone_value'] = input('Enter your phone : ')   

                    elif choice_update == 4:
                        cls()
                        i['email_value'] = input('Enter your email : ')   

                    elif choice_update == 5:
                        choice_quit = toQuit()

                        if choice_quit == 'n':
                            print('==================================')
                            print('Success')
                            print('==================================')

                        elif choice_quit == 'Y':
                            print('==================================')
                            print('Success')
                            print('==================================')
                            return

        if i['id'] != user_id:
            print('ID not found!')
            return updateUser()
        
    except:
        print('Incorect input')
        return updateUser()


def tryceptLoop():
    try:
        choose = int(input('Select number \n'+
                            '1-Input data \n'+
                            '2-Delete data \n' +
                            '3-Sort information \n'+
                            '4-Update information \n'+
                            '5-Show all information\n' +
                            '6-Export to PDF\n' + 
                            '7-Export to CSV\n' + 
                            '8-Input from CSV\n' +
                            '9-Quit    \n'+
                            '================================== \n'+
                            'Enter your answer : '))
        print('==================================')
        return choose
    except:
        print('==================================')
        print('Incorrect input !')
        print('==================================')
        return tryceptLoop()

def tryceptSort():
    try:
        choice_sort = int(input('Select number \n'+
                                    '1-Sort id \n'+
                                    '2-Sort name \n'+
                                    '3-Sort birth \n'+
                                    '4-Quit\n'+
                                    '==================================\n'+
                                    'Enter your answer : '))
        return choice_sort
    except:
        print('==================================')
        print('Incorrect input !')
        print('==================================')
        return tryceptSort()

def trycept_ASC_DES():
    try:
        choice_asc_des = int(input('Select number \n'+
                                    '1-Ascending \n'+
                                    '2-Descending\n'+
                                    '==================================\n'+
                                    'Enter your answer : '))
        
        return choice_asc_des
    except:
        print('==================================')
        print('Incorrect input !')
        print('==================================')
        return trycept_ASC_DES()


def toQuit():
    choice_quit = input('Are you sure? \n'+
                        'Y/n : ')

    if choice_quit == 'Y':
        print()

    elif choice_quit == 'n':
        cls()


    else:
        return toQuit()
    return choice_quit

while True:
    print('==================================')
    lua_chon = tryceptLoop()

    if lua_chon == 1:
        cls()
        user = inputUserKB()
        lst.append(user)

    elif lua_chon == 2:
        cls()
        if len(lst) == 0:
            print('==================================')
            print('No Data Found!')
            print('==================================')
        else:
            removeInfor(lst)
            print('==================================')
            print('Success')
            print('==================================')

    elif lua_chon == 3:
        cls()
        if len(lst) == 0:
            print('==================================')
            print('No Data Found!')
            print('==================================')
        else:
            while True:
                print('==================================')
                choices = tryceptSort()
                
                if choices == 1:
                    cls()
                    print('==================================')
                    asc_des = trycept_ASC_DES()

                    if asc_des == 1:
                        cls()
                        sortedUser()
                        print('==================================')
                        print('Success')
                        print('==================================')

                    elif asc_des == 2:
                        cls()
                        sortedUser()
                        lst.reverse()
                        print('==================================') 
                        print('Success')
                        print('==================================')

                elif choices == 2:
                    cls()
                    print('==================================')
                    asc_des = trycept_ASC_DES()

                    if asc_des == 1:
                        cls()
                        sortedName()
                        print('==================================')
                        print('Success')
                        print('==================================') 

                    elif asc_des == 2:
                        cls()
                        sortedName()
                        lst.reverse()
                        print('==================================')
                        print('Success')
                        print('==================================')

                elif choices == 3:
                    cls()
                    print('==================================')
                    asc_des = trycept_ASC_DES()
                    
                    if asc_des == 1:
                        cls()
                        sortedDate()
                        sortedMonth()
                        sortedYear()
                        print('==================================')
                        print('Success')
                        print('==================================')

                    elif asc_des == 2:

                        cls()
                        sortedDate()
                        sortedMonth()
                        sortedYear()                    
                        lst.reverse()
                        print('==================================')
                        print('Success')
                        print('==================================') 

                elif choices == 4:
                    cls()
                    sort_quit = toQuit()
                    if sort_quit == 'n':
                        print('==================================')
                        print('Success')
                        print('==================================')

                    elif sort_quit == 'Y':
                        print('==================================')
                        print('Success')
                        print('==================================')
                        break
            
    elif lua_chon == 4:
        cls()
        if len(lst) == 0:
            print('No Data Found')
        else:
            updateUser()

    elif lua_chon == 5: 
        cls()
        showInfor(lst)
        print('==================================')
        print('Success')
        print('==================================')
    
    elif lua_chon == 6:
        cls()
        ExportPDF(lst)
        print('==================================')
        print('Success')
        print('==================================')

    elif lua_chon == 7:
        cls()
        exportCSV(lst)
        print('==================================')
        print('Success')
        print('==================================')

    elif lua_chon == 8:
        cls()
        inputfromCSV()
        print('==================================')
        print('Success')
        print('==================================') 

    elif lua_chon == 9:

        loop_quit = toQuit()

        if loop_quit == 'n':
            print('==================================')
            print('Success')
            print('==================================')

        elif loop_quit == 'Y':
            print('==================================')
            print('Success')
            print('==================================')
            break