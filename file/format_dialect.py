import re
count = 0
sql_file = open('L3_RZ_AOC_PRVW_GM_STU_ABSNC_DTL_DLY_RPT_F.sql')
#file_dta = sql_file.read()
all_lines = sql_file.readlines()
for line in all_lines:
    if(line.find('USING') != -1):
        break
    count += 1
    print(line.strip('\n'))
sql_file.close()
print(count)


sql_file2 = open('L3_RZ_AOC_PRVW_GM_STU_ABSNC_DTL_DLY_RPT_F.sql')
content = sql_file2.read()
new_content = re.sub('USING','WHERE {after_where_condition}',content,1)
sql_file2.close()

print(re.sub('=','IN',new_content))

new_lines = []
for line in all_lines:
    new_lines.append(line.strip('\n'))

print()



#tgt = file_dta.find('USING')
