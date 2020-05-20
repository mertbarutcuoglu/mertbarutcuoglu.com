// adapted from: https://css-tricks.com/snippets/css/typewriter-effect/
var TxtType = function (el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
    this.blinkCursor();
    this.cursor = true;
};

TxtType.prototype.tick = function () {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];
    if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
    }
    this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';

    var that = this;
    var delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt && this.loopNum != 2) {
        delta = this.period;
        this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
    }
    if(this.loopNum < 3){
        setTimeout(function () {
            that.tick();
        }, delta);
    } 
};

TxtType.prototype.blinkCursor = function () {
    var typewriter = document.getElementsByClassName('typewrite');
    setInterval( () => {
        if (this.cursor) {
            typewriter[0].setAttribute('style', "color: black; border-right: 0.08em solid transparent;");
            this.cursor = false;
        } else {
            typewriter[0].setAttribute('style', "color: black; border-right: 0.08em solid black;");
            this.cursor = true;
        }
    }, 530); 
}


window.onload = function () {
    var elements = document.getElementsByClassName('typewrite');
    for (var i = 0; i < elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
            new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
};

