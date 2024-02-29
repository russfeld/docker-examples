## Python Example

### Database

Start database container

```bash
docker compose up -d
```

Restore data

```bash
docker exec -i postgres psql -U postgres postgres < database.sql
```

### Server

Python version: 3.10.12
Pipx version: 1.4.3
Poetry version: 1.8.1

Create server project

```bash
poetry new server
```

Install Flask and psycopg2

```bash
cd server
poetry add flask
poetry add psycopg2-binary
```

Update `server/server/__init__.py` to contain a Flask app

```py3
from flask import Flask,jsonify,render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__,
            static_url_path='', 
            static_folder='../public',
            template_folder='../public')

@app.route("/users")
def get_users():
    conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "postgres",
                            port = 5432)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return jsonify(rows)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template("index.html")

```

Create the folder `server/public` and add a simple `index.html` file there for testing


Test Server:

```bash
cd server
poetry run flask --app server run --debug --port=5001
```

Open web browser and navigate to http://localhost:5001/users to receive this output:

```json
[{"id":1,"name":"Russell Feldhausen","eid":"russfeld"},{"id":2,"name":"Nathan Bean","eid":"nhbean"},{"id":3,"name":"Josh Weese","eid":"weeser"}]
```

### Client

Leave server running in a terminal and open another to work on client.

Create Vue 3 project:

```bash
 npm create vue@latest
```

Use "client" as the project name, accept all defaults. 

Replace `App.vue` with the following:

```vue
<script setup>
import { ref } from 'vue';
const users = ref(null);
fetch('http://localhost:5001/users')
    .then(response => response.json())
    .then(data => users.value = data);
</script>

<template>
  <ul>
    <li v-for="user in users">{{ user.name }} ({{  user.eid }})</li>
  </ul>
</template>
```

Update `build` command in `package.json` to output to server folder:

```js
"scripts": {
    "dev": "vite",
    "build": "vite build --emptyOutDir --outDir ../server/public",
    "preview": "vite preview"
  },
```

Start client:

```bash
cd client
npm install 
npm run dev
```

Open the client at http://localhost:5173 in a webpage to see a list of users like the following:

* Russell Feldhausen (russfeld)
* Nathan Bean (nhbean)
* Josh Weese (weeser)

If it works, build the client and restart the server:

```bash
cd client
npm run build
```

```bash
cd server
npm run start
```

You should now be able to visit http://localhost:5001 to see the frontend working correctly. 