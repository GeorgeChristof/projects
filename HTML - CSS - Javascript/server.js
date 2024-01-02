const http = require("http")
const fs = require("fs");
const ws = require("ws");

function handler(req, res)
{
    console.log("--> GET "+req.url);

    let path = (new URL("http://127.0.0.1:8080" + req.url)).pathname.substring(1);
    if (path == "") {
        path = "index.html"
    }
    
    // Υπάρχει αρχείο με τέτοιο όνομα?
    if (fs.existsSync(path)) {

        // Διαβάζουμε τα περιεχόμενα του αρχείου:
        let data = fs.readFileSync(path);

        // Βρίσκουμε τι "τύπου" ειναι το αρχειο βασει ονόματος (κατάληξης):
        let contentType = 'text/html';

        // Στέλνουμε την απάντηση (data) μαζι με τα κατάλληλα
        // headers (πχ το μέγεθος του αρχειου σε bytes
        // το βαζουμε στο Content-Length header):
        res.writeHead(200, {'Content-type': contentType, 'Content-Length': data.length})
        res.end(data);
    }

    else {
        res.end('Hi You called '+path);
    }
}

const port = 8080;
const http_server = http.createServer( handler )

// Δημιουργομε εναν WebSocket Server να "τρέχει" παράλληλα με τον HTTP server:
const ws_server_public = new ws.WebSocketServer({noServer: true})
const ws_server_private = new ws.WebSocketServer({noServer: true})

http_server.on('upgrade', function upgrade(request, socket, head) {
    
    const url = new URL(request.url, 'http://localhost:8080')
    const pathname = url.pathname
    
    console.log("Upgrade on "+pathname)
    if (pathname === '/chat') {     //public
        ws_server_public.handleUpgrade(request, socket, head, function done(ws) {
            ws_server_public.emit('connection', ws, request);
        });
    } else if (pathname === '/privatechat') {   //private
        ws_server_private.handleUpgrade(request, socket, head, function done(ws) {
            ws_server_private.emit('connection', ws, request);
        });
    } else {
        socket.destroy();
    }
});

// Οταν δεχτει ενα νεο WS connection:
ws_server_public.on('connection', function(ws,request) {
    console.log('New connection');

    // Λεμε τι θα γινει όταν δέχεται μηνύματα σε αυτό το νεο
    // connection: θα τα κανει "broadcast" σε όλους τους clients
    ws.onmessage = broadcast;
    ws.onclose = onclose;
});

ws_server_private.on('connection', function(ws,request) {
    //let u = request.url;
    //let searchString = u.substring(u.lastIndexOf("?"));
    //let params = new URLSearchParams(searchString);
    //let roomId = params.get('room');
    console.log('New Private connection');

    // Λεμε τι θα γινει όταν δέχεται μηνύματα σε αυτό το νεο
    // connection: θα τα κανει "broadcast" σε όλους τους clients
    ws.onmessage = privateMessage;
    ws.onclose = onclose;
});

let users = [];
let privateUsers = [];

function onclose(evt) {
    let ws = evt.target;
    let userId = ws.userid

    console.log("User "+userId + " left!")
    // Θα πρεπει να βρω το user με αυτό το id στη λίστα που εχω
    // και να τον αφαιρέσω. 
    const leaveMessage = {type: "leave", userid: userId}
    ws_server_public.clients.forEach(function(conn) { 
        send(conn, leaveMessage);
    } );

}

// Η συνάρτηση broadcast διατρέχει όλα τα client connections
// και στέλνει τα data σε όλους:
function broadcast(evt)
{
    let ws = evt.target;

    let data = evt.data;
    console.log("SERVER got:" + data);
    let o = JSON.parse(data);
    if (o.type == 'connection') {
        // o.message = 'joined';
        ws.userid = o.id;
        ws.room = o.room;
        users.push({name: o.name, id: o.id});

        let response = {type: 'users', contacts: users};

        send(ws, response);

        ws_server_public.clients.forEach(function(conn) {
            if (conn !== ws) {
                conn.send(data);
            }
        })

    }
    else if (o.type.startsWith('invite')) {
        ws_server_public.clients.forEach(function(conn) {
            if (conn.userid == o.to) {
                conn.send(data);
            }
        });
    }
    else {
        if(o.hasOwnProperty("toUser")){
            ws_server_public.clients.forEach(function(conn) {
                if (conn.userid == o.toUser) {
                    conn.send(data);
                }
            });
            console.log("Private Message");
        }
        else{        
            ws_server_public.clients.forEach(function(conn) {
                    conn.send(data);
                    //public chat
            })
        }
    }
}

function privateMessage(evt)
{
    //let ws = evt.target;

    let data = evt.data;
    console.log("Private SERVER got:" + data);
    let o = JSON.parse(data);
    if (o.type == 'connection') {
        console.log('Connected');
        // o.message = 'joined';
        privateUsers.push({name: o.name, id: o.id});
    }
    else {
        if(o.hasOwnProperty("toUser")){
            ws_server_private.clients.forEach(function(conn) {
                    conn.send(data);
            });
            console.log("Private Messg");
        }
    }
}

function send(ws, data) {
    ws.send( JSON.stringify(data) );
}

http_server.listen(port)
console.log("Starting server at port "+port);