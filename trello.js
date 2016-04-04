var Trello = require("node-trello");

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

function getListFromID(listID) {
  t.get('/1/lists/' + listID, 
        {fields: "name", cards: "open", card_fields:"all"},
        function(err, data) {
    if (err) throw err;
    var cardsLen = data.cards.length;
    for (var i = 0; i < cardsLen; ++i) {
      console.log(JSON.stringify(data.cards[i].dateLastActivity, null, 4));
    }
  }); 
}

t.get('/1/members/me/boards', {lists: "open"}, 
      function(err, data) {
  if (err) throw err;
  var dataLen = data.length;
  for (var i = 0; i < dataLen; ++i) {
    if (data[i].name == "Master's Work") {
      //console.log(JSON.stringify(data[i], null, 4));
      var listsLen = data[i].lists.length;
      for (var j = 0; j < listsLen; j++) {
        var listID = ""
        var listStr = JSON.stringify(data[i].lists[j], null, 4);
        if (listStr.indexOf("Done") != -1) {
          //console.log(listStr);
          listID = data[i].lists[j].id;
	  getListFromID(listID);
	}
      }
    }
  }
});


//getListFromID("56706fff2afc1a3b4da70b36")




