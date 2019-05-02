var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const accountSid = process.env.Account_Sid; //account sid from twilio website
const authToken = process.env.Auth_Token; //get authecation token from twilio website
const client = require('twilio')(accountSid, authToken);

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

const ctrl = {
  'Up': 2,
  'Down' : 8,
  'Left' : 4,
  'Right' : 6,
  'Stop' : 5
};

var data = {
    ir: 0, 
    ultra: 0, 
    btn:2
};

var way = 0;
var chng = 0;

app.get('/', (req, res, next)=>{
	res.status(200).send("Happy Hacking");
});

//router for whatsapp messages 
app.post('/back',(req,res)=>{
    const temp = req.body.Body;
    data.btn = ctrl[temp];
	client.messages
	      .create({
	        body: `${temp} is set\nHAPPY HACKING\n:)`,
	        from: 'whatsapp:+14155238886',
	        to: 'whatsapp:+918930154773'
	      })
	      .then(message => console.log(message.body))
	      .done();      
});

app.post("/rpi", (req,res)=>{
  res.json(data);
});


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;