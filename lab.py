from reportlab.pdfgen import canvas

c = canvas.Canvas("infor.pdf", pagesize=(595.27, 841.89))

c.setFont('Times-Roman',10)

lst = []

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


def showInfor(user_lst): #Xuất tất cả các dữ liệu 
    for user in user_lst:
        outInfor(user)


def exportPDF(user_lst): # Xuất tất cả dữ liệu ra pdf
    for user in user_lst:
        drawInfoUserInPdf(user)    
    print('Success')


def drawInfoUserInPdf(user): #Xuất ra pdf
    global ToaDoY
    c.drawString(50,780-ToaDoY,'Birthday : ')
    c.drawString(50,760-ToaDoY,'Phone : ')
    c.drawString(50,740-ToaDoY,'Email : ')
    c.drawString(50,720-ToaDoY, '-'*30)


    c.drawString(50, 800-ToaDoY, user['name'],c.setFont('Times-Roman',30))
    c.drawString(120, 780-ToaDoY, user['phone_value'],c.setFont('Times-Roman',10))
    c.drawString(120, 760-ToaDoY, user['email_value'],c.setFont('Times-Roman',10))
    c.drawString(120, 740-ToaDoY, user['birthday'],c.setFont('Times-Roman',10))

    ToaDoY += 120

ToaDoY = 0

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


def reInfor(user_lst): # Xóa dữ liệu
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
        reInfor(lst)

    elif lua_chon == 3:
        while True:
            choices = int(input('Xin mời chọn \n'+
                                '1-Sort id \n'+
                                '2-Sort name \n'+
                                '3-Sort birth \n'+
                                '4-Quit'
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
        exportPDF(lst)

    elif lua_chon == 6:
        print('Done')
        break

c.showPage()
c.save()