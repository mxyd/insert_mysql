# 2020/12/22
# author:xieyudong
import pymysql
import datetime
db = pymysql.connect(host='117.36.75.166', port=3506,user='root',passwd='123456',db='zdbk_dev',charset='utf8')
cursor = db.cursor()
batch_type = ['DAY','NIGHT','DAY','NIGHT','DAY']
batch_status = ['PUSH_FINISH','READ_FINISH','PUSH_FINISH','READ_FINISH','PUSH_FINISH']
batch_no = ['10000001','10000002','10000003','10000004','10000005']
created_time = [
    datetime.datetime.strptime('2020-12-01','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-01','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-01','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-01','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-01','%Y-%m-%d'),
]
modified_time = [
    datetime.datetime.strptime('2020-12-12','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-12','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-12','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-12','%Y-%m-%d'),
    datetime.datetime.strptime('2020-12-12','%Y-%m-%d'),
]
dataList = []
for i in range(0,len(batch_type)):
    data = (
        (
            batch_type[i],
            batch_status[i],
            batch_no[i],
            created_time[i],
            modified_time[i]
        )
    )
    dataList.append(data)
    sql = 'insert into plc_push_record(batch_type,batch_status,batch_no,created_time,modified_time)values(%s,%s,%s,%s,%s)'
cursor.executemany(sql, dataList)
db.commit()