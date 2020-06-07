import pandas as pd
import csv
from itertools import zip_longest
import fileinput
import time
def index1():
    fi=open(r"C:\Users\vinod naidu\Desktop\hots.csv","r",errors="ignore")
    pos=fi.tell()
    line=fi.readline()
    a=line.split(",")
    l=[]
    l1=[]
    while line:
        pos=fi.tell()
        line=fi.readline()
        a=line.split(",")
        l.append(pos)
        l1.append(a[0])
           
    #print(l1)
        

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\vinod naidu\Desktop\index3.csv','w', newline='',errors="ignore") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("PrimaryKey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("index3.csv",index_col=0)
    b=a.sort_values(["PrimaryKey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("index3.csv")

    myfile.close()
    fi.close()
index1()    
def add1():
    start=time.time()
    id1=input("enter id: \n")
    with open(r"C:\Users\vinod naidu\Desktop\hots.csv", 'r',errors="ignore") as myfile:
        if id1 in myfile.read():
            print("primary key present")
        else:
            d1=input("enter hotel name: \n")
            d2=input("enter hotel address: \n")
            d3=input("enter review date: \n")
            d4=input("enter negative review: \n")
            d5=input("enter positive review: \n")
            d6=input("enter rating: \n")
            with open(r"C:\Users\vinod naidu\Desktop\hots.csv", 'a',errors="ignore") as file:
                str=id1+","+d1+","+d2+","+d3+","+d4+","+d5+","+d6
                file.write(str)
                file.write("\n")
                end=time.time()
                print('The time taken to add a new record in seconds ')
                print(int(end - start))
def delete1():
    start=time.time()
    data =pd.read_csv(r"C:\Users\vinod naidu\Desktop\hots.csv",index_col="id",engine='python')
    del_id = int(input('Enter the id to delete: \n'))
    data.drop([del_id],inplace=True) 
    a=pd.DataFrame(data)
    print("DELETED SUCCESSFULLY")
    b=a.to_csv(r"C:\Users\vinod naidu\Desktop\hots.csv") 
    end=time.time()
    print('The time taken to delete a record in seconds ')
    print(int(end - start))
def search1():
    start=time.time()
    fi=open(r"C:\Users\vinod naidu\Desktop\index3.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
      
    l1= l[: len(l) -3]
    #print(l1)
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = int(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
        
    else:
        print("found")
        fi=open(r"C:\Users\vinod naidu\Desktop\index3.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index,value in enumerate(l2): 
                if(result==index):
                    a=value
                    
                    
        
        print(a)
        fi=open(r"C:\Users\vinod naidu\Desktop\hots.csv","r",errors="ignore")
        fi.seek(a)
        b=fi.readline()
        c=b.split(",")
        
        d1=c[0]
        a1=c[1]
        b1=c[2]
        c1=c[3]
        e1=c[4]
        f1=c[5]
        g1=c[6]
        print("Review id: " +c[0])
        print("\n")
        print("Hotel Name: "+c[1])
        print("\n")
        print("Hotel Address: " +c[2])
        print("\n")
        print("Review Date: "+c[3])
        print("\n")
        print("Negative review: " +c[4])
        print("\n")
        print("Positive Review: "+c[5])
        print("\n")
        print("Rating: "+c[6])
        print("\n")
        end=time.time()
        print('The time taken to search a record in seconds  ')
        print(int(end - start))
        fi.close()
        
def modify():
    start=time.time()
    fi=open(r"C:\Users\vinod naidu\Desktop\index3.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 2]
    #print(l1)
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = int(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
    else:
        print("found")
        fi=open(r"C:\Users\vinod naidu\Desktop\index3.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index, value in enumerate(l2): 
                if(result==index):
                    a=value
        #fi.close()

        f1=open(r"C:\Users\vinod naidu\Desktop\hots.csv","a+",errors="ignore")
        f1.seek(a)
        b=f1.readline()
        c=b.split(",")
        d1=c[0]
        a1=c[1]
        b1=c[2]
        c1=c[3]
        e1=c[4]
        f1=c[5]
        g1=c[6]
        print("Review id: " +c[0])
        print("\n")
        print("Hotel Name: "+c[1])
        print("\n")
        print("Hotel Address: " +c[2])
        print("\n")
        print("Review Date: "+c[3])
        print("\n")
        print("Negative review: " +c[4])
        print("\n")
        print("Positive Review: "+c[5])
        print("\n")
        print("Rating: "+c[6])
        print("\n")
        ch=0
        while (ch!=4):
            print("Enter 1 to modify Hotel Name")
            print("Enter 2 to modify Hotel Address")
            print("Enter 3 to modify Review Date")
            print("Enter 4 to go back to main menu")
            ch=int(input("PLEASE ENTER YOUR OPTION: "))
            if(ch==1):
                name1=input("Enter the new Hotel Name")
                a1=name1
                str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1
                f1=open(r"C:\Users\vinod naidu\Desktop\hots.csv","a+",errors="ignore")
                f1.seek(a)
                f1.write(str)
                data =pd.read_csv(r"C:\Users\vinod naidu\Desktop\hots.csv",index_col="id")
                data.drop([int(d1)],inplace=True) 
                data1=pd.DataFrame(data)
                data2=data1.to_csv(r"C:\Users\vinod naidu\Desktop\hots.csv")            
                end=time.time()
                print('The time taken to modify the record in seconds ')
                print(int(end - start))
                f1.close()
            elif(ch==2):
                name1=input("Enter the Hotel Address")
                b1=name1
                str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1
                f1=open(r"C:\Users\vinod naidu\Desktop\hots.csv","a+",errors="ignore")
                f1.seek(a)
                f1.write(str)
                data =pd.read_csv(r"C:\Users\vinod naidu\Desktop\hots.csv",index_col="id")
                data.drop([int(d1)],inplace=True) 
                data1=pd.DataFrame(data)
                data2=data1.to_csv(r"C:\Users\vinod naidu\Desktop\hots.csv")
                f1.close()
                end=time.time()
                print('The time taken to modify the record in seconds')
                print(int(end - start))
            elif(ch==3):
                name1=input("Enter the new Review Date")
                c1=name1
                str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1
                f1=open(r"C:\Users\vinod naidu\Desktop\hots.csv","a+",errors="ignore")
                f1.seek(a)
                f1.write(str)
                data =pd.read_csv(r"C:\Users\vinod naidu\Desktop\hots.csv",index_col="id")
                data.drop([int(d1)],inplace=True) 
                data1=pd.DataFrame(data)
                data2=data1.to_csv(r"C:\Users\vinod naidu\Desktop\hots.csv")
                f1.close()
                end=time.time()
                print('The time taken to modify the record in seconds ')
                print(int(end - start))
            else:
                main1()
        
    
    fi.close()
#modify()  
def index2():
    fi=open(r"C:\Users\vinod naidu\Desktop\hots.csv","r",errors="ignore")
    pos=fi.tell()
    line=fi.readline()
    a=line.split(",")
    l=[]
    l1=[]
    while line:
        pos=fi.tell()
        line=fi.readline()
        a=line.split(",")
        l.append(pos)
        l1.append(a[-1])
        
        

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\vinod naidu\Desktop\index4.csv','w', newline='',errors="ignore") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("secondarykey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("index4.csv",index_col=0)
    b=a.sort_values(["secondarykey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("index4.csv")

    myfile.close()
    fi.close()
index2()    
def search2():
    start=time.time()
    fi=open(r"C:\Users\vinod naidu\Desktop\index4.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 3]
    l2= list(map(float, l1))
    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = float(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
    else:
        print("found")
        fi=open(r"C:\Users\vinod naidu\Desktop\index4.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index, value in enumerate(l2): 
                if(result==index):
                    a=value
        

        fi=open(r"C:\Users\vinod naidu\Desktop\hots.csv","r",errors="ignore")
        fi.seek(a)
        b=fi.readline()
        c=b.split(",")
        d1=c[0]
        a1=c[1]
        b1=c[2]
        c1=c[3]
        e1=c[4]
        f1=c[5]
        g1=c[6]
        print("Review id: " +c[0])
        print("\n")
        print("Hotel Name: "+c[1])
        print("\n")
        print("Hotel Address: " +c[2])
        print("\n")
        print("Review Date: "+c[3])
        print("\n")
        print("Negative review: " +c[4])
        print("\n")
        print("Positive Review: "+c[5])
        print("\n")
        print("Rating: "+c[6])
        print("\n")
        end=time.time()
        print('The time taken to search the record in seconds ')
        print(int(end - start))
        fi.close()
def delete2():
    start=time.time()
    data =pd.read_csv(r"C:\Users\vinod naidu\Desktop\hots.csv",index_col="rating",engine='python')
    del_id = float(input('Enter the Rating to delete: \n'))
    data.drop([del_id],inplace=True) 
    a=pd.DataFrame(data)
    print("DELETED SUCCESSFULLY")
    b=a.to_csv(r"C:\Users\vinod naidu\Desktop\hots.csv")
    end=time.time()
    print('time taken to delete the file in ms ')
    print(int(end - start))    
def main1(): 
    print("------WELCOME TO HOTEL REVIEW DATASET------")
    ch=0
    while(ch!=7):
        print("PRESS 1 TO ADD A NEW HOTEL REVIEW RECORD")
        print("PRESS 2 TO DELETE A HOTEL REVIEW RECORD BASED ON PRIMARY KEY ")
        print("PRESS 3 TO DELETE A HOTEL REVIEW RECORD BASED ON SECONDARY KEY ")
        print("PRESS 4 TO SEARCH FOR A HOTEL REVIEW BASED ON PRIMARY KEY")
        print("PRESS 5 TO SEARCH FOR A HOTEL REVIEW BASED ON SECONDARY KEY")
        print("PRESS 6 TO MODIFY A HOTEL REVIEW")
        print("PRESS 7 TO EXIT")
        ch=int(input("PLEASE ENTER YOUR OPTION: "))
        if(ch==1):
            index1()
            index2()
            add1()
            index2()
            index1()
        elif (ch==2):
            index1()
            index2()
            delete1()
            index2()
            index1()
        elif (ch==3):
            index2()
            index1()
            delete2()
            index1()
            index2()
        elif (ch==4):
            index1()
            search1()
            index1()
        elif (ch==5):
            index2()
            search2()
            index2()     
        elif (ch==6):
            index1()
            index2()
            modify()
            index2()
            index1()
        else:
           print("invalid choice") 
           
main1()