#!/bin/bash
pth1=`find / -name ttf`
pth2=${pth1}"/msyh.ttf"
echo "当前文字目录为：$pth2"
 if [ ! -e "$pth2" ]; then
     cp msyh.ttf $pth1
    cp msyh.ttf /usr/share/fonts
    echo '复制完成' 
 else 
    echo "字体文件已存在"
    echo "或者请手动检查文件是否复制成功"

    for file_a in ${pth1}/*  
        do  
        temp_file=`basename $file_a`  
        echo $temp_file  
    done  

 fi 
pth3=`find / -name matplotlibrc`
echo "mat字体配置文件：===========$pth3"
echo "删除字体配置文件中的注释"
sed -i 's/#font.family/font.family/g' $pth3
sed -i 's/#font.sans-serif     :/font.sans-serif     :Microsoft YaHei,/g' $pth3
echo "删除成功"
pth4=`find / -name fontList.py3k.cache`
if [ ! -e "$pth4" ]; then
    echo "缓存文件不存在"
    echo "删除非标准缓存文件"
    rm -rf ~/.matplotlib/*.cache
 else 
 echo "查找到mat缓存文件正在删除" 
    rm -rf $pth4
    echo "删除成功" 
    
fi     

