var express = require('express');
var router = express.Router();

const pgp = require('pg-promise')(/* options */)
const db = pgp('postgres://postgres:postgres@db:5432/postgres')


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

/* GET users listing. */
router.get('/all', function(req, res, next) {
  db.many('SELECT * FROM users')
  .then((data) => {
    res.json(data);
  })
  .catch((error) => {
    console.log('ERROR:', error)
  })
});

module.exports = router;
