var Typed = require(typed.min.js)

particlesJS.load('particles-js','/static/assets/particlesjs-config.json', function(){
    console.log('callback - particles.js config loaded');
})

var terminalTyped = new Typed("#terminalType", {
    typeSpeed: 35,
    backspeed: 0,
    backDelay: 5000,
    loop: false,
    onComplete: function(self) {
      setTimeout(function() {
        self.reset();
      }, 1000);
    }
  });



