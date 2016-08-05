//https://github.com/parano/GeneticAlgorithm-TSP




var canvas, ctx=0
var WIDTH, HEIGHT=0
var points = []=0
var running=0
var canvasMinX, canvasMinY=0
var doPreciseMutate=0

var POPULATION_SIZE=0
var ELITE_RATE=0
var CROSSOVER_PROBABILITY=0
var MUTATION_PROBABILITY=0
var OX_CROSSOVER_RATE=0
var UNCHANGED_GENS=0

var mutationTimes=0
var dis=0
var bestValue, best=0
var currentGeneration=0
var currentBest=0
var population=0
var values=0
var fitnessValues=0
var roulette=0

$(function() {
  init();
  initData();
  points = data200;
  $('#addRandom_btn').click(function() {
    addRandomPoints(50);
    $('#status').text("");
    running = false;
  });
  $('#start_btn').click(function() { 
    if(points.length >= 3) {
      initData();
      GAInitialize();
      running = true;
    } else {
      alert("add some more points to the map!");
    }
  });
  $('#clear_btn').click(function() {
    running === false;
    initData();
    points = new Array();
  });
  $('#stop_btn').click(function() {
    if(running === false && currentGeneration !== 0){
      if(best.length !== points.length) {
          initData();
          GAInitialize();
      }
      running = true;
    } else {
      running = false;
    }
  });
});
function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $('#canvas').width();
  HEIGHT = $('#canvas').height();
  setInterval(draw, 10);
  init_mouse();
}
function init_mouse() {
  $("canvas").click(function(evt) {
    if(!running) {
      canvasMinX = $("#canvas").offset().left;
      canvasMinY = $("#canvas").offset().top;
      $('#status').text("");

      x = evt.pageX - canvasMinX;
      y = evt.pageY - canvasMinY;
      points.push(new Point(x, y));
    }
  });
}
function initData() {
      running = false;
      POPULATION_SIZE = 30;
      ELITE_RATE = 0.3;
      CROSSOVER_PROBABILITY = 0.9;
      MUTATION_PROBABILITY  = 0.01;
  //OX_CROSSOVER_RATE = 0.05;
      UNCHANGED_GENS = 0;
      mutationTimes = 0;
      doPreciseMutate = true;

      bestValue = undefined;
      best = [];
      currentGeneration = 0;
      currentBest;
      population = []; //new Array(POPULATION_SIZE);
}
function addRandomPoints(number) {
  running = false;
  for(var i = 0; i<number; i++) {
    points.push(randomPoint());
  values = new Array(POPULATION_SIZE);
  fitnessValues = new Array(POPULATION_SIZE);
  roulette = new Array(POPULATION_SIZE);  
  }
}
function drawCircle(point) {
  ctx.fillStyle   = '#000';
  ctx.beginPath();
  ctx.arc(point.x, point.y, 3, 0, Math.PI*2, true);
  ctx.closePath();
  ctx.fill();
}
function drawLines(array) {
  ctx.strokeStyle = '#f00';
  ctx.lineWidth = 1;
  ctx.beginPath();

  ctx.moveTo(points[array[0]].x, points[array[0]].y);
  for(var i=1; i<array.length; i++) {
    ctx.lineTo( points[array[i]].x, points[array[i]].y )
  }
  ctx.lineTo(points[array[0]].x, points[array[0]].y);

  ctx.stroke();
  ctx.closePath();
}
function draw() {
  if(running) {
    GANextGeneration();
    $('#status').text("There are " + points.length + " cities in the map, "
                      +"the " + currentGeneration + "th generation with "
                      + mutationTimes + " times of mutation. best value: "
                      + ~~(bestValue));
  } else {
    $('#status').text("There are " + points.length + " Cities in the map. ")
  }
  clearCanvas();
  if (points.length > 0) {
    for(var i=0; i<points.length; i++) {
      drawCircle(points[i]);
    }
    if(best.length === points.length) {
      drawLines(best);
    }
  }
}
function clearCanvas() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
}