#-------------------------------------------------------------------------
# Neina Cichon
# Retail Discount
# 2020-6-25
#--------------------------------------------------------------------------
import datetime
#--------------------------------------------------------------------------
#   Project 1 Function Area
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#1. Function Name:			ValidateYear            
#2. Function Description:	Validates that input for years worked is whole number and not negative
#--------------------------------------------------------------------------

def ValidateYear(years):
    global boolFlag
    try:
        years = float(years)
        if (years > 0):
            boolFlag = True
        else:
            print("Years worked must be a positive number.")
    except ValueError:
        years = int(0)
        print("Please enter number of years worked.")
    return years
#--------------------------------------------------------------------------
#1. Function Name:			ValidateStatus      
#2. Function Description:	Checks that status entered is valid "hourly" or "management", nothing else
#--------------------------------------------------------------------------

def ValidateStatus(status):
    global boolFlag
    try:
        status = str(status.lower())
        if status == "hourly" or status == "h":
            boolFlag=True
            status = "hourly"
        elif status == "management" or status == "m":
            boolFlag=True
            status= "management"
        else:
            print("Please enter either \"hourly\" or \"management\". ")
    except ValueError:
        print("Please enter if employee is \"hourly\" or \"management\".")
    return status

#--------------------------------------------------------------------------
#1. Function Name:			ValidateAmount
#2. Function Description	Validates that monetary inputs are positive numbers, and nothing else
#--------------------------------------------------------------------------

def ValidateAmount(purchaseAmount):
    global boolFlag
    try:
        purchaseAmount = float(purchaseAmount) 
        if (purchaseAmount >= 0):
            boolFlag = True
        else:
            print("Number must be a positive amount.")
    except ValueError:
        purchaseAmount= float(0)
        print("Please enter amount.")
    return purchaseAmount

#--------------------------------------------------------------------------
#1. Function Name:			ValidateMore
#2. Function Description	Validates that inputs checking for more employees is either "yes" or "no"  and nothing else
#--------------------------------------------------------------------------

def ValidateMore(MoreEmployees):
    global boolFlag
    global boolMoreEmployees
    try:
        MoreEmployees = str(MoreEmployees.lower())
        if MoreEmployees=="yes" or MoreEmployees == "y":
            boolMoreEmployees = True
            boolFlag = True
            MoreEmployees = "yes"
        elif MoreEmployees == "no" or MoreEmployees == "n":
            boolMoreEmployees = False
            boolFlag = True
            MoreEmployees = "no"
    except ValueError:
        print("Please enter yes or no.")
    return MoreEmployees


#--------------------------------------------------------------------------
#1. Function Name:			CalcDiscount
#2. Function Description	Calculates the discount of the employee based on status (hourly/management) and the number of years worked
#--------------------------------------------------------------------------
def CalcDiscount(status, years):
    global strEmployeeStatus
    global intYearsWorked
    global dblEmployeeDiscount 
    global cdblDiscountNone
    global cdblDiscount10
    global cdblDiscount14
    global cdblDiscount20
    global cdblDiscount24
    global cdblDiscount25
    global cdblDiscount30
    global cdblDiscount35
    global cdblDiscount40
     
    if strEmployeeStatus == "management":
        if intYearsWorked < 1:
            dblEmployeeDiscount = cdblDiscountNone
        elif intYearsWorked <= 3:
            dblEmployeeDiscount = cdblDiscount20
        elif intYearsWorked <= 6:
            dblEmployeeDiscount = cdblDiscount24
        elif intYearsWorked <= 10:
            dblEmployeeDiscount = cdblDiscount30
        elif intYearsWorked <= 15:
            dblEmployeeDiscount = cdblDiscount35
        elif intYearsWorked > 15:
            dblEmployeeDiscount = cdblDiscount40
    else:
        if intYearsWorked < 1:
            dblEmployeeDiscount = cdblDiscountNone
        elif intYearsWorked <= 3:
            dblEmployeeDiscount = cdblDiscount10
        elif intYearsWorked <= 6:
            dblEmployeeDiscount = cdblDiscount14
        elif intYearsWorked <= 10:
            dblEmployeeDiscount = cdblDiscount20
        elif intYearsWorked <= 15:
            dblEmployeeDiscount = cdblDiscount25
        elif intYearsWorked > 15:
            dblEmployeeDiscount= cdblDiscount30

    discPrint= format(dblEmployeeDiscount*100, '.2f')
    print("----------------------------------------------------------------------\n - Employee Discount Summary -\n----------------------------------------------------------------------")
    print("Employee discount is ", discPrint, "%" )

