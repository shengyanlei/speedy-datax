# speedy-datax
#### datax的二次开发及json生成:  
1. mysqlreader，mysqlwriter，修改mysql的版本及驱动，支持mysql8.0版本  
2. hdfswriter 添加写入hdfs时，目录不存在自动创建【注：需要用户有指定目录的创建权限】  
3. dataxCodeGeneration为使用python便捷生成指定datax-json文件【使用场景：mysqlreader-->hdfswriter】  
    后续拓展，添加exanple.json文件,添加需要修改的得逻辑
