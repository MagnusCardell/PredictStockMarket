from yahoo_finance import Share
from graphics import*

def get_past_data(symbol,date):
    stock = Share(symbol)
    dump=stock.get_historical(date,date)
    for a in dump:
        openPrice= a["Open"]
        closePrice=a["Close"]
        highPrice=a["High"]
        lowPrice=a["Low"]
        adj_close=a["Adj_Close"]
        data=[highPrice,lowPrice,openPrice,closePrice,adj_close]
    return data

def main():

    win=GraphWin("Stock Prediction Program",1600,800)
    win.setCoords(0,0,1600,800)
    win.setBackground("lightblue")
    Text(Point(800,790),"Welcome to Portfolio Helper!  Please input the stocks in your portfolio in the dark gray below:").draw(win)
    Text(Point(100,700),"Stock").draw(win)
    Text(Point(100,680),"Ticker:").draw(win)
    Text(Point(225,700),"Volume").draw(win)
    Text(Point(225,680),"Owned:").draw(win)
    Text(Point(345,700),"High").draw(win)
    Text(Point(345,680),"Price:").draw(win)
    Text(Point(465,700),"Low").draw(win)
    Text(Point(465,680),"Price:").draw(win)
    Text(Point(585,700),"Opening").draw(win)
    Text(Point(585,680),"Price:").draw(win)
    Text(Point(705,700),"Closing").draw(win)
    Text(Point(705,680),"Price:").draw(win)
    Text(Point(825,700),"Adj Closing").draw(win)
    Text(Point(825,680),"Price:").draw(win)
    Text(Point(1185,700),"Estimated").draw(win)
    Text(Point(1185,680),"Change:").draw(win)
    Text(Point(1305,700),"Suggested").draw(win)
    Text(Point(1305,680),"Action:").draw(win)

    Stock1=Entry(Point(100, 650),7)
    Stock1.draw(win)
    Stock2=Entry(Point(100, 600),7)
    Stock2.draw(win)
    Stock3=Entry(Point(100, 550),7)
    Stock3.draw(win)
    Stock4=Entry(Point(100, 500),7)
    Stock4.draw(win)
    Stock5=Entry(Point(100, 450),7)
    Stock5.draw(win)
    Stock6=Entry(Point(100, 400),7)
    Stock6.draw(win)
    Stock7=Entry(Point(100, 350),7)
    Stock7.draw(win)
    Stock8=Entry(Point(100, 300),7)
    Stock8.draw(win)
    Stock9=Entry(Point(100, 250),7)
    Stock9.draw(win)
    Stock10=Entry(Point(100, 200),7)
    Stock10.draw(win)
    Volume1=Entry(Point(225, 650), 7)
    Volume1.draw(win)
    Volume2=Entry(Point(225, 600),7)
    Volume2.draw(win)
    Volume3=Entry(Point(225, 550),7)
    Volume3.draw(win)
    Volume4=Entry(Point(225, 500),7)
    Volume4.draw(win)
    Volume5=Entry(Point(225, 450),7)
    Volume5.draw(win)
    Volume6=Entry(Point(225, 400),7)
    Volume6.draw(win)
    Volume7=Entry(Point(225, 350),7)
    Volume7.draw(win)
    Volume8=Entry(Point(225, 300),7)
    Volume8.draw(win)
    Volume9=Entry(Point(225, 250),7)
    Volume9.draw(win)
    Volume10=Entry(Point(225, 200),7)
    Volume10.draw(win)
    
    y_axis=[665,615,565,515,465,415,365,315,265,215]
    x_axis=[315,435,555,675,795,1155,1275]
    for x in x_axis:
        for y in y_axis:
            Boxes=Rectangle(Point(x,y),Point(x+60,y-25)).draw(win)
    START=Rectangle(Point(1380,80),Point(1480,180))
    START.setFill("Green")
    START.draw(win)
    button=Text(Point(1430,130),"COMPUTE")
    button.draw(win)
    x=True
    while x:    
        point=win.getMouse()
        pX=point.getX()
        pY=point.getY()
        if 1380 <= pX <= 1480 and 80<= pY <= 180:
            button.setText("Working...")
            button.setFill("yellow")
            x=False
    
    Portfolio=[]
    if Stock1.getText():
        Portfolio.append(Stock1.getText())
    if Stock2.getText():    
        Portfolio.append(Stock2.getText())
    if Stock3.getText():
        Portfolio.append(Stock3.getText())
    if Stock4.getText():
        Portfolio.append(Stock4.getText())
    if Stock5.getText():
        Portfolio.append(Stock5.getText())
    if Stock6.getText():
        Portfolio.append(Stock6.getText())
    if Stock7.getText():
        Portfolio.append(Stock7.getText())
    if Stock8.getText():
        Portfolio.append(Stock8.getText())
    if Stock9.getText():
        Portfolio.append(Stock9.getText())
    if Stock10.getText():
        Portfolio.append(Stock10.getText())
    year_data={}
    halfyear_data={}
    month_data={}
    week_data={}
    yestyest_data={}
    yest_data={}
    for stock in Portfolio:
        year_data[stock]=get_past_data(stock,"2014-07-15")
        halfyear_data[stock]=get_past_data(stock,"2015-07-15")
        month_data[stock]=get_past_data(stock,"2015-11-13")
        week_data[stock]=get_past_data(stock,"2015-12-10")
        yestyest_data[stock]=get_past_data(stock,"2015-12-15")
        yest_data[stock]=get_past_data(stock,"2015-12-16")

    if Stock1.getText():
        Text(Point(345,652),"${:.6s}".format(yest_data[Stock1.getText()][0])).draw(win)
        Text(Point(465,652),"${:.6s}".format(yest_data[Stock1.getText()][1])).draw(win)
        Text(Point(585,652),"${:.6s}".format(yest_data[Stock1.getText()][2])).draw(win)
        Text(Point(705,652),"${:.6s}".format(yest_data[Stock1.getText()][3])).draw(win)
        Text(Point(825,652),"${:.6s}".format(yest_data[Stock1.getText()][4])).draw(win)
        day1=float(yest_data[Stock1.getText()][4])-float(yestyest_data[Stock1.getText()][4])
        week1=float(yest_data[Stock1.getText()][4])-float(week_data[Stock1.getText()][4])
        month1=float(yest_data[Stock1.getText()][4])-float(month_data[Stock1.getText()][4])
        halfyear1=float(yest_data[Stock1.getText()][4])-float(halfyear_data[Stock1.getText()][4])
        year1=float(yest_data[Stock1.getText()][4])-float(year_data[Stock1.getText()][4])
        Text(Point(1185,652),Change(day1,week1,month1)).draw(win)
        Text(Point(1305,652),Action(day1,week1,month1,halfyear1,year1)).draw(win)

    if Stock2.getText():    
        Text(Point(345,602),"${:.6s}".format(yest_data[Stock2.getText()][0])).draw(win)
        Text(Point(465,602),"${:.6s}".format(yest_data[Stock2.getText()][1])).draw(win)
        Text(Point(585,602),"${:.6s}".format(yest_data[Stock2.getText()][2])).draw(win)
        Text(Point(705,602),"${:.6s}".format(yest_data[Stock2.getText()][3])).draw(win)
        Text(Point(825,602),"${:.6s}".format(yest_data[Stock2.getText()][4])).draw(win)
        day2=float(yest_data[Stock2.getText()][4])-float(yestyest_data[Stock2.getText()][4])
        week2=float(yest_data[Stock2.getText()][4])-float(week_data[Stock2.getText()][4])
        month2=float(yest_data[Stock2.getText()][4])-float(month_data[Stock2.getText()][4])
        halfyear2=float(yest_data[Stock2.getText()][4])-float(halfyear_data[Stock2.getText()][4])
        year2=float(yest_data[Stock2.getText()][4])-float(year_data[Stock2.getText()][4])
        Text(Point(1185,600),Change(day2,week2,month2)).draw(win)
        Text(Point(1305,600),Action(day2,week2,month2,halfyear2,year2)).draw(win)
        
    if Stock3.getText():
        Text(Point(345,552),"${:.6s}".format(yest_data[Stock3.getText()][0])).draw(win)
        Text(Point(465,552),"${:.6s}".format(yest_data[Stock3.getText()][1])).draw(win)
        Text(Point(585,552),"${:.6s}".format(yest_data[Stock3.getText()][2])).draw(win)
        Text(Point(705,552),"${:.6s}".format(yest_data[Stock3.getText()][3])).draw(win)
        Text(Point(825,552),"${:.6s}".format(yest_data[Stock3.getText()][4])).draw(win)
        day3=float(yest_data[Stock3.getText()][4])-float(yestyest_data[Stock3.getText()][4])
        week3=float(yest_data[Stock3.getText()][4])-float(week_data[Stock3.getText()][4])
        month3=float(yest_data[Stock3.getText()][4])-float(month_data[Stock3.getText()][4])
        halfyear3=float(yest_data[Stock3.getText()][4])-float(halfyear_data[Stock3.getText()][4])
        year3=float(yest_data[Stock3.getText()][4])-float(year_data[Stock3.getText()][4])
        Text(Point(1185,552),Change(day3,week3,month3)).draw(win)
        Text(Point(1305,552),Action(day3,week3,month3,halfyear3,year3)).draw(win)

    if Stock4.getText():
        Text(Point(345,502),"${:.6s}".format(yest_data[Stock4.getText()][0])).draw(win)
        Text(Point(465,502),"${:.6s}".format(yest_data[Stock4.getText()][1])).draw(win)
        Text(Point(585,502),"${:.6s}".format(yest_data[Stock4.getText()][2])).draw(win)
        Text(Point(705,502),"${:.6s}".format(yest_data[Stock4.getText()][3])).draw(win)
        Text(Point(825,502),"${:.6s}".format(yest_data[Stock4.getText()][4])).draw(win)
        day4=float(yest_data[Stock4.getText()][4])-float(yestyest_data[Stock4.getText()][4])
        week4=float(yest_data[Stock4.getText()][4])-float(week_data[Stock4.getText()][4])
        month4=float(yest_data[Stock4.getText()][4])-float(month_data[Stock4.getText()][4])
        halfyear4=float(yest_data[Stock4.getText()][4])-float(halfyear_data[Stock4.getText()][4])
        year4=float(yest_data[Stock4.getText()][4])-float(year_data[Stock4.getText()][4])
        Text(Point(1185,500),Change(day4,week4,month4)).draw(win)
        Text(Point(1305,500),Action(day4,week4,month4,halfyear4,year4)).draw(win)
    if Stock5.getText():
        Text(Point(345,452),"${:.6s}".format(yest_data[Stock5.getText()][0])).draw(win)
        Text(Point(465,452),"${:.6s}".format(yest_data[Stock5.getText()][1])).draw(win)
        Text(Point(585,452),"${:.6s}".format(yest_data[Stock5.getText()][2])).draw(win)
        Text(Point(705,452),"${:.6s}".format(yest_data[Stock5.getText()][3])).draw(win)
        Text(Point(825,452),"${:.6s}".format(yest_data[Stock5.getText()][4])).draw(win)
        day5=float(yest_data[Stock5.getText()][4])-float(yestyest_data[Stock5.getText()][4])
        week5=float(yest_data[Stock5.getText()][4])-float(week_data[Stock5.getText()][4])
        month5=float(yest_data[Stock5.getText()][4])-float(month_data[Stock5.getText()][4])
        halfyear5=float(yest_data[Stock5.getText()][4])-float(halfyear_data[Stock5.getText()][4])
        year5=float(yest_data[Stock5.getText()][4])-float(year_data[Stock5.getText()][4])
        Text(Point(1185,452),Change(day5,week5,month5)).draw(win)
        Text(Point(1305,452),Action(day5,week5,month5,halfyear5,year5)).draw(win)
    if Stock6.getText():
        Text(Point(345,402),"${:.6s}".format(yest_data[Stock6.getText()][0])).draw(win)
        Text(Point(465,402),"${:.6s}".format(yest_data[Stock6.getText()][1])).draw(win)
        Text(Point(585,402),"${:.6s}".format(yest_data[Stock6.getText()][2])).draw(win)
        Text(Point(705,402),"${:.6s}".format(yest_data[Stock6.getText()][3])).draw(win)
        Text(Point(825,402),"${:.6s}".format(yest_data[Stock6.getText()][4])).draw(win)
        day6=float(yest_data[Stock6.getText()][4])-float(yestyest_data[Stock6.getText()][4])
        week6=float(yest_data[Stock6.getText()][4])-float(week_data[Stock6.getText()][4])
        month6=float(yest_data[Stock6.getText()][4])-float(month_data[Stock6.getText()][4])
        halfyear6=float(yest_data[Stock6.getText()][4])-float(halfyear_data[Stock6.getText()][4])
        year6=float(yest_data[Stock6.getText()][4])-float(year_data[Stock6.getText()][4])
        Text(Point(1185,400),Change(day6,week6,month6)).draw(win)
        Text(Point(1305,400),Action(day6,week6,month6,halfyear6,year6)).draw(win)
    if Stock7.getText():
        Text(Point(345,352),"${:.6s}".format(yest_data[Stock7.getText()][0])).draw(win)
        Text(Point(465,352),"${:.6s}".format(yest_data[Stock7.getText()][1])).draw(win)
        Text(Point(585,352),"${:.6s}".format(yest_data[Stock7.getText()][2])).draw(win)
        Text(Point(705,352),"${:.6s}".format(yest_data[Stock7.getText()][3])).draw(win)
        Text(Point(825,352),"${:.6s}".format(yest_data[Stock7.getText()][4])).draw(win)
        day7=float(yest_data[Stock7.getText()][4])-float(yestyest_data[Stock7.getText()][4])
        week7=float(yest_data[Stock7.getText()][4])-float(week_data[Stock7.getText()][4])
        month7=float(yest_data[Stock7.getText()][4])-float(month_data[Stock7.getText()][4])
        halfyear7=float(yest_data[Stock7.getText()][4])-float(halfyear_data[Stock7.getText()][4])
        year7=float(yest_data[Stock7.getText()][4])-float(year_data[Stock7.getText()][4])
        Text(Point(1185,352),Change(day7,week7,month7)).draw(win)
        Text(Point(1305,352),Action(day7,week7,month7,halfyear7,year7)).draw(win)
    if Stock8.getText():
        Text(Point(345,302),"${:.6s}".format(yest_data[Stock8.getText()][0])).draw(win)
        Text(Point(465,302),"${:.6s}".format(yest_data[Stock8.getText()][1])).draw(win)
        Text(Point(585,302),"${:.6s}".format(yest_data[Stock8.getText()][2])).draw(win)
        Text(Point(705,302),"${:.6s}".format(yest_data[Stock8.getText()][3])).draw(win)
        Text(Point(825,302),"${:.6s}".format(yest_data[Stock8.getText()][4])).draw(win)
        day8=float(yest_data[Stock8.getText()][4])-float(yestyest_data[Stock8.getText()][4])
        week8=float(yest_data[Stock8.getText()][4])-float(week_data[Stock8.getText()][4])
        month8=float(yest_data[Stock8.getText()][4])-float(month_data[Stock8.getText()][4])
        halfyear8=float(yest_data[Stock8.getText()][4])-float(halfyear_data[Stock8.getText()][4])
        year8=float(yest_data[Stock8.getText()][4])-float(year_data[Stock8.getText()][4])
        Text(Point(1185,300),Change(day8,week8,month8)).draw(win)
        Text(Point(1305,300),Action(day8,week8,month8,halfyear8,year8)).draw(win)

    if Stock9.getText():
        Text(Point(345,252),"${:.6s}".format(yest_data[Stock9.getText()][0])).draw(win)
        Text(Point(465,252),"${:.6s}".format(yest_data[Stock9.getText()][1])).draw(win)
        Text(Point(585,252),"${:.6s}".format(yest_data[Stock9.getText()][2])).draw(win)
        Text(Point(705,252),"${:.6s}".format(yest_data[Stock9.getText()][3])).draw(win)
        Text(Point(825,252),"${:.6s}".format(yest_data[Stock9.getText()][4])).draw(win)
        day9=float(yest_data[Stock9.getText()][4])-float(yestyest_data[Stock9.getText()][4])
        week9=float(yest_data[Stock9.getText()][4])-float(week_data[Stock9.getText()][4])
        month9=float(yest_data[Stock9.getText()][4])-float(month_data[Stock9.getText()][4])
        halfyear9=float(yest_data[Stock9.getText()][4])-float(halfyear_data[Stock9.getText()][4])
        year9=float(yest_data[Stock9.getText()][4])-float(year_data[Stock9.getText()][4])
        Text(Point(1185,252),Change(day9,week9,month9)).draw(win)
        Text(Point(1305,252),Action(day9,week9,month9,halfyear9,year9)).draw(win)
    if Stock10.getText():
        Text(Point(345,202),"${:.6s}".format(yest_data[Stock10.getText()][0])).draw(win)
        Text(Point(465,202),"${:.6s}".format(yest_data[Stock10.getText()][1])).draw(win)
        Text(Point(585,202),"${:.6s}".format(yest_data[Stock10.getText()][2])).draw(win)
        Text(Point(705,202),"${:.6s}".format(yest_data[Stock10.getText()][3])).draw(win)
        Text(Point(825,202),"${:.6s}".format(yest_data[Stock10.getText()][4])).draw(win)
        day10=float(yest_data[Stock10.getText()][4])-float(yestyest_data[Stock10.getText()][4])
        week10=float(yest_data[Stock10.getText()][4])-float(week_data[Stock10.getText()][4])
        month10=float(yest_data[Stock10.getText()][4])-float(month_data[Stock10.getText()][4])
        halfyear10=float(yest_data[Stock10.getText()][4])-float(halfyear_data[Stock10.getText()][4])
        year10=float(yest_data[Stock10.getText()][4])-float(year_data[Stock10.getText()][4])
        Text(Point(1185,200),Change(day10,week10,month10)).draw(win)
        Text(Point(1305,200),Action(day10,week10,month10,halfyear10,year10)).draw(win)


    button.setText("Quit")
    button.setFill("Red")
    x=True
    while x:    
        point=win.getMouse()
        pX=point.getX()
        pY=point.getY()
        if 1380 <= pX <= 1480 and 80<= pY <= 180:

            x=False
    win.close()
