# 2020/12/22
# author:xieyudong

import pymysql
db = pymysql.connect(host='117.36.75.166', port=3506,user='root',passwd='123456',db='zdbk_dev',charset='utf8')
cursor = db.cursor()
account_no = ['HO1001','HO1002','HO1003','PR2001','PR2002']
reason_code = ['DELAY','DELAY','DELAY','RELATION','RELATION']
batch_no = ['10000001','10000002','10000003','10000004','10000005']
personal_no = [1001,1002,1003,2001,2002]
product_no = ['HO','HO','HO','PR','PR']
product_version = ['1.0.0','1.0.0','1.0.0','1.0.0','1.0.0']
loan_no = ['HO100100001','HO100100002','HO100100003','PR200100001','PR200100002']
contract_number = ['CHO100100001','CHO100100002','CHO100100003','CPR200100001','CPR200100002']
loan_date = ['2019-01-01','2019-01-01','2019-01-01','2019-01-01','2019-01-01']
loan_capital = [1000.99,10001.99,666.998,7654.987,99999.99]
total_periods = [1,5,1,3,10]
loan_term = ['一个月','五个月','一个月','三个月','十个月']
no_repay_capital = [500.99,5001.99,200.998,3550.987,45000.09]
repaid_capital = [500,5000,466,4104,54999.9]
overdue_stage = ['M1','M5','M1','M3','M10']
overdue_days = ['30','150','30','90','300']
should_repay_amount = [3000.99,20001.99,2666.998,17654.987,119999.99]
min_should_repay_amount = [1000.99,10001.99,666.998,7654.987,99999.99]
overdue_amount = [2000,10001.99,2000,10000,20000]
min_overdue_amount = [100,1000,200,1000,2000]
overdue_capital = [1000,5000,1000.01,5000,1000]
overdue_interest  = [1000,5000,1000.01,5000,1000]
overdue_fine  = [500,2500,500,2500,500]
overdue_compound  = [500,2500,500,2500,500]
overdue_other_fee  = [1.01,1.01,1.01,1.01,1.01]
m1_amount  = [285,1428.85,2000,95,28,1093.56,14285.71]
m2_amount  = [571.42,2856.85,190.56,2187.12,28571.42]
m3_amount  = [829.42,4284.85,285.84,3280.68,42875.13]
m4_amount  = [1114.42,5712.85,381.12,4374.24,57142.84]
m5_amount  = [1684.42,7140.85,476.40,5467.8,71428.55]
m6_amount  = [1969.42,8592.85,571.68,6561.36,85714.26]
after_m6_amount  = [2000,10001.99,666.998,7654.987,99999.99]
afterm6amount  = [2000,10001.99,666.998,7654.987,99999.99]
m1amount  = [285,1428.85,2000,95,28,1093.56,14285.71]
m2amount  = [571.42,2856.85,190.56,2187.12,28571.42]
m3amount  = [829.42,4284.85,285.84,3280.68,42875.13]
m4amount  = [1114.42,5712.85,381.12,4374.24,57142.84]
m5amount  = [1684.42,7140.85,476.40,5467.8,71428.55]
m6amount  = [1969.42,8592.85,571.68,6561.36,85714.26]
datalist = []
for i in range(0,len(account_no)):
    data = (
        (
        account_no[i],
        reason_code[i],
        batch_no[i],
        personal_no[i],
        product_no[i],
        product_version[i],
        loan_no[i],
        contract_number[i],
        loan_date[i],
        loan_capital[i],
        total_periods[i],
        loan_term[i],
        no_repay_capital[i],
        repaid_capital[i],
        overdue_stage[i],
        overdue_days[i],
        should_repay_amount[i],
        min_should_repay_amount[i],
        overdue_amount[i],
        min_overdue_amount[i],
        overdue_capital[i],
        overdue_interest[i],
        overdue_fine[i],
        overdue_compound[i],
        overdue_other_fee[i],
        m1_amount[i],
        m2_amount[i],
        m3_amount[i],
        m4_amount[i],
        m5_amount[i],
        m6_amount[i],
        after_m6_amount[i],
        afterm6amount[i],
        m1amount[i],
        m2amount[i],
        m3amount[i],
        m4amount[i],
        m5amount[i],
        m6amount[i]
        )
    )
    datalist.append(data)

    sql = """insert into plc_loan_temp(
        account_no,
        reason_code,
        batch_no,
        personal_no,
        product_no,
        product_version,
        loan_no,
        contract_number,
        loan_date,
        loan_capital,
        total_periods,
        loan_term,
        no_repay_capital,
        repaid_capital,
        overdue_stage,
        overdue_days,
        should_repay_amount,
        min_should_repay_amount,
        overdue_amount,
        min_overdue_amount,
        overdue_capital,
        overdue_interest,
        overdue_fine,
        overdue_compound,
        overdue_other_fee,
        m1_amount,
        m2_amount,
        m3_amount,
        m4_amount,
        m5_amount,
        m6_amount,
        after_m6_amount,
        afterm6amount,
        m1amount,
        m2amount,
        m3amount,
        m4amount,
        m5amount,
        m6amount
    )values(
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s
         )
    """
cursor.executemany(sql,datalist)
db.commit()