from dataxJson.tableColumn import mysql_table_info
import json
from datetime import datetime
#自动生成datax-json
def datax_json(table_name,type):
    table_info = mysql_table_info(table_name)
    hdfs_column=[]
    for i in range(len(table_info[1])):
        if(table_info[2][i][0:3]=="int" or table_info[2][i][0:6]=="bigint"):
            hdfs_column.append({"name":table_info[1][i],"type":table_info[2][i]})
        else:
            hdfs_column.append({"name": table_info[1][i], "type": "string"})

    #读取示例json文件
    with open("dataxJson/example.json", "r") as file:
        json_data = file.read()

    data = json.loads(json_data)
    # hdfs
    if(type=="full"):
        path ="/user/hive/warehouse/shyl_ods.db/{table_name}_full/dt={date}".format(table_name=table_name,date=datetime.now().strftime("%Y-%m-%d"))
    elif(type=="inc"):
        path = "/user/hive/warehouse/shyl_ods.db/{table_name}_inc/dt={date}".format(table_name=table_name,date=datetime.now().strftime("%Y-%m-%d"))
    else:
        raise ValueError("Invalid value for 'type'. Expected 'full' or 'inc', got: {}".format(type))
    # hive
    # if(type=="full"):
    #     path ="/user/hive/warehouse/shyl_ods.db/{table_name}_full".format(table_name=table_name)
    # elif(type=="inc"):
    #     path = "/user/hive/warehouse/shyl_ods.db/{table_name}_inc".format(table_name=table_name)
    # else:
    #     raise ValueError("Invalid value for 'type'. Expected 'full' or 'inc', got: {}".format(type))

    data["job"]["content"][0]["reader"]["parameter"]["connection"][0]["table"]=[table_name]
    data["job"]["content"][0]["writer"]["parameter"]["column"]=hdfs_column
    data["job"]["content"][0]["writer"]["parameter"]["path"] = path

    # 输出到文件
    output_file = f"dataxjob/{table_name}_{type}.json".format(table_name=table_name,type=type)
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

    print("Modified data written to", output_file)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table_full=["activity_info","activity_rule","base_category1","base_category2","base_category3","base_dic","base_province","base_region"
        ,"base_trademark","cart_info","coupon_info","coupon_info","sku_attr_value","sku_sale_attr_value","sku_info","spu_info"]
    for e in table_full:
        datax_json(e,"full")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
