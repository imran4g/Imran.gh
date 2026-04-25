
const express= require("express");
const path = require("path");

const app =express();

const port= 8000;

app.get("/",function(req,res){

  res.send(`

    <h1>Team name: Bro Code</h1>
    <h2> Team Members:</h2>
    <p> 1) Imran Ghiasi, imrang@my.yourku.ca , Seaction M Lab 01</p>
    <p> 2) Robin masson, Robinmas@my.yorku.ca, section M, Lab 03</p>
    <p> 3) Ibraheem Yaqub, yaqub03@my.yorku.ca, section M, Lab 03</p>
    <p> 4) Har Dhian Singh, hardhian@my.yorku.ca , section M, Lab 04</p>

    <h2>Tile: Guess that Number! (What number am I thinking of?)</h2>

    <p1> For this project me and my group decided to make a number guesser where the program will choose from a number 1-X allowing the player to keep attempting to see how many they can get in a row. The score will keep rising for how long they are able to go. Once they fail, the score will reset. We believe this project is a great choice for us since we feel we can accomplish this with our abilities as well as still being able to learn new things along the way of making it.<p1>



     `);


});



app.use(express.static(path.join(__dirname,'../','frontend',)))

app.get("/homepage",function(req,res){
  
  res.sendFile(path.join(__dirname,"../",'frontend','brocode.html'));
});






app.listen(port,function(){

  console.log('this is listening to you &{port}')

});






