particlesJS.load('particles-js','/static/assets/particlesjs-config.json', function(){
    console.log('callback - particles.js config loaded');
})

var terminalTyped = new Typed("#terminalType", {
    strings: [
      '^1000cd /etc/apache2/sites-available/<br>`<span class="terminal-user">abiacarl@example.com: /etc/apache2/sites-available$</span>`^1000 ls -la^1000 <br>`total 104<br>drwxr-xr-x 2 root root 4096 Jan 17 18:43 .<br>drwxr-xr-x 8 root root 4096 Jan 17 &nbsp;2018 ..<br>-rw-r--r-- 1 root root 1332 Aug &nbsp;7&nbsp;&nbsp;2015 000-default.conf<br>-rw-r--r-- 1 root root 1332 Aug &nbsp;7&nbsp;&nbsp;2015 default-ssl.conf<br><span class="terminal-user">abiacarl@example.com: /etc/apache2/sites-available$</span>`^2000a2ensite 000-default.conf<br>`<span class="terminal-user">abiacarl@example.com: /etc/apache2/sites-available$</span>`^1000service apache2 restart<br>`<span class="terminal-user">abiacarl@example.com: /etc/apache2/sites-available$</span>`^1000cd /var/www/sandboxes/abiacarl/<br>`abiacarl@example.com:~$`^1000 clear'
    ],
    typeSpeed: 40,
    backspeed: 0,
    backDelay: 3000,
    loop: false,
    onComplete: function(self) {
      setTimeout(function() {
        self.reset();
      }, 1000);
    }
  });

