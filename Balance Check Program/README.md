# Mobile shop and Electronic wallets balance check program
#### Video Demo:  <https://youtu.be/M4dsidKhWXw>
#### Description:

In the name of Allah, the most merciful and all thanks to him and peace be upon his messenger Mohammad PBUH, Alsalamualaykum (peace be upon you)

###### Introduction
Explaining my project will be huge for it is a 1800 code line program and about 45 different functions and uses 16 different tables in a database, and it also holds Arabic names for the interface and function names so it will take more effort to explain it. It is a Python program that I used the library "tkinter" to implement it.

My friend has got a mobile shop, and he works for an employer in it, this employer makes lots of mistakes concerning the
calculations of transactions and who sent what to whom, so I thought of this program to be able to help him.

PS My friend is not that rich to buy his program for his shop.

###### This program does mainly three things:
1. Keep track of electronic wallet (EW) transactions
2. Make sure the final financial balance throughout the day is correct
3. Keep track of installments whether the store is the debtor or the debted

I made a "notebook" command in the Tkinter to be able to make "three tabs", each tab for a purpose.
some tabs make multiple demands concerning these three points but the first tab only does that first point, which is to keep track of electronic wallet transactions.

##### 1. Electronic wallets (EWs) transactions tab "فودافون كاش":
Here in Egypt, we have electronic wallets (EWs) which are related to mobile numbers, every network company makes a service that allows people to transfer money through these wallets. Egyptian mobile shops make use of this service to be able to transfer money to other wallets for the people who don't own those wallets (even though they own a mobile number), and this is of great use because some traders need money in a certain time of the day to pay for something instantly through these electronic wallets (EWs) and then returns this 
money later at night as cash.

For each of these transactions the mobile shop gets a profit out of it, like 1% profit each transaction, but when lots of transactions happen to/from lots of people and several times in the day (and maybe for the same person to and from him several times) it may cause confusion and make lots of mistakes during the calculations. so, I made this program to keep track of every transaction of those, so that the employer will not need to do anything except just insert the client name (which is saved in the database and he can insert a new one too), and the amount he sent to him or received from him and to/from which number (which is also saved in the database and he can also insert a new one).

The first tab (the most right) is called "فودافون كاش" which is "Vodafone cash" which is the name of the electronic wallet used in that mobile shop.

###### At the top right corner
There are two buttons "إضافة عميل" and "إضافة رقم" which are to add a client to the database or a new EW number. 
Know that, to insert a new EW number it must be all integers, no special characters, and no letters or it will raise an error.

###### At the top left side
There are two rows, the first one lets the user choose one of the (already saved clients and shown by a drop-down menu) in the database to send EW balance to him (that the user decides by entering numbers to the Entry widget) through an EW number that is already saved in the database as well (and revealed using a drop-down menu as well, but it only shows the last 4 digits of the whole number for simplicity when inserting a transaction). and for the second row it uses the same method but to receive balance on one of the EW wallets from a client.
The first row translates to "the client (drop-down menu) received amount (Entry widget) from the (EW) number (drop-down menu) (Complete sending transaction button)" and the second row says the same but instead of "client received" it says "client sent".

Know that, the program handles false entries, the amount sent/received must be in integers, and the EW number and the amount sent/received (at least) must be chosen to be able to press the send/receive buttons or else it will raise an error.
Know that, you can transact amounts even though you didn't choose a client and it will show in the table as "إضافة خارجية" which translates to "foreign entry", and I made this option to compensate any errors that may arise in the actual EW number balances so that the employer won't be "strictly" controlled by the program.

###### At the bottom right side
There is a table that shows the numbers currently present in the database "الرقم" column, and the available balance in it "المتوفر".

Know that, when you insert a new EW number in the database it automatically updates the table to contain this new EW number.
Know that, whenever the available balance in any number gets to zero it goes down to the bottom of the table and gets highlighted in grey.
know that, the table is descendingly ordered according to the available balance.

###### At the left side
There are two tables at the top of each other, the table at the bottom shows a list of clients that are in the database in the column "الاسم", and it shows the amount of balance that this client is debited to the store with the "عليه" column, and the amount of money that he is debiting the store with (just in case) in the "له" column.

