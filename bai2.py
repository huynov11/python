from reportlab.pdfgen import canvas
c = canvas.Canvas("infor.pdf", pagesize=(595.27, 841.89))
c.setFont('Times-Roman',10)
ToaDoY = 0
lst = []
while True:
    print('==================================')
    lua_chon = int(input('Xin mời chọn \n'+
                            '1-Nhập dữ liệu \n'+
                            '2-Hiện toàn thông tin vừa nhập \n'+
                            '3-Quit    \n'
                            '================================== \n'+
                            'Mời nhập : '))
    print('==================================')
    if lua_chon == 1:
        #input
        name = str(input("Nhập tên : "))
        ngay = int(input("Nhập ngày sinh : "))
        thang = int(input("Nhập tháng sinh : "))
        nam = int(input("Nhập năm sinh : "))
        birthday= (f"{ngay}-{thang}-{nam} ")
        phone_value = input("Nhập số điện thoại : ")
        email_value = input('Nhập email \n'+
                            'ex: abcdef@gmail.com : '  )

        print('==================================')
        #print ques
        c.drawString(50,780-ToaDoY,'Birthday : ')
        c.drawString(50,760-ToaDoY,'Phone : ')
        c.drawString(50,740-ToaDoY,'Email : ')
        c.drawString(50,720-ToaDoY,'------------------------------------------------------------------------------------------------------------------------------------------------')
        #print answer
        c.drawString(50, 800-ToaDoY, name,c.setFont('Times-Roman',30))
        c.drawString(120, 780-ToaDoY, birthday,c.setFont('Times-Roman',10))
        c.drawString(120, 760-ToaDoY, phone_value,c.setFont('Times-Roman',10))
        c.drawString(120, 740-ToaDoY, email_value,c.setFont('Times-Roman',10))
        lst.append(name)
        lst.append(email_value)
        lst.append(phone_value)
        lst.append(birthday)
        ToaDoY += 120

    elif lua_chon == 2:
        print(lst)
        print('==================================')
    elif lua_chon == 3: 
        break
c.showPage()
c.save()