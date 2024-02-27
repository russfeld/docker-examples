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

Delete `routes/index.js` file and lines `var indexRouter = require('./routes/index');` and `app.use('/', indexRouter);` from `app.js`

Install database library

```bash
cd server
npm install pg-promise
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

```
cd server
npm run start
```

Open web browser and navigate to https://localhost:3000/users to receive this output:

```json
[{"id":1,"name":"Russell Feldhausen","eid":"russfeld"},{"id":2,"name":"Nathan Bean","eid":"nhbean"},{"id":3,"name":"Josh Weese","eid":"weeser"}]
```