Know that, whenever the employer inserts a new client into the database, the table automatically updates to include the new client in that table.
Know that, whenever a client has got no debts (which means column "عليه" has 0 value) it will go to the bottom of the list and gets highlighted in grey, for the table in descendingly ordered according to the value the store is debiting the client with.

###### The table at the top
Shows the daily logs (transactions) that are done during the day, the "الرقم" column shows the global number of transactions that are done since the start of the use of the program in the store, the "اسم العميل" column shows the name of the client, the "دفع" column shows the amount the client paid (if he paid) (that column become 0 if he received), and "استقبل" column shows the amount the client received (if he received) (that column become 0 if he paid), the "من/على الرقم" column shows the number that the client sent to or received from, and "الساعة" column shows the time (hh:mm:ss) in which this transaction happened.

Know that, whenever a transaction is successful, all three tables update to increase/decrease the value of the EW number in the EW numbers table, and to increase/decrease the depted amount or increase/decrease the depting amount of the client in the client table, and to add the new transaction log to the logs table.
Know that 4 checking message boxes will be raised after the transaction to make sure that all of the 3 tables were updated and the transaction was successfully done.

That's for the first tab.

##### 2. Daily logs tab "معاملات"
This tab shows 4 tables each one for a different function:

###### For the table at the top right corner
It is the products selling table "المبيعات", shows a log of products that were sold during the day and their amount, where the "الرقم" column shows the number of the log ever since the program was used, and the "الاسم" column indicates the name or the type of the product (whichever clarifies) and "القيمة" indicates the value it was sold with, and the "الساعة" column shows the time at which the product was inserted (hh:mm:ss)

###### For the table at the top left corner "رصيد داخل"
It is the table that keeps track of any cash that went inside the store for any reason, where all of the columns have the same indications as the first table.

###### For the table at the bottom left corner "رصيد خارج"
It is the table that keeps track of any cash that went outside of the store for any reason, where all of the columns have the same indications as the first table.

###### For the table at the bottom right corner "ديون يومية"
It is the table that keeps track of any debts that are on the store for other parties, where all of the columns have the same indications as the first table. But, this is the only table that you can right-click on any of its records to delete it, and it can't be removed in any other ways throughout the interface, it will stay in this table every day until the employer removes it himself after he has paid the debt.
 
Know that, all of these tables are not sorted except on the timing of inserting the log where the last log is at the top.
Know that, for all these tables, you can't leave any field blank, or else an error will arise. 
Know that, for all these tables, you can't insert any non-numeric characters into the "القيمة" Entry or else an error will arise.

That's for the second tab.

##### 3. Balance Check and installments tab "تصفية"
I will explain the two tables on the right side at first, then explain how the financial balance is done because the rest of the widgets are related to it, and then explain every widget.

###### At the right side
There are two tables, the table at the bottom "الأقساط" shows the clients that bought products from the shop but paid it in installments, at the top of the table there are two buttons, the one called "إضاقة قسط" introduces a new installment by popping up a window that has "العميل" entry, that says the name of the client, and "السلعة" entry that says the name or specifications of the product sold, and the "عدد الشهور" entry which says the number of months of installments, and "جنيه/الشهر" entry which says how much Egyptian pounds (EGP) will the client be paying per month, and the "إتمام" button to insert this information to the database.

Know that, Once information is added to the database the table updates to show it.
Know that, all entries must be inserted or else an error will arise.
Know that the entry of the number of months and the EGP per month must only be integers or an error will arise.

