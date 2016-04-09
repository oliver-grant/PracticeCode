var Trello = require("node-trello");
var async  = require("async");
var t = new Trello("16f60be4c670af4fc8857141515bdda3", "712c22653001f7a637be02757e7926a8051183e21e51d560e70a74f67506f101");


function nPrint(str) {
  console.log(JSON.stringify(str, null, 4));
}

function getListFromID(listID, boardsCallBack) {
  t.get('/1/lists/' + listID, 
        {fields: "name", cards: "open", card_fields:"all"},
        function(err, data) {
    if (err) throw err;
    async.each(data.cards,
      function(item, callback) {
        getCardFromID(item.id, callback);
      },
      function(err) {
        if (err) throw err;
        boardsCallBack();
      });
  }); 
}

function updateHash(myHash, key, val) {
  if (key in myHash) {
    myHash[key] += val;
  } else {
    myHash[key] = val;
  }

}


function getCardFromID(cardID, callback) {
  t.get('/1/cards/' + cardID,
        {actions: "all"},
        function(err, card) {
    if (err) throw err;
    var actionsLen = card.actions.length;
    sub_total = 0;
    var myHash = {};
    for (var i = 0; i < actionsLen; ++i) {
      if (card.actions[i].data.listAfter != undefined) {
        var listAfter = JSON.stringify(card.actions[i].data.listAfter, null, 4);
        if (listAfter.indexOf("Done") != -1) {
	  actionTime = new  Date(Date.parse(card.actions[i].date) - 4*60*60*1000);
	  actionTimeStr = actionTime.toISOString();
          updateHash(myHash, 
                     actionTimeStr.split("T")[0],  
                     parseFloat(card.name.split(" ")[0]));
	}
      }
    }
    accum(myHash);
    callback();
  });
}

var total = 0;
var totHash = {};

function accum(myHash) {
  for (var item in myHash) {
    updateHash(totHash, item, myHash[item]);
  }
}

t.get('/1/members/me/boards', {lists: "open"}, 
      function(err, data) {
  if (err) throw err;
  var dataLen = data.length;
  for (var i = 0; i < dataLen; ++i) {
    if (data[i].name == "Master's Work") {
      async.each(data[i].lists,
        function(item, callback) {
          var listStr = JSON.stringify(item, null, 4);
          if (listStr.indexOf("Done") != -1) {
            listID = item.id;
	    getListFromID(listID, callback);
	  } else {
            callback();
          }
        },
        function(err) {
          if (err) throw err;
          printHash(totHash);
        });
    }
  }
});

function printHash(myHash) {
  retVals = []
  for (var item in myHash) {
    retVals.push(item + ": " + myHash[item]);
  }
  retVals.sort()
  for (var item in retVals) {
    nPrint(retVals[item]);
  }

}

