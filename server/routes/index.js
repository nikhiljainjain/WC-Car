const express = require('express');
const router = express.Router();
const accountSid = process.env.Account_Sid; //account sid from twilio website
const authToken = process.env.Auth_Token; //get authecation token from twilio website
const client = require('twilio')(accountSid, authToken);

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

//router for whatsapp messages 
router.post('/back',(req,res)=>{
    const temp = req.body.Body; 
    //let msg = `${temp} is set`;
    
    if (temp === 'Up' || temp === 'Down'){
      data.btn = ctrl[temp];
      //chng = 1;
    }else if (temp === 'Left' || temp === 'Right'){
      data.btn = ctrl[temp];
      //chng = 1;
    }/*else if (temp == 'Ir'){
      data.ir = way%2;
      data.ultra = (way+1)%2;
      chng = 1;
    }else if (temp == 'Ultra'){
      data.ir = way%2;
      data.ultra = (way+1)%2;
      chng = 1;
    }else if (chng == 0){
      //this part can integrate with diglow flow
      msg = 'How can I help you';
    }*/
    
    client.messages
          .create({
            body: `${temp} is set`,
            from: 'whatsapp:+14155238886',
            to: 'whatsapp:+918930154773'
          })
          .then(message => console.log(message.body))
          .done();      
    /*
    //this var is usefull when working with IR & utlra sonic sensor with rpi
    way++;
    //chng var will change if the message recevie contain any direction or
    //instruction for IR/UTLRASONIC sensor
    chng = 0;*/
});

//response data back to rasberry pi
router.post("/rpi", (req,res)=>{
  res.json(data);
});

module.exports = router;