###### The installment table
Got columns where the "#" column indicates the number of installments since the start of using the program for financial balance, the "العميل" column shows the name of the client, "السلعة" column shows the name of the product he bought or any specifications for it, "ابتدى" shows the date (dd/MM/yyyy) when the installments started, the "ثمن" column shows the total quantity of installments (and it's calculated by the program), "مج الشهر" tells the total months of installments, "دُفع" column shows the total number of months that the client paid his installments, the "ج/ش" column shows the value of each installment per month.

Know that, the table is ordered by the most recently added installment at the top.
Know that, you can tell the program that the client paid a month of installment by right-clicking on the record and pressing "دفع شهر" and this will automatically update the table to increase the number of months of paid installments.
Know that, whenever a client pays his/her final installment the record automatically gets highlighted in grey and goes down to the bottom of the table.
Know that, you can't right-click anymore on any record that's highlighted in grey.

###### At the left side
There's a button called "سجل", and this button will be repeated throughout elements of this tab. This button opens a new window that has a date entry at the first row of it and a "إتمام" or "done" button, and at the bottom side there's a table that shows the history of paid installments, where "#" shows the number of paid installment log since the start of using the program, and "الاسم" column which shows the name of the client that paid the installment, and the "رقم القسط" column which indicates the installment number that this client paid for, and it is revealed in the "#" column in the previous table of installments, and the "القيمة" column which shows how much that client paid (and this value can't be changed, since its the value of the EGP/month that was first entered during the insertion of the installment), and "التاريخ" column which shows the date of the payment (dd/mm/yyyy) and the "الساعة" column which shows the timing of the payment (hh:mm:ss).

Know that, by choosing a date, the table shows the paid installments ONLY on this date.

###### The other table 
At the top of the installments table which is called "الجمعيات", this table shows information about anyone who gave the store any money so that the store will pay for it in installments, like the opposite of the previous table. The table and its buttons and everything are the same as the previous table except that the column "السلعة" (which shows the product name in the installments table) is removed, as well as its entry from the "إضافة جمعية" button (which inserts a new sponsor), but everything else concerning the meaning of column names and functionality and table sorting and records highlighting and way to increment payment months and the history "سجل" all are of the same method.

Now, to understand the rest of the widgets I have to explain how the balance check works.
PS I will explain what the "سجل" button that is on each of those frames does after explaining how the financial balance works. 

The balance check checks for every parameter in the store and they are summarized in 10 parameters:

P.S. For each parameter I will express it with a symbol to use it in the balance check equation later.

##### Financial Balance Parameters
1. some companies made machines that send balance to the phone number of clients to be able to make phone calls and receive calls (which is different than the EW, this machine sends money that CAN ONLY BE USED for the network services, like using internet data or making calls, but the EW sends money in a digital form and can be withdrawed later). The mobile shop of my friend has got 4 machines, each one has got a balance on it to be sent to clients who need it. Those machines are represented in the top left widget which is called "المكن" which has got 4 entries, each one indicating the available balance on each machine that is to be inserted (AT THE END OF THE DAY). Then, by clicking the "إتمام" button it sums all these values into the label in front of "مجموع المكن اليوم" and highlights it in green indicating that it was successfully done.
Consider This summation to be (RM)

2. 3. 4. 5 In the previous tab "مبيعات" we talked about 4 tables, the first table for sold products, the second for any cash sent TO the store, the third for any cash sent FROM the store, the fourth for store debts. The next 4 frames under the "المكن" frame are used to bring out the summation of these logs, where "الرصيد الداخل" frame by pressing the "إتمام" button brings out the summation of records that are in the "cash entered" table in front of the label "مجموع اليوم" and it highlights the value in green to make sure that it was done.
Consider sold products to be (MM) input cash to be (RH) output cash to be (RD) and store debts to be (DM)

The "الرصيد الخارج" does the same function but it sums the contents of the "cash out" table. The "المبيعات" frame does the same function but it sums the contents of the "sold products" table. The "الديون" frame does the same function but it sums the contents of the "debts" table and all get highlighted in green by pressing "إتمام".

6. 7. In the "فودافون كاش" tab, the first tab of the EW, we explained that in the end there is a balance on the EW numbers and debts that are on the clients that used it, so the "فودافون كاش" frame is responsible, to sum up, these values, where the value in front of the label "مجموع ديون العملاء" is the summation of debts on the clients, and the value in front of the "مجموع رصيد الأرقام" is the summation of the balance on all owned EW numbers. This summation is revealed by clicking the "إتمام" button and after that, the values get highlighted in green making sure it was done.
Consider the summation of debts to be (VCO) and the summation of EW balances to be (VCR)

8. Here is the entry of the cash available in the store, it is inserted and then the "إتمام" button is pressed to insert the value and shows it in front of the label "رصيد الدرج", then the value is highlighted in green make sure the entry is successful.
Know that only numerical values must be inserted in the "رصيد الدرج" frame or else an error will arise.
Consider this value to be (D)

9. Some people give the shop owner their money to invest in the EW business, and here comes the role of the frame at the top right side which is called "الثوابت". The button "إضافة ثابت" opens up a window asking for the client name "اسم العميل" and the value he will invest "المبلغ". Make sure the entered invested value is only an integer or else an error will arise.

After pressing the "إتمام" button the value is inserted into the database, and it can be shown by going to the previous "ثوابت" frame and clicking on the button "قائمة الثوابت" which opens a window that contains a table the column "#" which shows the record number ever since the start of the program, and the "الاسم" column which shows the client name, and the "القيمة" column which shows the invested amount, and the "الساعة" column which shows the time in (hh:mm:ss) and the "التاريخ" column which shows the date (dd/MM/yyyy) when the client invested his money or a change happened to its amount.

In this table, you can right-click on any of the records to show a drop-down menu having 3 options, The first one is "زيادة القيمة" which increases the amount of the invested money for the selected client record by showing a window showing an entry to that value, and this value must only be integer or else an error will arise. The second choice is "إنقاص القيمة" which decreases the invested value of the chosen client record by showing the same window with the same functionality to insert the value of the decrease, but with one slight difference; if the invested value hits zero by this decrease it will ask you if you would like to delete this record for the client if you click "no" or "cancel" it will do nothing, but if you press "yes" it will decrease the value to zero and put the record at the bottom of the table and highlight it in grey and you won't be able to right-click on it again. The table is ordered where the last added investment is at the top of the table. For the third choice "إزالة الثابت" it does the same thing if you decrease the investment amount to 0, it asks you if you would like to delete the record and does the same thing.

In the original frame, if you press "إتمام" it will sum the investment values available and put the sum in front of the label "المجموع" and highlight it in green to make sure the process is complete. 
Consider this value to be (S)

10. Any person who paid an installment will be considered an addition to the inserted cash into the store, and as mentioned, the program only knows if a client paid for an installment by right-clicking on his record and pressing "دفع شهر" and so this value also plays a role in our balance checking and I will explain how it's got after I explain the calculations. 
Consider this value to be (K)

##### The main Method
The way my friend checks for the balance validity and that all transactions are correct he calculates how much balance the store owns as a whole YESTERDAY, then he adds the TODAY's PROFIT to that amount and so X is generated.
Then he calculates what the store owns TODAY, if calculations are correct then the store must own TODAY what it owned YESTERDAY + PROFIT, if not then there's a problem.

When calculating what the shop owns, we don't take into consideration our installments or the client's installments for simplicity.

Consider what the shop owns today to be (MKY) what the shop owned yesterday to be (MKB) and the profit to be (RBH)

MKY = MKB + RBH (that's what it should be)
so MKY - (MKB + RBH) = Imbalance and I will express it with (GZ) (eqn. 1)

I consider the profit here to be any cash that entered the store minus any cash that went outside of it

so, RBH = RD + K + MM - RH

MKB should be a given from yesterday.

MKY = money the shop owns - debts (eqn. 2)
money the shop owns = VCO + VCR + RM + D
debts = DM + S

so, by substituting in eqn. 2 --> MKY = VCO + VCR + RM + D - DM - S

so, by substituting in eqn. 1 --> GZ = VCO + VCR + RM + D - DM - S - MKB - RD - K - MM - RH

In the middle column of the "تصفية" tab, there are 6 values at the top and they show this summary after pressing the red button "إتمام تصفية اليوم", this button does lots of things so let's break it down.

###### What does the red button do?
1. It takes all the values that are parameters in the financial balance (which are all marked in green on their labels) and does these calculations to bring out the financial summary, which is for the first row at the right it says "تصفية اليوم السابق" which is equivalent to MKB, and at the first row left column it says "المكسب" which is equivalent to RBH, the second row at the right side it says "الرصيد بعد المكسب" which is equivalent to MKB + RBH, and the second row left side is "الرصيد الحقيقي" which is MKY, the third-row right side it says "العجز/الزيادة" which is equivalent to GZ.

After pressing that button, all of the balancing parameters are set to 0 and the green highlight returns to the normal color, and then the first 4 labels turn into green highlights except for the GZ value, if the absolute GZ value > 100 it highlights will be red indicating big imbalance that should be fixed.

For the last item at the 3rd row left side, this shows the summation of GZ since a month back to show the overall sight of the balance.

2. After clicking this button it means that the financial day is over, so it clears up all the logs, in the second tab it clears the sold products log, the input cash log, and the output cash log, but it leaves the debt log as it is till the employer explicitly removes the debt.
For the first tab, it clears up the transactions log (the top left table) but it keeps the EW number balances as it is, and the clients' debts as it is.
For the third tab, it only clears the balance parameters, for the tables it keeps them as they are for they have got nothing to do with the financial balance. 

3. It clears the text field, in that text field, the employer can write any remarks throughout the day, after he writes it the red button removes whatever he has written.

Know that, the red button will raise an error if you didn't press "إتمام" on all of the financial balance parameters.

But, What happens to those logs that were emptied? 
Those logs can be retrieved back according to their date by the "سجل" buttons that we said we would talk about later, for each of the balance parameters frames there is a "سجل" button, as well as the installments tables.

###### The History Buttons "سجل":
1. for the "سجل" button at the RM frame, the D frame shows a window with a table at the bottom showing the value and the timing when the red button was pressed (AKA their values at that timing), and at the top there's date selection to find the value of these frames at that certain day.

2. For the DM frame, MM frame, RD frame, RH frame, it shows a window with the same style showing the logs of that day, like the name of the products, and their values, and the timing when the red button was pressed.

3. for the EW frame "فودافون كاش" it shows a window but with two tables at the bottom and date selection for each table at the top, and a drop-down menu for both EW numbers and debted clients, the left table shows all the clients with their debt values, and the right table shows all the numbers with their balance values at the timing of pressing the red button that day, and at the top you can chose to show only logs of one number at certain day or throughout all the days, as well as the debts of one certain client.

If you specify a client name/EW number and a date it will show how much dept that person/balance the EW number had during that date only, if you specify a client name/EW number ONLY without prior determination for a date it will show all the debts/balances throughout each day of completing the financial balance, if you specify only a date it will show all the clients/EW numbers debts/balances in that day only.

4. for the S frame, it shows a window with a table with date selection at the top and a table at the bottom, it shows each CHANGE that happened to an investment value, but for the current investments they can be shown at the "قائمة الثوابت" button, and the previous investments are at the bottom of the table highlighted in grey.

5. As for the installments' histories they were explained in a prior paragraph.

Know that, in all of the "سجل" windows, if you don't press the "تمام" Button, the default data shown are all of the data in the history, but if you press it, it will only show the transactions ONLY at the specified date, except for the EW history button it has got an additional parameter which is the transactions concerning a specific client or a specific number and they were explained. 

I have mentioned that I will explain how the program gets the (K) value that was paid during the day, and this happens by comparing the previous id to the installments, for example, if the red button is pressed, it saves the last installment transaction "id" that was paid, and when pressing the red button for the next day it compares the last installment transaction id in the logs with the previous id in the last day, if there's a difference then a new balance is added and it calculates it, if not then it considers the (K) value as 0.

Now, for the last button, which is the button up the red button "سجل التصفيات".
This button brings out a window with a table at its left side, an uneditable text field at the right side, and a date selection at the top of it.

This table shows all of the financial balance parameters history, where "#" is the number of balances (AKA days), the "تاريخ" shows the date (dd/MM/yyyy), the "الساعة" shows the hour (hh:mm:ss) of pressing the red button, the "الثابت" shows the S value at the time of pressing the red button, "آخر قسط" shows the last transaction id in the installment log table (the bottom table) by which the (K) value is determined, the "الأقساط" is the K value in that day, "مج المحافظ" shows VCR, the "مج عملاء المحافظ" is the VCO, "الربح" shows the RBH, "تصف افتراضية" shows the MKB + RBH, "تصف حقيقية" shows the MKY, "الزيادة" shows the GZ.

On the right side, it shows the notes taken during that day and the previous days showing the date of each day at the top of the text.

Know that only in this history log, when choosing a certain date, it shows the logs IN that date AND before that date.

Thank you very much for using my Program.
Alsalamualaykum.