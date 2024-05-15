import pyinputplus as pyip
def bmi(weight:float, height:float)->float:
        return round(weight / (height/100)**2, ndigits=2)

def get_status(bmi:float)->str:
    if bmi <18.5:
        remind = '體重過輕'
    elif bmi >=18.5 and bmi <24:
        remind = '正常體重'
    elif bmi >=24 and bmi <27:
        remind = '體重過重'
    elif bmi >=27 and bmi <30:
        remind = '輕度肥胖'
    elif bmi >=30 and bmi <35:
        remind = '中度肥胖'
    else:
        remind = '重度肥胖'
    return remind
name = pyip.inputStr("請輸入姓名:")
height = pyip.inputFloat("請輸入身高(cm):")
weight = pyip.inputFloat("請輸入體重(kg):")

bmi_count= bmi(weight, height)

print(f"{name},您的BMI值為:{bmi_count}")
        
print(f"您目前:{get_status(bmi_count)}")