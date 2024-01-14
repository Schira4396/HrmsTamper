# HrmsTamper
👉适用于某EHR&amp;HRM的加解密工具，可直接用于sqlmap

​	逻辑来自https://github.com/vaycore/HrmsTool

​	原版是java写的，需要手动指定注入语句生成payload，太麻烦，于是写了个tamper

👉不需要放到sqlmap的tamper目录，直接在此目录使用即可，如下：

```python
sqlmap -u https://example.com/?code=1" -p "code" --tamper hrmsTamper.py
```

👉如果目标接口的加密方式不是DES，请修改hrmsTamper.py的tamper函数，把encryptEncode改为encodeSafe即可，如下：

```python
retVal = encryptEncode(payload) #注释掉
# 修改为以下：
retVal = encodeSafe(payload)
```

👉**免责声明**

本工具仅面向**合法授权**的企业安全建设行为，例如企业内部攻防演练、漏洞验证和复测，如您需要测试本工具的可用性，请自行搭建靶机环境。

在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。**请勿对非授权目标使用。**

如您在使用本工具的过程中存在任何非法行为，**您需自行承担相应后果**，我们将不承担任何法律及连带责任。
