import time
import random
import tkinter as tk

leader_board = ['Kim' ,'Lee' ,'Park' ,'Kim' ,'Jung']
time_board = [2.0, 3.0, 4.0, 5.0, 6.0]

root = tk.Tk()
root.title('마우스 정확도 & 반응속도 테스트 v1.0')
root.geometry('1280x720+320+100')
root.resizable(False,False)


'''
frame = LabelFrame(root, padx=5, pady=5)   # 프레임이 나타나지 않는 이유는 무엇인가?
frame.pack(padx=10, pady=10)
'''



#for i in leader_board:
    #print(i,'위',leader_board[i], end_time='\n')

#print(time_board)

   
def play1():
    global start_time
    start_time = time.time()  # 시간 측정 시작
    
    btn1.destroy()  
    
    global buttonTarget1  
    buttonTarget1 = tk.Button(root, text = 'Click', width = 5, height =2, bg='green', activebackground = 'red',command=play2)
    loc1 = random.uniform(1, 1200)
    loc2 = random.uniform(20, 690)
    buttonTarget1.place(x= loc1, y= loc2)  # 난수 생성 후 좌표에 난수 입력
 
def play2():
    buttonTarget1.destroy()

    global buttonTarget2
    buttonTarget2 = tk.Button(root, text = 'Click', width = 5, height =2, bg='green', activebackground = 'red', command=play3)
    loc1 = random.uniform(1, 1200)
    loc2 = random.uniform(20, 690)
    buttonTarget2.place(x= loc1, y= loc2)  

def play3():
    buttonTarget2.destroy()
    
    global buttonTarget3
    buttonTarget3 = tk.Button(root, text = 'Click', width = 5, height =2, bg='green', activebackground = 'red',command=play4)
    loc1 = random.uniform(1, 1200)
    loc2 = random.uniform(20, 690)
    buttonTarget3.place(x= loc1, y= loc2)  

def play4():
    buttonTarget3.destroy()
    
    global buttonTarget4
    buttonTarget4 = tk.Button(root, text = 'Click', width = 5, height =2, bg='green', activebackground = 'red', command=play5)
    loc1 = random.uniform(1, 1200)
    loc2 = random.uniform(20, 690)
    buttonTarget4.place(x= loc1, y= loc2)  

def play5():
    buttonTarget4.destroy()
    
    global buttonTarget5
    buttonTarget5 = tk.Button(root, text = 'Click', width = 5, height =2, bg='green', activebackground = 'red', command= result)
    loc1 = random.uniform(1, 1200)
    loc2 = random.uniform(20, 690)
    buttonTarget5.place(x= loc1, y= loc2)  

def continuePlay():
    
    global window1
    window1.destroy()
    global btn1
    btn1 = tk.Button(root, text='시작', width=10, height=2, command = play1)  
    btn1.pack()
   
def continuePlay1():
    
    global window2
    window2.destroy()
    global btn1
    btn1 = tk.Button(root, text='시작', width=10, height=2, command = play1)  
    btn1.pack()

def result():
    buttonTarget5.destroy()
    global time_board
    global end_time
    end_time = time.time() - start_time
    

    for i in range(5):  # 순위 결정 loop  
        
        if end_time <= time_board[i]: # 순위권에 들었을 때만 수행하고 그렇지 않으면 elif 로 넘어간다

            def entry_leader_board(event):
                
                #window1.destroy()
             
                
                leader_board.insert(i, entry.get())  # 이름을 입력받은 것을 이름순위표에 넣음  
                leader_board.pop(-1)
              
                result_label1 = tk.Label(window1, anchor='w', text= '1위 %s, %f 초' %(str(leader_board[0]),time_board[0]))
                result_label1.pack()
                result_label2 = tk.Label(window1, anchor='w', text= '2위 %s, %f 초' %(str(leader_board[1]),time_board[1]))
                result_label2.pack()
                result_label3 = tk.Label(window1, anchor='w', text= '3위 %s, %f 초' %(str(leader_board[2]),time_board[2]))
                result_label3.pack()
                result_label4 = tk.Label(window1, anchor='w', text= '4위 %s, %f 초' %(str(leader_board[3]),time_board[3]))
                result_label4.pack()                                         
                result_label5 = tk.Label(window1, anchor='w', text= '5위 %s, %f 초' %(str(leader_board[4]),time_board[4]))
                result_label5.pack()

                btn_child = tk.Button(window1, text='계속 하려면 누르세요', command= continuePlay)
                btn_child.pack()
                btn_child1 = tk.Button(window1, text='프로그램 종료', command= lambda:root.destroy())
                btn_child1.pack()

                                         
            time_board.insert(i,end_time) # 기록된 시간을 시간 순위표에 기입하고 밀려난 순위를 삭제
            time_board.pop(-1)
            print(time_board)   # 잘 들어갔나 확인
            

            global window1  
            window1 = tk.Toplevel(root)
            window1.geometry("400x300+820+100")
            window1.title('순위')

            name_label1 = tk.Label(window1, text='%s 초로 %s 위 입니다'%(str(end_time),str(i+1)))
            name_label1.pack()
            name_label2 = tk.Label(window1, text='축하합니다. 이름을 입력하세요')
            name_label2.pack()
                                         
            global entry            
            entry = tk.Entry(window1)
            entry.bind("<Return>", entry_leader_board)
            entry.pack()
            
            break  #실질적으로는 이름 입력하고 return 누르기 전에 이미 break 가 실행된다
  

        elif end_time > time_board[4]:
            
            global window2
            window2 = tk.Toplevel(root)
            window2.geometry("320x200+820+100")
    
            lbl_result = tk.Label(window2, text='걸린시간은 %f 초, (개당 %f 초)'%(end_time, end_time/5))
            lbl_result.pack()

            global btn_child
            btn_child = tk.Button(window2, text='계속 하려면 누르세요', command= continuePlay1)
            btn_child.pack()

            btn_child1 = tk.Button(window2, text='프로그램 종료', command= lambda:root.destroy())
            btn_child1.pack()
                                           
            break
      

   
instruction1 = tk.Label(root, text='마우스 클릭의 정확도와 속도를 측정합니다')
instruction1.pack()

btn1 = tk.Button(root, text='시작', width=10, height=2, command = play1)
btn1.pack()


root.mainloop()





        

