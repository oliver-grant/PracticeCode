var Trello = require("node-trello");
var async  = require("async");
var t = new Trello("16f60be4c670af4fc8857141515bdda3", "712c22653001f7a637be02757e7926a8051183e21e51d560e70a74f67506f101");

var success = function(successMsg) {
  console.log("asdf" + successMsg);
};

var error = function(errorMsg) {
  console.log("asdfasdfsdaf" + errorMsg);
};
// 1/members/me

//5548e5e760780913763d97a5

//t.get('/1/member/me/lists', {lists: "open" }, function(err, data) {

function getListFromID(listID, boardsCallBack) {
  t.get('/1/lists/' + listID, 
        {fields: "name", cards: "open", card_fields:"all"},
        function(err, data) {
    if (err) throw err;
    async.each(data.cards,
      function(item, callback) {
console.log("call from list");
        getCardFromID(item.id, callback);
      },
      function(err) {
        if (err) throw err;
console.log("boardscallback");
        boardsCallBack();
      });

    //var cardsLen = data.cards.length;
    //for (var i = 0; i < cardsLen; ++i) {
    //  getCardFromID(data.cards[i].id, callback);
      //console.log(JSON.stringify(data.cards[i], null, 4));
    //}
  }); 
}


function getCardFromID(cardID, callback) {
  t.get('/1/cards/' + cardID,
        {actions: "all"},
        function(err, card) {
    if (err) throw err;
    var actionsLen = card.actions.length;
//console.log(actionsLen);
    sub_total = 0;
    for (var i = 0; i < actionsLen; ++i) {
      if (card.actions[i].data.listAfter != undefined) {
        var listAfter = JSON.stringify(card.actions[i].data.listAfter, null, 4);
        if (listAfter.indexOf("Done") != -1) {
          //console.log(card.name.split(" ")[0]);
          sub_total += parseFloat(card.name.split(" ")[0]);
	}
      }
    }
    accum(sub_total);
console.log("callback"); 
    callback();
  });
}

var total = 0;
//getCardFromID("56fdcfe43d843b07caea095f");
function accum(sub_total) {
  total += sub_total;
}

t.get('/1/members/me/boards', {lists: "open"}, 
      function(err, data) {
  if (err) throw err;
  var dataLen = data.length;
  for (var i = 0; i < dataLen; ++i) {
    if (data[i].name == "Master's Work") {
      //console.log(JSON.stringify(data[i], null, 4));
      async.each(data[i].lists,
        function(item, callback) {
          var listStr = JSON.stringify(item, null, 4);
          if (listStr.indexOf("Done") != -1) {
            listID = item.id;
console.log("call from boards");
	    getListFromID(listID, callback);
	  } else {
            callback();
          }
        },
        function(err) {
          if (err) throw err;
          console.log(total);
        });
    }
  }
});
//console.log(total);

//getListFromID("56706fff2afc1a3b4da70b36")

/*
var listsLen = data[i].lists.length;
      
      for (var j = 0; j < listsLen; j++) {
        var listID = ""
        var listStr = JSON.stringify(data[i].lists[j], null, 4);
        if (listStr.indexOf("Done") != -1) {
          //console.log(listStr);
          listID = data[i].lists[j].id;
          async.
	  getListFromID(listID, accum);
	}
      }
*/
