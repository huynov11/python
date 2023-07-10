from xhtml2pdf import pisa

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


def inputUser(): #Nhập thông tin

    user = {}
    user['id'] = trEx_int('id')
    user['name'] = input('Enter your name : ')
    user['date'] = trEx_int('date')
    user['month'] = trEx_int('month')
    user['year'] = trEx_int('year')
    user['birthday']= (f"{user['date']}-{user['month']}-{user['year']} ")
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
            user1 = lst[j]
            user2 = lst[j+1]
            if user1['date'] > user2['date']:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
                return  
        


def sortedMonth():
    global lst
    swapped = False
    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user1 = lst[j]
            user2 = lst[j+1]
            if user1['month'] > user2['month']:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
                return 



def sortedYear():

    global lst
    swapped = False
    for i in range(len(lst)-1): 
        for j in range(0,len(lst)-1-i): 
            user1 = lst[j]
            user2 = lst[j+1]
            if user1['year'] > user2['year']:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
                return  
    sortedDate()
    sortedMonth()
    print(lst)


def removeInfor(user_lst): # Xóa dữ liệu
    del_user = int(input('Enter id : '))
    for i in range(len(user_lst)):
        if user_lst[i]['id'] == del_user:
            del user_lst[i]
            break

            

while True:
    print('==================================')
    lua_chon = int(input('Xin mời chọn \n'+
                            '1-Input data \n'+
                            '2-Delete data \n' +
                            '3-Sort information \n'+
                            '4-Show all information\n' +
                            '5-Export to pdf\n' + 
                            '6-Quit    \n'
                            '================================== \n'+
                            'Enter your answer : '))
    print('==================================')

    if lua_chon == 1:
        #input
        user = inputUser()
        lst.append(user)

    elif lua_chon == 2:
        removeInfor(lst)

    elif lua_chon == 3:
        while True:
            choices = int(input('Xin mời chọn \n'+
                                '1-Sort id \n'+
                                '2-Sort name \n'+
                                '3-Sort birth \n'+
                                '4-Quit\n'+
                                'Enter your answer : '))
            
            if choices == 1:
                sortedUser()

            elif choices == 2:
                sortedName()

            elif choices == 3:
                sortedDate()
                sortedMonth()
                sortedYear()

            elif choices == 4:
                break
            
    elif lua_chon == 4:
        showInfor(lst)

    elif lua_chon == 5: 
        for i in lst:
            user_html = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>TEST</title>

    </head>
    <body>
        <div><img src="https://scontent-hkg4-1.xx.fbcdn.net/v/t1.30497-1/143086968_2856368904622192_1959732218791162458_n.png?_nc_cat=1&cb=99be929b-59f725be&ccb=1-7&_nc_sid=7206a8&_nc_ohc=DH2e7R2-NdgAX8QfZX-&_nc_ht=scontent-hkg4-1.xx&oh=00_AfC15rMxMACqzfDATkLyr4TN-IugZ-q5srOeXqV547CMfw&oe=64D1E6F8" ></div>
        <div>
            <h1>ID  : {i['id']}  </h1>
        </div>
        <div>
            <h1>Name : {i['name']}   </h1>
        </div>
        <div>
            <h1>Birthday : {i['birthday']}   </h1>
        </div> 
        <div>
            <h1>Phone : {i['phone_value']}  </h1>
        </div>
        <div>
            <h1>Email : {i['email_value']}  </h1>
        </div>
        <hr>
    </body>
</html>
"""
        
            source_html.append(user_html)


        output_filename = "infor.pdf"
        source = ''.join(source_html)
        print(source)
        def convert_to_pdf(sourcePDF,outputPDF):


            result_file = open(outputPDF,'w+b')
            pisa_status = pisa.CreatePDF(sourcePDF,dest=result_file)

            result_file.close()
            return pisa_status.error

        if __name__ == '__main__':
            pisa.showLogging()
            convert_to_pdf(source,output_filename)
        print('Success')
    
    elif lua_chon == 6:
        print('Done')
        break