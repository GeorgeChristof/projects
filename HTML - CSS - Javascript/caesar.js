map1 = new Map();
map2 = new Map();
var index = 0;

for(var i=913; i <= 937; i++){
    if(i == 930)
        continue;
    map1.set(index , String.fromCharCode(i));
    index++;
}

var index = 0;

for(var i=913; i <= 937; i++){
    if(i == 930)
        continue;
    map2.set( String.fromCharCode(i), index);
    index++;
}

function encrypt(text,shift){
    var result = "";
    for (var i = 0; i < text.length; i++) {
        var c = text.charAt(i);
        var mp = map2.get(c);
        if(mp == undefined){
            result += c;
        }else
        {
            mp = (mp + shift) % 24;
            var c2 = map1.get(mp);
            result += c2;
        }
    }
return result;
}

function decrypt(text,shift){
    var result = "";
    shift = (24 - shift) % 24;
    result = encrypt(text,shift);
    return result;
}