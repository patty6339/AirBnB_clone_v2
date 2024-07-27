This folder contains files for the project web_flask

### What is a Web Framework

A web framework is a software platform that provides a foundation and a set of tools for developing web applications. It streamlines the development process by offering standard solutions for common web development tasks, such as handling HTTP requests, managing sessions, and interacting with databases. Examples of web frameworks include Django, Flask, Ruby on Rails, and Spring.

### How to Build a Web Framework with Flask

1. **Install Flask**: Use `pip install Flask` to install Flask.
2. **Create a Flask Application**: 
   - Create a Python file (e.g., `app.py`).
   - Import Flask and initialize the app: 
     ```python
     from flask import Flask
     app = Flask(__name__)
     ```
3. **Define Routes**: Use the `@app.route` decorator to define routes.
4. **Run the Application**: Use `app.run()` to start the server.

### How to Define Routes in Flask

Routes in Flask are defined using the `@app.route` decorator. A route maps a URL to a function. For example:
```python
@app.route('/')
def home():
    return 'Hello, World!'
```
In this example, the function `home` is called when the root URL (`/`) is accessed.

### What is a Route

A route in a web framework is a mapping between a URL and a function or method that handles the request made to that URL. It defines what content or response should be provided when a specific URL is accessed.

### How to Handle Variables in a Route

Variables can be included in routes by using angle brackets. For example:
```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```
In this example, `<username>` is a variable that will capture the value passed in the URL.

### What is a Template

A template is a file that defines the structure and layout of a web page, typically written in HTML. Templates allow for dynamic content generation by embedding placeholders that can be replaced with actual data during rendering.

### How to Create an HTML Response in Flask by Using a Template

1. **Create a Template**: Save an HTML file in a `templates` directory (e.g., `templates/index.html`).
2. **Render the Template**:
   ```python
   from flask import render_template

   @app.route('/')
   def home():
       return render_template('index.html')
   ```

### How to Create a Dynamic Template (Loops, Conditions…)

Use Jinja2 syntax within your HTML templates to add loops, conditions, and other logic. For example:
```html
<!-- templates/index.html -->
<!doctype html>
<html>
<body>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% if user %}
        <p>Hello, {{ user }}!</p>
    {% else %}
        <p>Hello, Guest!</p>
    {% endif %}
</body>
</html>
```
In the corresponding route:
```python
@app.route('/')
def home():
    return render_template('index.html', items=['Apple', 'Banana', 'Cherry'], user='John')
```

### How to Display in HTML Data from a MySQL Database

1. **Install MySQL Connector**: Use `pip install mysql-connector-python`.
2. **Connect to the Database**:
   ```python
   import mysql.connector

   conn = mysql.connector.connect(
       host='localhost',
       user='yourusername',
       password='yourpassword',
       database='yourdatabase'
   )
   cursor = conn.cursor()
   ```
3. **Query the Database**:
   ```python
   cursor.execute('SELECT * FROM your_table')
   results = cursor.fetchall()
   ```
4. **Pass Data to Template**:
   ```python
   @app.route('/data')
   def data():
       cursor.execute('SELECT * FROM your_table')
       results = cursor.fetchall()
       return render_template('data.html', data=results)
   ```
5. **Display Data in Template**:
   ```html
   <!-- templates/data.html -->
   <!doctype html>
   <html>
   <body>
       <table>
           {% for row in data %}
           <tr>
               {% for item in row %}
               <td>{{ item }}</td>
               {% endfor %}
           </tr>
           {% endfor %}
       </table>
   </body>
   </html>
   ```