def Change(day,week,month):
    
    if day>0 and week>0 and month>0:
        return "Positive"
    elif day>0 and week>0 and month<=0: 
        return "Positive"
    elif day>0 and week<=0 and month>0: 
        return "Positive"
    elif day<=0 and week>0 and month>0: 
        return "Positive"
    else:
        return "Negative"


def Action(day,week,month,halfyear,year):

    if day>0 and week>0 and month>0 and halfyear>0 and year>0:
        return "Buy"
    elif day<=0 and week>0 and month>0 and halfyear>0 and year>0:
        return "Buy"
    elif day>0 and week<=0 and month>0 and halfyear>0 and year>0:
        return "Buy"
    elif day>0 and week>0 and month<=0 and halfyear>0 and year>0:
        return "Buy"
    elif day>0 and week>0 and month>0 and halfyear<=0 and year>0:
        return "Buy"
    elif day>0 and week>0 and month>0 and halfyear>0 and year<=0:
        return "Buy"
    elif day<=0 and week>0 and month>0 and halfyear>0 and year<=0:
        return "Buy"
    elif day>0 and week<=0 and month<=0 and halfyear>0 and year>0:
        return "Buy"
    elif day>0 and week<=0 and month>0 and halfyear>0 and year<=0:
        return "Buy"
    elif day>0 and week>0 and month<=0 and halfyear<=0 and year>0:
        return "Buy"
    elif day>0 and week>0 and month<=0 and halfyear>0 and year<=0:
        return "Buy"
    elif day>0 and week>0 and month>0 and halfyear<=0 and year<=0:
        return "Buy"
    elif day<=0 and week>0 and month>0 and halfyear<=0 and year>0:
        return "Hold"
    elif day>0 and week<=0 and month>0 and halfyear<=0 and year>0:
        return "Hold"
    elif day>0 and week>0 and month<=0 and halfyear<=0 and year<=0:
        return "Hold"
    elif day>0 and week<=0 and month>0 and halfyear<=0 and year<=0:
        return "Hold"
    elif day>0 and week<=0 and month<=0 and halfyear<=0 and year>0:
        return "Hold"
    elif day<=0 and week>0 and month>0 and halfyear<=0 and year<=0:
        return "Hold"
    else:
        return "Sell"

main()
