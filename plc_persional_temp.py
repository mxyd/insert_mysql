# 2020/12/21
# author:xieyudong
"""客户表"""
import pymysql
import datetime
db = pymysql.connect(host='117.36.75.166', port=3506,user='root',passwd='123456',db='zdbk_dev',charset='utf8')
cursor = db.cursor()
batch_no=['10000001','10000002','10000003','10000004','10000005']
personal_type = ['PERSOANL','ENTERPRISE','PERSOANL','ENTERPRISE','PERSOANL']
personal_no = [1001,1002,1003,2001,2002]
personal_name = ['张三','李四','王五','赵六','赵一']
id_type = ['ID_CARD','CREDIT_CODE','ID_CARD','CREDIT_CODE','ID_CARD']
id_card = ['110101199003077053','110101199003070652','110101199003073431','110101199003070871','110101199003070433']
english_name = ['Tom','Mark','Bill','Vincent','William']
sex = ['male','female','male','female','male']
birthday = ['1990-03-07','1990-03-07','1990-03-07','1990-03-07','1990-03-07']
nationality = ['中国','中国','中国','中国','中国']
language = ['中文','中文','中文','中文','中文']
nation = ['汉','汉','汉','汉','汉']
education = ['大专','本科','硕士','博士','研究生']
graduate_school = ['上海大学','北京大学','青岛大学','合肥大学','深圳大学']
enrollment_time = ['2009-09-01','2009-09-01','2009-09-01','2009-09-01','2009-09-01']
graduation_time = ['2013-07-05','2013-07-05','2013-07-05','2013-07-05','2013-07-05']
income = ['5000','10000','15000','20000','25000']
id_card_address = ['上海','北京','青岛','合肥','深圳']
mobile_no_address = ['上海','北京','青岛','合肥','深圳']
ip_address = ['上海','北京','青岛','合肥','深圳']
online_status = ['在线','在线','在线','在线','在线']
personal_rank = ['一级','一级','一级','一级','一级']
first_date = [
    datetime.datetime.strptime('2010-10-01','%Y-%m-%d'),
    datetime.datetime.strptime('2010-10-01','%Y-%m-%d'),
    datetime.datetime.strptime('2010-10-01','%Y-%m-%d'),
    datetime.datetime.strptime('2010-10-01','%Y-%m-%d'),
    datetime.datetime.strptime('2010-10-01','%Y-%m-%d'),
    ]
up_months = [1,2,3,4,5]
company_name = ['招东银行','招东律所','招东公安局','招东银行数据中心','招东航天']
industry = ['银行','律师','警察','IT','航天']
company_type = ['国企','私企','国企','国企','私企']
occupation = ['一级','一级','一级','一级','一级']
marital = ['未婚','已婚','未婚','已婚','未婚']
house_type = ['租房','租房','租房','租房','租房']
local_phone_area_code = ['029','029','029','029','029']
local_phone = ['83145678','83145679','83145680','83145681','83145682']
company_phone_area_code = ['029','029','029','029','029']
company_phone = ['583145678','583145679','583145680','583145681','583145682']
register_phone_area_code = ['029','029','029','029','029']
register_phone = ['83145678','83145679','83145680','83145681','83145682']
deposit_account_flag = ['一般客户','重要客户','一般客户','重要客户','一般客户']
wechat_no_flag = ['是','是','是','是','是']
email_flag = ['是','是','是','是','是']
risk_flag = ['高','底','高','底','高',]
lately_pay_date = ['2020.10.15','2020.10.15','2020.10.15','2020.10.15','2020.10.15']
lately_pay_amount = [1800.09,1800.11,1800.12,1800.13,1800.14]
total_accounts = [5,5,5,5,5]
merge_accounts = [5,5,5,5,5]
net_interest_flag = ['是','是','是','是','是']
delay_max_account_no = ['600001','600002','600003','600004','600005']
delay_max_account_type = ['房产账户','房产账户','房产账户','房产账户','房产账户']
history_max_overdue_stage = ['5','6','7','8','9']
credit_code = ['91420100333437374F','91310000607431448P','913301106680053894','915114255671827814','91310120069360143D']
org_code = ['333437374','682874345','607431448','668005389','567182781']
texpayer_id = ['91420100333437374F','91110108682874345L','91310000607431448P','913301106680053894','915114255671827814']
establishment_date = [
    datetime.datetime.strptime('2015-05-08','%Y-%m-%d'),
    datetime.datetime.strptime('2015-05-08','%Y-%m-%d'),
    datetime.datetime.strptime('2015-05-08','%Y-%m-%d'),
    datetime.datetime.strptime('2015-05-08','%Y-%m-%d'),
    datetime.datetime.strptime('2015-05-08','%Y-%m-%d'),]
