import json


def getArrItem(json_dict):

    json_str = json.loads(json_dict)
    courseIds = json_str['courseIds']
    resList= []
    for courseId in courseIds:
        resList.append(courseId)
    return resList

json_str = getArrItem('{"dictType": 202, "courseIds": ["1904", "1909", "2024", "2026", "2027", "2028", "2029", "2187"], "categoryIds": ["198"], "productUuid": "2002020042014230062185", "propertyKey": "6", "propertyDesc": "随堂练习平台"}')
print(json_str)


CREATE OR REPLACE FUNCTION "edw_alo7"."getArrElement"(target_json varchar,column_Name varchar)
      RETURNS "pg_catalog"."varchar" AS $BODY$
        import json
        json_str = json.loads(target_json)
        try:
            arrItems = json_str[column_Name]
            for item in arrItems:
                return item
      $BODY$
      LANGUAGE plpythonu STABLE