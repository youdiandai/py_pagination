# py_pagination
通用的页面分页小工具
## 使用方法
1. 在需要分页的页面引入pagination.js和jquery.js
```html
    <script src="{{ url_for("static",filename="pagination.js") }}"></script>
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
```
2. 在页面编写表格
```html
<table id="table">
        <thead>
        <tr>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
        </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    <div>
        <div id="widget"></div>
    </div>
```
表格需要设置id (这里为设置为table)，并在需要放置导航栏的地方放置一个div，也需要设置id(这里设置为widget)

3. 在页面中创建一个JavaScript列表，列表的每一项为表格中每一项的名字，和Python中返回的item的属性对应
```javascript
var column_name = ['name','sex','age'];
```

4. 在页面中创建分页对象，并调用turnPage变量跳转到第一页以初始化表格
```javascript
    var pagination = new Pagination('/get_persons', column_name, 'table', 'widget', 'pagination');
    pagination.turnPage(1);
```
创建Pagination变量的第一个变量为请求数据的接口url，第二个变量为步骤3中创建的变量的，第三个变量为表格的id，第四个变量为导航栏DIV的id，第四项为该分页对象的名称

5. 编写接口路由
```python
@app.route('/get_persons', methods=['POST'])
def get_person():
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(_persons, page=page, per_page=10)
    return jsonify(pagination.get_dict())
```
在程序中引用pagination.py,并在路由中初始化模块中定义的Pagination类，该类接收三个参数，需要分页的数据的集合，页数，每页的元素个数
最后调用Pagination实例的get_dict方法，将结果作为json返回

## demo使用方法
需要python3

1. 创建虚拟环境
```
~/Documents/work/py_pagination/demo#virtualenv -p python3 venv
~/Documents/work/py_pagination/demo#pip install flask
~/Documents/work/py_pagination/demo#python app.py
```
2. 使用浏览器访问http://127.0.0.1:5000
