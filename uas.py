# untuk melihat list yang belum terurut
my_list = [18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5]
print("list yang belum terurut :",list)
banyak_list = len (my_list)

# Mengurutkan dengan Bubble Sort
# Bubble Sort
data = [18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5,18,7,6,19,4,24,12,11,10,5]
print("data sebelum diurutkan :", data)
banyak_data = len (data)

for i in range (banyak_data-1):
    for j in range (banyak_data-1) :
        if data [j]>data[j+1] :
            temp = data [j]
            data [j] = data [j+1]
            data [j+1] = temp
print ("data setelah diurutkan:", data)
