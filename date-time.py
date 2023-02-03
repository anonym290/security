import jdatetime
import datetime
x = int(input('Your Age... : '))
#jalali
a = jdatetime.datetime.now()
#miladi
b = datetime.datetime.now()


userBirthYear_Miladi = b.year - x;
userBirthYear_Jalali = a.year - x;

print('Your Age',x,'\n','Your Birth Day In Miladi Date',userBirthYear_Miladi,'\n','Your BirthDay In Jalali Date',userBirthYear_Jalali)
