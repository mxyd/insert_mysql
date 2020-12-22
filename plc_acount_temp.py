# 2020/12/22
# author:xieyudong
import pymysql
import datetime
db = pymysql.connect(host='117.36.75.166', port=3506,user='root',passwd='123456',db='zdbk_dev',charset='utf8')
cursor = db.cursor()
batch_no = ['10000003','10000002','10000003','10000004','10000005']
personal_no =[1003,1002,1002,2003,2002]
product_type = ['房产','房产','房产','汽车','汽车']
product_no = ['HO','HO','HO','PR','PR']
product_channel = ['房产渠道','房产渠道','房产渠道','汽车渠道','汽车渠道']
account_no = ['HO1003','HO1002','HO1003','PR2001','PR2002']
reason_code = ['DELAY','DELAY','DELAY','RELATION','RELATION']
bill_date = ['2020-11-06','2020-11-06','2020-11-06','2020-11-06','2020-11-06']
pay_date = ['2020-10-15','2020-10-15','2020-10-15','2020-10-15','2020-10-15']
pre_bill_date = ['2020-10-06','2020-10-06','2020-10-06','2020-10-06','2020-10-06']
next_bill_date = ['2020-12-06','2020-12-06','2020-12-06','2020-12-06','2020-12-06']
pre_pay_date = ['2020-10-15','2020-10-15','2020-10-15','2020-10-15','2020-10-15']
next_pay_date = ['2020-12-15','2020-12-15','2020-12-15','2020-12-15','2020-12-15']
overdue_stage = ['M1','M5','M1','M3','M10']
repay_rating = ['优','优','优','优','优']
overdue_loans = [1,1,1,1,1]
deduction_card_number = ['6216610200036587035','6216610200036587036','6216610200036587038','6216610200036587039','6216610200036587020']
deduction_card_bank = ['中国银行','中国银行','中国银行','中国银行','中国银行']
deduction_card_flag = ['是','是','是','是','是']
replace_card_number = ['6216610200036587021','6216610200036587022','6216610200036587022','6216610200036587024','6216610200036587025']
monitor_flag = ['有变动','有变动','有变动','有变动','有变动']
risk_control_code = ['N001','N002','N003','N004','N005']
risk_control_update_time = [
    datetime.datetime.strptime('2020-04-08','%Y-%m-%d'),
    datetime.datetime.strptime('2020-04-08','%Y-%m-%d'),
    datetime.datetime.strptime('2020-04-08','%Y-%m-%d'),
    datetime.datetime.strptime('2020-04-08','%Y-%m-%d'),
    datetime.datetime.strptime('2020-04-08','%Y-%m-%d'),
]
pre_risk_control_code = ['PR001','PR002','PR003','PR004','PR005']
pre_risk_control_update_time = [
    datetime.datetime.strptime('2020-05-08', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-05-08', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-05-08', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-05-08', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-05-08', '%Y-%m-%d'),
]
risk_status = ['有风险','有风险','有风险','有风险','有风险','有风险']
risk_status_update_date = ['2020-06-08','2020-06-08','2020-06-08','2020-06-08','2020-06-08']
risk_status_update_agent = ['王柳','王柳','王柳','王柳','王柳']
risk_status_update_reason = ['长时间未还款','长时间未还款','长时间未还款','长时间未还款','长时间未还款']
plan_balance = [1000.03,1000.03,1000.03,1000.03,1000.03]
case_money = [1000,20000,1000,2000,400000]
small_amount_flag = ['小','小','小','小','小']
capital_balance = [8080,4220,1060.99,8892.98,12522.09]
interest_balance = [100.05,100,100.05,100,100.05]
fine_balance = [50.05,50,50.05,50,50.05]
compound_balance = [50.05,50,50.05,50,50.05]
other_fee_balance =[10.05,10,10.05,10,10.05]
should_repay_amount = [2000.99,20003.99,2666.998,17654.987,119999.99]
min_should_repay_amount = [1000.99,10003.99,666.998,7654.987,99999.99]
overdue_amount = [2000,10003.99,2000,10000,20000]
min_overdue_amount = [100,1000,200,1000,2000]
overdue_capital = [1000,5000,1000.03,5000,1000]
overdue_interest = [1000,5000,1000.03,5000,1000]
overdue_fine = [500,2500,500,2500,500]
overdue_compound =  [500,2500,500,2500,500]
overdue_other_fee = [1.03,1.03,1.03,1.03,1.03]
m1_amount= [285,1428.85,2000,95,28,1092.56,14285.71]
m2_amount  = [571.42,2856.85,190.56,2187.12,28571.42]
m3_amount  = [829.42,4284.85,285.84,2280.68,42875.12]
m4_amount  = [1114.42,5712.85,281.12,4274.24,57142.84]
m5_amount  = [1684.42,7140.85,476.40,5467.8,71428.55]
m6_amount  = [1969.42,8592.85,571.68,6561.26,85714.26]
after_m6_amount  = [2000,10003.99,666.998,7654.987,99999.99]
lately_pay_date = [
    datetime.datetime.strptime('2020-11-15', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-11-15', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-11-15', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-11-15', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-11-15', '%Y-%m-%d'),
]
lately_pay_amount = [1000.91,1000.91,1000.91,1000.91,1000.91]
net_interest_flag = ['无','无','无','无','无']
history_max_overdue_stage = ['M12','M12','M12','M12','M12']
history_max_overdue_stage_flag = ['最高','最高','最高','最高','最高']
history_max_overdue_amount = [66666.19,66666.19,66666.19,66666.19,66666.19,]
total_loans = [5,5,5,5,5]
balance_loans = [5,5,5,5,5]
delay_loans = [5,5,5,5,5]
first_overdue_m2_date = [
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
]
first_overdue_m2_amount = [2000.09,2000.09,2000.09,2000.09,2000.09]
first_overdue_m3_date = [
    datetime.datetime.strptime('2020-02-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-03', '%Y-%m-%d'),
]
first_overdue_m3_amount = [2000.09,2000.09,2000.09,2000.09,2000.09]
first_overdue_m7_date = [
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
]
first_overdue_m7_amount = [10000.09,10000.09,10000.09,10000.09,10000.09]
overdue_days = ['20','150','20','90','200']
guaranty_type = ['房产','房产','房产','汽车','汽车']
guaranty = ['房产','房产','房产','汽车','汽车']
guarantee_name = ['王依依','王依依','王依依','王依依','王依依']
guarantee_id_card = ['610321198911046524','610321198911046525','610321198911046526','610321198911046527','610321198911046528',]
guarantee_no = ['9999990','9999991','9999992','9999992','9999994']
guarantee_phone = ['12099999999','12099999998','12099999997','12099999996','12099999995','12099999994']
guarantee_adress = ['上海龙阳路','上海龙阳路','上海龙阳路','上海龙阳路','上海龙阳路']
quaranty_limit = [10000.998,10000.998,10000.998,10000.998,10000.998]
contract_number = ['SQ0003','SQ0002','SQ0002','SQ0004','SQ0005']
credit_limit = [8989.003,8989.003,8989.003,8989.003,8989.003]
current_limit = [8989.003,8989.003,8989.003,8989.003,8989.003]
used_limit = [8989.003,8989.003,8989.003,8989.003,8989.003]
available_limit = [0.00,0.00,0.00,0.00,0.00]
should_repay_limit_rate = [100,100,100,100,100]
total_limit_rate = [100,100,100,100,100]
first_use_date = [
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
]
history_delay_flag = ['是','是','是','是','是']
half_year_repay_times = [1,2,1,11,1,10]
first_m7_months = [2,5,7,9,11]
out_days = [10,15,15,15,15]
out_date_stage = ['2020-12-15','2020-12-15','2020-12-15','2020-12-15','2020-12-15']
no_repay_flag = ['是','是','是','是','是']
afterm6amount = [0.03,0.03,0.03,0.03,0.03]
firstm7months = [2,5,7,9,11]
first_overduem2amount = [2000.09,2000.09,2000.09,2000.09,2000.09]
first_overduem2date = [
    datetime.datetime.strptime('2020-02-01', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-01', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-01', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-01', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-02-01', '%Y-%m-%d'),
]
first_overduem3amount = [2000.09,2000.09,2000.09,2000.09,2000.09]
first_overduem3date = [
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-03-03', '%Y-%m-%d'),
]
first_overduem7amount = [10000.09,10000.09,10000.09,10000.09,10000.09]
first_overduem7date = [
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
    datetime.datetime.strptime('2020-07-03', '%Y-%m-%d'),
]
m1amount  = [285,1428.85,2000,95,28,1093.56,14285.71]
m2amount  = [571.42,2856.85,190.56,2187.12,28571.42]
m3amount  = [829.42,4284.85,285.84,3280.68,42875.13]
m4amount  = [1114.42,5712.85,381.12,4374.24,57142.84]
m5amount  = [1684.42,7140.85,476.40,5467.8,71428.55]
m6amount  = [1969.42,8592.85,571.68,6561.36,85714.26]
dataList = []
for i in range(0,len(batch_no)):
    data = (
        (
            batch_no[i],
            personal_no[i],
            product_type[i],
            product_no[i],
            product_channel[i],
            account_no[i],
            reason_code[i],
            bill_date[i],
            pay_date[i],
            pre_bill_date[i],
            next_bill_date[i],
            pre_pay_date[i],
            next_pay_date[i],
            overdue_stage[i],
            repay_rating[i],
            overdue_loans[i],
            deduction_card_number[i],
            deduction_card_bank[i],
            deduction_card_flag[i],
            replace_card_number[i],
            monitor_flag[i],
            risk_control_code[i],
            risk_control_update_time[i],
            pre_risk_control_code[i],
            pre_risk_control_update_time[i],
            risk_status[i],
            risk_status_update_date[i],
            risk_status_update_agent[i],
            risk_status_update_reason[i],
            plan_balance[i],
            case_money[i],
            small_amount_flag[i],
            capital_balance[i],
            interest_balance[i],
            fine_balance[i],
            compound_balance[i],
            other_fee_balance[i],
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
            lately_pay_date[i],
            lately_pay_amount[i],
            net_interest_flag[i],
            history_max_overdue_stage[i],
            history_max_overdue_stage_flag[i],
            history_max_overdue_amount[i],
            total_loans[i],
            balance_loans[i],
            delay_loans[i],
            first_overdue_m2_date[i],
            first_overdue_m2_amount[i],
            first_overdue_m3_date[i],
            first_overdue_m3_amount[i],
            first_overdue_m7_date[i],
            first_overdue_m7_amount[i],
            overdue_days[i],
            guaranty_type[i],
            guaranty[i],
            guarantee_name[i],
            guarantee_id_card[i],
            guarantee_no[i],
            guarantee_phone[i],
            guarantee_adress[i],
            quaranty_limit[i],
            contract_number[i],
            credit_limit[i],
            current_limit[i],
            used_limit[i],
            available_limit[i],
            should_repay_limit_rate[i],
            total_limit_rate[i],
            first_use_date[i],
            history_delay_flag[i],
            half_year_repay_times[i],
            first_m7_months[i],
            out_days[i],
            out_date_stage[i],
            no_repay_flag[i],
            afterm6amount[i],
            firstm7months[i],
            first_overduem2amount[i],
            first_overduem2date[i],
            first_overduem3amount[i],
            first_overduem3date[i],
            first_overduem7amount[i],
            first_overduem7date[i],
            m1amount[i],
            m2amount[i],
            m3amount[i],
            m4amount[i],
            m5amount[i],
            m6amount[i],
        )
    )
    dataList.append(data)
    sql = """ insert into plc_account_temp(
        batch_no,
        personal_no,
        product_type,
        product_no,
        product_channel,
        account_no,
        reason_code,
        bill_date,
        pay_date,
        pre_bill_date,
        next_bill_date,
        pre_pay_date,
        next_pay_date,
        overdue_stage,
        repay_rating,
        overdue_loans,
        deduction_card_number,
        deduction_card_bank,
        deduction_card_flag,
        replace_card_number,
        monitor_flag,
        risk_control_code,
        risk_control_update_time,
        pre_risk_control_code,
        pre_risk_control_update_time,
        risk_status,
        risk_status_update_date,
        risk_status_update_agent,
        risk_status_update_reason,
        plan_balance,
        case_money,
        small_amount_flag,
        capital_balance,
        interest_balance,
        fine_balance,
        compound_balance,
        other_fee_balance,
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
        lately_pay_date,
        lately_pay_amount,
        net_interest_flag,
        history_max_overdue_stage,
        history_max_overdue_stage_flag,
        history_max_overdue_amount,
        total_loans,
        balance_loans,
        delay_loans,
        first_overdue_m2_date,
        first_overdue_m2_amount,
        first_overdue_m3_date,
        first_overdue_m3_amount,
        first_overdue_m7_date,
        first_overdue_m7_amount,
        overdue_days,
        guaranty_type,
        guaranty,
        guarantee_name,
        guarantee_id_card,
        guarantee_no,
        guarantee_phone,
        guarantee_adress,
        quaranty_limit,
        contract_number,
        credit_limit,
        current_limit,
        used_limit,
        available_limit,
        should_repay_limit_rate,
        total_limit_rate,
        first_use_date,
        history_delay_flag,
        half_year_repay_times,
        first_m7_months,
        out_days,
        out_date_stage,
        no_repay_flag,
        afterm6amount,
        firstm7months,
        first_overduem2amount,
        first_overduem2date,
        first_overduem3amount,
        first_overduem3date,
        first_overduem7amount,
        first_overduem7date,
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
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s)
    """
cursor.executemany(sql,dataList)
db.commit()