import pandas as pd


df = pd.read_csv('abc.csv')

new = []

lst = []

lst_user = []

success = []

with open('abc.csv','r') as f:
    my_data = f.readlines()


for data in my_data:

    split_tring =data.split('\n')
    new_srting = ''.join(split_tring)
    lst.append(new_srting)

for data_user in range(1,len(lst)):

    orginal = ''.join(lst[data_user])
    k_string = orginal.split(',')
    lst_user.append(k_string)

    print(success)


# user = {}


# for i in range(len(lst_user)):
#     for j in df:
#         new_keys = {j:''}
#         user.update(new_keys)
#     new.append(user)




# for i in new:
#     success.append([i])


for i in range(len(lst_user)):  
    for j in success[i]:
        # print(j)
        for k in lst_user[i]:   
            # print(k)
            if j['ID'] == '':
                j['ID'] = k

            elif j['Name'] == '':
                j['Name'] = k

            elif j['Phone'] == '':
                j['Phone'] = k
            # print(success)
print(success)