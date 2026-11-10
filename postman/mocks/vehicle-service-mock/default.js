const http = require('http');
const PORT = process.env.PORT || 4500;

const server = http.createServer((req, res) => {
  const { method, url } = req;

  // @endpoint GET /vehicles
  if (method === 'GET' && url === '/vehicles') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify([
      {
        "id": 1,
        "nickName": "The Lisa Marie",
        "vin": "4M2DV11W4RDJ53329",
        "make": "Mercury",
        "model": "Villager",
        "year": "1994",
        "miles": 159864
      },
      {
        "id": 2,
        "nickName": "Dolly",
        "vin": "JN8AZ2KR1AT169594",
        "make": "Nissan",
        "model": "Cube",
        "year": "2010",
        "miles": 59000
      }
    ]));
    return;
  }

  // @endpoint POST /vehicles
  if (method === 'POST' && url === '/vehicles') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      res.writeHead(201, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        "id": 1,
        "nickName": "The Lisa Marie",
        "vin": "4M2DV11W4RDJ53329",
        "make": "Mercury",
        "model": "Villager",
        "year": "1994",
        "miles": "159,864"
      }));
    });
    return;
  }

  // @endpoint GET /vehicles/:id
  if (method === 'GET' && /^\/vehicles\/\d+$/.test(url)) {
    const id = parseInt(url.split('/')[2]);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      "id": id,
      "nickName": "The Lisa Marie",
      "vin": "4M2DV11W4RDJ53329",
      "make": "Mercury",
      "model": "Villager",
      "year": "1994",
      "miles": 159864
    }));
    return;
  }

  // @endpoint PATCH /vehicles/:id
  if (method === 'PATCH' && /^\/vehicles\/\d+$/.test(url)) {
    const id = parseInt(url.split('/')[2]);
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        "id": id,
        "nickName": "The Lisa Marie",
        "vin": "4M2DV11W4RDJ53329",
        "make": "Mercury",
        "model": "Villager",
        "year": "1994",
        "miles": 159999
      }));
    });
    return;
  }

  // @endpoint DELETE /vehicles/:id
  if (method === 'DELETE' && /^\/vehicles\/\d+$/.test(url)) {
    res.writeHead(204, {});
    res.end('');
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Mock route not defined', method, url }));
});

server.listen(PORT, () => console.log('Vehicle Service Mock running on port ' + PORT));
