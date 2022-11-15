import tkinter as tk
import time
from tkinter import messagebox


current_balance = 5000
pin = '1234'
my_pin = '1234'
global old_pin
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage, PinChangePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller

        self.controller.title('VSG Systems')
        self.controller.state('zoomed')
        #self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/urban boutique/Documents/atm tutorial/atm.png'))

        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#999999')
        space_label.pack()

        pin_label = tk.Label(self,
                                                      text='Enter 4 Digit PIN',
                                                      font=('Times New Roman',16),
                                                      bg='#999999',
                                                      fg='#000000')
        pin_label.pack(pady=10)

        my_pin = tk.StringVar()
        pin_entry_box = tk.Entry(self,
                                                              textvariable=my_pin,
                                                              font=('orbitron',12),
                                                              width=32)
        pin_entry_box.focus_set()
        pin_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            pin_entry_box.configure(fg='black',show='*')
            
        pin_entry_box.bind('<FocusIn>',handle_focus_in)

        def check_pin():
           if my_pin.get() == pin:
               my_pin.set('')
               incorrect_pin_label['text']=''
               controller.show_frame('MenuPage')
           else:
               incorrect_pin_label['text']='Incorrect PIN'
                
        submit_button = tk.Button(self,
                                                     text='Submit',
                                                     command=check_pin,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=40,
                                                     height=3)
        submit_button.pack(pady=10)

        incorrect_pin_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        fg='#000000',
                                                                        bg='#888888',
                                                                        anchor='n')
        incorrect_pin_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
        


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('Times New Roman',20),
                                                           fg='#000000',
                                                           bg='#999999')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                                           text='Please Make a Selection',
                                                           font=('Arial',13),
                                                           fg='#000000',
                                                           bg='#999999',
                                                           anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#888888')
        button_frame.pack(fill='both',expand=True)

        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = tk.Button(button_frame,
                                                            text='Balance',
                                                            command=balance,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=2)
        balance_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = tk.Button(button_frame,
                                                            text='Deposit',
                                                            command=deposit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=2)
        deposit_button.grid(row=0,column=1,pady=5)

        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = tk.Button(button_frame,
                                                            text='Withdraw',
                                                            command=withdraw,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=2)
        withdraw_button.grid(row=1,column=0,pady=5)

        def pinchange():
            controller.show_frame('PinChangePage')
            
        pinchange_button = tk.Button(button_frame,
                                                            text='Pin Change',
                                                            command=pinchange,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=2)
        pinchange_button.grid(row=1,column=1,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=2)
        exit_button.grid(row=2,column=0,columnspan=2,sticky="we",pady=5)


        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class WithdrawPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller


        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                                           text='Choose the amount you want to withdraw',
                                                           font=('orbitron',13),
                                                           fg='#000000',
                                                           bg='#999999')
        choose_amount_label.pack()

        button_frame = tk.Frame(self,bg='#888888')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance 
            if current_balance-amount<0:
                messagebox.showerror("Error","Not Enough Balance")
            else:                
                current_balance -= amount
                controller.shared_data['Balance'].set(current_balance)
                controller.show_frame('MenuPage')
            
        fifty_button = tk.Button(button_frame,
                                                       text='50',
                                                       command=lambda:withdraw(50),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        fifty_button.grid(row=0,column=0,pady=5)

        hundred_button = tk.Button(button_frame,
                                                       text='100',
                                                       command=lambda:withdraw(100),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        hundred_button.grid(row=1,column=0,pady=5)

        two_hundred_button = tk.Button(button_frame,
                                                       text='200',
                                                       command=lambda:withdraw(200),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        two_hundred_button.grid(row=2,column=0,pady=5)

        five_hundred_button = tk.Button(button_frame,
                                                       text='500',
                                                       command=lambda:withdraw(500),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        five_hundred_button.grid(row=3,column=0,pady=5)

        one_thousand_button = tk.Button(button_frame,
                                                       text='1000',
                                                       command=lambda:withdraw(1000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        one_thousand_button.grid(row=0,column=1,pady=5)

        two_thousand_button = tk.Button(button_frame,
                                                       text='2000',
                                                       command=lambda:withdraw(2000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        two_thousand_button.grid(row=1,column=1,pady=5)

        five_thousand_button = tk.Button(button_frame,
                                                       text='5000',
                                                       command=lambda:withdraw(5000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=30,
                                                       height=2)
        five_thousand_button.grid(row=2,column=1,pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                                              textvariable=cash,
                                                              width=36,
                                                              justify='right')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=7)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=30,
                                                    height=2)
        menu_button.grid(row=5,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=30,
                                                 height=2)
        exit_button.grid(row=5,column=1,pady=5)

        def other_amount(_):
            global current_balance
            if current_balance-int(cash.get())<0:
                # select_label=tk.Label(self,
                #                             text="You do not have enough balance. You will be redirected in 3 seconds.",
                #                             font=('orbitron',13),
                #                             fg='#000000',
                #                             bg='#999999',
                #                             anchor='w')
                # select_label.pack(pady=20)
                # time.sleep(3)
                # controller.show_frame('MenuPage')
                messagebox.showerror("Error","Not Enough Balance")
            else:
                current_balance -= int(cash.get())
                controller.shared_data['Balance'].set(current_balance)
                cash.set('')
                controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
   

class DepositPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller

        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#999999')
        space_label.pack()

        enter_amount_label = tk.Label(self,
                                                      text='Enter amount',
                                                      font=('orbitron',13),
                                                      bg='#999999',
                                                      fg='#000000')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
            
        deposit_button = tk.Button(self,
                                                     text='Deposit',
                                                     command=deposit_cash,
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=30,
                                                     height=2)
        deposit_button.pack(pady=5)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(self,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=30,
                                                    height=2)
        menu_button.pack(pady=5)        
        
        two_tone_label = tk.Label(self,bg='#888888')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class BalancePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller

        
        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('orbitron',13),
                                                  fg='#000000',
                                                  bg='#999999',
                                                  anchor='w')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#888888')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=30,
                                                    height=2)
        menu_button.grid(row=0,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=30,
                                                 height=2)
        exit_button.grid(row=1,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()

class PinChangePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#999999')
        self.controller = controller

        heading_label = tk.Label(self,
                                                     text='VSG ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#000000',
                                                     background='#999999')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#999999')
        space_label.pack()

        enter_old_pin_label = tk.Label(self,
                                                      text='Enter Old Pin',
                                                      font=('orbitron',13),
                                                      bg='#999999',
                                                      fg='#000000')
        enter_old_pin_label.pack(pady=10)

        oldpin=tk.StringVar()

        old_pin_entry = tk.Entry(self,
                                                  textvariable=oldpin,
                                                  show = '*',
                                                  font=('orbitron',12),
                                                  width=22)
        old_pin_entry.pack(ipady=7)

        new_old_pin_label = tk.Label(self,
                                                      text='Enter New Pin',
                                                      font=('orbitron',13),
                                                      bg='#999999',
                                                      fg='#000000')
        new_old_pin_label.pack(pady=10)

        newpin=tk.StringVar()

        new_pin_entry = tk.Entry(self,
                                                  textvariable=newpin,
                                                  show = '*',
                                                  font=('orbitron',12),
                                                  width=22)
        new_pin_entry.pack(ipady=7)

        again_new_old_pin_label = tk.Label(self,
                                                      text='Enter New Pin Again',
                                                      font=('orbitron',13),
                                                      bg='#999999',
                                                      fg='#000000')
        again_new_old_pin_label.pack(pady=10)

        againnewpin=tk.StringVar()

        again_new_pin_entry = tk.Entry(self,
                                                  textvariable=againnewpin,
                                                  show = '*',
                                                  font=('orbitron',12),
                                                  width=22)
        again_new_pin_entry.pack(ipady=7)    



        def pin_change():
            global my_pin

            if my_pin == oldpin.get():
                if newpin.get() == againnewpin.get():
                    my_pin = newpin.get()
                    # print('Pin Changed Successfully')
                    controller.show_frame('MenuPage')
                else:
                    # print('Pin Not Matched')
                    messagebox.showerror('Error','New Pin Not Matched')
            else:
                messagebox.showerror('Error', 'Old Pin Not Matched')
                # print('Old Pin Not Matched')
            

        submit_button = tk.Button(self,
                                                     text='Submit',
                                                     command=pin_change,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=30,
                                                     height=2)
        submit_button.pack(pady=10)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(self,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=30,
                                                    height=2)
        menu_button.pack(pady=5)        


        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1000x1000")
    app.minsize(445,600)
    app.maxsize(445,600)
    app.mainloop()
