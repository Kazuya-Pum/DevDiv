const functions = require("firebase-functions");
const express = require("express");
const app = express();
const fs = require("fs");

app.use(express.static("public"));

app.get("/app", (req, res) => {
  fs.readFile("./index.html", "utf-8", doReard);

  /**
   * a
   * @param {*} err a
   * @param {*} data a
   */
  function doReard(err, data) {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write(data);
    res.end();
  }
});

exports.app = functions.https.onRequest(app);
