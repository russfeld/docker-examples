## JavaScript Example

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

Node Version: 18.10

```bash
cd server
npx express-generator --no-view
```

Delete `routes/index.js` file.

Install libraries, database library and CORS library

```bash
cd server
npm install
npm install pg-promise
npm install cors
```

Update `app.js` to match below:

```js
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors')

var usersRouter = require('./routes/users');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(cors())

app.use('/users', usersRouter);

module.exports = app;
```

Update `routes/users.js` to match below to query database:

```js
var express = require('express');
var router = express.Router();

const pgp = require('pg-promise')(/* options */)
const db = pgp('postgres://postgres:postgres@localhost:5432/postgres')


/* GET users listing. */
router.get('/', function(req, res, next) {
  db.many('SELECT * FROM users')
  .then((data) => {
    res.json(data);
  })
  .catch((error) => {
    console.log('ERROR:', error)
  })
});

module.exports = router;
```

Start server:

```bash
cd server
npm run start
```

Open web browser and navigate to https://localhost:3000/users to receive this output:

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
fetch('http://localhost:3000/users')
    .then(response => response.json())
    .then(data => users.value = data);
</script>

<template>
  <ul>
    <li v-for="user in users">{{ user.name }} ({{  user.eid }})</li>
  </ul>
</template>
```

Start client:

```bash
cd client
npm install
npm run dev
```