#--------------------------------------------------------------------------
#1. Function Name:			CalcYTDDiscount
#2. Function Description	Calculates the YTD Discount amount already earned
#--------------------------------------------------------------------------

def CalcYTDDiscount(discount, prevPurchase):
    global dblPreviousPurchase
    global dblYTDDiscountTotal

    dblYTDDiscountTotal = (dblPreviousPurchase * dblEmployeeDiscount)

    ytdDiscPrint = format(dblYTDDiscountTotal, '.2f')
    print("The total YTD discount amount is $", ytdDiscPrint)

#--------------------------------------------------------------------------
#1. Function Name:			CalcTotal
#2. Function Description	Calculates total amount of purchase with discount
#--------------------------------------------------------------------------
def CalcTotal(discount, currentPurchase, ytdDiscount):
    global cdblMaxDiscount
    global dblCurrentPurchaseAmount
    global dblYTDDiscountTotal
    global dblTotal

    if dblYTDDiscountTotal >= cdblMaxDiscount:
            dblCurrentDisc = 0                                               
            dblYTDDiscountTotal = cdblMaxDiscount
    elif dblYTDDiscountTotal < cdblMaxDiscount:   
        if ((dblCurrentPurchaseAmount * dblEmployeeDiscount) + (dblYTDDiscountTotal)) > cdblMaxDiscount:    
            dblCurrentDisc = (cdblMaxDiscount - dblYTDDiscountTotal)                      
        else:
            dblCurrentDisc = (dblCurrentPurchaseAmount * dblEmployeeDiscount)                    
    dblTotal = (dblCurrentPurchaseAmount - dblCurrentDisc)
    
    todayPurchPrint = format(dblCurrentPurchaseAmount, '.2f')
    todayDiscPrint = format( dblCurrentDisc,'.2f')
    totalPrint = format(dblTotal, '.2f')

    print("The total purchase today before discount is $", todayPurchPrint)
    print("The total employee discount today is $", todayDiscPrint)
    print("The total purchase amount with discount is $", totalPrint)
    print("----------------------------------------------------------------------")

#--------------------------------------------------------------------------
#1. Function Name:			CalcDailyTotalBefore
#2. Function Description	Calculates the running total of daily purchases before discounts
#--------------------------------------------------------------------------

def CalcDailyTotalBefore(purchaseAmount):
    global cdblAllTotalBefore
    cdblAllTotalBefore += purchaseAmount

#--------------------------------------------------------------------------
#1. Function Name:			CalcDailyTotalAfter
#2. Function Description:	Calculates the running total of daily purchases after discounts
#--------------------------------------------------------------------------

def CalcDailyTotalAfter(discountPurchaseAmount):
    global cdblAllTotalAfter
    cdblAllTotalAfter = cdblAllTotalAfter + discountPurchaseAmount

#--------------------------------------------------------------------------
#1. Function Name:		    Display
#2. Function Description:   Displays the running totals after no more employees are being entered	
#--------------------------------------------------------------------------

def GetDate():
    global strDays
    today = datetime.datetime.today()
    strDays = today.strftime("%B %d, %Y")

    return strDays
    

#--------------------------------------------------------------------------
#1. Function Name:		    Display
#2. Function Description:   Displays the running totals after no more employees are being entered	
#--------------------------------------------------------------------------

