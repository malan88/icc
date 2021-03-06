function byID(id) { return document.getElementById(id); }
function byCls (el, cl) { return el ? el.getElementsByClassName(cl) : []; }
function first(el, cl) { return byCls(el, cl)[0]; }
function byTag (el, tg) { return el ? el.getElementsByTagName(tg) : []; }
function allof (cl) { return byCls(document, cl); }
function atload(func) { document.addEventListener('DOMContentLoaded', func); }
function windowSize() { return document.documentElement.clientWidth; }
function newel(el, attrs) {
    // a new style new element method to be used in place of newEl
    var el = document.createElement(el);
    for (let k in attrs)
        el[k] = attrs[k];
    return el;
}

function newEl(el, cl) {
        var el = document.createElement(el);
        el.className = cl;
        return el;
}
function parentByID(el, re) {
    while(!el.id || !el.id.match(re)) { el = el.parentNode; }
    return el;
}
function parentNum(el, prefix='') {
    // get the parent whose id contains a number (and possibly a prefix)
    string = ['^', prefix, '\\d+'];
    var re = new RegExp(string.join(''), 'g');
    return parentByID(el, re);
}
// get the id of the parent whose id contains a number/prefix
function parentNumID(el, prefix='') { return parentNum(el, prefix).id; }

function parentByCls(el, cls) {
    while(!el.className || !el.className.match(cls)) { el = el.parentNode; }
    return el;
}
