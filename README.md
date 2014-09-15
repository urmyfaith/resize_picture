## 需求

> 经常可能有需要压缩图片的需求.

> 但是一些批量处理图片的软件又仅仅支持压缩一个目录下的图片,

> 所以写下了这个图片处理程序:

**需要安装**:

* python 2.x

* Image模块

**特点:**

* 压缩当前目录,子目录图片

* 每次压缩,宽度,高度减半

* 支持中文目录.

----


## **压缩文件的思路:**

1>.遍历当前目录,

* 确定当前目录路径

* 确定当前目录所包含的图片

2>. 处理当前目录下的图片

3>. 记录处理结果.


## 代码实现:

```python
# -*- coding: utf-8 -*-

import Image
import os
import os.path
import sys
import time

fp=open('log.info','a+')
path=os.path.dirname(__file__)
time_now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

i=1
for  root, dirs,files in os.walk(path):
    current_dir=root 
    if not len(files):
        pass
    else:
        k=1
        for f in files:
            if f.endswith('.jpg') :
                filepath = os.path.join(current_dir,f)
                total_number = "%03d" % i
                file_in_dir_number = "%03d" % k
                i = i+1
                k = k+1
                try:   
                    img = Image.open(filepath)
                    w,h = img.size
                    img.resize((w/2,h/2)).save(filepath,"JPEG")
                    log_info=str(total_number)+"\t"+"SMALLSIZE\t"+current_dir+"\t"+ \
                              file_in_dir_number+"\t"+f+"\t"+str(w)+"\t"+str(h)+ \
                              "\tSUCESS\t"+str(w/2)+"\t"+str(h/2)+"\t"+time_now
                except:
                    log_info=str(total_number)+"\t"+"SMALLSIZE\t"+current_dir \
                              +"\t"+file_in_dir_number+"\t"+f+"\t"+"width"+"\t"+"height" \
                              +"\tSUCESS\t"+"width_s"+"\t"+"height_s"+"\t"+time_now
                fp.write(log_info+"\n")
fp.close()

```


##测试的文件夹目录:

**D:\desktop\demo**
```python
D:\desktop\demo\
|   IMG_4342.jpg
|   IMG_4343.jpg
|   resizeV_SUCESS.py
|
+---AAA
|       IMG_4599.jpg
|       IMG_4600.jpg
|
+---BBB
|   |   IMG_4309.jpg
|   |   IMG_4310.jpg
|   |   IMG_4311.jpg
|   |
|   \---BBB1111
|           IMG_4323.jpg
|           IMG_4324.jpg
|
\---CCC
    |   IMG_1715.JPG
    |   IMG_1716.JPG
    |
    \---CCC111
        |   IMG_1447.JPG
        |   IMG_1448.JPG
        |
        \---CCC222
                IMG_0792.JPG
                IMG_0793.JPG
```

python文件所在目录为"**D:\desktop\demo\**"

文件所在目录图片

一级子目录AAA下图片

二级子目录BBB,BBB1111下图片

三级子目录CCC,CCC111,CCC222下图片.

## 测试结果:
测试的文件目录

![test-py-file-tree.png](https://raw.githubusercontent.com/urmyfaith/resize_picture/master/images/test-py-file-tree.png)

测试前照片大小

![file_size_befor_test.png](https://raw.githubusercontent.com/urmyfaith/resize_picture/master/images/file_size_befor_test.png)

测试后照片大小

![file_size_after_resize.png](https://raw.githubusercontent.com/urmyfaith/resize_picture/master/images/file_size_after_resize.png)

生产的log.info查看

![log_info.png](https://raw.githubusercontent.com/urmyfaith/resize_picture/master/images/log_info.png)


## 另外,文件支持中文目录

