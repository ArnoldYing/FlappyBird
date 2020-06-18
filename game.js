//
// Variable instantiation/ declaration
//

const cvs = document.getElementById("myCanvas");
const ctx = cvs.getContext("2d");

//define images
var birdImg = new Image();
var bgImg = new Image();
var fg = new Image();
var pipeTop = new Image();
var pipeBot = new Image();

birdImg.src = "images/flappybird/bird.png";
bgImg.src = "images/flappybird/bg.png";
fg.src = "images/flappybird/fg.png";
pipeTop.src = "images/flappybird/pipeNorth.png";
pipeBot.src = "images/flappybird/pipeSouth.png";

//Define variables
var x = 10; //bird starting x position
var y = 150; //bird starting y position
var gravity = 0.5; //acceleration from gravity



//
//FSM
//

//FSM game state controller
const state = {
    current : 0, 
    ready : 0, 
    game : 1, 
    end : 2
};

//keydown event definition
function switchState(e) {
    console.log(e);
    if (e.code == "Space") {
        console.log(state.current);
        switch (state.current) {
            case state.ready:
                state.current = state.game;
                break;
            case state.game:
                //state.current = state.end;
                bird.flap();
                break;
            case state.end: 
                state.current = state.ready;
                break;
        }
    }
}

//when space key pressed, switch game state or call bird.flap if in game state already
document.addEventListener("keydown", switchState);



//
// Objects
//

//bg
const bg = {
    x : 0, 
    y : 0,
    w : 400, 
    h : 500, 
    draw : function () {
        ctx.drawImage(bgImg, 0, 0, this.w, this.h, this.x, this.y, this.w, this.h);
    }
}

//bird
const bird = {
    bX : x, 
    bY : y, 
    w : 38, 
    h : 26, 
    speed : 0, 
    acc : gravity, 
    jump : 12,

    draw : function () {
        ctx.drawImage(birdImg, 0, 0, this.w, this.h, this.bX, this.bY, this.w, this.h);
    },
    flap : function () {
        this.speed -= this.jump;
    },
    update : function () {
        if (state.current == state.ready) {
            bX = x;
            bY = y;
        } else {
            this.speed += this.acc;
            this.bY += this.speed;

            //check if bird hits top or bottom boundary
            if ((this.bY - this.h / 2) <= 0) { //touching top
                if (state.current = state.game)
                    state.current = state.end;
            } else if ((this.bY + this.h / 2) >= cvs.height) {
                if (state.current = state.game)
                    state.current = state.end;
            }
        }
    }
};



//
// function definitions
//

function draw() {
    ctx.fillStyle = "#70c5ce";
    ctx.fillRect(0, 0, cvs.width, cvs.height);

    bg.draw();
    bird.draw();
}

function loop() {
    bird.update();
    draw();
    requestAnimationFrame(loop);
}

loop();
