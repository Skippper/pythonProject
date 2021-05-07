import csv

import re

# 格式化文件,处理数据
# file = pd.read_csv('/Users/saybot/Downloads/student_info (1).csv',header=1,usecols=[8])

file_path = '/Users/saybot/Downloads/student_info (1).csv'
target_path = '/Users/saybot/Downloads/process_dta.csv'


def process_file(file_path, target_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        with open(target_path, mode='w') as f:
            field_names = ['爱乐号',
                           '昵称',
                           '中文名',
                           '性别',
                           '班级号',
                           '班级名',
                           '课程名',
                           '学校名',
                           '带班教师',
                           '历史学习总时间'
                           '当月周在线时长',
                           '周完成率',
                           '周正确率',
                           '总做题数',
                           '本月做题数',
                           '历史智慧屋学习时长',
                           '本月智慧屋学习时长',
                           '本月登陆次数',
                           '读书总次数',
                           '本月读书次数',
                           '会员到期时间'
                           ]
            writer = csv.DictWriter(f, fieldnames=field_names)
            for row in spamreader:
                line = row[8]
                line_dta = line.replace('\n', '').strip()
                ifmatches = re.match(".*[0-9]{11,}", line_dta)
                if ifmatches:
                    str_arr = line_dta.split('|')
                    res_str = ''
                    for item in range(len(str_arr)):

                        for process_str_cnt in range(len(str_arr[item].split(','))):

                            if process_str_cnt != len(str_arr[item].split(',')) - 1:
                                res_str += str_arr[item].split(',')[process_str_cnt].split('(')[0] + '(' + \
                                           str_arr[item].split(',')[process_str_cnt].split('(')[1][0:3] + \
                                           '****' + str_arr[item].split(',')[process_str_cnt].split('(')[1][7:] + ','
                            else:
                                res_str += str_arr[item].split(',')[process_str_cnt].split('(')[0] + '(' + \
                                           str_arr[item].split(',')[process_str_cnt].split('(')[1][0:3] + \
                                           '****' + str_arr[item].split(',')[process_str_cnt].split('(')[1][7:]
                        if item != len((str_arr)) - 1:
                            res_str += '|'
                    row[8] = res_str
                res_dict = {}
                for num in range(len(field_names)):
                    res_dict[field_names[num]] = row[num]

                writer.writerow(res_dict)


if __name__ == '__main__':
    print("正在处理文件 " + file_path)
    process_file(file_path=file_path, target_path=target_path)
    print("处理完成,处理后的文件在 " + target_path)