def Display(TotalBefore, TotalAfter):
    global cdblAllTotalBefore
    global cdblAllTotalAfter
    global strDays

    runningTotBeforePrint = format(cdblAllTotalBefore, '.2f')
    runningTotAfterPrint = format(cdblAllTotalAfter, '.2f')
    print("----------------------------------------------------------------------\n - Daily All Employee Summary -", strDays,"\n----------------------------------------------------------------------")
    
    print("The daily total before discount is $", cdblAllTotalBefore)
    print("The daily total after discount is $", cdblAllTotalAfter)

    print("----------------------------------------------------------------------\n\n\nThis program has been brought to you by Neina.")

#--------------------------------------------------------------------------
# Assignment # Main Processing Area   
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Declare Variables
#--------------------------------------------------------------------------


cdblAllTotalBefore = float()
cdblAllTotalAfter = float()
dblEmployeeDiscount = float()
dblYTDDiscAmt = float()
dblPurchaseAmt = float()
dblTotal = float()
dblCurrentDisc = float()
cdblMaxDiscount = float(200)
cdblDiscountNone = float(0)
cdblDiscount10 = float(0.1)
cdblDiscount14 = float(0.14)
cdblDiscount20 = float(0.2)
cdblDiscount24 = float(0.24)
cdblDiscount25 = float(0.25)
cdblDiscount30 = float(0.3)
cdblDiscount35 = float(0.35)
cdblDiscount40 = float(0.4)
boolMoreEmployees= bool(True)


#--------------------------------------------------------------------------
# Gather Input and call functions to validate input
#--------------------------------------------------------------------------

while boolMoreEmployees is True:

        #Loop until intYearsWorked is valid
        boolFlag = bool(False)
        while boolFlag is False:
            intYearsWorked = str(input("Enter number of years worked: "))
            intYearsWorked = ValidateYear(intYearsWorked)

        #Loop until strEmployeeStatus is valid
        boolFlag = bool(False)
        while boolFlag is False:
            strEmployeeStatus = str(input("Enter employee status - Hourly(H) or Management(M): "))
            strEmployeeStatus = ValidateStatus(strEmployeeStatus)

        #Loop until dblPreviousPurchase is valid
        boolFlag = bool(False)
        while boolFlag is False:
            dblPreviousPurchase = str(input("Enter total amount of previous purchases before discount: "))
            dblPreviousPurchase = ValidateAmount(dblPreviousPurchase)

        #Loop until dblCurrentPurchaseAmount is valid
        boolFlag = bool(False)
        while boolFlag is False:
            dblCurrentPurchaseAmount = str(input("Enter total of today's purchase: "))
            dblCurrentPurchaseAmount = ValidateAmount(dblCurrentPurchaseAmount)
#--------------------------------------------------------------------------
# Calculations and Display Output for each employee
#--------------------------------------------------------------------------

        CalcDiscount(strEmployeeStatus, intYearsWorked)
        CalcYTDDiscount(dblEmployeeDiscount, dblPreviousPurchase)
        CalcTotal(dblEmployeeDiscount, dblCurrentPurchaseAmount, dblYTDDiscountTotal)
        
#--------------------------------------------------------------------------
# Loop for each employee
#--------------------------------------------------------------------------        

        boolFlag= bool(False)
        while boolFlag is False:
            strMoreEmployees = str(input("Would you like to add another employee purchase? Enter Yes(Y) or No(N): "))
            ValidateMore(strMoreEmployees)
#--------------------------------------------------------------------------
# Call Calculations for running total
#--------------------------------------------------------------------------        
        
        GetDate()
        CalcDailyTotalBefore(dblCurrentPurchaseAmount)
        CalcDailyTotalAfter(dblTotal)

#--------------------------------------------------------------------------
# Display Running Total Output
#--------------------------------------------------------------------------

Display(dblCurrentPurchaseAmount, dblTotal)

	

