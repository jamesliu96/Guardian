Guardian 光腚·总菊
======

Introduction 介绍
------

This app will definitely make the 'Guardian always asshole' happy.

为响应国家号召，创造文明社会，将影像胸部及以下部分彻底截掉。

Demonstration 示例
------

![1.png](https://raw.githubusercontent.com/jamesliu96/Guardian/master/demo/1.png)

![2.png](https://raw.githubusercontent.com/jamesliu96/Guardian/master/demo/2.png)

![3.png](https://raw.githubusercontent.com/jamesliu96/Guardian/master/demo/3.png)

How To 用法
------

### Simple Usage

1. [Sign up](http://www.faceplusplus.com/uc/people/signup) or use your [existing Face++ account](http://www.faceplusplus.com/uc/people/login).
2. [Create a Face++ App](http://www.faceplusplus.com/create-a-new-app/).
3. Copy the `API Key` and `API Secret` into `guardian.cfg`
```Python
API_KEY = "<your face++ api key here>"
API_SECRET = "<your face++ api secret here>"
```
4. You can switch to use the server in China mainland (Aliyun) by uncommenting `# SERVER = "http://api.cn.faceplusplus.com/"`.
5. Install the requirements by simply run `sudo pip install -r requirements.txt`.
6. Run `python guardian.py test/*` to test or run with your own images `python guardian.py your_image.jpg`.

### 简单用法

1. [注册](http://www.faceplusplus.com.cn/uc/people/signup)或[登录](http://www.faceplusplus.com/uc/people/login) Face++ 账号
2. [创建一个 Face++ App](http://www.faceplusplus.com.cn/create-a-new-app/)
3. 拷贝`API Key`和`API Secret`进`guardian.cfg`
```Python
API_KEY = "<your face++ api key here>"
API_SECRET = "<your face++ api secret here>"
```
4. 你可以去掉`# SERVER = "http://api.cn.faceplusplus.com/"`的注释以使用位于中国大陆的Face++的服务器（阿里云）
5. 运行`sudo pip install -r requirements.txt`以安装所依赖的库
6. 运行`python guardian.py test/*`或使用你自己的图片`python guardian.py your_photo.jpg`来测试

### Advanced usage

See details in `guardian.py` and `guardian.cfg` (LAZY am I ╮(╯▽╰)╭).

### 进阶用法

请读代码`guardian.py`与`guardian.cfg`（懒得写了 ╮(╯▽╰)╭）

Acknowledgements 鸣谢
------

![Face++ inside](https://raw.githubusercontent.com/jamesliu96/Guardian/master/facepp_inside.png)

License
------

The MIT License (MIT)

Copyright (c) 2015 James Liu \<j@jamesliu.info\>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