license_start_time = ['2015-05-08','2008-11-25','2001-02-23','2007-10-17','2011-01-14']
registered_capital = [2234155300.00,404000000.00,78000000.00,120000000.00,91556199.00]
registration_time = ['2015-05-08','2008-11-25','2001-02-23','2007-10-17','2011-01-14']
public_bank_card_number = ['6216610200016587010','6216610200016587011','6216610200016587012','6216610200016587013','6216610200016587014']
public_bank_name = ['中国银行','中国银行','中国银行','中国银行','中国银行']
business_scope = ['医疗护理','律师服务','安保服务','数据服务','航空航天']
legal_name = ['张三','李四','王五','赵六','赵一']
legal_id_card = ['110101199003077055','110101199003070657','110101199003073439','110101199003070879','110101199003070438']
legal_sex = ['male','female','male','female','male']
legal_card_number = ['6216610200016587020','6216610200016587021','6216610200016587022','6216610200016587023','6216610200016587024']
legal_mobile_no = ['13555555555','13555555556','13555555557','13555555558','13555555559']
core_enterprise_no = ['11111111','11111111','11111111','11111111','11111111']
core_enterprise_name = ['招东银行','招东律所','招东公安局','招东银行数据中心','招东航天']
core_enterprise_adress = ['上海市浦东区龙阳路','上海市浦东区龙阳路','上海市浦东区龙阳路','上海市浦东区龙阳路','上海市浦东区龙阳路']
phone = ['1366666666','1366666667','1366666668','1366666669','1366666610','1366666611']
email = ['1366666666@163.com','1366666667@163.com','1366666668@163.com','1366666669@163.com','1366666610@163.com','1366666611@163.com']
wechat = ['1366666666','1366666667','1366666668','1366666669','1366666610','1366666611']
dataList = []
for i in range(0,len(batch_no)):
    data = (
        (batch_no[i],personal_type[i],personal_no[i],personal_name[i],id_type[i],id_card[i],
         english_name[i],sex[i],birthday[i],nationality[i],language[i],nation[i],education[i],graduate_school[i],
        enrollment_time[i],graduation_time[i],income[i],id_card_address[i],mobile_no_address[i],
         ip_address[i],online_status[i],personal_rank[i],first_date[i],up_months[i],company_name[i],
         industry[i],company_type[i],occupation[i],marital[i],house_type[i],local_phone_area_code[i],
         local_phone[i],company_phone_area_code[i],company_phone[i],register_phone_area_code[i],
         register_phone[i],deposit_account_flag[i],wechat_no_flag[i],email_flag[i],risk_flag[i],lately_pay_date[i],
         lately_pay_amount[i],total_accounts[i],merge_accounts[i],net_interest_flag[i],delay_max_account_no[i],
         delay_max_account_type[i],history_max_overdue_stage[i],credit_code[i],org_code[i],texpayer_id[i],
         establishment_date[i],license_start_time[i],registered_capital[i],registration_time[i],public_bank_card_number[i],
         public_bank_name[i],business_scope[i],legal_name[i],legal_id_card[i],legal_sex[i],legal_card_number[i],
         legal_mobile_no[i],core_enterprise_no[i],core_enterprise_name[i],core_enterprise_adress[i],
         phone[i],email[i],wechat[i]
         )
    )
    dataList.append(data)
    sql = """insert into plc_personal_temp(
     batch_no, personal_type,personal_no, personal_name,id_type,id_card,english_name,sex,
    birthday,nationality,language,nation,education,graduate_school,enrollment_time, graduation_time,income,id_card_address,
    mobile_no_address,ip_address,online_status,personal_rank,first_date,up_months, company_name,industry,company_type,occupation,
    marital,house_type,local_phone_area_code,local_phone,company_phone_area_code,company_phone,register_phone_area_code,
    register_phone,deposit_account_flag, wechat_no_flag,email_flag,risk_flag, lately_pay_date,lately_pay_amount,
     total_accounts,merge_accounts,net_interest_flag,delay_max_account_no,delay_max_account_type, history_max_overdue_stage,
      credit_code,org_code,texpayer_id,establishment_date,license_start_time,registered_capital,
      registration_time,public_bank_card_number,public_bank_name,business_scope,legal_name, legal_id_card,
      legal_sex,  legal_card_number,legal_mobile_no,core_enterprise_no, core_enterprise_name,
     core_enterprise_adress,phone,email,  wechat
    ) values(
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s
    )"""
cursor.executemany(sql,dataList)
db.commit()





